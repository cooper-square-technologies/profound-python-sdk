# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyOverviewV1ReportsOverviewPostResponse", "AccuracyTrendPoint", "AccuracyScoreBreakdown", "AccuracyThemeTrendSeries", "AccuracyThemeTrendPoint", "AccuracyTrendSeriesMeta"]


class AccuracyTrendSeriesMeta(BaseModel):

    id: str

    label: str

    total: int

class AccuracyThemeTrendPoint(BaseModel):

    date: str

    total: int

    accurate: int

    ratio: float

class AccuracyThemeTrendSeries(BaseModel):

    id: str

    label: str

    data: List[AccuracyThemeTrendPoint]

class AccuracyScoreBreakdown(BaseModel):

    status: str

    count: int

    share: float

    countChange: Optional[int] = None

    shareChange: Optional[float] = None

class AccuracyTrendPoint(BaseModel):

    date: str

    total: int

    accurate: int

    ratio: float

    prevPeriodData: Optional[AccuracyTrendPoint] = None



class AccuracyOverviewV1ReportsOverviewPostResponse(BaseModel):

    trend_by_period: List[AccuracyTrendPoint] = FieldInfo(alias="trendByPeriod")

    overall_accuracy: float = FieldInfo(alias="overallAccuracy")

    accuracy_change: Optional[float] = FieldInfo(alias="accuracyChange", default=None)

    score_breakdown: List[AccuracyScoreBreakdown] = FieldInfo(alias="scoreBreakdown")

    theme_trend: Optional[List[AccuracyThemeTrendSeries]] = FieldInfo(alias="themeTrend", default=None)

    available_series: Optional[List[AccuracyTrendSeriesMeta]] = FieldInfo(alias="availableSeries", default=None)
