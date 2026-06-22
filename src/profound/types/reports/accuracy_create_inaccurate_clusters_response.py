# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateInaccurateClustersResponse", "Data"]


class Data(BaseModel):
    canonical_claim: str = FieldInfo(alias="canonicalClaim")

    citation_hostnames: List[str] = FieldInfo(alias="citationHostnames")

    claim_count: int = FieldInfo(alias="claimCount")

    cluster_id: str = FieldInfo(alias="clusterId")

    kb_path: str = FieldInfo(alias="kbPath")

    kb_snippet: str = FieldInfo(alias="kbSnippet")

    reasoning: str

    response_count: int = FieldInfo(alias="responseCount")

    response_share: float = FieldInfo(alias="responseShare")

    total_response_count: int = FieldInfo(alias="totalResponseCount")

    description: Optional[str] = None

    response_share_delta: Optional[float] = FieldInfo(alias="responseShareDelta", default=None)


class AccuracyCreateInaccurateClustersResponse(BaseModel):
    data: List[Data]

    total_count: int = FieldInfo(alias="totalCount")
