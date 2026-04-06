# matplotlib_utilities

## Overview

`matplotlib_utilities` builds publication-style multi-panel figures by combining:

- layout (`GraphLayout`, `TableAxis`)
- global figure parameters (`GraphParameters`)
- per-plot kwargs as dataclasses (`subparameters`)
- a coordinator (`MatplotGraphMaker`) that creates the figure/axes and dispatches drawing calls

## Components

| Component | Description |
| --------- | ----------- |
| [`maker.py`](./maker.py) | `MatplotGraphMaker`: figure/axes creation, scatter/plot/imshow, colorbar, legend, lines, labels, tick styling |
| [`parameter.py`](./parameter.py) | `GraphParameters`: font size, spacing, DPI, figure size, aspect ratio limits |
| [`layout.py`](./layout.py) | `GraphLayout`: row/column grid and helpers such as `from_number` |
| [`table_axis.py`](./table_axis.py) | `TableAxis`: row-major vs column-major layout when deriving grids |
| [`graph_axis.py`](./graph_axis.py) | `GraphAxis`: X/Y axis enum for labels and related helpers |
| [`subparameters/`](./subparameters/README.md) | Dataclasses (`Subparameters` subclasses) and enums for Matplotlib kwargs |
| [`utils/`](./utils/README.md) | Markers, colormap enum, color typing, subplot index types, journal-style ticks |

