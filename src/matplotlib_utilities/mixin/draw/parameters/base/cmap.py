from __future__ import annotations

import math
from dataclasses import dataclass

from .....utils import ColorMap


@dataclass
class CmapParameters:
    """
    Parameters for colormap scaling (cmap, vmin, vmax).
    """

    cmap: str | None = None
    vmin: float | None = None
    vmax: float | None = None

    def __post_init__(self) -> None:
        self._validate_values()
        if self.cmap is not None:
            ColorMap(self.cmap)
        post_init = getattr(super(), "__post_init__", None)
        if callable(post_init):
            post_init()

    def _validate_values(self) -> None:
        vmin = self.vmin
        vmax = self.vmax
        if vmin is None or vmax is None:
            return

        vmin, vmax = float(vmin), float(vmax)
        for name, value in (("vmin", vmin), ("vmax", vmax)):
            if not math.isfinite(value):
                raise ValueError(f"{name} must be finite")
        if vmin > vmax:
            raise ValueError("vmin must be less than or equal to vmax")
