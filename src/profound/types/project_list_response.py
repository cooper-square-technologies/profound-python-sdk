# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

from .shared.pagination import Pagination

__all__ = ["ProjectListResponse", "Data", "DataLiveGeneration"]


class DataLiveGeneration(BaseModel):
    run_id: str

    status: Literal["queued", "running", "completed", "failed"]

    started_at: Optional[datetime] = None

    finished_at: Optional[datetime] = None

    error: Optional[str] = None


class Data(BaseModel):
    project_id: str

    category_id: str

    status: Optional[Literal["suggested", "tracked", "retired"]] = None

    title: str

    summary: Optional[str] = None

    initiated_by_user_id: Optional[str] = None

    topics: Optional[List[str]] = None

    updated_at: Optional[datetime] = None

    task_types: Optional[List[str]] = None

    task_count: Optional[int] = None

    new_task_count: Optional[int] = None

    retired_at: Optional[datetime] = None

    retired_reason: Optional[str] = None

    live_generation: Optional[DataLiveGeneration] = None


class ProjectListResponse(BaseModel):
    data: List[Data]

    pagination: Optional[Pagination] = None
    """Offset-based pagination parameters."""
