# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProjectRetrieveResponse", "Data", "DataLiveGeneration", "DataTask"]


class DataTask(BaseModel):
    task_id: str

    project_id: str

    category_id: str

    type: Optional[str] = None

    title: str

    summary: Optional[str] = None

    brief: Optional[str] = None

    topic: Optional[str] = None

    impact: Optional[int] = None

    reference_url: Optional[str] = None

    reference_label: Optional[str] = None

    status: Optional[Literal["not_started", "in_progress", "done", "abandoned"]] = None

    status_changed_at: Optional[datetime] = None

    is_new: Optional[bool] = None

    created_at: Optional[datetime] = None


class DataLiveGeneration(BaseModel):
    run_id: str

    status: Literal["queued", "running", "completed", "failed"]

    started_at: Optional[datetime] = None

    finished_at: Optional[datetime] = None

    error: Optional[str] = None


class Data(BaseModel):
    project_id: str

    category_id: str

    origin_run_id: Optional[str] = None

    initiated_by_user_id: Optional[str] = None

    title: str

    summary: Optional[str] = None

    why: Optional[str] = None

    topics: Optional[List[str]] = None

    prompts: Optional[List[str]] = None

    measurement: Optional[Dict[str, object]] = None

    source_kind: Optional[Literal["generate", "adhoc"]] = None

    source_prompt: Optional[str] = None

    status: Optional[Literal["suggested", "tracked", "retired"]] = None

    task_count: Optional[int] = None

    new_task_count: Optional[int] = None

    retired_at: Optional[datetime] = None

    retired_reason: Optional[str] = None

    latest_version_id: Optional[str] = None

    version_count: Optional[int] = None

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None

    live_generation: Optional[DataLiveGeneration] = None

    tasks: Optional[List[DataTask]] = None


class ProjectRetrieveResponse(BaseModel):
    data: Data
