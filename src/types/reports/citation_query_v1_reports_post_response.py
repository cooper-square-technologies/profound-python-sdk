# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional, Union

from ..._models import BaseModel
from ..report_info import ReportInfo

__all__ = ["CitationQueryV1ReportsPostResponse", "CitationsResult"]


class CitationsResult(BaseModel):

    metrics: List[Optional[Union[int, float, str]]]

    dimensions: List[str]



class CitationQueryV1ReportsPostResponse(BaseModel):

    info: ReportInfo
    """Base model for report information."""

    data: List[CitationsResult]
