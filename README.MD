app/ <br/>
├── api/ <br/>
│ ├── v1/ <br/>
│ │ ├── endpoints/ # Rotas por recurso (ex: users.py, items.py) <br/>
│ │ └── dependencies/ # Injeção de dependências <br/>
│ └── main.py # Inicialização da aplicação FastAPI <br/>
│ <br/>
├── schemas/ # DTOs com Pydantic (entrada e saída de dados) <br/>
│ ├── user.py <br/>
│ └── auth.py <br/>
│ <br/>
├── domain/ # Camada de domínio (regras e lógica de negócio) <br/>
│ ├── models/ # Entidades do domínio <br/>
│ ├── services/ # Casos de uso / lógica de aplicação <br/>
│ └── repositories/ # Interfaces abstratas de persistência <br/>
│ <br/>
├── infrastructure/ # Implementações técnicas concretas <br/>
│ ├── database/ <br/>
│ │ ├── models/ # Models ORM (ex: SQLAlchemy) <br/>
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
└── requirements.txt # Dependências do projeto <br/>