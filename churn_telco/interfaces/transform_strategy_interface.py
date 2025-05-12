from abc import ABC, abstractmethod

class TransformDataStrategy(ABC):
    @abstractmethod
    def transform(self):
        ...
