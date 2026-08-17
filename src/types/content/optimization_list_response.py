# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..pagination import Pagination

__all__ = ["OptimizationListResponse", "ContentOptimizationResponseInfo", "OptimizationQuery", "ContentOptimization"]


class ContentOptimization(BaseModel):

    id: str

    title: str

    created_at: datetime

    extracted_input: Optional[str] = None

    type: Literal["file", "text", "url"]

    status: str

class OptimizationQuery(BaseModel):

    asset_id: str

    pagination: Optional[Pagination] = None
    """Pagination parameters for the results. Default is 10,000 rows with no offset."""

class ContentOptimizationResponseInfo(BaseModel):

    total_rows: int

    query: OptimizationQuery



class OptimizationListResponse(BaseModel):

    info: ContentOptimizationResponseInfo

    data: List[ContentOptimization]
