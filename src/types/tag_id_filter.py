# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TagIdFilter"]


class TagIdFilter(BaseModel):
    """Filter by tag (prompt group) UUID."""

    field: Union[Literal["tag_id"], Literal["tag"]]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]
