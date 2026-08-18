# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ClaimModelOccurrence"]


class ClaimModelOccurrence(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    occurrence: Optional[float] = None
    """Only populated for entries in `models`; omitted from grouped-section `model`."""
