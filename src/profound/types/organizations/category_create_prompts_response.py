# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..named_resource import NamedResource

__all__ = ["CategoryCreatePromptsResponse", "Prompt"]


class Prompt(BaseModel):
    """Preview of a prompt that was (or would be) created."""

    id: str
    """Generated prompt ID."""

    language: str
    """Language code."""

    prompt: str
    """The prompt text."""

    topic: NamedResource
    """Resolved topic."""

    analysis_types: Optional[List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]] = None
    """Analysis types assigned to this prompt."""

    asset: Optional[NamedResource] = None
    """Generic id+name reference used across domain boundaries."""

    personas: Optional[List[NamedResource]] = None
    """Resolved personas."""

    platforms: Optional[List[NamedResource]] = None
    """Resolved platforms."""

    regions: Optional[List[NamedResource]] = None
    """Resolved regions."""

    tags: Optional[List[NamedResource]] = None
    """Resolved tags."""


class CategoryCreatePromptsResponse(BaseModel):
    """Response from creating prompts."""

    dry_run: bool
    """Whether this was a dry run (no changes persisted)."""

    created: Optional[int] = None
    """Number of prompts created."""

    prompts: Optional[List[Prompt]] = None
    """List of created (or previewed) prompts with resolved references."""

    tags_created: Optional[int] = None
    """Number of new tags created."""

    topics_created: Optional[int] = None
    """Number of new topics created."""
