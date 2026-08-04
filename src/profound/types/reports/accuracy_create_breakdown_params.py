# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AccuracyCreateBreakdownParams", "Pagination"]


class AccuracyCreateBreakdownParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[str]

    start_date: Required[str]

    breakdown_by: Literal["citation", "platform", "topic", "prompt", "tag", "region", "persona", "theme"]

    citation_categories: Optional[SequenceNotStr[str]]

    comparison_end_date: Optional[str]

    comparison_start_date: Optional[str]

    date_bucket: Optional[str]

    exclude_topic_ids: bool

    group_by: Optional[List[Literal["platform", "topic", "prompt", "tag", "region", "persona", "theme", "date"]]]

    include_no_persona: bool

    include_no_tag: bool

    limit: int

    offset: int

    pagination: Optional[Pagination]
    """Canonical grouped pagination plan for Accuracy Breakdown rows."""

    persona_ids: Optional[SequenceNotStr[str]]

    platform_ids: Optional[SequenceNotStr[str]]

    prompt_ids: Optional[SequenceNotStr[str]]

    region_ids: Optional[SequenceNotStr[str]]

    search_query: Optional[str]

    sort_by: Literal["citationShare", "accuracy"]

    sort_order: Literal["asc", "desc"]

    tag_filter_type: Literal["all", "any"]

    tag_ids: Optional[SequenceNotStr[str]]

    topic_ids: Optional[SequenceNotStr[str]]


class Pagination(TypedDict, total=False):
    """Canonical grouped pagination plan for Accuracy Breakdown rows."""

    dimension: Literal["group"]

    direction: Optional[Literal["asc", "desc"]]

    metric: Literal["accuracy", "inaccurate_claims"]

    mode: Literal["current", "delta"]
