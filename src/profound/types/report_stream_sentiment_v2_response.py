# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, TYPE_CHECKING, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ReportStreamSentimentV2Response",
    "SentimentV2Info",
    "SentimentRow",
    "SentimentRowModel",
    "SentimentRowTopic",
    "SentimentRowRegion",
    "SentimentRowPrompt",
    "SentimentRowPersona",
    "SentimentRowTag",
    "SentimentRowTheme",
    "SentimentRowClaim",
    "SentimentRowRun",
    "SentimentRowCompetitor",
    "SentimentRowPrevious",
]


class SentimentRowPrevious(BaseModel):
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


class SentimentRowCompetitor(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowRun(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowClaim(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowTheme(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowTag(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowPersona(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowPrompt(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowRegion(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowTopic(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowModel(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRow(BaseModel):
    date: Optional[str] = None

    model: Optional[SentimentRowModel] = None

    topic: Optional[SentimentRowTopic] = None

    region: Optional[SentimentRowRegion] = None

    prompt: Optional[SentimentRowPrompt] = None

    persona: Optional[SentimentRowPersona] = None

    tag: Optional[SentimentRowTag] = None

    theme: Optional[SentimentRowTheme] = None

    claim: Optional[SentimentRowClaim] = None

    run: Optional[SentimentRowRun] = None

    competitor: Optional[SentimentRowCompetitor] = None

    positive_sentiment: Optional[float] = None

    negative_sentiment: Optional[float] = None

    occurrence: Optional[float] = None

    previous: Optional[SentimentRowPrevious] = None
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


class SentimentV2Info(BaseModel):
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


ReportStreamSentimentV2Response: TypeAlias = Union[SentimentV2Info, SentimentRow]
