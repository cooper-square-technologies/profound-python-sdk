# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateClaimCitationsResponse", "Data"]


class Data(BaseModel):
    citation_category: str = FieldInfo(alias="citationCategory")

    citation_count: float = FieldInfo(alias="citationCount")

    citation_share: float = FieldInfo(alias="citationShare")

    domain_category: str = FieldInfo(alias="domainCategory")

    hostname: str

    href: str

    path: str

    snippet: str

    citation_share_delta: Optional[float] = FieldInfo(alias="citationShareDelta", default=None)


class AccuracyCreateClaimCitationsResponse(BaseModel):
    data: List[Data]

    total_count: int = FieldInfo(alias="totalCount")
