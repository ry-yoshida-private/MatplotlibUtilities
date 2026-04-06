from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike

from .base_class import Subparameters
from ..utils import Marker
from ..utils.color_types import ScatterColorArg

@dataclass
class ScatterParameters(Subparameters):
    """
    Parameters for the scatter plot.
    
    Attributes:
    ----------
    s: float | ArrayLike | None
        Marker area in points², scalar or one value per point (matplotlib *s*).
        None omits *s* so matplotlib uses its default (``rcParams['lines.markersize'] ** 2``).
    c: ScatterColorArg | None
        Marker face color: a single color, one color per point, or a 1-D array of
        scalars. Scalars are painted using *cmap* with optional *vmin* / *vmax*
        (matplotlib *c*).
    alpha: float | None
        Opacity of the markers.
    marker: Marker
        Marker style.
    cmap: str | None
        Registered colormap *name* (e.g. *viridis*) used only when *c* is numeric
        data to map; ignored when *c* is already an explicit color or color array.
    linewidths: float | None
        Edge line width(s) of the markers.
    edgecolors: ScatterColorArg | None
        Marker edge colors; same kinds of values as *c* (matplotlib also accepts *face*).
    vmin: float | None
        Lower bound of the colormap when *c* is numeric; None uses the data minimum.
    vmax: float | None
        Upper bound of the colormap when *c* is numeric; None uses the data maximum.
    plotnonfinite: bool
        If True, plot points whose *c* value is non-finite; if False, they are dropped.
    """
    s: float | ArrayLike | None = None
    c: ScatterColorArg | None = None
    alpha: float | None = None
    marker: Marker = Marker.POINT
    cmap: str | None = None
    linewidths: float | None = None
    edgecolors: ScatterColorArg | None = None
    vmin: float | None = None
    vmax: float | None = None
    plotnonfinite: bool = False

    def __post_init__(self):
        if self.s is not None:
            s_arr = np.asarray(self.s, dtype=float)
            if np.any(s_arr < 0):
                raise ValueError("s must be non-negative")
        if self.alpha is not None and not (0 <= self.alpha <= 1):
            raise ValueError("alpha must be between 0 and 1")
