# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .field_diff import FieldDiff
from .named_resource_diff_list import NamedResourceDiffList

__all__ = ["CategoryUpdatePromptsResponse", "Prompt"]


class Prompt(BaseModel):
    """Preview of changes applied (or to be applied) to a single prompt.

    Only changed fields are included.
    """

    id: str
    """ID of the updated prompt."""

    asset: Optional[FieldDiff] = None
    """Shows the old and new value for a changed field."""

    language: Optional[FieldDiff] = None
    """Shows the old and new value for a changed field."""

    personas: Optional[NamedResourceDiffList] = None
    """Shows which resources were added or removed."""

    platforms: Optional[NamedResourceDiffList] = None
    """Shows which resources were added or removed."""

    prompt: Optional[FieldDiff] = None
    """Shows the old and new value for a changed field."""

    prompt_type: Optional[FieldDiff] = None
    """Shows the old and new value for a changed field."""

    regions: Optional[NamedResourceDiffList] = None
    """Shows which resources were added or removed."""

    tags: Optional[NamedResourceDiffList] = None
    """Shows which resources were added or removed."""

    topic: Optional[FieldDiff] = None
    """Shows the old and new value for a changed field."""


class CategoryUpdatePromptsResponse(BaseModel):
    """Response from updating prompts."""

    dry_run: bool
    """Whether this was a dry run (no changes persisted)."""

    prompts: Optional[List[Prompt]] = None
    """List of prompts with their change diffs."""

    tags_created: Optional[int] = None
    """Number of new tags created."""

    topics_created: Optional[int] = None
    """Number of new topics created."""

    updated: Optional[int] = None
    """Number of prompts that had changes."""
