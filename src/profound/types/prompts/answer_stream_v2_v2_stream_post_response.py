# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, TYPE_CHECKING, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..shared.dimension_ref import DimensionRef

__all__ = [
    "AnswerStreamV2V2StreamPostResponse",
    "AnswersV2Info",
    "AnswerRow",
    "AnswerRowCitationDetail",
    "AnswerRowCitationDetailGroup",
]


class AnswerRowCitationDetailGroup(BaseModel):
    group_id: int

    group_position: int


class AnswerRowCitationDetail(BaseModel):
    url: str

    clean_url: str

    title: str

    text: Optional[str] = None

    hostname: str

    path: str

    positions: Optional[List[int]] = None

    groups: Optional[List[AnswerRowCitationDetailGroup]] = None

    first_cited_at: Optional[str] = None

    citation_category: Optional[str] = None


class AnswerRow(BaseModel):
    run_id: Optional[str] = None

    date: Optional[str] = None

    model: Optional[DimensionRef] = None

    topic: Optional[str] = None

    topic_id: Optional[str] = None

    region: Optional[str] = None

    persona: Optional[str] = None

    tags: Optional[List[str]] = None

    prompt: Optional[str] = None

    prompt_id: Optional[str] = None

    response: Optional[str] = None

    mentions: Optional[List[str]] = None

    citations: Optional[List[str]] = None

    citation_details: Optional[List[AnswerRowCitationDetail]] = None
    """Citation metadata. `positions` identify citation locations in the answer text. Each `groups` entry represents a rendered citation pill; `group_position` is the source's position within that pill."""

    search_queries: Optional[List[str]] = None

    analysis_types: Optional[List[str]] = None

    sentiment_claims: Optional[List[Dict[str, object]]] = None

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


class AnswersV2Info(BaseModel):
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

    include: List[str]
    """Row fields returned (echoes `include`, or all fields when omitted)."""

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


AnswerStreamV2V2StreamPostResponse: TypeAlias = Union[AnswersV2Info, AnswerRow]
