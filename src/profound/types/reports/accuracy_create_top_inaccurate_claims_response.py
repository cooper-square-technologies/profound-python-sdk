# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateTopInaccurateClaimsResponse", "Data"]


class Data(BaseModel):
    cluster_id: str = FieldInfo(alias="clusterId")

    canonical_claim: str = FieldInfo(alias="canonicalClaim")

    claim_occurrence: float = FieldInfo(alias="claimOccurrence")

    claim_occurrence_delta: Optional[float] = FieldInfo(alias="claimOccurrenceDelta", default=None)


class AccuracyCreateTopInaccurateClaimsResponse(BaseModel):
    data: List[Data]
