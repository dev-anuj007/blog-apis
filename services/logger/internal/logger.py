from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def critical(self) -> None:
        pass

    @abstractmethod
    def error(self) -> None:
        pass

    @abstractmethod
    def info(self) -> None:
        pass

    @abstractmethod
    def warning(self) -> None:
        pass
