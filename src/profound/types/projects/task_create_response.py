# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TaskCreateResponse", "Data"]


class Data(BaseModel):
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


class TaskCreateResponse(BaseModel):
    data: Data
