# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyBreakdownV1BreakdownPostResponse", "Data"]


class Data(BaseModel):
    id: str

    name: str

    group_ids: Optional[Dict[str, str]] = FieldInfo(alias="groupIds", default=None)

    group_names: Optional[Dict[str, str]] = FieldInfo(alias="groupNames", default=None)

    share: float

    share_change: Optional[float] = FieldInfo(alias="shareChange", default=None)

    response_accuracy: float = FieldInfo(alias="responseAccuracy")

    accuracy_change: Optional[float] = FieldInfo(alias="accuracyChange", default=None)

    accurate_count: Optional[int] = FieldInfo(alias="accurateCount", default=None)

    inaccurate_count: int = FieldInfo(alias="inaccurateCount")

    inaccurate_count_change: Optional[int] = FieldInfo(alias="inaccurateCountChange", default=None)

    prompt_count: Optional[int] = FieldInfo(alias="promptCount", default=None)

    citation_category: Optional[str] = FieldInfo(alias="citationCategory", default=None)

    has_score: Optional[bool] = FieldInfo(alias="hasScore", default=None)


class AccuracyBreakdownV1BreakdownPostResponse(BaseModel):
    data: List[Data]

    total_count: int = FieldInfo(alias="totalCount")
