# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional, Union

from .._models import BaseModel

from .report_info import ReportInfo

__all__ = ["ReportCitationsResponse", "Data"]


class Data(BaseModel):
    metrics: List[Optional[Union[float, str]]]

    dimensions: List[str]


class ReportCitationsResponse(BaseModel):
    info: ReportInfo
    """Base model for report information."""

    data: List[Data]
