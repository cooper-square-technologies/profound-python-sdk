# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, List, Optional
from typing_extensions import Literal, Required, TypedDict

from .id_or_name_param import IDOrNameParam

__all__ = ["CategoryUpdatePromptsParams", "Prompt"]


class CategoryUpdatePromptsParams(TypedDict, total=False):
    prompts: Required[Iterable[Prompt]]
    """List of prompt updates. Each entry must include an `id` and at least one field to change."""

    dry_run: bool
    """When true, validate and preview changes without persisting them."""


class Prompt(TypedDict, total=False):
    """Fields to update on an existing prompt. Only provided fields are changed; omitted fields are left unchanged."""

    id: Required[str]
    """ID of the prompt to update."""

    prompt: Optional[str]
    """New prompt text."""

    topic: Optional[IDOrNameParam]
    """New topic. A new topic is created if the name doesn't exist."""

    language: Optional[str]
    """New language code. Must be enabled for the organization."""

    tags: Optional[Iterable[IDOrNameParam]]
    """New tag set. Replaces all existing tags on the prompt."""

    regions: Optional[Iterable[IDOrNameParam]]
    """New region set. Replaces all existing regions."""

    platforms: Optional[Iterable[IDOrNameParam]]
    """New platform set. Replaces all existing platforms."""

    personas: Optional[Iterable[IDOrNameParam]]
    """New persona set. Replaces all existing personas."""

    analysis_types: Optional[List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]]
    """New analysis types. Replaces all existing analysis types on the prompt."""

    prompt_type: Optional[str]
    """Deprecated. Use analysis_types instead."""

    asset: Optional[IDOrNameParam]
    """Asset reference. Required when analysis_types includes 'sentiment'."""
