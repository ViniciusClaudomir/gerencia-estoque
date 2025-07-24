from app.core.i18n import i18n
from app.core.logger import logger

i18nImpl = i18n()

class SqlInjection(Exception):
     def __init__(self, message):
        super().__init__(message)
        logger.error(i18nImpl.get_label('SQL_DETECTED') + ' | ' + message)
