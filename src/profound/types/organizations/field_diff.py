# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FieldDiff"]


class FieldDiff(BaseModel):
    """Shows the old and new value for a changed field."""

    new: Optional[object] = None
    """New value."""

    old: Optional[object] = None
    """Previous value."""
