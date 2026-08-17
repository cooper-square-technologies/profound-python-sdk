# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Union
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ReportStreamVisibilityResponse", "SseSummaryEventData"]


class SseSummaryEventData(BaseModel):
    query: Dict[str, object]
    """The normalized query used to build the stream."""

    total_rows: int
    """Total number of rows available before pagination is applied."""


ReportStreamVisibilityResponse: TypeAlias = Union[SseSummaryEventData, Dict[str, object]]
