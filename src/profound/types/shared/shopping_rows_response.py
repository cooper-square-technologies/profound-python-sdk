# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List

from ..._models import BaseModel

from .info import Info

__all__ = ["ShoppingRowsResponse"]


class ShoppingRowsResponse(BaseModel):
    info: Info
    """Base model for report information."""

    data: List[Dict[str, object]]
