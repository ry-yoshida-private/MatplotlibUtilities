from dataclasses import dataclass

from ....subparameter import Subparameters
from ....utils import Marker
from ....utils.color import MplColor
from .base import ArtistParameters, LabelParameters, LineStyleParameters


@dataclass
class PlotParameters(
    LineStyleParameters,
    LabelParameters,
    ArtistParameters,
    Subparameters,
):
    """
    Parameters for the plot.

    Attributes:
    ----------
    # own
    color: MplColor | None
        The color of the plot.
    marker: Marker | None
        The marker of the plot.
    markersize: float | None
        The size of the markers.
    markeredgewidth: float | None
        The width of the marker edges.
    markeredgecolor: MplColor | None
        The color of the marker edges.
    markerfacecolor: MplColor | None
        The color of the marker faces.
    solid_capstyle: str | None
        The style of the cap of the lines.
    solid_joinstyle: str | None
        The style of the join of the lines.
    drawstyle: str | None
        The style of the drawing of the lines.
    # inherited from LineStyleParameters
    linewidth: float | None
        The width of the lines.
    linestyle: Linestyle | None
        The style of the lines.
    antialiased: bool | None
        Whether to antialias the plot.
    # inherited from LabelParameters
    label: str | None
        The label string for axis, legend, and other uses.
    # inherited from ArtistParameters
    alpha: float | None
        The alpha of the plot.
    zorder: float | None
        The order of the plot.
    """
    color: MplColor | None = None
    marker: Marker | None = None
    markersize: float | None = None
    markeredgewidth: float | None = None
    markeredgecolor: MplColor | None = None
    markerfacecolor: MplColor | None = None
    solid_capstyle: str | None = None
    solid_joinstyle: str | None = None
    drawstyle: str | None = None

    def __post_init__(self):
        super().__post_init__()
        if self.markersize is not None and self.markersize <= 0:
            raise ValueError("markersize must be positive")
        if self.markeredgewidth is not None and self.markeredgewidth <= 0:
            raise ValueError("markeredgewidth must be positive")
