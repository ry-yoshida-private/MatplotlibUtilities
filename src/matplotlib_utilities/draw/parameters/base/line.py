from dataclasses import dataclass

from ....utils import Linestyle
from ....utils.color import MplColor
from .artist import ArtistParameters


@dataclass
class LineStyleParameters(ArtistParameters):
    """
    Common line-like kwargs shared by line/plot-style artists.
    """

    color: MplColor | None = None
    linewidth: float | None = None
    linestyle: Linestyle | None = None
    label: str | None = None
    antialiased: bool | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.linewidth is not None and self.linewidth <= 0:
            raise ValueError("linewidth must be positive")
