# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UpdatePromptStatusBody"]


class UpdatePromptStatusBody(BaseModel):

    prompt_ids: List[str]
    """IDs of the prompts to update."""

    status: Literal["active", "disabled", "deleted"]
    """Target status: 'active', 'disabled', or 'deleted'."""

    dry_run: Optional[bool] = None
    """When true, validate and preview changes without persisting them."""
