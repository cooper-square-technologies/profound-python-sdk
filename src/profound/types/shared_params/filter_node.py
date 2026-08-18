# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["FilterNode"]


_FilterNodeReservedKeywords = TypedDict(
    "_FilterNodeReservedKeywords",
    {
        "and": Optional[Iterable["FilterNode"]],
        "or": Optional[Iterable["FilterNode"]],
        "not": Optional["FilterNode"],
    },
    total=False,
)


class FilterNode(_FilterNodeReservedKeywords, total=False):
    field: Optional[str]

    op: Optional[str]

    value: object
