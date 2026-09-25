# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
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
    """ISO 3166-1 alpha-3 country codes (e.g. USA). Omit to include every region."""

    platforms: List[Literal["chatgpt.com", "gemini.google.com", "perplexity.ai"]]
    """Platforms to restrict to. Omit to include every platform."""
