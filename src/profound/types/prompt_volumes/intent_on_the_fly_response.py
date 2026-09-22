# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["IntentOnTheFlyResponse", "Info", "Data"]


class Data(BaseModel):
    main_classification: str

    sub_category_classification: Optional[str] = None

    pct_conversation: float


class Info(BaseModel):
    total_rows: int

    truncated: Optional[bool] = None

    query: Optional[Dict[str, object]] = None


class IntentOnTheFlyResponse(BaseModel):
    info: Info
    """
    Metadata for volume query response.
    truncated indicates if results hit MAX_ROWS limit.
    """

    data: List[Data]
