# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, TYPE_CHECKING

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ShoppingTriggerRateResponse", "Info", "Data", "DataTopic", "DataRegion", "DataPersona", "DataPrompt"]


class DataPrompt(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class DataPersona(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class DataRegion(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class DataTopic(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class Data(BaseModel):
    date: Optional[str] = None

    topic: Optional[DataTopic] = None

    region: Optional[DataRegion] = None

    persona: Optional[DataPersona] = None

    prompt: Optional[DataPrompt] = None

    total_runs: Optional[int] = None

    shopping_triggered_runs: Optional[int] = None

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


class Info(BaseModel):
    total_results: Optional[int] = None
    """Total rows matching the query before pagination (null when not computed)."""

    count: int
    """Number of rows returned in `data` for this page."""

    next_cursor: Optional[str] = None
    """Opaque cursor for the next page; null on the last page."""

    models: List[str]
    """Display names of the models the report covers."""

    start_date: str
    """Echoed request start date (YYYY-MM-DD, ET)."""

    end_date: str
    """Echoed request end date (YYYY-MM-DD, ET)."""

    filter: Optional[Dict[str, object]] = None
    """Echoed normalized filter tree, or null when no filter was sent."""

    metrics: List[str]
    """Metrics returned per row."""

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


class ShoppingTriggerRateResponse(BaseModel):
    info: Info

    data: List[Data]
