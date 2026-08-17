# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias
from ..._models import BaseModel

__all__ = ["VisibilityStreamV1ReportsStreamPostResponse", "VisibilityStreamV1ReportsStreamPostResponse", "Query", "VisibilityStreamV1ReportsStreamPostResponse2"]

class VisibilityStreamV1ReportsStreamPostResponse2(BaseModel):
    pass

class Query(BaseModel):
    pass

class VisibilityStreamV1ReportsStreamPostResponse(BaseModel):

    query: Query
    """The normalized query used to build the stream."""

    total_rows: int
    """Total number of rows available before pagination is applied."""



VisibilityStreamV1ReportsStreamPostResponse: TypeAlias = Union[VisibilityStreamV1ReportsStreamPostResponse, VisibilityStreamV1ReportsStreamPostResponse2]
