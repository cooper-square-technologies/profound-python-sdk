# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FolderDeleteParams"]


class FolderDeleteParams(TypedDict, total=False):

    path: Required[str]
    """Folder path to delete."""

    recursive: bool
    """When false, only empty folders are deleted and non-empty folders return a conflict. When true, the folder and all contents are deleted."""

    organization_id: Optional[str]
    """Organization scope for API keys that can access multiple organizations."""
