# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from ..shared.project_task import ProjectTask
from ..shared.pagination import Pagination

__all__ = ["TaskListResponse"]


class TaskListResponse(BaseModel):
    data: List[ProjectTask]

    pagination: Optional[Pagination] = None
    """Offset-based pagination parameters."""
