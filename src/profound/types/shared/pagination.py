# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Pagination"]


class Pagination(BaseModel):
    limit: Optional[int] = None
    """Maximum number of results to return. Default is 10,000, maximum is 50,000."""

    offset: Optional[int] = None
    """Offset for the results. Used for pagination."""
