from dataclasses import dataclass

from .base_class import Subparameters
from .utils import (
    Aspect,
    Interpolation,
    InterpolationStage,
    Origin,
    )

@dataclass
class ImshowParameters(Subparameters):
    """
    Parameters for the imshow plot.
    
    Attributes:
    ----------
    cmap: str | None
        The colormap used to map scalar data to colors.
    norm: str | None
        The normalization method used to scale scalar data to the [0, 1] range.
    aspect: Aspect | float | None
        The aspect ratio of the axes. Use Aspect enum values for 'equal' or 'auto', or a float for custom ratio.
    interpolation: Interpolation | None
        The interpolation method used for resampling. Use Interpolation enum values.
    interpolation_stage: InterpolationStage | None
        The stage at which interpolation is performed. Use InterpolationStage enum values.
    alpha: float | None
        The alpha blending value, between 0 (transparent) and 1 (opaque).
    vmin: float | None
        The minimum value for the colormap scaling.
    vmax: float | None
        The maximum value for the colormap scaling.
    origin: Origin | None
        Place the [0, 0] index of the array in the upper left or lower left corner of the axes. Use Origin enum values.
    extent: tuple[float, float, float, float] | None
        The bounding box in data coordinates that the image will fill: (left, right, bottom, top).
    filternorm: bool
        A parameter for the antigrain image resize filter. If True, the filter normalizes 
        integer values and corrects rounding errors.
    filterrad: float
        The filter radius for filters that have a radius parameter (e.g., 'sinc', 'lanczos', 
        'blackman'). Must be > 0.
    resample: bool
        When True, use a full resampling method. When False, only resample when the output 
        image is larger than the input image.
    url: str | None
        Set the url of the created AxesImage.
    """
    cmap: str | None = None
    norm: str | None = None
    aspect: Aspect | float | None = None
    interpolation: Interpolation | None = None
    interpolation_stage: InterpolationStage | None = None
    alpha: float | None = None
    vmin: float | None = None
    vmax: float | None = None
    origin: Origin | None = None
    extent: tuple[float, float, float, float] | None = None
    filternorm: bool = True
    filterrad: float = 4.0
    resample: bool = True
    url: str | None = None

    def __post_init__(self):
        """
        Validate parameters after initialization.
        """
        if self.alpha is not None and not (0 <= self.alpha <= 1):
            raise ValueError("alpha must be between 0 and 1")
        if self.aspect is not None and not isinstance(self.aspect, (Aspect, float)):
            raise ValueError("aspect must be Aspect enum or a float")
        if self.origin is not None and not isinstance(self.origin, Origin):
            raise ValueError("origin must be Origin enum")
        if self.filterrad <= 0:
            raise ValueError("filterrad must be greater than 0")
        if self.extent is not None and len(self.extent) != 4:
            raise ValueError("extent must be a tuple of 4 floats: (left, right, bottom, top)")

    @property
    def to_dict(self) -> dict:
        """
        Convert parameters to a dictionary compatible with matplotlib.pyplot.imshow.
        """
        result = {}
        if self.cmap is not None:
            result["cmap"] = self.cmap
        if self.norm is not None:
            result["norm"] = self.norm
        if self.aspect is not None:
            result["aspect"] = self.aspect.value if isinstance(self.aspect, Aspect) else self.aspect
        if self.interpolation is not None:
            result["interpolation"] = self.interpolation.value
        if self.interpolation_stage is not None:
            result["interpolation_stage"] = self.interpolation_stage.value
        if self.alpha is not None:
            result["alpha"] = self.alpha
        if self.vmin is not None:
            result["vmin"] = self.vmin
        if self.vmax is not None:
            result["vmax"] = self.vmax
        if self.origin is not None:
            result["origin"] = self.origin.value
        if self.extent is not None:
            result["extent"] = self.extent
        result["filternorm"] = self.filternorm
        result["filterrad"] = self.filterrad
        result["resample"] = self.resample
        if self.url is not None:
            result["url"] = self.url
        return result