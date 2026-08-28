# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel

from .report_info import ReportInfo
from .report_result import ReportResult

__all__ = ["ReportResponse"]


class ReportResponse(BaseModel):
    """Base response model for reports."""

    info: ReportInfo
    """Base model for report information."""

    data: List[ReportResult]
