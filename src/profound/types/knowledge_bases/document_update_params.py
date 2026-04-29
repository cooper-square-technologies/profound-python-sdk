# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DocumentUpdateParams"]


class DocumentUpdateParams(TypedDict, total=False):
    name: Required[str]
    """Document name or path to update."""

    text: Required[str]
    """Replacement text content for the document."""

    organization_id: Optional[str]
    """Organization scope for API keys that can access multiple organizations."""

    folder: Optional[str]
    """Folder path containing the document."""
