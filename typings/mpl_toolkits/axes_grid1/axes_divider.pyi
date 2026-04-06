from typing import Any

from matplotlib.axes import Axes

class AxesDivider:
    def append_axes(
        self,
        loc: str,
        axes_class: type[Axes] | None = None,
        **kwargs: Any,
    ) -> Axes: ...
