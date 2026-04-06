# subparameters.utils

## Overview

Small **enum modules** (and related types) shared by subparameter dataclasses—for example `ImshowParameters` uses aspect/interpolation/origin enums, and `ColorbarParameters` uses location, orientation, extend, and spacing enums.

## Components

| Component | Description |
| --------- | ----------- |
| [`aspect.py`](./aspect.py) | `Aspect` for axis aspect handling |
| [`interpolation.py`](./interpolation.py) | `Interpolation` for `imshow` resampling |
| [`interpolation_stage.py`](./interpolation_stage.py) | `InterpolationStage` (e.g. data vs rgba vs auto) |
| [`origin.py`](./origin.py) | `Origin` for image coordinate origin |
| [`location.py`](./location.py) | `Location` for anchored artists / colorbar placement |
| [`orientation.py`](./orientation.py) | `Orientation` for vertical vs horizontal colorbars (and line orientation) |
| [`colorbar_extend.py`](./colorbar_extend.py) | `ColorbarExtend` for over/under/neither |
| [`colorbar_spacing.py`](./colorbar_spacing.py) | `ColorbarSpacing` for fraction/pad-style spacing |
