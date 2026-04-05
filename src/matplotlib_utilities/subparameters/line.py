from dataclasses import dataclass
from .base_class import Subparameters

@dataclass
class LineParameters(Subparameters):
    """
    Parameters for the line.

    TODO: Add more parameters.
    """
    color: str | None = None
    

    @property
    def to_dict(self) -> dict:
        """
        Convert parameters to a dictionary compatible with matplotlib.pyplot.axvline.
        """
        return {
            "color": self.color,
        }

