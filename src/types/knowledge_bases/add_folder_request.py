# File generated from our OpenAPI spec by Scalar. See README.md for details.


from ..._models import BaseModel

__all__ = ["AddFolderRequest"]


class AddFolderRequest(BaseModel):

    path: str
    """Folder path to create."""
