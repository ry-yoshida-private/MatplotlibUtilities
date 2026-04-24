from dataclasses import dataclass

from ....subparameter import Subparameters
from ....utils.color import MplColor


@dataclass
class LegendParameters(Subparameters):
    """
    Parameters for the legend.

    Attributes:
    ----------
    loc: str | None
        The location of the legend.
    bbox_to_anchor: tuple | None
        Box that is used to position the legend in conjunction with loc.
    ncol: int | None
        The number of columns that the legend has.
    fontsize: int | str | None
        The font size of the legend.
    frameon: bool | None
        Whether the legend should be drawn on a frame.
    fancybox: bool | None
        Whether round edges should be enabled around the legend background.
    shadow: bool | None
        Whether to draw a shadow behind the legend.
    framealpha: float | None
        The alpha transparency of the legend background.
    facecolor: MplColor | None
        The legend background color.
    edgecolor: MplColor | None
        The legend frame edge color.
    title: str | None
        The legend title.
    title_fontsize: int | str | None
        The font size of the legend title.
    """

    loc: str | None = None
    bbox_to_anchor: tuple[float, ...] | None = None
    ncol: int | None = None
    fontsize: int | str | None = None
    frameon: bool | None = None
    fancybox: bool | None = None
    shadow: bool | None = None
    framealpha: float | None = None
    facecolor: MplColor | None = None
    edgecolor: MplColor | None = None
    title: str | None = None
    title_fontsize: int | str | None = None
