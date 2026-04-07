from enum import Enum


class Orientation(Enum):
    """
    Orientation options for matplotlib elements (e.g., colorbar, legend).
    
    Attributes:
    ----------
    VERTICAL: Vertical orientation.
    HORIZONTAL: Horizontal orientation.
    """
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"

    @property
    def ax_line_attribute(self) -> str:
        match self:
            case Orientation.VERTICAL:
                return "axvline"
            case Orientation.HORIZONTAL:
                return "axhline"
