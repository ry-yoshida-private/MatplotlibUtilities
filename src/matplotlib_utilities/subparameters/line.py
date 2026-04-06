from dataclasses import dataclass

from ..utils.color_types import MplColor
from .base_class import Subparameters

@dataclass
class LineParameters(Subparameters):
    """
    Parameters for the line.

    TODO: Add more parameters.
    """
    color: MplColor | None = None

