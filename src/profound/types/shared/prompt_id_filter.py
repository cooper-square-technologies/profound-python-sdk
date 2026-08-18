# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PromptIDFilter"]


class PromptIDFilter(BaseModel):
    """Filter by prompt UUID."""

    field: Literal["prompt_id"]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]
