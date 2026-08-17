# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CursorPagination"]


class CursorPagination(BaseModel):
    """Cursor-based pagination metadata."""

    limit: Optional[int] = None
    """Maximum number of results to return. Default is 10,000, maximum is 50,000."""

    next_cursor: Optional[str] = None
    """Token for the next page, if more results are available."""
