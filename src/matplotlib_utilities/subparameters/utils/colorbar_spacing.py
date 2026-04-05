from enum import Enum


class ColorbarSpacing(Enum):
    """
    Spacing options for matplotlib colorbar.
    
    Attributes:
    ----------
    UNIFORM: Each color gets the same space.
    PROPORTIONAL: Space is proportional to the data interval.
    """
    UNIFORM = "uniform"
    PROPORTIONAL = "proportional"
