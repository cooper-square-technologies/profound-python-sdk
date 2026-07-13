# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProjectCreateResponse", "Data"]


class Data(BaseModel):
    project_id: str

    run_id: str

    status: Optional[Literal["queued", "running"]] = None


class ProjectCreateResponse(BaseModel):
    data: Data
