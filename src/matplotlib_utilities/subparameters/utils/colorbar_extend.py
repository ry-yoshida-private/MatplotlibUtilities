from enum import Enum


class ColorbarExtend(Enum):
    """
    Extend options for matplotlib colorbar.
    
    Attributes:
    ----------
    NEITHER: No extensions.
    BOTH: Extend on both ends.
    MIN: Extend on minimum end.
    MAX: Extend on maximum end.
    """
    NEITHER = "neither"
    BOTH = "both"
    MIN = "min"
    MAX = "max"
