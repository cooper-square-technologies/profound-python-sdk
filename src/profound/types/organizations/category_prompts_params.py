# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CategoryPromptsParams"]


class CategoryPromptsParams(TypedDict, total=False):
    analysis_type: List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]
    """Filter by analysis type (visibility, sentiment, accuracy)."""

    cursor: Optional[str]
    """Pagination cursor from a previous response."""

    limit: int
    """Maximum number of prompts to return."""

    order_dir: Literal["asc", "desc"]
    """Sort direction by creation date."""

    persona_id: SequenceNotStr[str]
    """Filter by persona IDs."""

    platform_id: SequenceNotStr[str]
    """Filter by platform IDs."""

    prompt_type: List[Literal["visibility", "sentiment"]]
    """Deprecated. Use analysis_type instead."""

    region_id: SequenceNotStr[str]
    """Filter by region IDs."""

    status: List[Literal["active", "disabled"]]
    """Filter by prompt status. Defaults to `active` only."""

    tag_id: SequenceNotStr[str]
    """Filter by tag IDs."""

    topic_id: SequenceNotStr[str]
    """Filter by topic IDs."""
