from dataclasses import dataclass


@dataclass
class LabelParameters:
    """
    Common label keyword argument for matplotlib artists and related API.
    """

    label: str | None = None
