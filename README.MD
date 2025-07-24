![Grafo](graph_financial.png)
<br/>
<br/>
Basicamente a aplicação conta com 4 tools, dentro da 'database_tools'
 1 - Validação de sql
 2 - Coleta de esquema da base de dados postgreesql, porem foi usado sqlalchemy, caso queira alterar a base com mais facilidade
 3 - Execução da consulta sql, vale lembrar que caso a primeira etapa encontre problemas, é finalizado e o sql malicioso não é executado
 4 - Formatação de dados, atualmente string, mas poderia ser graficos.
<br/>
## Estruturas das pastas e como navegar:
<br/>
app/ <br/>
├── api/ <br/>
│ ├── v1/ <br/>
│ │ ├── endpoints/ # Rotas por recurso (ex: users.py, items.py) <br/>
│ └── main.py # Inicialização da aplicação FastAPI <br/>
│ <br/>
├── schemas/ # DTOs com Pydantic (entrada e saída de dados) <br/>
│ ├── request <br/>
│ └── response <br/>
│ <br/>
├── domain/ # Camada de domínio (regras e lógica de negócio) <br/>
│ ├── models/ # Entidades do domínio <br/>
│ ├── services/ # Casos de uso / lógica de aplicação <br/>
│ └── repositories/ # Interfaces abstratas de persistência <br/>
│ <br/>
├── infrastructure/ # Implementações técnicas concretas <br/>
│ ├── database/ <br/>
│ │ ├── repositories/ # Implementações dos repositórios <br/>
│ │ └── session.py # Conexão e sessão com o banco <br/>
│ └── external_services/ # Integrações com APIs externas, serviços, etc. <br/>
│ <br/>
├── core/ # Configuração e utilitários globais <br/>
│ ├── config.py # Variáveis de ambiente <br/>
│ └── security.py # Autenticação, JWT, etc. <br/>
│ <br/>
├── utils/ # Funções auxiliares e genéricas <br/>
│ └── helpers.py <br/>
│ <br/>
├── tests/ # Testes automatizados <br/>
│ ├── unit/ <br/>
│ └── integration/ <br/>
│ <br/>

