# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

from .shared.live_generation import LiveGeneration

__all__ = ["ProjectListStatusV1StatusGetResponse", "Data"]


class Data(BaseModel):
    project_id: str

    category_id: str

    status: Literal["suggested", "tracked", "retired"]

    live_generation: Optional[LiveGeneration] = None

    updated_at: Optional[datetime] = None


class ProjectListStatusV1StatusGetResponse(BaseModel):
    data: Data
