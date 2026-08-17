# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, List, Optional
from typing_extensions import Literal, Required, TypedDict

from .id_or_name_param import IDOrNameParam

__all__ = ["CategoryCreatePromptsParams", "Prompt"]


class CategoryCreatePromptsParams(TypedDict, total=False):
    prompts: Required[Iterable[Prompt]]
    """List of prompts to create."""

    dry_run: bool
    """When true, validate and preview changes without persisting them."""


class Prompt(TypedDict, total=False):
    """A single prompt to create within a category."""

    id: Optional[str]
    """Optional client-generated UUID for the prompt. When provided, creation is idempotent: retrying a request with the same id will not create a duplicate prompt. Omit to have the server generate one (non-idempotent)."""

    prompt: Required[str]
    """The prompt text to be sent to AI platforms."""

    topic: Required[IDOrNameParam]
    """Topic to assign. A new topic is created if the name doesn't exist."""

    language: Required[str]
    """Language code (e.g. 'en-US')"""

    tags: Iterable[IDOrNameParam]
    """Tags to assign. New tags are created if names don't exist."""

    regions: Required[Iterable[IDOrNameParam]]
    """Regions where the prompt will be collected."""

    platforms: Required[Iterable[IDOrNameParam]]
    """AI platforms where the prompt will be collected."""

    personas: Iterable[IDOrNameParam]
    """Personas to use when collecting. Omit for default (no persona)."""

    analysis_types: Optional[List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]]
    """Analysis types: 'visibility', 'sentiment', 'accuracy'. Defaults to ['visibility']."""

    prompt_type: Optional[str]
    """Deprecated. Use analysis_types instead. 'Visibility' or 'Sentiment'."""

    asset: Optional[IDOrNameParam]
    """Required for Sentiment prompts. The brand asset to evaluate."""
