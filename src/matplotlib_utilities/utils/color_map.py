from enum import Enum

from matplotlib.cm import get_cmap
from matplotlib.colors import Colormap

class ColorMap(Enum):
    # --- Perceptually Uniform Sequential ---
    MAGMA = 'magma'
    INFERNO = 'inferno'
    PLASMA = 'plasma'
    VIRIDIS = 'viridis'
    CIVIDIS = 'cividis'
    TURBO = 'turbo'

    # --- Sequential ---
    BLUES = 'Blues'
    GREENS = 'Greens'
    GREYS = 'Greys'
    ORANGES = 'Oranges'
    PURPLES = 'Purples'
    REDS = 'Reds'
    YlGn = 'YlGn'
    YlOrRd = 'YlOrRd'

    # --- Diverging ---
    BRBG = 'BrBG'
    PRGN = 'PRGn'
    PIYG = 'PiYG'
    PUOR = 'PuOr'
    RDBU = 'RdBu'
    RDGY = 'RdGy'
    RDYLBU = 'RdYlBu'
    RDYLGN = 'RdYlGn'
    SPECTRAL = 'Spectral'
    COOLWARM = 'coolwarm'
    SEISMIC = 'seismic'

    # --- Qualitative ---
    ACCENT = 'Accent'
    DARK2 = 'Dark2'
    PAIRED = 'Paired'
    PASTEL1 = 'Pastel1'
    SET1 = 'Set1'
    TAB10 = 'tab10'
    TAB20 = 'tab20'

    # --- Cyclic ---
    TWILIGHT = 'twilight'
    TWILIGHT_SHIFTED = 'twilight_shifted'

    # --- Miscellaneous / Legacy ---
    HOT = 'hot'
    JET = 'jet'
    RAINBOW = 'rainbow'
    TERRAIN = 'terrain'
    BINARY = 'binary'
    BONE = 'bone'
    COOL = 'cool'
    COPPER = 'copper'   

    def is_reversed(self) -> bool:
        """
        Check if the colormap is reversed.

        Returns
        -------
        bool
            True if the colormap is reversed, False otherwise.
        """
        return self.value.endswith('_r')

    @property
    def colormap_object(self) -> Colormap:
        """
        Get the colormap object.

        Returns
        -------
        Colormap
            The colormap object.
        """
        return get_cmap(self.value)

