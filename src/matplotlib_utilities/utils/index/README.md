# utils.index

## Overview

Types for **addressing subplots** inside a flattened axes array. `MatplotGraphMaker` accepts a `SubplotIndex`, which is either a linear subplot number plus row hint or an explicit row/column pair.

## Components

| Component | Description |
| --------- | ----------- |
| [`subplot_number.py`](./subplot_number.py) | `SubplotNumber`: subplot index by sequential number and `row_index` |
| [`row_column_index.py`](./row_column_index.py) | `RowColumnIndex`: zero-based row and column indices |
| [`subplot_index.py`](./subplot_index.py) | `SubplotIndex = RowColumnIndex \| SubplotNumber` type alias |
