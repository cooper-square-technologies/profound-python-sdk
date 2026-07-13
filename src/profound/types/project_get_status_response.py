# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProjectGetStatusResponse", "Data", "DataLiveGeneration"]


class DataLiveGeneration(BaseModel):
    run_id: str

    status: Literal["queued", "running", "completed", "failed"]

    error: Optional[str] = None

    finished_at: Optional[datetime] = None

    started_at: Optional[datetime] = None


class Data(BaseModel):
    category_id: str

    project_id: str

    status: Literal["suggested", "tracked", "retired"]

    live_generation: Optional[DataLiveGeneration] = None

    updated_at: Optional[datetime] = None


class ProjectGetStatusResponse(BaseModel):
    data: Data
