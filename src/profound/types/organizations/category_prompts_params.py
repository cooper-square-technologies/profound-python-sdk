# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict
from ..._types import SequenceNotStr

__all__ = ["CategoryPromptsParams"]


class CategoryPromptsParams(TypedDict, total=False):
    limit: int
    """Maximum number of prompts to return."""

    cursor: Optional[str]
    """Pagination cursor from a previous response."""

    order_by: Literal["created_at", "prompt"]
    """Field used to order prompts."""

    order_dir: Literal["asc", "desc"]
    """Sort direction for the selected order field."""

    analysis_type: List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]
    """Filter by analysis type (visibility, sentiment, accuracy)."""

    prompt_type: List[Literal["visibility", "sentiment"]]
    """Deprecated. Use analysis_type instead."""

    status: List[Literal["active", "disabled"]]
    """Filter by prompt status. Defaults to `active` only."""

    topic_id: SequenceNotStr[str]
    """Filter by topic IDs."""

    tag_id: SequenceNotStr[str]
    """Filter by tag IDs."""

    region_id: SequenceNotStr[str]
    """Filter by region IDs."""

    platform_id: SequenceNotStr[str]
    """Filter by platform IDs."""

    persona_id: SequenceNotStr[str]
    """Filter by persona IDs."""
