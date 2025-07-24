from app.core.logger import logger

class DBConfigurationError(Exception):
     def __init__(self, message):
        super().__init__(message)
        logger.error("Database configuration error")
