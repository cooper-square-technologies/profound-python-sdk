# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TaskCreateResponse", "Data"]


class Data(BaseModel):
    category_id: str

    project_id: str

    task_id: str

    title: str

    brief: Optional[str] = None

    created_at: Optional[datetime] = None

    impact: Optional[int] = None

    is_new: Optional[bool] = None

    reference_label: Optional[str] = None

    reference_url: Optional[str] = None

    status: Optional[Literal["not_started", "in_progress", "done", "abandoned"]] = None

    status_changed_at: Optional[datetime] = None

    summary: Optional[str] = None

    topic: Optional[str] = None

    type: Optional[str] = None


class TaskCreateResponse(BaseModel):
    data: Data
