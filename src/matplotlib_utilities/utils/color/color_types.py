"""Re-export palette types from the color package; small shims for matplotlib-only shapes."""

from __future__ import annotations

from typing import TypeAlias

from color import ColorType, HexType, HsvFloatType, RgbFloatType, RgbIntType, RgbaIntType
from matplotlib.typing import ColorType as MplColorType
from numpy.typing import ArrayLike

MplColor: TypeAlias = ColorType | MplColorType
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
