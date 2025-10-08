# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.pagination import Pagination

__all__ = ["PromptAnswersParams", "Filter", "Include"]


class PromptAnswersParams(TypedDict, total=False):
    category_id: Required[str]

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    filters: Iterable[Filter]

    include: Include

    pagination: Pagination
    """Pagination parameters for the results. Default is 10,000 rows with no offset."""


class Filter(TypedDict, total=False):
    field: Required[Literal["region", "topic", "model", "prompt_type", "prompt", "tag"]]

    operator: Required[
        Literal[
            "is",
            "not_is",
            "in",
            "not_in",
            "contains",
            "not_contains",
            "contains_case_insensitive",
            "not_contains_case_insensitive",
            "matches",
        ]
    ]

    value: Required[Union[str, SequenceNotStr[str], int, Iterable[int]]]
    """Value for the filter.

    Can be a single value or a list of depending on the operator.
    """


class Include(TypedDict, total=False):
    asset: bool

    citations: bool

    created_at: bool

    mentions: bool

    model: bool

    prompt: bool

    prompt_id: bool

    prompt_type: bool

    region: bool

    response: bool

    run_id: bool

    tags: bool

    themes: bool

    topic: bool
