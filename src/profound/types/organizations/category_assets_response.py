# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["CategoryAssetsResponse", "CategoryAssetsResponseItem"]


class CategoryAssetsResponseItem(BaseModel):
    id: str

    name: str

    website: str

    alternate_domains: Optional[List[str]] = None

    is_owned: bool

    created_at: datetime

    logo_url: str


CategoryAssetsResponse: TypeAlias = List[CategoryAssetsResponseItem]
