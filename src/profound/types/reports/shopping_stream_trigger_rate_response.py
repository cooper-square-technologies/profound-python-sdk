# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ShoppingStreamTriggerRateResponse",
    "ShoppingTriggerRateV2Info",
    "ShoppingTriggerRateRow",
    "ShoppingTriggerRateRowPersona",
    "ShoppingTriggerRateRowPrompt",
    "ShoppingTriggerRateRowRegion",
    "ShoppingTriggerRateRowTopic",
]


class ShoppingTriggerRateV2Info(BaseModel):
    """`summary` event payload (the report `info` block)."""

    count: int
    """Number of rows returned in `data` for this page."""

    end_date: str
    """Echoed request end date (YYYY-MM-DD, ET)."""

    metrics: List[str]
    """Metrics returned per row."""

    models: List[str]
    """Display names of the models the report covers."""

    start_date: str
    """Echoed request start date (YYYY-MM-DD, ET)."""

    filter: Optional[Dict[str, object]] = None
    """Echoed normalized filter tree, or null when no filter was sent."""

    next_cursor: Optional[str] = None
    """Opaque cursor for the next page; null on the last page."""

    total_results: Optional[int] = None
    """Total rows matching the query before pagination (null when not computed)."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ShoppingTriggerRateRowPersona(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class ShoppingTriggerRateRowPrompt(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class ShoppingTriggerRateRowRegion(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class ShoppingTriggerRateRowTopic(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class ShoppingTriggerRateRow(BaseModel):
    """`result` event payload — one trigger row."""

    date: Optional[str] = None

    persona: Optional[ShoppingTriggerRateRowPersona] = None
    """An `{id, name}` reference for a grouped dimension value."""

    prompt: Optional[ShoppingTriggerRateRowPrompt] = None
    """An `{id, name}` reference for a grouped dimension value."""

    region: Optional[ShoppingTriggerRateRowRegion] = None
    """An `{id, name}` reference for a grouped dimension value."""

    shopping_triggered_runs: Optional[int] = None

    topic: Optional[ShoppingTriggerRateRowTopic] = None
    """An `{id, name}` reference for a grouped dimension value."""

    total_runs: Optional[int] = None

    trigger_rate_percentage: Optional[float] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


ShoppingStreamTriggerRateResponse: TypeAlias = Union[ShoppingTriggerRateV2Info, ShoppingTriggerRateRow]
