# `draw` — `Draw` and plot kwargs

`Draw` is attached to `MatplotGraphMaker` as `maker.draw`. It forwards to Matplotlib axes methods using optional `*Parameters` dataclasses (see [`parameters/`](./parameters/__init__.py)); each dataclass exposes `to_dict` for kwargs.

## `maker.draw` methods

| Method | Subparameters | Underlying API |
| ------ | ------------- | -------------- |
| `plot(x, y, index, subparams=...)` | `PlotParameters` | `Axes.plot` |
| `scatter(x, y, index, subparams=...)` | `ScatterParameters` | `Axes.scatter` |
| `imshow(image, index, subparams=...)` | `ImshowParameters` | `Axes.imshow` |
| `set_colorbar(index=..., image=..., subparams=...)` | `ColorbarParameters` | `Figure.colorbar` + `make_axes_locatable` |
| `legend(index, subparams=...)` | `LegendParameters` | `Axes.legend` |
| `line(value, orientation, index, subparams=...)` | `LineParameters` | `axhline` / `axvline` via `Orientation` |
| `arrow(x, y, dx, dy, index, subparams=...)` | `ArrowParameters` | `Axes.arrow` |

**Not implemented:** `imscatter`, `hist`, `bar` (currently raise `NotImplementedError`).

## Code layout

| File | Role |
| ---- | ---- |
| [`drawing.py`](./drawing.py) | `Draw` implementation |
| [`parameters/`](./parameters/) | Dataclasses and re-exported enums (`Aspect`, `Linestyle`, …) |

Package root exports the common `*Parameters` types and enums; extra symbols (e.g. `Subparameters`, `ArrowParameters`) are available from `matplotlib_utilities.draw.parameters`.

Back to package overview: [../README.md](../README.md).
