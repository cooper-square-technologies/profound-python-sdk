# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TaskUpdateStatusV1IDIDStatusPostResponse", "Data"]


class Data(BaseModel):
    task_id: str

    project_id: str

    status: Literal["not_started", "in_progress", "done", "abandoned"]

    changed_at: datetime

    changed_by: Optional[str] = None

    note: Optional[str] = None


class TaskUpdateStatusV1IDIDStatusPostResponse(BaseModel):
    data: Data
