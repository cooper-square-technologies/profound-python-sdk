# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..named_resource import NamedResource

__all__ = ["CategoryPromptsResponse", "Data", "Info"]


class Data(BaseModel):
    id: str

    created_at: datetime

    language: str

    platforms: List[NamedResource]

    prompt: str

    regions: List[NamedResource]

    status: Literal["active", "disabled"]

    topic: NamedResource
    """Generic id+name reference used across domain boundaries."""

    updated_at: datetime

    analysis_types: Optional[List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]] = None

    personas: Optional[List[NamedResource]] = None

    prompt_type: Optional[str] = None

    tags: Optional[List[NamedResource]] = None


class Info(BaseModel):
    limit: int

    next_cursor: Optional[str] = None

    total_rows: int


class CategoryPromptsResponse(BaseModel):
    data: List[Data]

    info: Info
