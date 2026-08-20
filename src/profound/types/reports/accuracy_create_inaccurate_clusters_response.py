# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateInaccurateClustersResponse", "Data", "DataModel"]


class DataModel(BaseModel):
    api_model_id: str = FieldInfo(alias="modelId")

    occurrence: float


class Data(BaseModel):
    cluster_id: str = FieldInfo(alias="clusterId")

    canonical_claim: str = FieldInfo(alias="canonicalClaim")

    neutral_theme: Optional[str] = FieldInfo(alias="neutralTheme", default=None)

    description: Optional[str] = None

    kb_path: str = FieldInfo(alias="kbPath")

    kb_snippet: str = FieldInfo(alias="kbSnippet")

    reasoning: str

    claim_count: int = FieldInfo(alias="claimCount")

    response_count: int = FieldInfo(alias="responseCount")

    total_response_count: int = FieldInfo(alias="totalResponseCount")

    response_share: float = FieldInfo(alias="responseShare")

    response_share_delta: Optional[float] = FieldInfo(alias="responseShareDelta", default=None)

    citation_hostnames: List[str] = FieldInfo(alias="citationHostnames")

    models: Optional[List[DataModel]] = None


class AccuracyCreateInaccurateClustersResponse(BaseModel):
    data: List[Data]

    total_count: int = FieldInfo(alias="totalCount")
