from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike

from ....subparameter import Subparameters
from ....utils import Marker
from ....utils.color import ScatterColorArg
from .base import ArtistParameters, CmapParameters, LabelParameters


@dataclass
class ScatterParameters(
    CmapParameters,
    LabelParameters,
    ArtistParameters,
    Subparameters,
):
    """
    Parameters for the scatter plot.

    Attributes:
    ----------
    # own
    s: float | ArrayLike | None
        Marker area in points squared.
    c: ScatterColorArg | None
        Marker face color or scalar values for colormap mapping.
    marker: Marker
        Marker style.
    linewidths: float | None
        Edge line width of the markers.
    edgecolors: ScatterColorArg | None
        Marker edge colors.
    plotnonfinite: bool
        Whether to draw points with non-finite c values.
    # inherited from CmapParameters
    cmap: str | None
        The colormap name used when `c` contains numeric values.
    vmin: float | None
        The lower data bound mapped to the start of the colormap.
    vmax: float | None
        The upper data bound mapped to the end of the colormap.
    # inherited from LabelParameters
    label: str | None
        The label string for axis, legend, and other uses.
    # inherited from ArtistParameters
    alpha: float | None
        Opacity of the markers.
    zorder: float | None
        Drawing order of the markers.
    """

    s: float | ArrayLike | None = None
    c: ScatterColorArg | ArrayLike | None = None
    marker: Marker = Marker.POINT
    linewidths: float | ArrayLike | None = None
    edgecolors: ScatterColorArg | ArrayLike | None = None
    plotnonfinite: bool = False

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.s is not None:
            s_arr = np.asarray(self.s, dtype=float)
            if np.any(s_arr < 0):
                raise ValueError("s must be non-negative")
