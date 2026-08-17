# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyClusterVerificationPairsV1ReportsClusterVerificationPairsPostResponse", "ClusterVerificationPair"]


class ClusterVerificationPair(BaseModel):

    pairId: str

    snippetIdx: int

    kbPath: str

    quote: str

    reasoning: str

    sourceUpdatedAt: Optional[str] = None



class AccuracyClusterVerificationPairsV1ReportsClusterVerificationPairsPostResponse(BaseModel):

    data: List[ClusterVerificationPair]

    cluster_reasoning: Optional[str] = FieldInfo(alias="clusterReasoning", default=None)
