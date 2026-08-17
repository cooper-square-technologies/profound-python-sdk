# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DeleteFolderRequest"]


class DeleteFolderRequest(BaseModel):

    path: str
    """Folder path to delete."""

    recursive: Optional[bool] = None
    """When false, only empty folders are deleted and non-empty folders return a conflict. When true, the folder and all contents are deleted."""
