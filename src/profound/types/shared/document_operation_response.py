# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DocumentOperationResponse"]


class DocumentOperationResponse(BaseModel):
    message: str
    """Operation result message."""

    name: str
    """Document name."""

    path: str
    """Document path."""

    folder: Optional[str] = None
    """Document folder path."""
