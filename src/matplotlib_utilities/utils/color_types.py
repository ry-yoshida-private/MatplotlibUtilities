"""Re-export palette types from ``color``; small shims for matplotlib-only shapes."""

from __future__ import annotations

from typing import TypeAlias

from color import ColorType, HexType, HsvFloatType, RgbFloatType, RgbIntType, RgbaIntType
from matplotlib.typing import ColorType as MplColorType
from numpy.typing import ArrayLike

# ``color.ColorType`` covers hex / RGB / HSV / ndarray forms used with this library.
# Union adds matplotlib-only literals such as ``(rgb, alpha)`` pairs and float RGBA 4-tuples.
MplColor: TypeAlias = ColorType | MplColorType

# ``scatter(..., c=...)`` / ``edgecolors``: palette colors plus general array-likes (e.g. colormap scalars).
ScatterColorArg: TypeAlias = ColorType | ArrayLike

__all__ = [
    "ColorType",
    "HexType",
    "HsvFloatType",
    "MplColor",
    "RgbFloatType",
    "RgbIntType",
    "RgbaIntType",
    "ScatterColorArg",
]
