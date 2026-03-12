# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CategoryPromptsResponse", "Data", "DataPlatform", "DataRegion", "DataTopic", "DataTag", "Info"]


class DataPlatform(BaseModel):
    """Generic id+name reference used across domain boundaries."""

    id: str

    name: str


class DataRegion(BaseModel):
    """Generic id+name reference used across domain boundaries."""

    id: str

    name: str


class DataTopic(BaseModel):
    """Generic id+name reference used across domain boundaries."""

    id: str

    name: str


class DataTag(BaseModel):
    """Generic id+name reference used across domain boundaries."""

    id: str

    name: str


class Data(BaseModel):
    id: str

    created_at: datetime

    platforms: List[DataPlatform]

    prompt: str

    prompt_type: str

    regions: List[DataRegion]

    topic: DataTopic
    """Generic id+name reference used across domain boundaries."""

    tags: Optional[List[DataTag]] = None


class Info(BaseModel):
    limit: int

    next_cursor: Optional[str] = None

    total_rows: int


class CategoryPromptsResponse(BaseModel):
    data: List[Data]

    info: Info
