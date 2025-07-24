from app.core.logger import logger
import re

class Utils:


    @staticmethod
    def sql_is_present(message:str) -> bool:
        '''
        Avaliar possiveis comandos sql através de regex
        '''
        pattern = re.compile(r"(?i)\b(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|ALTER|--|#|;|' OR '| OR 1=1|xp_cmdshell|exec|concat|benchmark)\b")
        return bool(pattern.search(message))