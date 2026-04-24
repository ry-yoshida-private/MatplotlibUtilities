from dataclasses import dataclass

from ....subparameter import Subparameters
from .base import ColorParameters



@dataclass
class BarParameters(ColorParameters, Subparameters):
    """
    Parameters for the bar plot.

    Attributes:
    ----------
    height: float | None
        The height of the bars.
    width: float | None
        The width of the bars.
    bottom: float | None
        The bottom of the bars.
    align: str | None
        The alignment of the bars.
    """
    height: float | None = None
    width: float | None = None
    bottom: float | None = None
    align: str | None = None
