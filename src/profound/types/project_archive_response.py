# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProjectArchiveResponse", "Data", "DataLiveGeneration"]


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

    created_at: Optional[datetime] = None

    initiated_by_user_id: Optional[str] = None

    latest_version_id: Optional[str] = None

    live_generation: Optional[DataLiveGeneration] = None

    measurement: Optional[Dict[str, object]] = None

    new_task_count: Optional[int] = None

    origin_run_id: Optional[str] = None

    prompts: Optional[List[str]] = None

    retired_at: Optional[datetime] = None

    retired_reason: Optional[str] = None

    source_kind: Optional[Literal["generate", "adhoc"]] = None

    source_prompt: Optional[str] = None

    status: Optional[Literal["suggested", "tracked", "retired"]] = None

    summary: Optional[str] = None

    task_count: Optional[int] = None

    topics: Optional[List[str]] = None

    updated_at: Optional[datetime] = None

    version_count: Optional[int] = None

    why: Optional[str] = None


class ProjectArchiveResponse(BaseModel):
    data: Data
