# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TopicIDFilter"]


class TopicIDFilter(BaseModel):
    """Filter by topic UUID."""

    field: Literal["topic_id", "topic"]
    """- `topic` - Deprecated"""

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]
