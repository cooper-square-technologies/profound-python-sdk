# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CategoryUpdatePromptStatusParams"]


class CategoryUpdatePromptStatusParams(TypedDict, total=False):
    prompt_ids: Required[SequenceNotStr[str]]
    """IDs of the prompts to update."""

    status: Required[Literal["active", "disabled", "deleted"]]
    """Target status: 'active', 'disabled', or 'deleted'."""

    dry_run: bool
    """When true, validate and preview changes without persisting them."""
