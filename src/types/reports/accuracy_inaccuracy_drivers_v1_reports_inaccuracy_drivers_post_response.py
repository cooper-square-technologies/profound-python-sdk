# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AccuracyInaccuracyDriversV1ReportsInaccuracyDriversPostResponse", "InaccuracyDriverRow"]


class InaccuracyDriverRow(BaseModel):

    rowId: str

    clusterId: str

    canonicalClaim: str

    snippet: str

    snippetClaimId: str

    claimOccurrence: float

    claimOccurrenceDelta: Optional[float] = None

    href: str

    citationCategory: str

    domainCategory: str

    citationCount: int



class AccuracyInaccuracyDriversV1ReportsInaccuracyDriversPostResponse(BaseModel):

    data: List[InaccuracyDriverRow]
