# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GenerationRetrieveResponse", "Data"]


class Data(BaseModel):
    run_id: str

    category_id: str

    mode: Literal["generate", "adhoc"]

    focus_prompt: Optional[str] = None

    status: Literal["queued", "running", "completed", "failed"]

    started_at: Optional[datetime] = None

    finished_at: Optional[datetime] = None

    error: Optional[str] = None


class GenerationRetrieveResponse(BaseModel):
    data: Data
