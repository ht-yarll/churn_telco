from abc import ABC, abstractmethod

class ExtractDataStrategy(ABC):
    @abstractmethod
    def extract(self):
        ...