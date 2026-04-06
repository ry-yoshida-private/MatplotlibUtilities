# subparameters

## Overview

This package holds **dataclass-based subparameters**: each class subclasses [`Subparameters`](./base_class.py) and implements `to_dict` for safe forwarding of kwargs to Matplotlib (skipping `None`, unwrapping enum-like `.value` when present).

Shared enums and small helpers used by those dataclasses live in [`subparameters/utils/`](./utils/README.md).

## Components

| Component | Description |
| --------- | ----------- |
| [`base_class.py`](./base_class.py) | Abstract `Subparameters` base with `to_dict` |
| [`scatter.py`](./scatter.py) | `ScatterParameters` for `Axes.scatter` |
| [`plot.py`](./plot.py) | `PlotParameters` for `Axes.plot` |
| [`line.py`](./line.py) | `LineParameters` for reference lines (`draw_line`, etc.) |
| [`imshow.py`](./imshow.py) | `ImshowParameters` for `Axes.imshow` |
| [`tick_params.py`](./tick_params.py) | `TickParamsParameters` for `Axes.tick_params` |
| [`colorbar.py`](./colorbar.py) | `ColorbarParameters` plus scalar mappable helpers |
| [`legend.py`](./legend.py) | `LegendParameters` for `Axes.legend` |
| [`utils/`](./utils/README.md) | Enums: aspect, interpolation, origin, location, orientation, colorbar extend/spacing |

## Imports

The top-level `matplotlib_utilities` package exposes a subset of symbols from here; use `matplotlib_utilities.subparameters` when you need every parameter class and enum (`ScatterParameters`, `ImshowParameters`, `PlotParameters`, `LineParameters`, `Subparameters`, etc.).
