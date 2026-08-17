# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias
from ..._models import BaseModel

__all__ = ["WebSearchResultStreamResponse", "WebSearchResultStreamResponse", "Query", "WebSearchResultStreamResponse2"]

class WebSearchResultStreamResponse2(BaseModel):
    pass

class Query(BaseModel):
    pass

class WebSearchResultStreamResponse(BaseModel):

    query: Query
    """The normalized query used to build the stream."""

    total_rows: int
    """Total number of rows available before pagination is applied."""



WebSearchResultStreamResponse: TypeAlias = Union[WebSearchResultStreamResponse, WebSearchResultStreamResponse2]
