# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional, Union

from ..._models import BaseModel

from ..report_info import ReportInfo

__all__ = ["WebSearchResultQueryResponse", "Data"]


class Data(BaseModel):
    metrics: List[Union[int, float, str]]

    dimensions: List[Optional[str]]


class WebSearchResultQueryResponse(BaseModel):
    info: ReportInfo
    """Base model for report information."""

    data: List[Data]
