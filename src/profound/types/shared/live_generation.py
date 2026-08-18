# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LiveGeneration"]


class LiveGeneration(BaseModel):
    run_id: str

    status: Literal["queued", "running", "completed", "failed"]

    started_at: Optional[datetime] = None

    finished_at: Optional[datetime] = None

    error: Optional[str] = None
