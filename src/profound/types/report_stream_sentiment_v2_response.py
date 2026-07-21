# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ReportStreamSentimentV2Response",
    "SentimentV2Info",
    "SentimentRow",
    "SentimentRowClaim",
    "SentimentRowCompetitor",
    "SentimentRowModel",
    "SentimentRowPersona",
    "SentimentRowPrevious",
    "SentimentRowPrompt",
    "SentimentRowRegion",
    "SentimentRowRun",
    "SentimentRowTag",
    "SentimentRowTheme",
    "SentimentRowTopic",
]


class SentimentV2Info(BaseModel):
    """`summary` event payload (the report `info` block)."""

    asset: str
    """The analyzed brand name."""

    count: int
    """Number of rows returned in `data` for this page."""

    end_date: str
    """Echoed request end date (YYYY-MM-DD, ET)."""

    metrics: List[str]
    """Sentiment metrics returned per row."""

    models: List[str]
    """Display names of the models the report covers."""

    start_date: str
    """Echoed request start date (YYYY-MM-DD, ET)."""

    comparison_end_date: Optional[str] = None
    """Comparison-window end (when requested)."""

    comparison_start_date: Optional[str] = None
    """Comparison-window start (when requested)."""

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


class SentimentRowClaim(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowCompetitor(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowModel(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowPersona(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowPrevious(BaseModel):
    """Comparison-window metrics (when requested)."""

    negative_sentiment: Optional[float] = None

    occurrence: Optional[float] = None

    positive_sentiment: Optional[float] = None

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


class SentimentRowPrompt(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowRegion(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowRun(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowTag(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowTheme(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRowTopic(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class SentimentRow(BaseModel):
    """`result` event payload — one sentiment row."""

    cited_websites: Optional[List[str]] = None

    claim: Optional[SentimentRowClaim] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    competitor: Optional[SentimentRowCompetitor] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    date: Optional[str] = None

    model: Optional[SentimentRowModel] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    negative_sentiment: Optional[float] = None

    occurrence: Optional[float] = None

    persona: Optional[SentimentRowPersona] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    positive_sentiment: Optional[float] = None

    prev_date: Optional[str] = None

    previous: Optional[SentimentRowPrevious] = None
    """Comparison-window metrics (when requested)."""

    prompt: Optional[SentimentRowPrompt] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    rank: Optional[int] = None

    region: Optional[SentimentRowRegion] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    run: Optional[SentimentRowRun] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    tag: Optional[SentimentRowTag] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    theme: Optional[SentimentRowTheme] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    topic: Optional[SentimentRowTopic] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

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
