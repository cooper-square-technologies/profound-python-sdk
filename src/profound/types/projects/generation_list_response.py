# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.pagination import Pagination

__all__ = ["GenerationListResponse", "Data"]


class Data(BaseModel):
    category_id: str

    mode: Literal["generate", "adhoc"]

    run_id: str

    status: Literal["queued", "running", "completed", "failed"]

    error: Optional[str] = None

    finished_at: Optional[datetime] = None

    focus_prompt: Optional[str] = None

    started_at: Optional[datetime] = None


class GenerationListResponse(BaseModel):
    data: List[Data]

    pagination: Optional[Pagination] = None
    """Offset-based pagination parameters."""
