# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict
from ..._types import SequenceNotStr

__all__ = ["AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostParams"]


class AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostParams(TypedDict, total=False):

    start_date: Required[str]

    end_date: Required[str]

    comparison_start_date: Optional[str]

    comparison_end_date: Optional[str]

    category_id: Required[str]

    topic_ids: Optional[Iterable[str]]

    exclude_topic_ids: bool

    tag_ids: Optional[Iterable[str]]

    tag_filter_type: Literal["all", "any"]

    include_no_tag: bool

    region_ids: Optional[Iterable[str]]

    platform_ids: Optional[Iterable[str]]

    persona_ids: Optional[Iterable[str]]

    include_no_persona: bool

    prompt_ids: Optional[Iterable[str]]

    citation_categories: Optional[SequenceNotStr[str]]

    limit: int
