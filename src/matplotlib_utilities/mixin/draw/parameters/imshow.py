from dataclasses import dataclass

from matplotlib.colors import Normalize

from ....subparameter import Subparameters
from ....utils import Aspect, InterpolationMethod, InterpolationStage, Origin
from .base import ArtistParameters, CmapParameters


@dataclass
class ImshowParameters(CmapParameters, ArtistParameters, Subparameters):
    """
    Parameters for the imshow plot.

    Attributes:
    ----------
    cmap, vmin, vmax
        See base.cmap.CmapParameters.
    norm: Normalize | None
        Data normalization before colormap mapping.
    aspect: Aspect | float | None
        The aspect ratio of the axes.
    interpolation: InterpolationMethod | None
        The interpolation method used for resampling.
    interpolation_stage: InterpolationStage | None
        The stage at which interpolation is performed.
    alpha: float | None
        The alpha blending value between 0 and 1.
    zorder: float | None
        Drawing order of the image.
    origin: Origin | None
        Place the [0, 0] index of the array in upper left or lower left.
    extent: tuple[float, float, float, float] | None
        Bounding box in data coordinates: (left, right, bottom, top).
    filternorm: bool
        Parameter for the antigrain image resize filter.
    filterrad: float
        Filter radius for filters that have a radius parameter.
    resample: bool
        Whether to use full resampling.
    url: str | None
        URL of the created AxesImage.
    """

    norm: Normalize | None = None
    aspect: Aspect | float | None = None
    interpolation: InterpolationMethod | None = None
    interpolation_stage: InterpolationStage | None = None
    origin: Origin | None = None
    extent: tuple[float, float, float, float] | None = None
    filternorm: bool = True
    filterrad: float = 4.0
    resample: bool = True
    url: str | None = None

    def __post_init__(self):
        super().__post_init__()
        if self.filterrad <= 0:
            raise ValueError("filterrad must be greater than 0")
        if self.extent is not None and len(self.extent) != 4:
            raise ValueError("extent must be a tuple of 4 floats: (left, right, bottom, top)")
