# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["CategoryTopicsResponse", "CategoryTopicsResponseItem"]


class CategoryTopicsResponseItem(BaseModel):
    id: str

    name: str

    status: Literal["active", "disabled"]


CategoryTopicsResponse: TypeAlias = List[CategoryTopicsResponseItem]
