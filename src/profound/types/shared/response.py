# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Union

from ..._models import BaseModel

from .info import Info

__all__ = ["Response", "Data"]


class Data(BaseModel):
    metrics: List[Union[float, str]]

    dimensions: List[str]


class Response(BaseModel):
    """Base response model for reports."""

    info: Info
    """Base model for report information."""

    data: List[Data]
