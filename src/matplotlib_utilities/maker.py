from cProfile import label
import numpy as np
import gc
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import Colorbar
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import AxesDivider

from .utils import (
    SubplotIndex,
    RowColumnIndex,
    ColorMap,

    )
from .layout import GraphLayout
from .parameter import GraphParameters
from .graph_axis import GraphAxis
from .subparameters import (
    # Parameters
    ScatterParameters,
    ImshowParameters,
    TickParamsParameters,
    ColorbarParameters,
    PlotParameters,
    LineParameters,
    LegendParameters,
    # Enums
    Orientation,
    )

class MatplotGraphMaker:
    """
    A class for making matplotlib graphs.

    Attributes:
    ----------
    layout: GraphLayout
        The layout of the matplotlib graphs.
    params: GraphParameters
        The parameters for the MatplotGraphMaker.
    fig: Figure
        The figure of the matplotlib graphs.
    ax: np.ndarray
        The axes of the matplotlib graphs.
    """
    def __init__(
        self, 
        layout: GraphLayout | None = None,
        parameters: GraphParameters | None = None
        ) -> None:
        """
        Initialize the MatplotGraphMaker.

        Parameters
        ----------
        layout: GraphLayout
            The layout of the matplotlib graphs.
        params: GraphParameters
            The parameters for the MatplotGraphMaker.
        """
        self.layout: GraphLayout = layout or GraphLayout(number=1, column=1, row=1)
        self.parameters: GraphParameters = parameters or GraphParameters()
        self.fig, self.ax = self._create_canvas()

    def finalize(
        self, 
        save_path: str | None = None,
        is_showing_result_enabled: bool = True
        ) -> None:
        """
        Finalize the matplotlib graphs.
        -> Saving the figure and showing the result.

        Parameters
        ----------
        save_path: str | None = None
            The path to save the figure.
        is_showing_result_enabled: bool = True
            Whether to show the result.
        """
        plt.subplots_adjust(
            wspace=self.parameters.w_space, 
            hspace=self.parameters.h_space
            )
        if save_path is not None:
            plt.savefig(save_path, bbox_inches='tight')
        
        if is_showing_result_enabled:
            plt.show()
        else:
            plt.close()
            gc.collect()

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
            The index of the subplot. If None, the colorbar will be added to the entire figure.
        image: np.ndarray | None = None
            The image data to determine the colorbar scale from.
            If None, vmin and vmax must be specified in subparams.
        subparams: ColorbarParameters | None = None
            The subparameters for the colorbar.
        """
        subparams = subparams or ColorbarParameters()
        sm: ScalarMappable = subparams.create_scalar_mappable(image)
        ax: Axes | None = None if index is None else self._access_subplot(index=index)

        divider: AxesDivider = make_axes_locatable(ax)
        cax: Axes = subparams.create_cax(divider=divider)
        cbar: Colorbar = plt.colorbar(sm, cax=cax)
        if subparams.label is not None:
            cbar.set_label(subparams.label)

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
        getattr(self.ax[row_index, column_index], axis_attribute)(label)

    def imshow(
        self,
        image: np.ndarray,
        index: SubplotIndex,
        subparams: ImshowParameters | None = None
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
        subplot = self._access_subplot(index=index)
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
        subplot = self._access_subplot(index=index)
        subplot.plot(x, y, **subparams.to_dict)

    def scatter(
        self, 
        x: np.ndarray, 
        y: np.ndarray,
        index: SubplotIndex,
        confidences: np.ndarray | None = None,
        subparams: ScatterParameters | None = None
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
        confidences: np.ndarray | None = None
            The confidences of the data.
        subparams: ScatterParameters | None = None
            The subparameters for the scatter plot.
        """
        subparams = subparams or ScatterParameters()
        subplot = self._access_subplot(index=index)
        scatter_kwargs = subparams.to_dict.copy()
        if confidences is not None:
            scatter_kwargs["c"] = confidences
        subplot.scatter(
            x=x, 
            y=y, 
            **scatter_kwargs
            )

    def imscatter(self):
        raise NotImplementedError("Not implemented yet.")

    def hist(self):
        raise NotImplementedError("Not implemented yet.")
    
    def bar(self):
        raise NotImplementedError("Not implemented yet.")

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
        subplot = self._access_subplot(index=index)
        subplot.legend(**subparams.to_dict)

    def delete_axis_label(
        self, 
        index: SubplotIndex, 
        subparams: TickParamsParameters | None = None
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
        subplot = self._access_subplot(index=index)
        subplot.tick_params(**subparams.to_dict)

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
        upper: floatgetattr(subplot, attribute)(lower, upper)
            The upper limit.
        index: SubplotIndex
            The index of the subplot.
        axis: GraphAxis
            The axis to set the limit on.
        """
        subplot = self._access_subplot(index=index)
        attribute = axis.limit_set_attribute
        getattr(subplot, attribute)(lower, upper)

    def draw_line(
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
        subplot = self._access_subplot(index=index)
        attribute = orientation.ax_line_attribute
        getattr(subplot, attribute)(x=value, **subparams.to_dict)

    def get_subplot_index_from_number(
        self, 
        number: int
        ) -> SubplotIndex:
        """
        Get the subplot index from the number.

        Parameters
        ----------
        number: int
            The number of the subplot.
        """
        row_index, column_index = self.layout.from_number_to_row_column_index(number=number)
        return RowColumnIndex(
            row_index=row_index, 
            column_index=column_index
            )

    def get_subplot_index_from_row_column(
        self, 
        row_index: int, 
        column_index: int
        ) -> SubplotIndex:
        """
        Get the subplot index from the row and column.

        Parameters
        ----------
        row_index: int
            The index of the row.
        column_index: int
            The index of the column.
        """
        return RowColumnIndex(
            row_index=row_index, 
            column_index=column_index
            )

    def _access_subplot(
        self, 
        index: SubplotIndex
        ) -> Axes:
        """
        Access the subplot.

        Parameters
        ----------
        index: SubplotIndex
            The index of the subplot.
        """
        row_index, column_index = index.tuple
        return self.ax[row_index, column_index]

    def _create_canvas(self) -> tuple[Figure, np.ndarray]:
        """
        Create a canvas for the matplotlib graphs.

        Returns
        -------
        tuple[Figure, np.ndarray]:
            A tuple of the figure and the axes.
        """
        row = self.layout.row
        column = self.layout.column
        plt.rcParams["font.size"] = self.parameters.font_size
        fig, ax = plt.subplots(
            row, 
            column, 
            dpi=self.parameters.dpi, 
            figsize=self.parameters.figsize, 
            squeeze=False
            )   
        return fig, ax


#######################################################

def main():
    import numpy as np
    
    from .parameter import GraphParameters
    from .maker import MatplotGraphMaker
    from .graph_axis import GraphAxis
    from .layout import GraphLayout
    from .utils import (
        SubplotNumber,
        RowColumnIndex,
        SubplotIndex,
        SubplotNumber,
        )
    from .table_axis import TableAxis

    num_graph = 4

    layout = GraphLayout.from_number(
        number=num_graph,
        axis=TableAxis.COLUMN,
        axis_value=num_graph // 2
        )
    params = GraphParameters()
    graph_maker = MatplotGraphMaker(
        layout=layout,
        parameters=params
        )
    
    x1 = np.random.randn(100)
    y1 = np.random.randn(100)
    confidences = np.random.rand(100) 
    index = graph_maker.get_subplot_index_from_number(number=0)
    graph_maker.scatter(
        index=index,
        x=x1,
        y=y1,
        confidences=confidences
        )
    graph_maker.set_label(
        label="x",
        index=SubplotNumber(number=0, row_index=0),
        axis=GraphAxis.X
        )
    index = graph_maker.get_subplot_index_from_number(number=1)
    graph_maker.plot(
        index=index,
        x=x1,
        y=y1,
        subparams=None
        )
    graph_maker.draw_line(
        value=0.5,
        orientation=Orientation.VERTICAL,
        index=graph_maker.get_subplot_index_from_number(number=1),
        subparams=LineParameters(
            color="red"
            )
        )

if __name__ == "__main__":
    main()