# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DimensionRef"]


class DimensionRef(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None
