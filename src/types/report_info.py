# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ReportInfo", "Query"]


class Query(BaseModel):
    pass



class ReportInfo(BaseModel):
    """Base model for report information."""

    total_rows: int

    query: Optional[Query] = None
