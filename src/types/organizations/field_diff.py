# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FieldDiff"]


class FieldDiff(BaseModel):
    """Shows the old and new value for a changed field."""

    old: Optional[str] = None
    """Previous value."""

    new: Optional[str] = None
    """New value."""
