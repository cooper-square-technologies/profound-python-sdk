# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, TYPE_CHECKING

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..shared.dimension_ref import DimensionRef

__all__ = ["SentimentQueryV2V2PostResponse", "Info", "Data", "DataPrevious"]


class DataPrevious(BaseModel):
    positive_sentiment: Optional[float] = None

    negative_sentiment: Optional[float] = None

    occurrence: Optional[float] = None

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


class Data(BaseModel):
    date: Optional[str] = None

    model: Optional[DimensionRef] = None

    topic: Optional[DimensionRef] = None

    region: Optional[DimensionRef] = None

    prompt: Optional[DimensionRef] = None

    persona: Optional[DimensionRef] = None

    tag: Optional[DimensionRef] = None

    theme: Optional[DimensionRef] = None

    claim: Optional[DimensionRef] = None

    run: Optional[DimensionRef] = None

    competitor: Optional[DimensionRef] = None

    positive_sentiment: Optional[float] = None

    negative_sentiment: Optional[float] = None

    occurrence: Optional[float] = None

    previous: Optional[DataPrevious] = None
    """Comparison-window metrics (when requested)."""

    prev_date: Optional[str] = None

    cited_websites: Optional[List[str]] = None

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

    asset: str
    """The analyzed brand name."""

    metrics: List[str]
    """Sentiment metrics returned per row."""

    comparison_start_date: Optional[str] = None
    """Comparison-window start (when requested)."""

    comparison_end_date: Optional[str] = None
    """Comparison-window end (when requested)."""

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


class SentimentQueryV2V2PostResponse(BaseModel):
    info: Info

    data: List[Data]
