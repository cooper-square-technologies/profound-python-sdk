# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ReportQuerySentimentV2Params", "ClaimFilters"]


class ReportQuerySentimentV2Params(TypedDict, total=False):
    asset_name: Required[str]

    category_id: Required[str]

    end_date: Required[str]

    start_date: Required[str]

    claim_filters: Optional[ClaimFilters]

    comparison_end_date: Optional[str]

    comparison_start_date: Optional[str]

    date_bucket: Optional[Literal["daily", "weekly", "monthly"]]

    exclude_topic_ids: bool

    group_by: Optional[
        List[Literal["topic", "region", "platform", "prompt", "persona", "tag", "theme", "claim", "run", "competitor"]]
    ]

    include_no_persona: bool

    include_no_tag: bool

    limit: Optional[int]

    metrics: Optional[List[Literal["sentiment", "occurrence"]]]

    offset: int

    owned_asset_names_to_exclude: SequenceNotStr[str]

    persona_ids: Optional[SequenceNotStr[str]]

    platform_ids: Optional[SequenceNotStr[str]]

    prompt_ids: Optional[SequenceNotStr[str]]

    region_ids: Optional[SequenceNotStr[str]]

    run_ids: Optional[SequenceNotStr[str]]

    sort_by: Optional[Literal["occurrence", "assessment_count", "positive_sentiment", "negative_sentiment"]]

    sort_direction: Literal["asc", "desc"]

    tag_filter_type: Literal["all", "any"]

    tag_ids: Optional[SequenceNotStr[str]]

    topic_ids: Optional[SequenceNotStr[str]]


class ClaimFilters(TypedDict, total=False):
    claim: Optional[str]

    claim_id: Optional[str]

    sentiment: Optional[Literal["positive", "negative"]]

    theme_id: Optional[str]
