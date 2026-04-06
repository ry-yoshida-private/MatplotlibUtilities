"""Put ``src`` on ``sys.path`` so ``import matplotlib_utilities`` works from repo root."""

from __future__ import annotations

import sys
from pathlib import Path

_repo_root = Path(__file__).resolve().parents[1]
_src = str(_repo_root / "src")
if _src not in sys.path:
    sys.path.insert(0, _src)
