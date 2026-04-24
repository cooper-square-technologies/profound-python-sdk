# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PromptTypeFilter"]


class PromptTypeFilter(TypedDict, total=False):
    """Filter by prompt type (visibility or sentiment).

    .. deprecated::
        Use :class:`AnalysisTypeFilter` instead. ``prompt_type`` is normalised
        to ``analysis_type`` at parse time.
    """

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
