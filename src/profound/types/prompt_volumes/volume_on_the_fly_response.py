# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["VolumeOnTheFlyResponse", "Info", "Data"]


class Data(BaseModel):
    country_code: str

    platform: str

    matching_type: str

    frequency: str

    date: date

    volume: float


class Info(BaseModel):
    total_rows: int

    truncated: Optional[bool] = None

    query: Optional[Dict[str, object]] = None


class VolumeOnTheFlyResponse(BaseModel):
    info: Info
    """
    Metadata for volume query response.
    truncated indicates if results hit MAX_ROWS limit.
    """

    data: List[Data]
