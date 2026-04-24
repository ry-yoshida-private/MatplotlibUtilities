from dataclasses import dataclass

from .....utils import Linestyle
from .....utils.color import MplColor


@dataclass
class LineStyleParameters:
    """
    Common line-like kwargs shared by line and plot style artists.
    """

    color: MplColor | None = None
    linewidth: float | None = None
    linestyle: Linestyle | None = None
    antialiased: bool | None = None

    def __post_init__(self) -> None:
        if self.linewidth is not None and self.linewidth <= 0:
            raise ValueError("linewidth must be positive")
