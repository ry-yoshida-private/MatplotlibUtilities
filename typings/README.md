# MatplotlibUtilities

## Overview

MatplotlibUtilities (`matplotlib_utilities`) is a small Python library that wraps common Matplotlib workflows: subplot layout, typed “subparameter” dataclasses for plot kwargs, and a `MatplotGraphMaker` facade for scatter, plot, imshow, colorbars, legends, and annotations.

For package structure and modules, see [src/matplotlib_utilities/README.md](src/matplotlib_utilities/README.md).

## Installation

Install runtime dependencies from the repository root:

```bash
pip install -r requirements.txt
```

The test suite expects the package on the path (see `pythonpath` in `pyproject.toml`). From the repo root you can run:

```bash
pytest
```

You can also install the package in editable mode with `pip install -e .` from the repository root (see `pyproject.toml`).

## Quick example

```python
import numpy as np
from matplotlib_utilities import (
    GraphLayout, 
    GraphParameters, 
    MatplotGraphMaker,
    PlotParameters,
    ScatterParameters
)

layout = GraphLayout.from_row_column(row=1, column=2)
maker = MatplotGraphMaker(layout=layout, parameters=GraphParameters())

x = np.linspace(0, 1, 50)
y = np.sin(x * 10)
z = np.cos(x * 10)

idx0 = maker.get_subplot_index_from_number(number=0)
idx1 = maker.get_subplot_index_from_number(number=1)
maker.plot(index=idx0, x=x, y=y, subparams=PlotParameters())
# Third quantity as color (matplotlib ``c``) on a 2D scatter.
maker.scatter(index=idx1, x=x, y=y, subparams=ScatterParameters(c=z, cmap="viridis"))
maker.finalize(is_showing_result_enabled=True)
```

## Notes

- `requirements.txt` includes a Git dependency for `color` (used with typed color arguments in subparameters).
- Subplot indexing types live under [`src/matplotlib_utilities/utils/index/`](src/matplotlib_utilities/utils/index/README.md).
