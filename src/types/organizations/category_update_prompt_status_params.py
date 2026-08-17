# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CategoryUpdatePromptStatusParams"]


class CategoryUpdatePromptStatusParams(TypedDict, total=False):

    prompt_ids: Required[Iterable[str]]
    """IDs of the prompts to update."""

    status: Required[Literal["active", "disabled", "deleted"]]
    """Target status: 'active', 'disabled', or 'deleted'."""

    dry_run: bool
    """When true, validate and preview changes without persisting them."""
