# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateClusterVerificationPairsResponse", "Data"]


class Data(BaseModel):
    kb_path: str = FieldInfo(alias="kbPath")

    pair_id: str = FieldInfo(alias="pairId")

    quote: str

    reasoning: str

    snippet_idx: int = FieldInfo(alias="snippetIdx")

    source_updated_at: Optional[str] = FieldInfo(alias="sourceUpdatedAt", default=None)


class AccuracyCreateClusterVerificationPairsResponse(BaseModel):
    data: List[Data]

    cluster_reasoning: Optional[str] = FieldInfo(alias="clusterReasoning", default=None)
