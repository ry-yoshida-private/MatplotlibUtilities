from dataclasses import dataclass

from ...utils.color import MplColor
from ...subparameter import Subparameters

@dataclass
class LineParameters(Subparameters):
    """
    Parameters for the line.

    TODO: Add more parameters.
    """
    color: MplColor | None = None

