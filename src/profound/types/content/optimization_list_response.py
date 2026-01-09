# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..shared.pagination import Pagination

__all__ = ["OptimizationListResponse", "Data", "Info", "InfoQuery"]


class Data(BaseModel):
    created_at: datetime

    dify_workflow_run_id: str

    document_title: str

    document_version: int

    extracted_input: Optional[str] = None

    extracted_type: Optional[str] = None

    latest_workflow_step: Optional[str] = None


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
