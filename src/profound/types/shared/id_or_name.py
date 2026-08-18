# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IDOrName"]


class IDOrName(BaseModel):
    """
    Reference by id, name, or both. Plain strings work too:
    UUIDs become id lookups, other strings become name lookups.
    """

    id: Optional[str] = None
    """UUID of the resource."""

    name: Optional[str] = None
    """Display name of the resource."""
