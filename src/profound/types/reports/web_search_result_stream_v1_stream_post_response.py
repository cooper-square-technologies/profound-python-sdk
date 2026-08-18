# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Union
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["WebSearchResultStreamV1StreamPostResponse", "SseSummaryEventData"]


class SseSummaryEventData(BaseModel):
    query: Dict[str, object]
    """The normalized query used to build the stream."""

    total_rows: int
    """Total number of rows available before pagination is applied."""


WebSearchResultStreamV1StreamPostResponse: TypeAlias = Union[SseSummaryEventData, Dict[str, object]]
