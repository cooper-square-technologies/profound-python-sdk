# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["ProjectListResponse", "Data", "DataLiveGeneration"]


class DataLiveGeneration(BaseModel):
    run_id: str

    status: Literal["queued", "running", "completed", "failed"]

    error: Optional[str] = None

    finished_at: Optional[datetime] = None

    started_at: Optional[datetime] = None


class Data(BaseModel):
    category_id: str

    project_id: str

    title: str

    initiated_by_user_id: Optional[str] = None

    live_generation: Optional[DataLiveGeneration] = None

    new_task_count: Optional[int] = None

    retired_at: Optional[datetime] = None

    retired_reason: Optional[str] = None

    status: Optional[Literal["suggested", "tracked", "retired"]] = None

    summary: Optional[str] = None

    task_count: Optional[int] = None

    task_types: Optional[List[str]] = None

    topics: Optional[List[str]] = None

    updated_at: Optional[datetime] = None


class ProjectListResponse(BaseModel):
    data: List[Data]

    pagination: Optional[Pagination] = None
    """Offset-based pagination parameters."""
