# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DocumentUpdateResponse"]


class DocumentUpdateResponse(BaseModel):
    message: str
    """Operation result message."""

    name: str
    """Document name."""

    path: str
    """Document path."""

    folder: Optional[str] = None
    """Document folder path."""
