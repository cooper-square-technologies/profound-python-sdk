# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Union

from .._models import BaseModel

__all__ = ["ReportResult"]


class ReportResult(BaseModel):
    """Base model for report results."""

    metrics: List[Union[float, str]]

    dimensions: List[str]
