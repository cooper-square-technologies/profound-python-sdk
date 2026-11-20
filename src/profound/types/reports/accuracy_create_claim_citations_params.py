# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict
from ..._types import SequenceNotStr

__all__ = ["AccuracyCreateClaimCitationsParams"]


class AccuracyCreateClaimCitationsParams(TypedDict, total=False):
    citation_categories: Optional[SequenceNotStr[str]]
    """Legacy category names or V2 classification/custom names. ORed with citation_category_pairs."""

    citation_category_taxonomy: Literal["legacy", "v2"]
    """Dataset used for category assignments and filters. V2 leaf group values are JSON [classification, subcategory] pairs."""

    citation_category_pairs: Optional[Iterable[Iterable[object]]]
    """V2-only exact [classification, subcategory] selections, ORed with citation_categories. An empty subcategory matches only the leaf with no subcategory under that classification."""

    start_date: Required[str]

    end_date: Required[str]

    comparison_start_date: Optional[str]

    comparison_end_date: Optional[str]

    category_id: Required[str]

    languages: Optional[SequenceNotStr[str]]

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

    cluster_id: Required[str]

    limit: int

    offset: int

    search_query: Optional[str]

    sort_order: Literal["asc", "desc"]
