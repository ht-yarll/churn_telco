from abc import ABC, abstractmethod

class LoadDataStrategy(ABC):
    @abstractmethod
    def load():
        ...