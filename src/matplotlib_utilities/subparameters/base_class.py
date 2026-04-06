from abc import ABC
from dataclasses import dataclass, Field, fields
from typing import Any


@dataclass
class Subparameters(ABC):
    """
    Base class for matplotlib kwarg dataclasses.

    Subclasses inherit to_dict by iterating dataclass fields. Override
    _to_dict_skip_field only when omit rules differ from the default (omit None).
    Enum-like values with a .value attribute are unwrapped in to_dict.
    """

    def _to_dict_skip_field(self, field: Field[Any], value: Any) -> bool:
        """When True, the field is omitted from the dict returned by to_dict."""
        return value is None

    @property
    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for f in fields(self):
            val = getattr(self, f.name)
            if self._to_dict_skip_field(f, val):
                continue
            if hasattr(val, "value"):
                out[f.name] = val.value
            else:
                out[f.name] = val
        return out
