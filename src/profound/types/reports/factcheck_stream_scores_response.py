# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, TYPE_CHECKING, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..shared.dimension_ref import DimensionRef

__all__ = ["FactcheckStreamScoresResponse", "FactcheckScoresInfo", "FactcheckScoreRow", "FactcheckScoreRowCitation"]


class FactcheckScoreRowCitation(BaseModel):
    url: Optional[str] = None

    citation_category: Optional[str] = None


class FactcheckScoreRow(BaseModel):
    date: Optional[str] = None

    model: Optional[DimensionRef] = None

    region: Optional[DimensionRef] = None

    persona: Optional[DimensionRef] = None

    prompt: Optional[DimensionRef] = None

    topic: Optional[DimensionRef] = None

    tag: Optional[DimensionRef] = None

    theme: Optional[DimensionRef] = None

    citation: Optional[FactcheckScoreRowCitation] = None

    accuracy: Optional[float] = None

    accurate: Optional[int] = None

    inaccurate: Optional[int] = None

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


class FactcheckScoresInfo(BaseModel):
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

    group_by: List[str]
    """Dimensions the scores are sliced by (empty → headline)."""

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


FactcheckStreamScoresResponse: TypeAlias = Union[FactcheckScoresInfo, FactcheckScoreRow]
