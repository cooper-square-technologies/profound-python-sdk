# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TaskUpdateStatusResponse", "Data"]


class Data(BaseModel):
    changed_at: datetime

    project_id: str

    status: Literal["not_started", "in_progress", "done", "abandoned"]

    task_id: str

    changed_by: Optional[str] = None

    note: Optional[str] = None


class TaskUpdateStatusResponse(BaseModel):
    data: Data
