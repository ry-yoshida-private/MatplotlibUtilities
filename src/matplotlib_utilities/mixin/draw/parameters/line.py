from dataclasses import dataclass

from ....subparameter import Subparameters
from .base import ArtistParameters, LabelParameters, LineStyleParameters


@dataclass
class LineParameters(LineStyleParameters, LabelParameters, ArtistParameters, Subparameters):
    """
    Parameters for the line.

    Attributes:
    ----------
    color: MplColor | None
        The color of the line.
    linewidth: float | None
        The width of the line.
    linestyle: Linestyle | None
        The style of the line.
    antialiased: bool | None
        Whether to antialias the line.
    label: str | None
        The label string.
    alpha: float | None
        The alpha of the line.
    zorder: float | None
        The drawing order.
    """
