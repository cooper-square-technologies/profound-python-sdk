# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ReportQuerySentimentResponse",
    "Data",
    "DataClaim",
    "DataCompetitor",
    "DataModel",
    "DataPersona",
    "DataPrevious",
    "DataPrompt",
    "DataRegion",
    "DataRun",
    "DataTag",
    "DataTheme",
    "DataTopic",
    "Info",
]


class DataClaim(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataCompetitor(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataModel(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataPersona(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataPrevious(BaseModel):
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


class DataPrompt(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataRegion(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataRun(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataTag(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataTheme(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataTopic(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class Data(BaseModel):
    """One group-combination row.

    Group dims and metrics present depend on `group_by`/`metrics`.
    """

    cited_websites: Optional[List[str]] = None

    claim: Optional[DataClaim] = None
    """An `{id, name}` reference for a grouped dimension value."""

    competitor: Optional[DataCompetitor] = None
    """An `{id, name}` reference for a grouped dimension value."""

    date: Optional[str] = None

    model: Optional[DataModel] = None
    """An `{id, name}` reference for a grouped dimension value."""

    negative_sentiment: Optional[float] = None

    occurrence: Optional[float] = None

    persona: Optional[DataPersona] = None
    """An `{id, name}` reference for a grouped dimension value."""

    positive_sentiment: Optional[float] = None

    prev_date: Optional[str] = None

    previous: Optional[DataPrevious] = None
    """Comparison-window metrics (when requested)."""

    prompt: Optional[DataPrompt] = None
    """An `{id, name}` reference for a grouped dimension value."""

    rank: Optional[int] = None

    region: Optional[DataRegion] = None
    """An `{id, name}` reference for a grouped dimension value."""

    run: Optional[DataRun] = None
    """An `{id, name}` reference for a grouped dimension value."""

    tag: Optional[DataTag] = None
    """An `{id, name}` reference for a grouped dimension value."""

    theme: Optional[DataTheme] = None
    """An `{id, name}` reference for a grouped dimension value."""

    topic: Optional[DataTopic] = None
    """An `{id, name}` reference for a grouped dimension value."""

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


class ReportQuerySentimentResponse(BaseModel):
    data: List[Data]

    info: Info
