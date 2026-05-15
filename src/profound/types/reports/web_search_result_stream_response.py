# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["WebSearchResultStreamResponse", "SseSummaryEventData"]


class SseSummaryEventData(BaseModel):
    query: Dict[str, object]
    """The normalized query used to build the stream."""

    total_rows: int
    """Total number of rows available before pagination is applied."""


WebSearchResultStreamResponse: TypeAlias = Union[SseSummaryEventData, Dict[str, object]]
