from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Subparameters(ABC):
    """
    BaseSubparameters is the base class for the subparameters.
    """
    @property
    @abstractmethod
    def to_dict(self) -> dict:
        pass