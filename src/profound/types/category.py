# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Category"]


class Category(BaseModel):
    id: str

    name: str

    internal_name: Optional[str] = None
