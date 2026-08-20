# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ..._models import BaseModel

__all__ = ["FolderCreateResponse"]


class FolderCreateResponse(BaseModel):
    message: str
    """Operation result message."""

    path: str
    """Folder path."""
