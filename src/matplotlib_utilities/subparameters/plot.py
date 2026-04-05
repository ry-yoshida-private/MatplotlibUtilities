from dataclasses import dataclass

from .base_class import Subparameters


@dataclass
class PlotParameters(Subparameters):
    """
    Parameters for the plot.

    Attributes:
    ----------
    color: str | None
        The color of the plot.
    linewidth: float | None
        The width of the lines.
    linestyle: str | None
        The style of the lines.
    marker: str | None
        The marker of the plot.
    markersize: float | None
        The size of the markers.
    markeredgewidth: float | None
        The width of the marker edges.
    markeredgecolor: str | None
        The color of the marker edges.
    markerfacecolor: str | None
        The color of the marker faces.
    alpha: float | None
        The alpha of the plot.
    label: str | None
        The label of the plot.
    zorder: float | None
        The order of the plot.
    solid_capstyle: str | None
        The style of the cap of the lines.
    solid_joinstyle: str | None
        The style of the join of the lines.
    drawstyle: str | None
        The style of the drawing of the lines.
    antialiased: bool | None
        Whether to antialias the plot.
    """

    color: str | None = None
    linewidth: float | None = None
    linestyle: str | None = None
    marker: str | None = None
    markersize: float | None = None
    markeredgewidth: float | None = None
    markeredgecolor: str | None = None
    markerfacecolor: str | None = None
    alpha: float | None = None

    # Labeling
    label: str | None = None

    # Drawing order
    zorder: float | None = None

    # Other
    solid_capstyle: str | None = None
    solid_joinstyle: str | None = None
    drawstyle: str | None = None
    antialiased: bool | None = None

    @property
    def to_dict(self) -> dict:
        """
        Convert parameters to a dictionary compatible with matplotlib.pyplot.plot.
        """
        return {
            k: v
            for k, v in {
                "color": self.color,
                "linewidth": self.linewidth,
                "linestyle": self.linestyle,
                "marker": self.marker,
                "markersize": self.markersize,
                "markeredgewidth": self.markeredgewidth,
                "markeredgecolor": self.markeredgecolor,
                "markerfacecolor": self.markerfacecolor,
                "alpha": self.alpha,
                "label": self.label,
                "zorder": self.zorder,
                "solid_capstyle": self.solid_capstyle,
                "solid_joinstyle": self.solid_joinstyle,
                "drawstyle": self.drawstyle,
                "antialiased": self.antialiased,
            }.items()
            if v is not None
        }
