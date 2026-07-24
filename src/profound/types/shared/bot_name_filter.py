# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BotNameFilter"]


class BotNameFilter(BaseModel):
    """Filter by bot name (user agent).

    Values come from analytics data and should
    not be enum-constrained because web-v2 may send newly cataloged user-agent names.
    """

    field: Literal["bot_name"]

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
