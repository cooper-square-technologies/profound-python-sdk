# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ..._models import BaseModel

__all__ = ["FolderCreateV1IDPostResponse"]


class FolderCreateV1IDPostResponse(BaseModel):
    message: str
    """Operation result message."""

    path: str
    """Folder path."""
