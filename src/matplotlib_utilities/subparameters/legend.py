from dataclasses import dataclass

from .base_class import Subparameters


@dataclass
class LegendParameters(Subparameters):
    """
    Parameters for the legend.

    Attributes:
    ----------
    loc: str | None
        The location of the legend (e.g. 'upper right', 'best').
    bbox_to_anchor: tuple | None
        Box that is used to position the legend in conjunction with loc.
    ncol: int | None
        The number of columns that the legend has.
    fontsize: int | str | None
        The font size of the legend.
    frameon: bool | None
        Whether the legend should be drawn on a patch (frame).
    fancybox: bool | None
        Whether round edges should be enabled around the legend's background.
    shadow: bool | None
        Whether to draw a shadow behind the legend.
    framealpha: float | None
        The alpha transparency of the legend's background.
    facecolor: str | None
        The legend's background color.
    edgecolor: str | None
        The legend's background patch edge color.
    title: str | None
        The legend's title.
    title_fontsize: int | str | None
        The font size of the legend's title.
    """

    loc: str | None = None
    bbox_to_anchor: tuple[float, ...] | None = None
    ncol: int | None = None
    fontsize: int | str | None = None
    frameon: bool | None = None
    fancybox: bool | None = None
    shadow: bool | None = None
    framealpha: float | None = None
    facecolor: str | None = None
    edgecolor: str | None = None
    title: str | None = None
    title_fontsize: int | str | None = None

    @property
    def to_dict(self) -> dict:
        """
        Convert parameters to a dictionary compatible with matplotlib.axes.Axes.legend.
        """
        return {
            k: v
            for k, v in {
                "loc": self.loc,
                "bbox_to_anchor": self.bbox_to_anchor,
                "ncol": self.ncol,
                "fontsize": self.fontsize,
                "frameon": self.frameon,
                "fancybox": self.fancybox,
                "shadow": self.shadow,
                "framealpha": self.framealpha,
                "facecolor": self.facecolor,
                "edgecolor": self.edgecolor,
                "title": self.title,
                "title_fontsize": self.title_fontsize,
            }.items()
            if v is not None
        }
