# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ..._models import BaseModel

from ..shared.project_task import ProjectTask

__all__ = ["TaskCreateResponse"]


class TaskCreateResponse(BaseModel):
    data: ProjectTask
