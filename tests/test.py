"""Smoke tests and the former ``maker`` module demo (non-interactive)."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import numpy as np
import pytest
from pathlib import Path

from matplotlib_utilities import (
    GraphAxis,
    GraphLayout,
    GraphParameters,
    LineParameters,
    MatplotGraphMaker,
    Orientation,
    ScatterParameters,
    SubplotNumber,
    TableAxis,
)


def build_demo_graph_maker() -> MatplotGraphMaker:
    num_graph = 4
    layout = GraphLayout.from_number(
        number=num_graph,
        axis=TableAxis.COLUMN,
        axis_value=num_graph // 2,
    )
    params = GraphParameters()
    graph_maker = MatplotGraphMaker(layout=layout, parameters=params)

    x1 = np.random.default_rng(0).standard_normal(100)
    y1 = np.random.default_rng(1).standard_normal(100)
    confidences = np.random.default_rng(2).random(100)

    index = graph_maker.get_subplot_index_from_number(number=0)
    # Per-point marker area (matplotlib *s*); map e.g. confidences to visible sizes.
    sizes = 20.0 + confidences * 80.0
    graph_maker.draw.scatter(
        index=index,
        x=x1,
        y=y1,
        subparams=ScatterParameters(s=sizes),
    )
    graph_maker.axis.set_label(
        label="x",
        index=SubplotNumber(number=0, row_index=0),
        axis=GraphAxis.X,
    )
    index = graph_maker.get_subplot_index_from_number(number=1)
    graph_maker.draw.plot(
        index=index,
        x=x1,
        y=y1,
        subparams=None,
    )
    graph_maker.draw.line(
        value=0.5,
        orientation=Orientation.VERTICAL,
        index=graph_maker.get_subplot_index_from_number(number=1),
        subparams=LineParameters(color="red"),
    )
    graph_maker.draw.line(
        value=0.0,
        orientation=Orientation.HORIZONTAL,
        index=graph_maker.get_subplot_index_from_number(number=1),
        subparams=LineParameters(color="blue"),
    )
    return graph_maker


def test_import_package() -> None:
    import matplotlib_utilities as mu  # noqa: F401

    assert hasattr(mu, "MatplotGraphMaker")


def test_graph_maker_demo_smoke(tmp_path: Path) -> None:
    graph_maker = build_demo_graph_maker()
    out = tmp_path / "demo.png"
    graph_maker.finalize(save_path=str(out), is_showing_result_enabled=False)
    assert out.is_file()
    assert out.stat().st_size > 0


@pytest.mark.parametrize("num_graph", [1, 2, 4])
def test_graph_layout_from_number(num_graph: int) -> None:
    layout = GraphLayout.from_number(
        number=num_graph,
        axis=TableAxis.COLUMN,
        axis_value=max(1, num_graph // 2),
    )
    assert layout.row * layout.column >= num_graph
