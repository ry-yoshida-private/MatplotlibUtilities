# pyright: reportUnknownMemberType=false

from __future__ import annotations

from typing import TYPE_CHECKING

from ..graph_axis import GraphAxis
from ..utils import SubplotIndex
from .parameters import TickParamsParameters

if TYPE_CHECKING:
    from ..maker import MatplotGraphMaker


class AxisOps:
    """
    Axis-related operations for :class:`MatplotGraphMaker`, exposed as maker.axis.
    """

    __slots__ = ("_maker",)

    def __init__(self, maker: MatplotGraphMaker) -> None:
        self._maker = maker

    def set_label(
        self,
        label: str,
        index: SubplotIndex,
        axis: GraphAxis,
    ) -> None:
        """
        Set the label on the subplot.

        Parameters
        ----------
        label: str
            The label to set.
        index: SubplotIndex
            The index of the subplot.
        axis: GraphAxis
            The axis to set the label on.
        """
        row_index, column_index = index.tuple
        axis_attribute = axis.label_set_attribute
        getattr(self._maker.ax[row_index, column_index], axis_attribute)(label)

    def set_lim(
        self,
        lower: float,
        upper: float,
        index: SubplotIndex,
        axis: GraphAxis,
    ) -> None:
        """
        Set the limit on the subplot.

        Parameters
        ----------
        lower: float
            The lower limit.
        upper: float
            The upper limit.
        index: SubplotIndex
            The index of the subplot.
        axis: GraphAxis
            The axis to set the limit on.
        """
        subplot = self._maker.access_subplot(index=index)
        attribute = axis.limit_set_attribute
        getattr(subplot, attribute)(lower, upper)

    def delete_axis_label(
        self,
        index: SubplotIndex,
        subparams: TickParamsParameters | None = None,
    ) -> None:
        """
        Delete the axis label on the subplot.

        Parameters
        ----------
        index: SubplotIndex
            The index of the subplot.
        subparams: TickParamsParameters | None = None
            The subparameters for the tick params.
        """
        subparams = subparams or TickParamsParameters()
        subplot = self._maker.access_subplot(index=index)
        subplot.tick_params(**subparams.to_dict)
