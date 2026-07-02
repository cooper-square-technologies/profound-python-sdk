# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyCreateBreakdownResponse", "Data"]


class Data(BaseModel):
    id: str

    inaccurate_count: int = FieldInfo(alias="inaccurateCount")

    name: str

    response_accuracy: float = FieldInfo(alias="responseAccuracy")

    share: float

    accuracy_change: Optional[float] = FieldInfo(alias="accuracyChange", default=None)

    accurate_count: Optional[int] = FieldInfo(alias="accurateCount", default=None)

    citation_category: Optional[str] = FieldInfo(alias="citationCategory", default=None)

    group_ids: Optional[Dict[str, str]] = FieldInfo(alias="groupIds", default=None)

    group_names: Optional[Dict[str, str]] = FieldInfo(alias="groupNames", default=None)

    inaccurate_count_change: Optional[int] = FieldInfo(alias="inaccurateCountChange", default=None)

    prompt_count: Optional[int] = FieldInfo(alias="promptCount", default=None)

    share_change: Optional[float] = FieldInfo(alias="shareChange", default=None)


class AccuracyCreateBreakdownResponse(BaseModel):
    data: List[Data]

    total_count: int = FieldInfo(alias="totalCount")
