# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["NumericMetricFilter"]


class NumericMetricFilter(BaseModel):
    field: str

    operator: Literal[">", ">=", "<", "<=", "=", "==", "!="]

    value: float
