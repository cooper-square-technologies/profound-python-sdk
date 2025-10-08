# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .report_info import ReportInfo
from .report_result import ReportResult

__all__ = ["ReportCitationsResponse"]


class ReportCitationsResponse(BaseModel):
    data: List[ReportResult]

    info: ReportInfo
    """Base model for report information."""
