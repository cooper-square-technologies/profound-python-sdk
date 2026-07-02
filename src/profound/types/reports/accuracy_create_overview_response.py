# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "AccuracyCreateOverviewResponse",
    "ScoreBreakdown",
    "TrendByPeriod",
    "AvailableSeries",
    "ThemeTrend",
    "ThemeTrendData",
]


class ScoreBreakdown(BaseModel):
    count: int

    share: float

    status: str

    count_change: Optional[int] = FieldInfo(alias="countChange", default=None)

    share_change: Optional[float] = FieldInfo(alias="shareChange", default=None)


class TrendByPeriod(BaseModel):
    accurate: int

    date: str

    ratio: float

    total: int

    prev_period_data: Optional[object] = FieldInfo(alias="prevPeriodData", default=None)

    verified: Optional[int] = None


class AvailableSeries(BaseModel):
    id: str

    label: str

    total: int


class ThemeTrendData(BaseModel):
    accurate: int

    date: str

    ratio: float

    total: int


class ThemeTrend(BaseModel):
    id: str

    data: List[ThemeTrendData]

    label: str


class AccuracyCreateOverviewResponse(BaseModel):
    overall_accuracy: float = FieldInfo(alias="overallAccuracy")

    score_breakdown: List[ScoreBreakdown] = FieldInfo(alias="scoreBreakdown")

    trend_by_period: List[TrendByPeriod] = FieldInfo(alias="trendByPeriod")

    accuracy_change: Optional[float] = FieldInfo(alias="accuracyChange", default=None)

    available_series: Optional[List[AvailableSeries]] = FieldInfo(alias="availableSeries", default=None)

    theme_trend: Optional[List[ThemeTrend]] = FieldInfo(alias="themeTrend", default=None)
