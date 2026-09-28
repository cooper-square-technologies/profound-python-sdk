# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateClaimCitationsResponse", "Data"]


class Data(BaseModel):
    href: str

    hostname: str

    path: str

    citation_category: str = FieldInfo(alias="citationCategory")

    domain_category: str = FieldInfo(alias="domainCategory")

    snippet: str

    citation_count: float = FieldInfo(alias="citationCount")

    citation_share: float = FieldInfo(alias="citationShare")
    """Citation share as a 0-100 percentage; 0.4718 means 0.4718%."""

    citation_share_delta: Optional[float] = FieldInfo(alias="citationShareDelta", default=None)
    """Change in citation share in percentage points."""


class AccuracyCreateClaimCitationsResponse(BaseModel):
    data: List[Data]

    total_count: int = FieldInfo(alias="totalCount")
