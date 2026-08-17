# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyBreakdownV1ReportsBreakdownPostResponse", "AccuracyBreakdownRow"]


class AccuracyBreakdownRow(BaseModel):

    id: str

    name: str

    share: float

    shareChange: Optional[float] = None

    responseAccuracy: float

    accuracyChange: Optional[float] = None

    inaccurateCount: int

    inaccurateCountChange: Optional[int] = None

    promptCount: Optional[int] = None

    citationCategory: Optional[str] = None



class AccuracyBreakdownV1ReportsBreakdownPostResponse(BaseModel):

    data: List[AccuracyBreakdownRow]

    total_count: int = FieldInfo(alias="totalCount")
