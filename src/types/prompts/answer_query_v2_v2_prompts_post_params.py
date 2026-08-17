# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._utils import PropertyInfo

__all__ = ["AnswerQueryV2V2PromptsPostParams", "FilterNode"]


class AnswerQueryV2V2PromptsPostParams(TypedDict, total=False):

    category_id: Required[str]

    start_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    end_date: Required[str]
    """YYYY-MM-DD, ET, inclusive"""

    include: Optional[Iterable[Literal["run_id", "date", "model", "topic", "topic_id", "persona", "region", "tags", "prompt", "prompt_id", "response", "mentions", "citations", "search_queries", "analysis_types", "sentiment_claims"]]]
    """Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`, `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`, `citations`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for all of them."""

    filter: Optional[FilterNode]
    """and/or/not tree over `model`, `topic`, `region`, `persona`, `prompt`, `tag`, `analysis_type` (visibility/sentiment/factcheck); plus top-level `and` leaves `domain` or `page` (`is` one value, or `in` a list). Substring-search the prompt with `{"field": "prompt", "op": "contains", "value": "…"}`."""

    limit: Optional[int]
    """Page size; default 10, max 50."""

    max_results: Optional[int]
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str]


class FilterNode(TypedDict, total=False):

    and_: Annotated[Optional[Iterable[FilterNode]], PropertyInfo(alias="and")]

    or_: Annotated[Optional[Iterable[FilterNode]], PropertyInfo(alias="or")]

    not_: Annotated[Optional[FilterNode], PropertyInfo(alias="not")]

    field: Optional[str]

    op: Optional[str]

    value: str

