# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Organization"]


class Organization(BaseModel):
    id: str

    name: Optional[str] = None
