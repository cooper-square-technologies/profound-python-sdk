# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ModelIDFilter"]


class ModelIDFilter(TypedDict, total=False):
    """Filter by AI model/platform UUID."""

    field: Required[Literal["model_id", "model"]]
    """- `model` - Deprecated"""

    operator: Required[Literal["is", "not_is", "in", "not_in"]]

    value: Required[Union[str, SequenceNotStr[str]]]
