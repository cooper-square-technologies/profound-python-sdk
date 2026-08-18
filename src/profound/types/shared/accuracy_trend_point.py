# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccuracyTrendPoint"]


class AccuracyTrendPoint(BaseModel):
    date: str

    total: int

    accurate: int

    verified: Optional[int] = None

    ratio: float

    prev_period_data: Optional["AccuracyTrendPoint"] = FieldInfo(alias="prevPeriodData", default=None)
