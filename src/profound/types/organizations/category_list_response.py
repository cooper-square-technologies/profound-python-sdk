# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["CategoryListResponse", "CategoryListResponseItem"]


class CategoryListResponseItem(BaseModel):
    """Generic id+name reference used across domain boundaries."""

    id: str

    name: str


CategoryListResponse: TypeAlias = List[CategoryListResponseItem]
