# utils

## Overview

Helper types shared across the package: **subplot indexing**, **markers**, a **colormap enum**, **structured color types** (including integration with the external `color` package), and a small **journal-style tick** helper.

## Components

| Component | Description |
| --------- | ----------- |
| [`index/`](./index/README.md) | `SubplotIndex` (union), `RowColumnIndex`, `SubplotNumber` |
| [`marker.py`](./marker.py) | `Marker` helper for marker styles |
| [`color_map.py`](./color_map.py) | `ColorMap` enum wrapping common Matplotlib colormap names |
| [`color_types.py`](./color_types.py) | Typed color aliases (`MplColor`, `ScatterColorArg`, RGB/RGBA/HSV forms, etc.) |
| [`to_journal_format.py`](./to_journal_format.py) | `to_journal_format(ax, ...)` for outward major/minor ticks |

`matplotlib_utilities.utils` is the usual import path for `Marker`, index types, `ColorMap`, and color type aliases. `to_journal_format` is used internally by `MatplotGraphMaker`; import it from `matplotlib_utilities.utils.to_journal_format` if you need it directly.
