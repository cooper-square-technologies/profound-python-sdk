# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict
from ..._types import SequenceNotStr

__all__ = ["AccuracyCreateClaimBreakdownParams"]


class AccuracyCreateClaimBreakdownParams(TypedDict, total=False):
    start_date: Required[str]

    end_date: Required[str]

    comparison_start_date: Optional[str]

    comparison_end_date: Optional[str]

    category_id: Required[str]

    topic_ids: Optional[SequenceNotStr[str]]

    exclude_topic_ids: bool

    tag_ids: Optional[SequenceNotStr[str]]

    tag_filter_type: Literal["all", "any"]

    include_no_tag: bool

    region_ids: Optional[SequenceNotStr[str]]

    platform_ids: Optional[SequenceNotStr[str]]

    persona_ids: Optional[SequenceNotStr[str]]

    include_no_persona: bool

    prompt_ids: Optional[SequenceNotStr[str]]

    citation_categories: Optional[SequenceNotStr[str]]

    cluster_id: Required[str]
