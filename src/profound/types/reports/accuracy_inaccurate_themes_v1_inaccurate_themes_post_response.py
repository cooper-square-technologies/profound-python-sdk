# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyInaccurateThemesV1InaccurateThemesPostResponse", "Data"]


class Data(BaseModel):
    theme_id: str = FieldInfo(alias="themeId")

    neutral_theme: str = FieldInfo(alias="neutralTheme")

    description: Optional[str] = None

    inaccurate_claim_count: int = FieldInfo(alias="inaccurateClaimCount")

    inaccurate_cluster_count: int = FieldInfo(alias="inaccurateClusterCount")

    total_claim_count: int = FieldInfo(alias="totalClaimCount")

    total_cluster_count: int = FieldInfo(alias="totalClusterCount")

    response_count: int = FieldInfo(alias="responseCount")

    total_response_count: int = FieldInfo(alias="totalResponseCount")

    response_share: float = FieldInfo(alias="responseShare")

    response_share_delta: Optional[float] = FieldInfo(alias="responseShareDelta", default=None)


class AccuracyInaccurateThemesV1InaccurateThemesPostResponse(BaseModel):
    data: List[Data]

    total_count: int = FieldInfo(alias="totalCount")
