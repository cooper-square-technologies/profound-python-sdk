# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AnalysisTypeFilter"]


class AnalysisTypeFilter(TypedDict, total=False):
    """Filter by analysis type (visibility, sentiment, or accuracy)."""

    field: Required[Literal["analysis_type"]]

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

    value: Required[
        Union[
            Literal["visibility", "sentiment", "sentiment_v2", "accuracy"],
            List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]],
        ]
    ]
