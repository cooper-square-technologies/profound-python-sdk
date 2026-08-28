# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ModelIDFilter"]


class ModelIDFilter(BaseModel):
    """Filter by AI model/platform UUID."""

    field: Literal["model_id", "model"]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]
