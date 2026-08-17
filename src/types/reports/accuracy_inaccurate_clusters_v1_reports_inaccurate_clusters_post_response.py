# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyInaccurateClustersV1ReportsInaccurateClustersPostResponse", "InaccurateClusterRow"]


class InaccurateClusterRow(BaseModel):

    clusterId: str

    canonicalClaim: str

    description: Optional[str] = None

    kbPath: str

    kbSnippet: str

    reasoning: str

    claimCount: int

    responseCount: int

    totalResponseCount: int

    responseShare: float

    responseShareDelta: Optional[float] = None

    citationHostnames: List[str]



class AccuracyInaccurateClustersV1ReportsInaccurateClustersPostResponse(BaseModel):

    data: List[InaccurateClusterRow]

    total_count: int = FieldInfo(alias="totalCount")
