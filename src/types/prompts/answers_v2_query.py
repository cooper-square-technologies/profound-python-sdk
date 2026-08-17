# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AnswersV2Query", "FilterNode"]


class FilterNode(BaseModel):

    and_: Optional[List[FilterNode]] = FieldInfo(alias="and", default=None)

    or_: Optional[List[FilterNode]] = FieldInfo(alias="or", default=None)

    not_: Optional[FilterNode] = FieldInfo(alias="not", default=None)

    field: Optional[str] = None

    op: Optional[str] = None

    value: Optional[str] = None



class AnswersV2Query(BaseModel):

    category_id: str

    start_date: str
    """YYYY-MM-DD, ET, inclusive"""

    end_date: str
    """YYYY-MM-DD, ET, inclusive"""

    include: Optional[List[Literal["run_id", "date", "model", "topic", "topic_id", "persona", "region", "tags", "prompt", "prompt_id", "response", "mentions", "citations", "search_queries", "analysis_types", "sentiment_claims"]]] = None
    """Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`, `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`, `citations`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for all of them."""

    filter: Optional[FilterNode] = None
    """and/or/not tree over `model`, `topic`, `region`, `persona`, `prompt`, `tag`, `analysis_type` (visibility/sentiment/factcheck); plus top-level `and` leaves `domain` or `page` (`is` one value, or `in` a list). Substring-search the prompt with `{"field": "prompt", "op": "contains", "value": "…"}`."""

    limit: Optional[int] = None
    """Page size; default 10, max 50."""

    max_results: Optional[int] = None
    """Stream endpoint only: cap the number of streamed rows (default: all)."""

    cursor: Optional[str] = None
