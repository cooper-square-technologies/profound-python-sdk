# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..report_info import ReportInfo

__all__ = ["WebSearchResultQueryResponse", "Data"]


class Data(BaseModel):
    dimensions: List[Optional[str]]

    metrics: List[float]


class WebSearchResultQueryResponse(BaseModel):
    data: List[Data]

    info: ReportInfo
    """Base model for report information."""
