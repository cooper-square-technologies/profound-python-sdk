# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
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

    language: Required[str]
    """Language code (e.g. 'en-US')"""

    platforms: Required[Iterable[IDOrNameParam]]
    """AI platforms where the prompt will be collected."""

    prompt: Required[str]
    """The prompt text to be sent to AI platforms."""

    regions: Required[Iterable[IDOrNameParam]]
    """Regions where the prompt will be collected."""

    topic: Required[IDOrNameParam]
    """Topic to assign. A new topic is created if the name doesn't exist."""

    id: Optional[str]
    """Optional client-generated UUID for the prompt.

    When provided, creation is idempotent: retrying a request with the same id will
    not create a duplicate prompt. Omit to have the server generate one
    (non-idempotent).
    """

    analysis_types: Optional[List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]]
    """Analysis types: 'visibility', 'sentiment', 'accuracy'.

    Defaults to ['visibility'].
    """

    asset: Optional[IDOrNameParam]
    """Reference by id, name, or both.

    Plain strings work too: UUIDs become id lookups, other strings become name
    lookups.
    """

    personas: Iterable[IDOrNameParam]
    """Personas to use when collecting. Omit for default (no persona)."""

    prompt_type: Optional[str]
    """Deprecated. Use analysis_types instead. 'Visibility' or 'Sentiment'."""

    tags: Iterable[IDOrNameParam]
    """Tags to assign. New tags are created if names don't exist."""
