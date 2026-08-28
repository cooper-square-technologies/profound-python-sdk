# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FolderCreateParams"]


class FolderCreateParams(TypedDict, total=False):
    path: Required[str]
    """Folder path to create."""

    organization_id: Optional[str]
    """Organization scope for API keys that can access multiple organizations."""
