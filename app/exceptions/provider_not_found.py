from app.core.logger import logger

class ProviderNotFound(Exception):
     def __init__(self, message):
        super().__init__(message)
        logger.error(f"Provider {message} not found!")
