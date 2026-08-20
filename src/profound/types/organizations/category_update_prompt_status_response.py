# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CategoryUpdatePromptStatusResponse"]


class CategoryUpdatePromptStatusResponse(BaseModel):
    dry_run: bool
    """Whether this was a dry run (no changes persisted)."""

    updated_prompts: Optional[int] = None
    """Number of prompts whose status was changed."""
