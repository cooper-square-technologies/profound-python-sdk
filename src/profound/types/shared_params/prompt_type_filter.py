# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PromptTypeFilter"]


class PromptTypeFilter(TypedDict, total=False):
    field: Required[Literal["prompt_type"]]

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

    value: Required[Union[Literal["visibility", "sentiment"], List[Literal["visibility", "sentiment"]]]]
