# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["CategoryAssetsResponse", "CategoryAssetsResponseItem"]


class CategoryAssetsResponseItem(BaseModel):
    id: str

    created_at: datetime

    is_owned: bool

    name: str

    website: str

    alternate_domains: Optional[List[str]] = None


CategoryAssetsResponse: TypeAlias = List[CategoryAssetsResponseItem]
