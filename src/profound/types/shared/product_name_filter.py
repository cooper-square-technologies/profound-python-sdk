# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ProductNameFilter"]


class ProductNameFilter(BaseModel):
    field: Literal["product_name"]

    operator: Literal[
        "is",
        "not_is",
        "in",
        "not_in",
        "contains",
        "not_contains",
        "matches",
        "contains_case_insensitive",
        "not_contains_case_insensitive",
    ]

    value: Union[str, List[str]]
