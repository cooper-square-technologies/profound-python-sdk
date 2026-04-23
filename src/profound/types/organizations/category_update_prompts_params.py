# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .id_or_name_param import IDOrNameParam

__all__ = ["CategoryUpdatePromptsParams", "Prompt"]


class CategoryUpdatePromptsParams(TypedDict, total=False):
    prompts: Required[Iterable[Prompt]]
    """List of prompt updates.

    Each entry must include an `id` and at least one field to change.
    """

    dry_run: bool
    """When true, validate and preview changes without persisting them."""


class Prompt(TypedDict, total=False):
    """Fields to update on an existing prompt.

    Only provided fields are changed; omitted fields are left unchanged.
    """

    id: Required[str]
    """ID of the prompt to update."""

    asset: Optional[IDOrNameParam]
    """Reference by id, name, or both.

    Plain strings work too: UUIDs become id lookups, other strings become name
    lookups.
    """

    language: Optional[str]
    """New language code. Must be enabled for the organization."""

    personas: Optional[Iterable[IDOrNameParam]]
    """New persona set. Replaces all existing personas."""

    platforms: Optional[Iterable[IDOrNameParam]]
    """New platform set. Replaces all existing platforms."""

    prompt: Optional[str]
    """New prompt text."""

    prompt_type: Optional[str]
    """'Visibility' or 'Sentiment'."""

    regions: Optional[Iterable[IDOrNameParam]]
    """New region set. Replaces all existing regions."""

    tags: Optional[Iterable[IDOrNameParam]]
    """New tag set. Replaces all existing tags on the prompt."""

    topic: Optional[IDOrNameParam]
    """Reference by id, name, or both.

    Plain strings work too: UUIDs become id lookups, other strings become name
    lookups.
    """
