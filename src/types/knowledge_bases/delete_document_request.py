# File generated from our OpenAPI spec by Scalar. See README.md for details.


from ..._models import BaseModel

__all__ = ["DeleteDocumentRequest"]


class DeleteDocumentRequest(BaseModel):

    name: str
    """Document path to delete."""
