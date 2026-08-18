# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional, TYPE_CHECKING, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QueryFanoutStreamV2V2StreamPostResponse", "QueryFanoutsV2Info", "QueryFanoutRow"]


class QueryFanoutRow(BaseModel):
    date: Optional[str] = None

    model: Optional[str] = None

    region: Optional[str] = None

    prompt: Optional[str] = None

    query: Optional[str] = None

    total_fanouts: Optional[float] = None

    fanouts_per_execution: Optional[float] = None

    share: Optional[float] = None

    query_variations: Optional[int] = None

    rank: Optional[int] = None

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


class QueryFanoutsV2Info(BaseModel):
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
    """Fanout metrics returned per row."""

    coverage_note: str
    """Caveat about which runs the fanout metrics cover."""

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


QueryFanoutStreamV2V2StreamPostResponse: TypeAlias = Union[QueryFanoutsV2Info, QueryFanoutRow]
