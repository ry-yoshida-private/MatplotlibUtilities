from dataclasses import dataclass
from typing import Any


from ...utils.color import MplColor
from .base import ArtistParameters


@dataclass
class AnnotateParameters(ArtistParameters):
    """
    Optional keyword arguments for :meth:`matplotlib.axes.Axes.annotate`.

    text, xy, and xytext are passed positionally or explicitly from :meth:`Draw.annotate`;
    this dataclass holds the coordinate system, arrow properties, and text styling.

    Attributes:
    ----------
    xycoords: str | Any | None
        The coordinate system that xy is given in.
    textcoords: str | Any | None
        The coordinate system that xytext is given in.
    arrowprops: dict[str, Any] | None
        The properties used to draw a FancyArrowPatch arrow between the positions.
    annotation_clip: bool | None
        Whether to clip the annotation when it is outside the axes area.
    color: MplColor | None
        The color of the text.
    fontsize: float | str | None
        The size of the font.
    fontweight: str | int | None
        The weight of the font.
    ha: str | None
        The horizontal alignment of the text.
    va: str | None
        The vertical alignment of the text.
    alpha: float | None
        The alpha of the text and arrow.
    rotation: float | str | None
        The rotation of the text in degrees.
    rotation_mode: str | None
        The rotation mode of the text ('default' or 'anchor').
    zorder: float | None
        The order of the annotation.
    visible: bool | None
        Whether the annotation is visible.
    """

    # Annotation specific
    xycoords: str | Any | None = None
    textcoords: str | Any | None = None
    arrowprops: dict[str, Any] | None = None
    annotation_clip: bool | None = None

    # Text styling
    color: MplColor | None = None
    fontsize: float | str | None = None
    fontweight: str | int | None = None
    ha: str | None = None
    va: str | None = None
    rotation: float | str | None = None
    rotation_mode: str | None = None
    visible: bool | None = None

    def __post_init__(self):
        """
        Validate parameters after initialization.
        """
        super().__post_init__()
        if self.fontsize is not None and isinstance(self.fontsize, (int, float)) and self.fontsize <= 0:
            raise ValueError("fontsize must be positive")