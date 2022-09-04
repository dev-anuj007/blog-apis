from asyncio.log import logger
from distutils.log import error
from email import message
from services.logger.logger_service import LoggerService


class TestLoggerService:
    def test_logger(self) -> None:
        try:
            logger = LoggerService.get_logger()
            logger.critical(message="CRITICAL:: logged")
            logger.error(message="ERROR:: logged")
            logger.info(message="INFO:: logged")
            logger.warning(message="WARNING:: logged")
        except Exception as err:
            assert False, f"Error:: {err}"
