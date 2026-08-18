# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ..._models import BaseModel

__all__ = ["FolderDeleteV1IDDeleteResponse"]


class FolderDeleteV1IDDeleteResponse(BaseModel):
    message: str
    """Operation result message."""

    path: str
    """Folder path."""
