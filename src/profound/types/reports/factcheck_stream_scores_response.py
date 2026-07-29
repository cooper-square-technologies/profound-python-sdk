# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "FactcheckStreamScoresResponse",
    "FactcheckScoresInfo",
    "FactcheckScoreRow",
    "FactcheckScoreRowCitation",
    "FactcheckScoreRowModel",
    "FactcheckScoreRowPersona",
    "FactcheckScoreRowPrompt",
    "FactcheckScoreRowRegion",
    "FactcheckScoreRowTag",
    "FactcheckScoreRowTheme",
    "FactcheckScoreRowTopic",
]


class FactcheckScoresInfo(BaseModel):
    """`summary` event payload (the report `info` block)."""

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


class FactcheckScoreRowCitation(BaseModel):
    citation_category: Optional[str] = None

    url: Optional[str] = None


class FactcheckScoreRowModel(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class FactcheckScoreRowPersona(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class FactcheckScoreRowPrompt(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class FactcheckScoreRowRegion(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class FactcheckScoreRowTag(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class FactcheckScoreRowTheme(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class FactcheckScoreRowTopic(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class FactcheckScoreRow(BaseModel):
    """`result` event payload — one accuracy score row."""

    accuracy: Optional[float] = None

    accurate: Optional[int] = None

    citation: Optional[FactcheckScoreRowCitation] = None

    date: Optional[str] = None

    inaccurate: Optional[int] = None

    model: Optional[FactcheckScoreRowModel] = None
    """An `{id, name}` reference for a grouped dimension value."""

    persona: Optional[FactcheckScoreRowPersona] = None
    """An `{id, name}` reference for a grouped dimension value."""

    prompt: Optional[FactcheckScoreRowPrompt] = None
    """An `{id, name}` reference for a grouped dimension value."""

    region: Optional[FactcheckScoreRowRegion] = None
    """An `{id, name}` reference for a grouped dimension value."""

    tag: Optional[FactcheckScoreRowTag] = None
    """An `{id, name}` reference for a grouped dimension value."""

    theme: Optional[FactcheckScoreRowTheme] = None
    """An `{id, name}` reference for a grouped dimension value."""

    topic: Optional[FactcheckScoreRowTopic] = None
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


FactcheckStreamScoresResponse: TypeAlias = Union[FactcheckScoresInfo, FactcheckScoreRow]
