from dataclasses import dataclass

from ....subparameter import Subparameters


@dataclass
class ArtistParameters(Subparameters):
    """
    Common artist kwargs shared by many matplotlib draw calls.

    Attributes:
    ----------
    alpha: float | None
        Opacity (0 transparent, 1 opaque).
    zorder: float | None
        Drawing order where larger values are drawn on top.
    """

    alpha: float | None = None
    zorder: float | None = None

    def __post_init__(self) -> None:
        if self.alpha is not None and not (0.0 <= self.alpha <= 1.0):
            raise ValueError("alpha must be between 0 and 1")
        if self.zorder is not None and self.zorder < 0:
            raise ValueError("zorder must be non-negative")
