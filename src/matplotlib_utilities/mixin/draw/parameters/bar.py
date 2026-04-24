from dataclasses import dataclass

from ....subparameter import Subparameters
from .base import ColorParameters



@dataclass
class BarParameters(
    ColorParameters,
    Subparameters,
):
    """
    Parameters for the bar plot.

    Attributes:
    ----------
    # own
    height: float | None
        The height of the bars.
    width: float | None
        The width of the bars.
    bottom: float | None
        The bottom of the bars.
    align: str | None
        The alignment of the bars.
    # inherited from ColorParameters
    facecolor: MplColor | None
        The color of the face of the artist.
    edgecolor: MplColor | None
        The color of the edge of the artist.
    """
    height: float | None = None
    width: float | None = None
    bottom: float | None = None
    align: str | None = None
