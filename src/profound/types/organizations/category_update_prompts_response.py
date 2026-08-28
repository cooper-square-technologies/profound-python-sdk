# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from .field_diff import FieldDiff
from .named_resource_diff_list import NamedResourceDiffList

__all__ = ["CategoryUpdatePromptsResponse", "Prompt"]


class Prompt(BaseModel):
    id: str
    """ID of the updated prompt."""

    prompt: Optional[FieldDiff] = None
    """Prompt text diff."""

    topic: Optional[FieldDiff] = None
    """Topic diff."""

    language: Optional[FieldDiff] = None
    """Language diff."""

    tags: Optional[NamedResourceDiffList] = None
    """Tags added and removed."""

    regions: Optional[NamedResourceDiffList] = None
    """Regions added and removed."""

    platforms: Optional[NamedResourceDiffList] = None
    """Platforms added and removed."""

    personas: Optional[NamedResourceDiffList] = None
    """Personas added and removed."""

    analysis_types: Optional[FieldDiff] = None
    """Analysis types diff."""

    asset: Optional[FieldDiff] = None
    """Asset diff."""


class CategoryUpdatePromptsResponse(BaseModel):
    dry_run: bool
    """Whether this was a dry run (no changes persisted)."""

    updated: Optional[int] = None
    """Number of prompts that had changes."""

    topics_created: Optional[int] = None
    """Number of new topics created."""

    tags_created: Optional[int] = None
    """Number of new tags created."""

    prompts: Optional[List[Prompt]] = None
    """List of prompts with their change diffs."""
