# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PromptTypeFilter"]


class PromptTypeFilter(BaseModel):
    """
    Filter by prompt type (visibility or sentiment).

    .. deprecated::
        Use :class:`AnalysisTypeFilter` instead. ``prompt_type`` is normalised
        to ``analysis_type`` at parse time.
    """

    field: Literal["prompt_type"]

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

    value: Union[Literal["visibility", "sentiment"], List[Literal["visibility", "sentiment"]]]
