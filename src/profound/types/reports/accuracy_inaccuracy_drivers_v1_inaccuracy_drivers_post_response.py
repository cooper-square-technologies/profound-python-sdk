# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyInaccuracyDriversV1InaccuracyDriversPostResponse", "Data"]


class Data(BaseModel):
    row_id: str = FieldInfo(alias="rowId")

    cluster_id: str = FieldInfo(alias="clusterId")

    canonical_claim: str = FieldInfo(alias="canonicalClaim")

    snippet: str

    snippet_claim_id: str = FieldInfo(alias="snippetClaimId")

    claim_occurrence: float = FieldInfo(alias="claimOccurrence")

    claim_occurrence_delta: Optional[float] = FieldInfo(alias="claimOccurrenceDelta", default=None)

    href: str

    citation_category: str = FieldInfo(alias="citationCategory")

    domain_category: str = FieldInfo(alias="domainCategory")

    citation_count: int = FieldInfo(alias="citationCount")


class AccuracyInaccuracyDriversV1InaccuracyDriversPostResponse(BaseModel):
    data: List[Data]
