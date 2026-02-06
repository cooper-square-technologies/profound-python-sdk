# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RegionIDFilter"]


class RegionIDFilter(BaseModel):
    field: Literal["region_id", "region"]
    """- `region` - Deprecated"""

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]
