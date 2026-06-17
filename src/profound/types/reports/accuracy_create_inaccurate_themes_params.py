# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AccuracyCreateInaccurateThemesParams"]


class AccuracyCreateInaccurateThemesParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[str]

    start_date: Required[str]

    citation_categories: Optional[SequenceNotStr[str]]

    comparison_end_date: Optional[str]

    comparison_start_date: Optional[str]

    exclude_topic_ids: bool

    include_no_persona: bool

    include_no_tag: bool

    limit: int

    offset: int

    persona_ids: Optional[SequenceNotStr[str]]

    platform_ids: Optional[SequenceNotStr[str]]

    prompt_ids: Optional[SequenceNotStr[str]]

    region_ids: Optional[SequenceNotStr[str]]

    search_query: Optional[str]

    sort_by: Literal["response_share"]

    sort_order: Literal["asc", "desc"]

    tag_filter_type: Literal["all", "any"]

    tag_ids: Optional[SequenceNotStr[str]]

    topic_ids: Optional[SequenceNotStr[str]]
