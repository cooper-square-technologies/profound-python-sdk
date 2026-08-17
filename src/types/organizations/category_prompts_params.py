# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["CategoryPromptsParams"]


class CategoryPromptsParams(TypedDict, total=False):

    limit: int
    """Maximum number of prompts to return."""

    cursor: Optional[str]
    """Pagination cursor from a previous response."""

    order_dir: Literal["asc", "desc"]
    """Sort direction by creation date."""

    analysis_type: Iterable[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]
    """Filter by analysis type (visibility, sentiment, accuracy)."""

    prompt_type: Iterable[Literal["visibility", "sentiment"]]
    """Deprecated. Use analysis_type instead."""

    status: Iterable[Literal["active", "disabled"]]
    """Filter by prompt status. Defaults to `active` only."""

    topic_id: Iterable[str]
    """Filter by topic IDs."""

    tag_id: Iterable[str]
    """Filter by tag IDs."""

    region_id: Iterable[str]
    """Filter by region IDs."""

    platform_id: Iterable[str]
    """Filter by platform IDs."""

    persona_id: Iterable[str]
    """Filter by persona IDs."""
