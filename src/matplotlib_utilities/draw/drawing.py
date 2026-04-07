# pyright: reportUnknownMemberType=false

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
from matplotlib.axes import Axes
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import Colorbar
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import AxesDivider

from .parameters import (
    AnnotateParameters,
    ArrowParameters,
    ColorbarParameters,
    ImshowParameters,
    LegendParameters,
    LineParameters,
    Orientation,
    PlotParameters,
    ScatterParameters,
    )
from ..utils import SubplotIndex

if TYPE_CHECKING:
    from ..maker import MatplotGraphMaker


class Draw:
    """
    Drawing operations for :class:`MatplotGraphMaker`, exposed as maker.draw.
    """

    __slots__ = ("_maker",)

    def __init__(self, maker: MatplotGraphMaker) -> None:
        self._maker = maker

    def set_colorbar(
        self,
        index: SubplotIndex | None = None,
        image: np.ndarray | None = None,
        subparams: ColorbarParameters | None = None,
    ) -> None:
        """
        Draw the colorbar on the subplot without displaying the image.

        Parameters
        ----------
        index: SubplotIndex | None = None
            The index of the subplot. If None, the colorbar is anchored from the first subplot
            (same figure; use when a single shared colorbar is intended).
        image: np.ndarray | None = None
            The image data to determine the colorbar scale from.
            If None, vmin and vmax must be specified in subparams.
        subparams: ColorbarParameters | None = None
            The subparameters for the colorbar.
        """
        subparams = subparams or ColorbarParameters()
        sm: ScalarMappable = subparams.create_scalar_mappable(image)
        ax: Axes = (
            self._maker.ax.flat[0]
            if index is None
            else self._maker.access_subplot(index=index)
        )

        divider: AxesDivider = make_axes_locatable(ax)
        cax: Axes = subparams.create_cax(divider=divider)
        cbar: Colorbar = self._maker.fig.colorbar(sm, cax=cax)
        if subparams.label is not None:
            cbar.set_label(subparams.label)

    def imshow(
        self,
        image: np.ndarray,
        index: SubplotIndex,
        subparams: ImshowParameters | None = None,
    ) -> None:
        """
        Show the image on the subplot.

        Parameters
        ----------
        image: np.ndarray
            The image to show.
        index: SubplotIndex
            The index of the subplot.
        subparams: ImshowParameters | None = None
            The subparameters for the imshow plot.
        """
        subparams = subparams or ImshowParameters()
        subplot = self._maker.access_subplot(index=index)
        subplot.imshow(image, **subparams.to_dict)

    def plot(
        self,
        x: np.ndarray,
        y: np.ndarray,
        index: SubplotIndex,
        subparams: PlotParameters | None = None,
    ) -> None:
        """
        Plot the data on the subplot.

        Parameters
        ----------
        x: np.ndarray
            The x values of the data.
        y: np.ndarray
            The y values of the data.
        index: SubplotIndex
            The index of the subplot.
        subparams: PlotParameters | None = None
            The subparameters for the plot.
        """
        subparams = subparams or PlotParameters()
        subplot = self._maker.access_subplot(index=index)
        subplot.plot(x, y, **subparams.to_dict)

    def arrow(
        self,
        x: float,
        y: float,
        dx: float,
        dy: float,
        index: SubplotIndex,
        subparams: ArrowParameters | None = None,
    ) -> None:
        """
        Draw an arrow from (x, y) to (x + dx, y + dy) on the subplot.

        Wraps :meth:`matplotlib.axes.Axes.arrow`. Matplotlib notes that this API can
        distort with aspect ratio; for publication-style arrows consider
        annotate with arrowprops instead.

        Parameters
        ----------
        x, y
            Base coordinates of the arrow.
        dx, dy
            Arrow vector in data coordinates.
        index
            Subplot index.
        subparams
            Geometry and patch keyword arguments (width, head shape, color, etc.).
        """
        subparams = subparams or ArrowParameters()
        subplot = self._maker.access_subplot(index=index)
        subplot.arrow(x, y, dx, dy, **subparams.to_dict)

    def scatter(
        self,
        x: np.ndarray,
        y: np.ndarray,
        index: SubplotIndex,
        subparams: ScatterParameters | None = None,
    ) -> None:
        """
        Scatter the data on the subplot.

        Parameters
        ----------
        x: np.ndarray
            The x values of the data.
        y: np.ndarray
            The y values of the data.
        index: SubplotIndex
            The index of the subplot.
        subparams: ScatterParameters | None = None
            The subparameters for the scatter plot (including *s* for marker area,
            per matplotlib scatter).
        """
        subparams = subparams or ScatterParameters()
        subplot = self._maker.access_subplot(index=index)
        subplot.scatter(x=x, y=y, **subparams.to_dict)

    def legend(
        self,
        index: SubplotIndex,
        subparams: LegendParameters | None = None,
    ) -> None:
        """
        Place a legend on the subplot.

        Parameters
        ----------
        index: SubplotIndex
            The index of the subplot.
        subparams: LegendParameters | None = None
            The subparameters for the legend.
        """
        subparams = subparams or LegendParameters()
        subplot = self._maker.access_subplot(index=index)
        subplot.legend(**subparams.to_dict)

    def line(
        self,
        value: float,
        orientation: Orientation,
        index: SubplotIndex,
        subparams: LineParameters | None = None,
    ) -> None:
        """
        Draw a line on the subplot.
        """
        subparams = subparams or LineParameters()
        subplot = self._maker.access_subplot(index=index)
        draw = getattr(subplot, orientation.ax_line_attribute)
        match orientation:
            case Orientation.VERTICAL:
                draw(x=value, **subparams.to_dict)
            case Orientation.HORIZONTAL:
                draw(y=value, **subparams.to_dict)

    def annotate(
        self,
        text: str,
        xy: tuple[float, float],
        index: SubplotIndex,
        xytext: tuple[float, float] | None = None,
        subparams: AnnotateParameters | None = None,
    ) -> None:
        """
        Annotate a point on the subplot with text.

        Wraps :meth:`matplotlib.axes.Axes.annotate`. Required inputs are the label
        string, the data point xy, and the subplot index; optional text placement
        and styling use xytext and subparams.

        Parameters
        ----------
        text
            The annotation string.
        xy
            The (x, y) point to annotate (data coordinates unless overridden by
            subparams.xycoords).
        index
            Subplot index.
        xytext
            If set, (x, y) where the text is drawn; coordinate system from
            subparams.textcoords. If None, matplotlib places text at xy.
        subparams
            Coordinate systems, arrow properties, clipping, and text styling
            (color, fontsize, ha, va, and related Text keywords).
        """
        subparams = subparams or AnnotateParameters()
        subplot = self._maker.access_subplot(index=index)
        subplot.annotate(text, xy, xytext=xytext, **subparams.to_dict)

    def imscatter(self) -> None:
        raise NotImplementedError("Not implemented yet.")

    def hist(self) -> None:
        raise NotImplementedError("Not implemented yet.")

    def bar(self) -> None:
        raise NotImplementedError("Not implemented yet.")