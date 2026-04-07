from enum import Enum


class ArrowShape(Enum):
    """
    shape for :meth:`matplotlib.axes.Axes.arrow` (left-half, right-half, or full arrow).
    """

    FULL = "full"
    LEFT = "left"
    RIGHT = "right"
