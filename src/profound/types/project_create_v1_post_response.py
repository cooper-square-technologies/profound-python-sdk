# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProjectCreateV1PostResponse", "Data"]


class Data(BaseModel):
    project_id: str

    run_id: str

    status: Optional[Literal["queued", "running"]] = None


class ProjectCreateV1PostResponse(BaseModel):
    data: Data
