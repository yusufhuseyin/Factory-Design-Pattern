from abc import ABC, abstractmethod

class DB(ABC):
    @abstractmethod
    def selectData(self):
        pass

    @abstractmethod
    def insertData(self):
        pass
