from sqlalchemy import text
from app.infrastructure.database.session import get_db

def execute_sql(sql_query:str) -> list:
    with get_db() as db:
        result = db.execute(text(sql_query))
    return result.fetchall()