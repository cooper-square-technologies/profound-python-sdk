# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..shared.accuracy_trend_point import AccuracyTrendPoint

__all__ = [
    "AccuracyOverviewV1OverviewPostResponse",
    "ScoreBreakdown",
    "ThemeTrend",
    "ThemeTrendData",
    "AvailableSeries",
]


class AvailableSeries(BaseModel):
    id: str

    label: str

    total: int


class ThemeTrendData(BaseModel):
    date: str

    total: int

    accurate: int

    ratio: float


class ThemeTrend(BaseModel):
    id: str

    label: str

    data: List[ThemeTrendData]


class ScoreBreakdown(BaseModel):
    status: str

    count: int

    share: float

    count_change: Optional[int] = FieldInfo(alias="countChange", default=None)

    share_change: Optional[float] = FieldInfo(alias="shareChange", default=None)


class AccuracyOverviewV1OverviewPostResponse(BaseModel):
    trend_by_period: List[AccuracyTrendPoint] = FieldInfo(alias="trendByPeriod")

    overall_accuracy: float = FieldInfo(alias="overallAccuracy")

    accuracy_change: Optional[float] = FieldInfo(alias="accuracyChange", default=None)

    score_breakdown: List[ScoreBreakdown] = FieldInfo(alias="scoreBreakdown")

    theme_trend: Optional[List[ThemeTrend]] = FieldInfo(alias="themeTrend", default=None)

    available_series: Optional[List[AvailableSeries]] = FieldInfo(alias="availableSeries", default=None)
