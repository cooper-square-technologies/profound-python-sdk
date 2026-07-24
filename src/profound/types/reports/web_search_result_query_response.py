# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ..._models import BaseModel
from ..report_info import ReportInfo

__all__ = ["WebSearchResultQueryResponse", "Data"]


class Data(BaseModel):
    dimensions: List[Optional[str]]

    metrics: List[Union[float, str]]


class WebSearchResultQueryResponse(BaseModel):
    data: List[Data]

    info: ReportInfo
    """Base model for report information."""
