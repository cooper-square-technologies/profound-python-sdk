# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CategoryUpdatePromptsParams", "UpdatePromptInput"]


class CategoryUpdatePromptsParams(TypedDict, total=False):

    prompts: Required[Iterable[UpdatePromptInput]]
    """List of prompt updates. Each entry must include an `id` and at least one field to change."""

    dry_run: bool
    """When true, validate and preview changes without persisting them."""


class UpdatePromptInput(TypedDict, total=False):

    id: Required[str]
    """ID of the prompt to update."""

    prompt: Optional[str]
    """New prompt text."""

    topic: Optional[object]
    """New topic. A new topic is created if the name doesn't exist."""

    language: Optional[str]
    """New language code. Must be enabled for the organization."""

    tags: Optional[Iterable[object]]
    """New tag set. Replaces all existing tags on the prompt."""

    regions: Optional[Iterable[object]]
    """New region set. Replaces all existing regions."""

    platforms: Optional[Iterable[object]]
    """New platform set. Replaces all existing platforms."""

    personas: Optional[Iterable[object]]
    """New persona set. Replaces all existing personas."""

    analysis_types: Optional[Iterable[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]]
    """New analysis types. Replaces all existing analysis types on the prompt."""

    prompt_type: Optional[str]
    """Deprecated. Use analysis_types instead."""

    asset: Optional[object]
    """Asset reference. Required when analysis_types includes 'sentiment'."""

