# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DocumentCreateParams"]


class DocumentCreateParams(TypedDict, total=False):
    name: Required[str]
    """Unique document name."""

    text: Required[str]
    """Text content to add to the document."""

    folder: Optional[str]
    """Folder path to add the document under."""

    organization_id: Optional[str]
    """Organization scope for API keys that can access multiple organizations."""
