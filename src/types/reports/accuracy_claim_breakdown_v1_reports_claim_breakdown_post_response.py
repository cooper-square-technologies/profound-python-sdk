# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AccuracyClaimBreakdownV1ReportsClaimBreakdownPostResponse", "ClaimBreakdownRow", "ClaimPromptBreakdownRow"]


class ClaimPromptBreakdownRow(BaseModel):

    id: str

    label: str

    responseCount: int

    totalResponseCount: int

    responseShare: float

    responseShareDelta: Optional[float] = None

    prevResponseCount: int

    prevTotalResponseCount: int

    promptId: str

    promptText: str

    topicId: str

    hasCurrent: bool

class ClaimBreakdownRow(BaseModel):

    id: str

    label: str

    responseCount: int

    totalResponseCount: int

    responseShare: float

    responseShareDelta: Optional[float] = None

    prevResponseCount: int

    prevTotalResponseCount: int



class AccuracyClaimBreakdownV1ReportsClaimBreakdownPostResponse(BaseModel):

    platform: List[ClaimBreakdownRow]

    prompt: List[ClaimPromptBreakdownRow]
