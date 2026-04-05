from dataclasses import dataclass

@dataclass
class TickParamsParameters:
    """
    Parameters for configuring tick marks and labels on matplotlib axes.

    Attributes:
    ----------
    bottom: bool = False
        Whether to show tick marks on the bottom axis.
    left: bool = False
        Whether to show tick marks on the left axis.
    right: bool = False
        Whether to show tick marks on the right axis.
    top: bool = False
        Whether to show tick marks on the top axis.
    labelbottom: bool = False
        Whether to show tick labels on the bottom axis.
    labelleft: bool = False
        Whether to show tick labels on the left axis.
    labelright: bool = False
        Whether to show tick labels on the right axis.
    labeltop: bool = False
        Whether to show tick labels on the top axis.
    """

    # Control visibility of tick marks (the small lines on the axes)
    bottom: bool = False
    left: bool = False
    right: bool = False
    top: bool = False
    
    # Control visibility of tick labels (the text values next to tick marks)
    labelbottom: bool = False
    labelleft: bool = False
    labelright: bool = False
    labeltop: bool = False

    @property
    def to_dict(self) -> dict:
        """
        Convert parameters to a dictionary compatible with matplotlib.pyplot.tick_params.

        Returns:
        --------
        dict: A dictionary of the parameters for matplotlib.pyplot.tick_params.
        """
        return {
            "bottom": self.bottom,
            "left": self.left,
            "right": self.right,
            "top": self.top,
            "labelbottom": self.labelbottom,
            "labelleft": self.labelleft,
            "labelright": self.labelright,
            "labeltop": self.labeltop,
            }