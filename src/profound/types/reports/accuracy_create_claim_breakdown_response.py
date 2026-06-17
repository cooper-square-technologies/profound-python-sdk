# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateClaimBreakdownResponse", "Platform", "Prompt"]


class Platform(BaseModel):
    id: str

    label: str

    prev_response_count: int = FieldInfo(alias="prevResponseCount")

    prev_total_response_count: int = FieldInfo(alias="prevTotalResponseCount")

    response_count: int = FieldInfo(alias="responseCount")

    response_share: float = FieldInfo(alias="responseShare")

    total_response_count: int = FieldInfo(alias="totalResponseCount")

    response_share_delta: Optional[float] = FieldInfo(alias="responseShareDelta", default=None)


class Prompt(BaseModel):
    id: str

    has_current: bool = FieldInfo(alias="hasCurrent")

    label: str

    prev_response_count: int = FieldInfo(alias="prevResponseCount")

    prev_total_response_count: int = FieldInfo(alias="prevTotalResponseCount")

    prompt_id: str = FieldInfo(alias="promptId")

    prompt_text: str = FieldInfo(alias="promptText")

    response_count: int = FieldInfo(alias="responseCount")

    response_share: float = FieldInfo(alias="responseShare")

    topic_id: str = FieldInfo(alias="topicId")

    total_response_count: int = FieldInfo(alias="totalResponseCount")

    response_share_delta: Optional[float] = FieldInfo(alias="responseShareDelta", default=None)


class AccuracyCreateClaimBreakdownResponse(BaseModel):
    platform: List[Platform]

    prompt: List[Prompt]
