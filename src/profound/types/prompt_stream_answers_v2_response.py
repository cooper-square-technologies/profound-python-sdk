# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PromptStreamAnswersV2Response", "AnswersV2Info", "AnswerRow", "AnswerRowCitationDetail", "AnswerRowModel"]


class AnswersV2Info(BaseModel):
    """`summary` event payload (the report `info` block)."""

    count: int
    """Number of rows returned in `data` for this page."""

    end_date: str
    """Echoed request end date (YYYY-MM-DD, ET)."""

    include: List[str]
    """Row fields returned (echoes `include`, or all fields when omitted)."""

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


class AnswerRowCitationDetail(BaseModel):
    clean_url: str

    hostname: str

    path: str

    title: str

    url: str

    citation_category: Optional[str] = None

    first_cited_at: Optional[str] = None

    text: Optional[str] = None


class AnswerRowModel(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class AnswerRow(BaseModel):
    """`result` event payload — one answer row."""

    analysis_types: Optional[List[str]] = None

    citation_details: Optional[List[AnswerRowCitationDetail]] = None

    citations: Optional[List[str]] = None

    date: Optional[str] = None

    mentions: Optional[List[str]] = None

    model: Optional[AnswerRowModel] = None
    """An `{id, name}` reference for a grouped dimension value."""

    persona: Optional[str] = None

    prompt: Optional[str] = None

    prompt_id: Optional[str] = None

    region: Optional[str] = None

    response: Optional[str] = None

    run_id: Optional[str] = None

    search_queries: Optional[List[str]] = None

    sentiment_claims: Optional[List[Dict[str, object]]] = None

    tags: Optional[List[str]] = None

    topic: Optional[str] = None

    topic_id: Optional[str] = None

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


PromptStreamAnswersV2Response: TypeAlias = Union[AnswersV2Info, AnswerRow]
