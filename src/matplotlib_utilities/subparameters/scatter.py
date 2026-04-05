from dataclasses import dataclass
from .base_class import Subparameters
from ..utils import Marker

@dataclass
class ScatterParameters(Subparameters):
    """
    Parameters for the scatter plot.
    
    Attributes:
    ----------
    s: float
        The size of the points.
    c: str | None
        The color of the points.
    alpha: float | None
        The alpha of the points.
    marker: Marker
        The marker of the points.
    cmap: str | None
        The colormap of the points.
    linewidths: float | None
        The linewidths of the points.
    edgecolors: str | None
        The edgecolors of the points.
    vmin: float | None
        The vmin of the points.
    vmax: float | None
        The vmax of the points.
    plotnonfinite: bool
        Whether to plot non-finite values.
    """
    s: float = 5
    c: str | None = None
    alpha: float | None = None
    marker: Marker = Marker.POINT
    cmap: str | None = None
    linewidths: float | None = None
    edgecolors: str | None = None
    vmin: float | None = None
    vmax: float | None = None
    plotnonfinite: bool = False

    def __post_init__(self):
        if self.s < 0:
            raise ValueError("s must be greater than 0")
        if self.alpha is not None and not (0 <= self.alpha <= 1):
            raise ValueError("alpha must be between 0 and 1")

    @property
    def to_dict(self) -> dict:
        """
        Convert parameters to a dictionary compatible with matplotlib.pyplot.scatter.
        """
        return {
            "s": self.s,
            "c": self.c,
            "alpha": self.alpha,
            "marker": self.marker.value,
            "cmap": self.cmap,
            "linewidths": self.linewidths,
            "edgecolors": self.edgecolors,
            "vmin": self.vmin,
            "vmax": self.vmax,
            }