import os
import traceback


from langchain.tools import BaseTool
from langchain.pydantic_v1 import BaseModel, Field
from langchain.callbacks.manager import CallbackManagerForToolRun
from  typing import Optional, Type

from app.infrastructure.database.session import get_db, get_table_info
from app.infrastructure.database.repositories.execute_queries import  execute_sql
from app.utils.Utils import Utils
from app.exceptions.sql_injection import SqlInjection




from app.core.logger import logger



class GetDBSchemaInput(BaseModel):
    pass

class GetDBSchemaTool(BaseTool):
    name:str = "collect_database_schema"
    description:str = "Recover database schema"

    def _init_(self):
        super(GetDBSchemaTool, self)._init_(self)
    
    def _run(self, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        try:
            with get_db() as db:
                logger.debug("Retrieving information about tables")
                return get_table_info(db)
        except Exception as e:
            tb = traceback.print_exception(e)
            logger.error(tb)
            return "Error when trying to query the database"

class QueryInDBInput(BaseModel):
    query: str = Field(description="Query sql about the user request message")

class QueryInDBTool(BaseTool):
    name:str = 'execute_query_in_database'
    description:str = 'execute query in database and given data'
    args_schema: Type[BaseModel] = QueryInDBInput

    def _init_(self):
        super(QueryInDBTool, self)._init_(self)
    
    def _run(self, query, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        try:
            logger.debug("Running query")
            result = execute_sql(query)
            return result
        except Exception as e:
            tb = traceback.print_exception(e)
            logger.error(tb)
            return "Error when trying to query the database"

class ValidatorSqlInjectionInput(BaseModel):
    user_message: str = Field(description="User message")

class ValidatorSqlInjectionTool(BaseTool):
    name:str = "sql_injection_validation"
    description:str = 'validates whether the user message contains SQL injection'
    args_schema: Type[BaseModel] = ValidatorSqlInjectionInput

    def _init_(self):
        super(ValidatorSqlInjectionTool, self)._init_(self)
    
    def _run(self, user_message, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        
        if Utils.sql_is_present(user_message):
            return 'NOK, sql injection detected'
        return 'Ok, execute a proxima tool!'
    


class FormatResponseQueryDatabaseIntput(BaseModel):
    data: list = Field(description="Data returned by the database after the query")

class FormatResponseQueryDatabaseInTextOutputTool(BaseTool):
    name:str = "format_data_in_text"
    description:str = 'Format the data in output text'
    args_schema: Type[BaseModel] = FormatResponseQueryDatabaseIntput

    def _init_(self):
        super(ValidatorSqlInjectionTool, self)._init_(self)
    
    def _run(self, data, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        
        return data

