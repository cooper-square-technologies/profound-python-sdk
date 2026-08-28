# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProjectUnarchiveResponse", "Data", "DataLiveGeneration"]


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


class ProjectUnarchiveResponse(BaseModel):
    data: Data
