# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias
from ..._models import BaseModel

__all__ = ["SentimentStreamV1ReportsStreamPostResponse", "SentimentStreamV1ReportsStreamPostResponse", "Query", "SentimentStreamV1ReportsStreamPostResponse2"]

class SentimentStreamV1ReportsStreamPostResponse2(BaseModel):
    pass

class Query(BaseModel):
    pass

class SentimentStreamV1ReportsStreamPostResponse(BaseModel):

    query: Query
    """The normalized query used to build the stream."""

    total_rows: int
    """Total number of rows available before pagination is applied."""



SentimentStreamV1ReportsStreamPostResponse: TypeAlias = Union[SentimentStreamV1ReportsStreamPostResponse, SentimentStreamV1ReportsStreamPostResponse2]
