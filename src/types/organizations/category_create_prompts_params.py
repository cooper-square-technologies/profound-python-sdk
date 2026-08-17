# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CategoryCreatePromptsParams", "CreatePromptInput"]


class CategoryCreatePromptsParams(TypedDict, total=False):

    prompts: Required[Iterable[CreatePromptInput]]
    """List of prompts to create."""

    dry_run: bool
    """When true, validate and preview changes without persisting them."""


class CreatePromptInput(TypedDict, total=False):

    prompt: Required[str]
    """The prompt text to be sent to AI platforms."""

    topic: Required[object]
    """Topic to assign. A new topic is created if the name doesn't exist."""

    language: Required[str]
    """Language code (e.g. 'en-US')"""

    tags: Iterable[object]
    """Tags to assign. New tags are created if names don't exist."""

    regions: Required[Iterable[object]]
    """Regions where the prompt will be collected."""

    platforms: Required[Iterable[object]]
    """AI platforms where the prompt will be collected."""

    personas: Iterable[object]
    """Personas to use when collecting. Omit for default (no persona)."""

    analysis_types: Optional[Iterable[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]]
    """Analysis types: 'visibility', 'sentiment', 'accuracy'. Defaults to ['visibility']."""

    prompt_type: Optional[str]
    """Deprecated. Use analysis_types instead. 'Visibility' or 'Sentiment'."""

    asset: Optional[object]
    """Required for Sentiment prompts. The brand asset to evaluate."""

