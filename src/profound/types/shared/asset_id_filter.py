# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AssetIDFilter"]


class AssetIDFilter(BaseModel):
    field: Literal["asset_id"]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]
