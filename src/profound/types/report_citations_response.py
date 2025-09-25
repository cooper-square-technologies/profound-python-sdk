# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .info import Info
from .result import Result
from .._models import BaseModel

__all__ = ["ReportCitationsResponse"]


class ReportCitationsResponse(BaseModel):
    data: List[Result]

    info: Info
    """Base model for report information."""
