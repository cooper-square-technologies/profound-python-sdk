# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateClaimBreakdownResponse", "Platform", "Prompt"]


class Prompt(BaseModel):
    id: str

    label: str

    response_count: int = FieldInfo(alias="responseCount")

    total_response_count: int = FieldInfo(alias="totalResponseCount")

    response_share: float = FieldInfo(alias="responseShare")

    response_share_delta: Optional[float] = FieldInfo(alias="responseShareDelta", default=None)

    prev_response_count: int = FieldInfo(alias="prevResponseCount")

    prev_total_response_count: int = FieldInfo(alias="prevTotalResponseCount")

    prompt_id: str = FieldInfo(alias="promptId")

    prompt_text: str = FieldInfo(alias="promptText")

    topic_id: str = FieldInfo(alias="topicId")

    has_current: bool = FieldInfo(alias="hasCurrent")


class Platform(BaseModel):
    id: str

    label: str

    response_count: int = FieldInfo(alias="responseCount")

    total_response_count: int = FieldInfo(alias="totalResponseCount")

    response_share: float = FieldInfo(alias="responseShare")

    response_share_delta: Optional[float] = FieldInfo(alias="responseShareDelta", default=None)

    prev_response_count: int = FieldInfo(alias="prevResponseCount")

    prev_total_response_count: int = FieldInfo(alias="prevTotalResponseCount")


class AccuracyCreateClaimBreakdownResponse(BaseModel):
    platform: List[Platform]

    prompt: List[Prompt]
