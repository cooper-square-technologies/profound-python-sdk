# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateInaccurateThemesResponse", "Data"]


class Data(BaseModel):
    description: str

    inaccurate_claim_count: int = FieldInfo(alias="inaccurateClaimCount")

    inaccurate_cluster_count: int = FieldInfo(alias="inaccurateClusterCount")

    neutral_theme: str = FieldInfo(alias="neutralTheme")

    response_count: int = FieldInfo(alias="responseCount")

    response_share: float = FieldInfo(alias="responseShare")

    theme_id: str = FieldInfo(alias="themeId")

    total_claim_count: int = FieldInfo(alias="totalClaimCount")

    total_cluster_count: int = FieldInfo(alias="totalClusterCount")

    total_response_count: int = FieldInfo(alias="totalResponseCount")

    response_share_delta: Optional[float] = FieldInfo(alias="responseShareDelta", default=None)


class AccuracyCreateInaccurateThemesResponse(BaseModel):
    data: List[Data]

    total_count: int = FieldInfo(alias="totalCount")
