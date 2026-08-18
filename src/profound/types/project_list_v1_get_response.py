# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

from .shared.live_generation import LiveGeneration
from .shared.pagination import Pagination

__all__ = ["ProjectListV1GetResponse", "Data"]


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

    live_generation: Optional[LiveGeneration] = None


class ProjectListV1GetResponse(BaseModel):
    data: List[Data]

    pagination: Optional[Pagination] = None
    """Offset-based pagination parameters."""
