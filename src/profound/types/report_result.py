# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from .._models import BaseModel

__all__ = ["ReportResult"]


class ReportResult(BaseModel):
    dimensions: List[str]

    metrics: List[Union[float, int]]
