# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateClusterVerificationPairsResponse", "Data"]


class Data(BaseModel):
    kb_path: str = FieldInfo(alias="kbPath")

    pair_id: str = FieldInfo(alias="pairId")

    quote: str

    reasoning: str

    snippet_idx: int = FieldInfo(alias="snippetIdx")


class AccuracyCreateClusterVerificationPairsResponse(BaseModel):
    data: List[Data]
