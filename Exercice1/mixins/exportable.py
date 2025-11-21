
from abc import ABC, abstractmethod

class Exportable(ABC):
    @abstractmethod
    def exporter(self):
        pass
