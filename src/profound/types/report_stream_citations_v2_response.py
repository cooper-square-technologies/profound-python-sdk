# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ReportStreamCitationsV2Response",
    "CitationsV2Info",
    "CitationRow",
    "CitationRowModel",
    "CitationRowPersona",
    "CitationRowPrompt",
    "CitationRowRegion",
    "CitationRowTopic",
]


class CitationsV2Info(BaseModel):
    """`summary` event payload (the report `info` block)."""

    analysis_types: List[str]
    """Analysis types the citations were drawn from."""

    count: int
    """Number of rows returned in `data` for this page."""

    end_date: str
    """Echoed request end date (YYYY-MM-DD, ET)."""

    metrics: List[str]
    """Metrics returned per row."""

    models: List[str]
    """Display names of the models the report covers."""

    scope: str
    """Citation scope: `all` or `owned`."""

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


class CitationRowModel(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class CitationRowPersona(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class CitationRowPrompt(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class CitationRowRegion(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class CitationRowTopic(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class CitationRow(BaseModel):
    """`result` event payload — one citation row."""

    citation_share: Optional[float] = None

    count: Optional[int] = None

    date: Optional[str] = None

    domain: Optional[str] = None

    first_cited_at: Optional[str] = None
    """Pages only."""

    model: Optional[CitationRowModel] = None
    """An `{id, name}` reference for a grouped dimension value."""

    page: Optional[str] = None

    persona: Optional[CitationRowPersona] = None
    """An `{id, name}` reference for a grouped dimension value."""

    prompt: Optional[CitationRowPrompt] = None
    """An `{id, name}` reference for a grouped dimension value."""

    rank: Optional[int] = None

    region: Optional[CitationRowRegion] = None
    """An `{id, name}` reference for a grouped dimension value."""

    topic: Optional[CitationRowTopic] = None
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


ReportStreamCitationsV2Response: TypeAlias = Union[CitationsV2Info, CitationRow]
