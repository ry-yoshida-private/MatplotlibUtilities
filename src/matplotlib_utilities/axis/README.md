# `axis` — `AxisOps` and tick kwargs

`AxisOps` is attached to `MatplotGraphMaker` as `maker.axis`. It targets a subplot via `SubplotIndex` and uses `GraphAxis` (`X` / `Y`) where the API is axis-specific.

## `maker.axis` methods

| Method | Purpose |
| ------ | ------- |
| `set_label(label, index, axis)` | `set_xlabel` / `set_ylabel` |
| `set_lim(lower, upper, index, axis)` | `set_xlim` / `set_ylim` |
| `delete_axis_label(index, subparams=...)` | `tick_params(**TickParamsParameters.to_dict)` to hide ticks/labels |

`TickParamsParameters` is defined under [`parameters/tick_params.py`](./parameters/tick_params.py). It is also exported from the package root for convenience.

## Code layout

| File | Role |
| ---- | ---- |
| [`axis_ops.py`](./axis_ops.py) | `AxisOps` implementation |

`GraphAxis` lives next to this package in [`../graph_axis.py`](../graph_axis.py).

Back to package overview: [../README.md](../README.md).
