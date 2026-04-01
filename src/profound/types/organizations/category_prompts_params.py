# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CategoryPromptsParams"]


class CategoryPromptsParams(TypedDict, total=False):
    cursor: Optional[str]

    limit: int

    order_dir: Literal["asc", "desc"]

    persona_id: SequenceNotStr[str]

    platform_id: SequenceNotStr[str]

    prompt_type: List[Literal["visibility", "sentiment"]]

    region_id: SequenceNotStr[str]

    tag_id: SequenceNotStr[str]

    topic_id: SequenceNotStr[str]
