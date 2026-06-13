# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from .._models import BaseModel
from .report_info import ReportInfo

__all__ = ["ReportCitationsResponse", "Data"]


class Data(BaseModel):
    dimensions: List[str]

    metrics: List[Union[float, str, None]]


class ReportCitationsResponse(BaseModel):
    data: List[Data]

    info: ReportInfo
    """Base model for report information."""
