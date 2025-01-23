from abc import ABC, abstractmethod

class DBFactory(ABC):
    @abstractmethod
    def createDB(self):
        pass
