# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, List, Optional
from typing_extensions import Literal, Required, TypedDict

from .shared_params.id_or_name import IDOrName

__all__ = ["OrganizationCreateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPostParams", "Prompt"]


class OrganizationCreateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPostParams(TypedDict, total=False):
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

    topic: Required[IDOrName]
    """Topic to assign. A new topic is created if the name doesn't exist."""

    language: Required[str]
    """Language code (e.g. 'en-US')"""

    tags: Iterable[IDOrName]
    """Tags to assign. New tags are created if names don't exist."""

    regions: Required[Iterable[IDOrName]]
    """Regions where the prompt will be collected."""

    platforms: Required[Iterable[IDOrName]]
    """AI platforms where the prompt will be collected."""

    personas: Iterable[IDOrName]
    """Personas to use when collecting. Omit for default (no persona)."""

    analysis_types: Optional[List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]]
    """Analysis types: 'visibility', 'sentiment', 'accuracy'. Defaults to ['visibility']."""

    prompt_type: Optional[str]
    """Deprecated. Use analysis_types instead. 'Visibility' or 'Sentiment'."""

    asset: Optional[IDOrName]
    """Required for Sentiment prompts. The brand asset to evaluate."""
