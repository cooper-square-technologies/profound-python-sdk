# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

from ..named_resource import NamedResource

__all__ = ["CategoryCreatePromptsResponse", "Prompt"]


class Prompt(BaseModel):
    id: str
    """Generated prompt ID."""

    prompt: str
    """The prompt text."""

    topic: NamedResource
    """Resolved topic."""

    language: str
    """Language code."""

    tags: Optional[List[NamedResource]] = None
    """Resolved tags."""

    regions: Optional[List[NamedResource]] = None
    """Resolved regions."""

    platforms: Optional[List[NamedResource]] = None
    """Resolved platforms."""

    personas: Optional[List[NamedResource]] = None
    """Resolved personas."""

    analysis_types: Optional[List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]] = None
    """Analysis types assigned to this prompt."""

    asset: Optional[NamedResource] = None
    """Resolved asset, if applicable."""


class CategoryCreatePromptsResponse(BaseModel):
    dry_run: bool
    """Whether this was a dry run (no changes persisted)."""

    created: Optional[int] = None
    """Number of prompts created."""

    topics_created: Optional[int] = None
    """Number of new topics created."""

    tags_created: Optional[int] = None
    """Number of new tags created."""

    prompts: Optional[List[Prompt]] = None
    """List of created (or previewed) prompts with resolved references."""
