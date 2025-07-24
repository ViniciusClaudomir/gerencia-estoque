import uuid

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver

from langchain_core.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

from langfuse.callback import CallbackHandler

from app.core.graph_config import load_configuration
from app.infrastructure.external_services.langgraph_addons import *
from app.domain.services.langgraph_warehouse_tools import (ValidatorSqlInjectionTool, FormatResponseQueryDatabaseInTextOutputTool,
                                                        GetDBSchemaTool, QueryInDBTool)

from app.schemas.response.conversation_response import ConversationResponse
import httpx

class WarehouseGraphService:
    
    def __init__(self):
        self.config = load_configuration(self.__class__.__name__)
        self.graph = self._make_graph()


    def make_database_tools(self):
        database_tools_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    self.config['database_tools']['prompt'],
                ),
                ("placeholder", "{messages}"),
            ]
        ).partial(time=datetime.now())


        database_tools_list = [

                   GetDBSchemaTool(),
                   QueryInDBTool(),
                   ValidatorSqlInjectionTool(),
                   FormatResponseQueryDatabaseInTextOutputTool()
                ]

        database_tools = database_tools_prompt | callChat(self.config['database_tools']['model']
                                                          ).bind_tools(database_tools_list)

        return database_tools, database_tools_list
    

    def router_principal_warehouse(self):
        
        nodes = ["database"]
        system_prompt = self.config['router_warehouse']['prompt']
        options = ["FINALIZAR"] + nodes
        function_def = {
            "name": "router_principal_warehouse",
            "description": "Select next node",
            "parameters": {
                "title": "routeSchema",
                "type": "object",
                "properties": {
                    "next": {
                        "title": "Next",
                        "anyOf": [
                            {"enum": options},
                        ],
                    }
                },
                "required": ["next"],
            },
        }
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder(variable_name="messages"),
                (
                    "system",
                    "Given the above conversation, who should act next?"
                    "Or should we END? Select one of: {options}",
                ),
            ]
        ).partial(options=str(options), members_atividades=", ".join(nodes))
        supervisor_atividades = (
            prompt
            | callChat(self.config['router_warehouse']['model']).bind_functions(functions=[function_def], function_call="router_principal_warehouse")
            | JsonOutputFunctionsParser()
        )
        return functools.partial(agent_node_supervisor, agent=supervisor_atividades, name="router_principal_warehouse")

    def _make_graph(self):

        warehouseSG = StateGraph(AgentState)

        warehouseSG.add_node('router_principal_warehouse',self.router_principal_warehouse())
        warehouseSG.set_entry_point('router_principal_warehouse')


        # Instance of database tools
        database, database_tools = self.make_database_tools()
        warehouseSG.add_node('database', RunnableInvoke(database, 30))
        warehouseSG.add_node('database_tools', create_tool_node_with_fallback(database_tools))
        warehouseSG.add_conditional_edges('database', tools_database_tool)
        warehouseSG.add_edge("database_tools", 'database')

        warehouseSG.add_conditional_edges("router_principal_warehouse", lambda x: x['next'], {
                                           'database':'database',
                                           'FINALIZAR':END,
                                           '__end__': END}
                                          )
        

        with SqliteSaver.from_conn_string("warehouse.db") as snapshot:
            warehouse_graph = warehouseSG.compile(checkpointer=snapshot)
            with open('graph_financial.png', 'wb') as arq:
                arq.write(warehouse_graph.get_graph(xray=True).draw_mermaid_png())
            yield warehouse_graph

    def process_message(self, content, thread_id = '') -> ConversationResponse:
        
        response = ConversationResponse()

        if not thread_id or not thread_id.strip():
            thread_id = str(uuid.uuid4())

        input_graph = {
                "messages": [
                    HumanMessage(content=content)
                ],
                "thread_id":thread_id,
                "next":None
            }
        result = []

        langfuse_handler = CallbackHandler(user_id="Teste", tags=['Warehouse Chat'], session_id=thread_id, httpx_client=httpx.Client(verify=False))
        config = {"configurable": {"thread_id": thread_id}, "run_name": "Warehouse Chat", "callbacks":[langfuse_handler], 'run_id':thread_id,
                'recursion_limit': 100}
        
        for s in next(self.graph).stream(input_graph, config):
            if "__end__" not in s:
                result.append(dict(s))
        
        print(result)
        response_message = ''
        for message in result:
            for node, content in message.items():
                messages = content.get('messages', '')
                if isinstance(messages, AIMessage):
                    response_message = messages.content



        response.thread_id = thread_id
        response.content = response_message
                
        return response