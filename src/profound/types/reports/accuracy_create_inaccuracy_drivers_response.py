# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateInaccuracyDriversResponse", "Data"]


class Data(BaseModel):
    """A top inaccurate claim paired with one of its most-cited pages."""

    canonical_claim: str = FieldInfo(alias="canonicalClaim")

    citation_category: str = FieldInfo(alias="citationCategory")

    citation_count: int = FieldInfo(alias="citationCount")

    claim_occurrence: float = FieldInfo(alias="claimOccurrence")

    cluster_id: str = FieldInfo(alias="clusterId")

    domain_category: str = FieldInfo(alias="domainCategory")

    href: str

    row_id: str = FieldInfo(alias="rowId")

    snippet: str

    snippet_claim_id: str = FieldInfo(alias="snippetClaimId")

    claim_occurrence_delta: Optional[float] = FieldInfo(alias="claimOccurrenceDelta", default=None)


class AccuracyCreateInaccuracyDriversResponse(BaseModel):
    data: List[Data]
