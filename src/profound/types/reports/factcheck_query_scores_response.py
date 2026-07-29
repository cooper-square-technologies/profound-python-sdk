# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "FactcheckQueryScoresResponse",
    "Data",
    "DataCitation",
    "DataModel",
    "DataPersona",
    "DataPrompt",
    "DataRegion",
    "DataTag",
    "DataTheme",
    "DataTopic",
    "Info",
]


class DataCitation(BaseModel):
    citation_category: Optional[str] = None

    url: Optional[str] = None


class DataModel(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataPersona(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataPrompt(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataRegion(BaseModel):
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
    """
    An accuracy score row: the headline (no dims), a daily point, or a per-dimension breakdown.
    """

    accuracy: Optional[float] = None

    accurate: Optional[int] = None

    citation: Optional[DataCitation] = None

    date: Optional[str] = None

    inaccurate: Optional[int] = None

    model: Optional[DataModel] = None
    """An `{id, name}` reference for a grouped dimension value."""

    persona: Optional[DataPersona] = None
    """An `{id, name}` reference for a grouped dimension value."""

    prompt: Optional[DataPrompt] = None
    """An `{id, name}` reference for a grouped dimension value."""

    region: Optional[DataRegion] = None
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
    count: int
    """Number of rows returned in `data` for this page."""

    end_date: str
    """Echoed request end date (YYYY-MM-DD, ET)."""

    group_by: List[str]
    """Dimensions the scores are sliced by (empty → headline)."""

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


class FactcheckQueryScoresResponse(BaseModel):
    data: List[Data]

    info: Info
