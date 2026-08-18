# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional, Union

from ..._models import BaseModel

from ..shared.info import Info

__all__ = ["CitationQueryV1PostResponse", "Data"]


class Data(BaseModel):
    metrics: List[Optional[Union[float, str]]]

    dimensions: List[str]


class CitationQueryV1PostResponse(BaseModel):
    info: Info
    """Base model for report information."""

    data: List[Data]
