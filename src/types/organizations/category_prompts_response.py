# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..named_resource import NamedResource

__all__ = ["CategoryPromptsResponse", "PaginationInfo", "Prompt"]


class Prompt(BaseModel):

    id: str

    analysis_types: Optional[List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]] = None

    prompt_type: Optional[str] = None

    prompt: str

    language: str

    status: Literal["active", "disabled"]

    topic: NamedResource
    """Generic id+name reference used across domain boundaries."""

    tags: Optional[List[NamedResource]] = None

    regions: List[NamedResource]

    platforms: List[NamedResource]

    personas: Optional[List[NamedResource]] = None

    created_at: datetime

    updated_at: datetime

class PaginationInfo(BaseModel):

    total_rows: int

    limit: int

    next_cursor: Optional[str] = None



class CategoryPromptsResponse(BaseModel):

    info: PaginationInfo

    data: List[Prompt]
