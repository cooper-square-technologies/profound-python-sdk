# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from ..shared.project_task import ProjectTask
from ..shared.pagination import Pagination

__all__ = ["TaskListV1IDGetResponse"]


class TaskListV1IDGetResponse(BaseModel):
    data: List[ProjectTask]

    pagination: Optional[Pagination] = None
    """Offset-based pagination parameters."""
