# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyClaimCitationsV1ReportsClaimCitationsPostResponse", "ClaimCitationRow"]


class ClaimCitationRow(BaseModel):

    href: str

    hostname: str

    path: str

    citationCategory: str

    domainCategory: str

    snippet: str

    citationCount: float

    citationShare: float

    citationShareDelta: Optional[float] = None



class AccuracyClaimCitationsV1ReportsClaimCitationsPostResponse(BaseModel):

    data: List[ClaimCitationRow]

    total_count: int = FieldInfo(alias="totalCount")
