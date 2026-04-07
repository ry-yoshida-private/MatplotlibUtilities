from enum import Enum


class Aspect(Enum):
    """
    Aspect ratio options for matplotlib imshow.

    Attributes:
    ----------
    EQUAL: Ensures square pixels.
    AUTO: Adjusts to fit data.
    """
    EQUAL = "equal"
    AUTO = "auto"
