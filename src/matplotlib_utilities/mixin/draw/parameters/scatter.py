from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike

from ....subparameter import Subparameters
from ....utils import Marker
from ....utils.color import ScatterColorArg
from .base import ArtistParameters, CmapParameters, LabelParameters


@dataclass
class ScatterParameters(CmapParameters, LabelParameters, ArtistParameters, Subparameters):
    """
    Parameters for the scatter plot.

    Attributes:
    ----------
    s: float | ArrayLike | None
        Marker area in points squared.
    c: ScatterColorArg | None
        Marker face color or scalar values for colormap mapping.
    alpha: float | None
        Opacity of the markers.
    zorder: float | None
        Drawing order of the markers.
    marker: Marker
        Marker style.
    cmap, vmin, vmax
        Colormap settings used when c is numeric.
    linewidths: float | None
        Edge line width of the markers.
    edgecolors: ScatterColorArg | None
        Marker edge colors.
    plotnonfinite: bool
        Whether to draw points with non-finite c values.
    """

    s: float | ArrayLike | None = None
    c: ScatterColorArg | None = None
    marker: Marker = Marker.POINT
    linewidths: float | None = None
    edgecolors: ScatterColorArg | None = None
    plotnonfinite: bool = False

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.s is not None:
            s_arr = np.asarray(self.s, dtype=float)
            if np.any(s_arr < 0):
                raise ValueError("s must be non-negative")
