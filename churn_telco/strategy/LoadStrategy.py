from abc import ABC, abstractmethod

class LoadData(ABC):
    @abstractmethod
    def load():
        ...