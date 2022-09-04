from abc import ABC, abstractclassmethod, abstractmethod


class Logger(ABC):
    @abstractmethod
    def critical(self):
        pass

    @abstractmethod
    def error(self):
        pass

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def warning(self):
        pass
