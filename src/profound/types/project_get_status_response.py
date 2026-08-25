# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProjectGetStatusResponse", "Data", "DataLiveGeneration"]


class DataLiveGeneration(BaseModel):
    run_id: str

    status: Literal["queued", "running", "completed", "failed"]

    started_at: Optional[datetime] = None

    finished_at: Optional[datetime] = None

    error: Optional[str] = None


class Data(BaseModel):
    project_id: str

    category_id: str

    status: Literal["suggested", "tracked", "retired"]

    live_generation: Optional[DataLiveGeneration] = None

    updated_at: Optional[datetime] = None


class ProjectGetStatusResponse(BaseModel):
    data: Data
