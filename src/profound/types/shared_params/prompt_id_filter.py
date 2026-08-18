# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict
from ..._types import SequenceNotStr

__all__ = ["PromptIDFilter"]


class PromptIDFilter(TypedDict, total=False):
    field: Required[Literal["prompt_id"]]

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]
