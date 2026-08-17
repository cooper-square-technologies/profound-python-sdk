# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostResponse", "TopInaccurateClaimRow"]


class TopInaccurateClaimRow(BaseModel):

    clusterId: str

    canonicalClaim: str

    claimOccurrence: float

    claimOccurrenceDelta: Optional[float] = None



class AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostResponse(BaseModel):

    data: List[TopInaccurateClaimRow]
