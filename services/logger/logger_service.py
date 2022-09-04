import os
from services.logger.internal.console_logger import ConsoleLogger


class LoggerService:
    ENVIRONMENT_NAME = os.getenv("ENVIRONMENT")

    @staticmethod
    def get_logger():
        if LoggerService.ENVIRONMENT_NAME == "local":
            return ConsoleLogger()
        else:
            raise Exception(f"Logger is not configurable for {LoggerService.ENVIRONMENT_NAME} environment yet !")
