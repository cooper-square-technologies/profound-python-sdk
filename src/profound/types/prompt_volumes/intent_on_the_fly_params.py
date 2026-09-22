# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

__all__ = ["IntentOnTheFlyParams"]


class IntentOnTheFlyParams(TypedDict, total=False):
    keyword: Required[str]

    matching_type: Required[Literal["exact_match", "phrase_match"]]

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    end_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    regions: SequenceNotStr[str]

    platforms: SequenceNotStr[str]
