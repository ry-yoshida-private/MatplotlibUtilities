from dataclasses import dataclass

from ....subparameter import Subparameters
from ....utils import ArrowShape
from .base import ArtistParameters, LabelParameters, LineStyleParameters


@dataclass
class ArrowParameters(LineStyleParameters, LabelParameters, ArtistParameters, Subparameters):
    """
    Optional keyword arguments for matplotlib.axes.Axes.arrow.

    Attributes:
    ----------
    width: float | None
        The width of the arrow.
    length_includes_head: bool | None
        Whether to include the head in the length.
    head_width: float | None
        The width of the head.
    head_length: float | None
        The length of the head.
    shape: ArrowShape | None
        The shape of the arrow.
    overhang: float | None
        The overhang of the arrow.
    head_starts_at_zero: bool | None
        Whether to start the head at zero.
    edgecolor, facecolor
        See base.color.ColorParameters.
    fill: bool | None
        Whether to fill the arrow.
    """

    width: float | None = None
    length_includes_head: bool | None = None
    head_width: float | None = None
    head_length: float | None = None
    shape: ArrowShape | None = None
    overhang: float | None = None
    head_starts_at_zero: bool | None = None
    fill: bool | None = None

    def __post_init__(self) -> None:
        """
        Validate parameters after initialization.
        """
        super().__post_init__()
        if self.width is not None and self.width <= 0:
            raise ValueError("width must be positive")
        if self.head_width is not None and self.head_width <= 0:
            raise ValueError("head_width must be positive")
        if self.head_length is not None and self.head_length <= 0:
            raise ValueError("head_length must be positive")
        if self.overhang is not None and self.overhang <= 0:
            raise ValueError("overhang must be positive")
