# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.pagination import Pagination

__all__ = ["OptimizationListResponse", "Data", "Info", "InfoQuery"]


class Data(BaseModel):
    id: str

    created_at: datetime

    extracted_input: Optional[str] = None

    status: str

    title: str

    type: Literal["file", "text", "url"]


class InfoQuery(BaseModel):
    asset_id: str

    pagination: Optional[Pagination] = None
    """Pagination parameters for the results. Default is 10,000 rows with no offset."""


class Info(BaseModel):
    query: InfoQuery

    total_rows: int


class OptimizationListResponse(BaseModel):
    data: List[Data]

    info: Info
