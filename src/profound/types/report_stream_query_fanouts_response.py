# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReportStreamQueryFanoutsResponse", "QueryFanoutsV2Info", "QueryFanoutRow"]


class QueryFanoutsV2Info(BaseModel):
    """`summary` event payload (the report `info` block)."""

    count: int
    """Number of rows returned in `data` for this page."""

    coverage_note: str
    """Caveat about which runs the fanout metrics cover."""

    end_date: str
    """Echoed request end date (YYYY-MM-DD, ET)."""

    metrics: List[str]
    """Fanout metrics returned per row."""

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


class QueryFanoutRow(BaseModel):
    """`result` event payload — one query-fanout row."""

    date: Optional[str] = None

    fanouts_per_execution: Optional[float] = None

    model: Optional[str] = None

    prompt: Optional[str] = None

    query: Optional[str] = None

    query_variations: Optional[int] = None

    rank: Optional[int] = None

    region: Optional[str] = None

    share: Optional[float] = None

    total_fanouts: Optional[float] = None

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


ReportStreamQueryFanoutsResponse: TypeAlias = Union[QueryFanoutsV2Info, QueryFanoutRow]
