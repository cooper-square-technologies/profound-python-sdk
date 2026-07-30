# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["CategoryGetCitationCategoriesResponse", "Data"]


class Data(BaseModel):
    name: str
    """Display name."""

    value: str
    """Value to pass to the v2 citations `citation_category` filter."""


class CategoryGetCitationCategoriesResponse(BaseModel):
    data: List[Data]
