# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict
from ..._types import SequenceNotStr

__all__ = ["ProductNameFilterParam"]


class ProductNameFilterParam(TypedDict, total=False):
    field: Required[Literal["product_name"]]

    operator: Required[
        Literal[
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
    ]

    value: Required[Union[str, SequenceNotStr[str]]]
