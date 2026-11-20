# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

from ..named_resource import NamedResource

__all__ = ["CategoryPromptsResponse", "Info", "Data"]


class Data(BaseModel):
    id: str

    analysis_types: Optional[List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]] = None
    """Analysis types assigned to this prompt. `sentiment_v2` is current sentiment, the same as the `sentiment` input."""

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

    created_at: str

    updated_at: str


class Info(BaseModel):
    total_rows: int

    limit: int

    next_cursor: Optional[str] = None


class CategoryPromptsResponse(BaseModel):
    info: Info

    data: List[Data]
