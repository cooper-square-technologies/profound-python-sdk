# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ReportResult"]


class ReportResult(BaseModel):
    """Base model for report results."""

    dimensions: List[str]

    metrics: List[float]
