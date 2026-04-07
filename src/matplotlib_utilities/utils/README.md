# utils

## Overview

Helper types shared across the package: **subplot indexing**, **markers**, a **colormap enum**, **structured color types** (including integration with the external `color` package), and **imshow/colorbar kwargs enums** (`Aspect`, `Location`, `ColorbarExtend`, …).

## Components

| Component | Description |
| --------- | ----------- |
| [`index/`](./index/README.md) | `SubplotIndex` (union), `RowColumnIndex`, `SubplotNumber` |
| [`marker.py`](./marker.py) | `Marker` helper for marker styles |
| [`color/`](./color/) | `ColorMap` enum (`color_map.py`) and typed color aliases (`color_types.py`: `MplColor`, `ScatterColorArg`, etc.) |
| `aspect.py`, [`interpolation/`](./interpolation/) (`method.py`, `stage.py`), `origin.py`, `location.py`, `orientation.py`, [`colorbar/`](./colorbar/) (`extend.py`, `spacing.py`) | Enums consumed by `draw.parameters` (imshow/colorbar kwargs) |

