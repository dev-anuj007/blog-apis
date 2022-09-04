from services.logger.internal.logger import Logger


class ConsoleLogger(Logger):
    def critical(self, *, message: str) -> None:
        print(message)

    def error(self, *, message: str) -> None:
        print(message)

    def info(self, *, message: str) -> None:
        print(message)

    def warning(self, *, message: str) -> None:
        print(message)
