from dataclasses import dataclass, Field
from typing import Any, Sequence
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize, Colormap
from matplotlib.ticker import Locator
from matplotlib.ticker import Formatter
from matplotlib.axes import Axes
from mpl_toolkits.axes_grid1.axes_divider import AxesDivider


from ...subparameter import Subparameters
from ...utils import (
    ColorMap,
    ColorbarExtend,
    ColorbarSpacing,
    Location,
    Orientation,
    )

@dataclass
class ColorbarParameters(Subparameters):
    """
    Parameters for the colorbar.
    
    Attributes:
    ----------
    label: str | None = None
        The label of the colorbar.
    cmap: ColorMap | None = None
        The colormap of the colorbar.
    vmin: float | None = None
        The minimum value of the colorbar.
    vmax: float | None = None
        The maximum value of the colorbar.
    location: Location | None = None
        The location, relative to the parent Axes, where the colorbar Axes is created.
        It also determines the orientation of the colorbar.
    orientation: Orientation | None = None
        The orientation of the colorbar. It is preferable to set the location
        of the colorbar, as that also determines the orientation.
    fraction: float = 0.15
        Fraction of original Axes to use for colorbar.
    shrink: float = 1.0
        Fraction by which to multiply the size of the colorbar.
    aspect: float = 20
        Ratio of long to short dimensions.
    pad: float | None = None
        Fraction of original Axes between colorbar and new image Axes.
        Defaults to 0.05 if vertical, 0.15 if horizontal.
    anchor: tuple[float, float] | None = None
        The anchor point of the colorbar Axes.
        Defaults to (0.0, 0.5) if vertical; (0.5, 1.0) if horizontal.
    panchor: tuple[float, float] | bool | None = None
        The anchor point of the colorbar parent Axes.
        If False, the parent axes' anchor will be unchanged.
        Defaults to (1.0, 0.5) if vertical; (0.5, 0.0) if horizontal.
    extend: ColorbarExtend = ColorbarExtend.NEITHER
        Make pointed end(s) for out-of-range values.
    extendfrac: None | str | float | tuple[float, float] = None
        Length of triangular colorbar extensions as a fraction of the interior colorbar length.
        If 'auto', makes extensions the same lengths as interior boxes.
    extendrect: bool = False
        If False the extensions will be triangular (the default).
        If True the extensions will be rectangular.
    ticks: None | list | Locator = None
        If None, ticks are determined automatically from the input.
    format: None | str | Formatter = None
        If None, ScalarFormatter is used. Format strings are supported.
    drawedges: bool = False
        Whether to draw lines at color boundaries.
    boundaries: None | Sequence = None
        If unset, the colormap will be displayed on a 0-1 scale.
    values: None | Sequence = None
        Must have a length 1 less than boundaries if boundaries is set.
    spacing: ColorbarSpacing | None = None
        For discrete colorbars, 'uniform' gives each color the same space;
        'proportional' makes the space proportional to the data interval.
    """
    label: str | None = None
    cmap: ColorMap | None = None
    vmin: float | None = None
    vmax: float | None = None
    location: Location | None = None
    orientation: Orientation | None = None
    fraction: float = 0.15
    shrink: float = 1.0
    aspect: float = 20
    pad: float | None = None
    anchor: tuple[float, float] | None = None
    panchor: tuple[float, float] | bool | None = None
    extend: ColorbarExtend = ColorbarExtend.NEITHER
    extendfrac: None | str | float | tuple[float, float] = None
    extendrect: bool = False
    ticks: None | list[float] | Locator = None
    format: None | str | Formatter = None
    drawedges: bool = False
    boundaries: None | Sequence[float] = None
    values: None | Sequence[float] = None
    spacing: ColorbarSpacing | None = None

    def __post_init__(self):
        """
        Validate parameters after initialization.
        """
        if self.fraction <= 0 or self.fraction > 1:
            raise ValueError("fraction must be between 0 and 1")
        if self.shrink <= 0 or self.shrink > 1:
            raise ValueError("shrink must be between 0 and 1")
        if self.aspect <= 0:
            raise ValueError("aspect must be greater than 0")
        if self.pad is not None and (self.pad <= 0 or self.pad > 1):
            raise ValueError("pad must be between 0 and 1")
        if self.anchor is not None:
            if len(self.anchor) != 2:
                raise ValueError("anchor must be a tuple of 2 floats")
        if self.panchor is not None and isinstance(self.panchor, tuple):
            if len(self.panchor) != 2:
                raise ValueError("panchor must be a tuple of 2 floats")
        if self.extend not in [ColorbarExtend.NEITHER, ColorbarExtend.BOTH, ColorbarExtend.MIN, ColorbarExtend.MAX]:
            raise ValueError("extend must be ColorbarExtend enum")
        if self.extendfrac is not None:
            if isinstance(self.extendfrac, tuple) and len(self.extendfrac) != 2:
                raise ValueError("extendfrac tuple must have 2 elements")
        if self.extendrect and self.extend == ColorbarExtend.NEITHER:
            raise ValueError("extendrect can only be True if extend is not NEITHER")
        if self.drawedges and self.boundaries is None:
            raise ValueError("drawedges can only be True if boundaries is set")
        if self.boundaries is not None and self.values is not None:
            if len(self.boundaries) != len(self.values) + 1:
                raise ValueError("boundaries must have a length 1 greater than values")

    def _get_vmin_vmax(
        self, 
        image: np.ndarray | None
        ) -> tuple[float, float]:
        """
        Get vmin and vmax values, using image data if not specified.
        
        Parameters
        ----------
        image: np.ndarray | None
            The image data to determine the scale from.
            If None, vmin and vmax must be specified in the parameters.
            
        Returns
        -------
        tuple[float, float]
            The (vmin, vmax) tuple.
            
        Raises
        ------
        ValueError
            If image is None and both vmin and vmax are not specified.
        """
        vmin = self.vmin
        vmax = self.vmax

        if image is not None:
            if vmin is None: 
                vmin = float(image.min())
            if vmax is None: 
                vmax = float(image.max())
        
        if vmin is None or vmax is None:
            raise ValueError("Either image must be provided, or both vmin and vmax must be specified.")
            
        return vmin, vmax

    def create_scalar_mappable(
        self, 
        image: np.ndarray | None = None
        ) -> ScalarMappable:
        """
        Create a ScalarMappable for the colorbar without displaying the image.
        
        Parameters
        ----------
        image: np.ndarray | None = None
            The image data to determine the colorbar scale from.
            If None, vmin and vmax must be specified in the parameters.
            
        Returns
        -------
        ScalarMappable
            The ScalarMappable object for creating the colorbar.
        """
        vmin, vmax = self._get_vmin_vmax(image)
        
        # Get colormap
        if self.cmap is None:
            self.cmap = ColorMap.VIRIDIS
        cmap_obj: Colormap = self.cmap.colormap_object
        
        # Create ScalarMappable
        norm = Normalize(vmin=vmin, vmax=vmax)
        sm = ScalarMappable(norm=norm, cmap=cmap_obj)
        sm.set_array([])  # Empty array since we're not displaying the image
        
        return sm

    def create_cax(
        self,
        divider: AxesDivider
        ) -> Axes:
        """
        Append colorbar axes to *divider* and return the new Axes.

        Parameters
        ----------
        divider: AxesDivider
            Divider for the parent axes (from make_axes_locatable).

        Returns
        -------
        Axes
            The colorbar axes.
        """
        location = self.location.value if self.location is not None else Location.RIGHT.value
        cax: Axes = divider.append_axes(
            loc=location,
            size=f"{self.fraction * 100}%",
            pad=self.pad
            )
        return cax

    def _to_dict_skip_field(self, field: Field[Any], value: Any) -> bool:
        return value == field.default
