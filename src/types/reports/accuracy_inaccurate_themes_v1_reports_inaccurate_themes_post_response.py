# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyInaccurateThemesV1ReportsInaccurateThemesPostResponse", "InaccurateThemeRow"]


class InaccurateThemeRow(BaseModel):

    themeId: str

    neutralTheme: str

    description: Optional[str] = None

    inaccurateClaimCount: int

    inaccurateClusterCount: int

    totalClaimCount: int

    totalClusterCount: int

    responseCount: int

    totalResponseCount: int

    responseShare: float

    responseShareDelta: Optional[float] = None



class AccuracyInaccurateThemesV1ReportsInaccurateThemesPostResponse(BaseModel):

    data: List[InaccurateThemeRow]

    total_count: int = FieldInfo(alias="totalCount")
