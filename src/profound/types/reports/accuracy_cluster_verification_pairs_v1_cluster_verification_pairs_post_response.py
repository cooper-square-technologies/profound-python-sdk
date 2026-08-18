# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyClusterVerificationPairsV1ClusterVerificationPairsPostResponse", "Data"]


class Data(BaseModel):
    pair_id: str = FieldInfo(alias="pairId")

    snippet_idx: int = FieldInfo(alias="snippetIdx")

    kb_path: str = FieldInfo(alias="kbPath")

    quote: str

    reasoning: str

    source_updated_at: Optional[str] = FieldInfo(alias="sourceUpdatedAt", default=None)


class AccuracyClusterVerificationPairsV1ClusterVerificationPairsPostResponse(BaseModel):
    data: List[Data]

    cluster_reasoning: Optional[str] = FieldInfo(alias="clusterReasoning", default=None)
