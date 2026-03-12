# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["OrganizationListAssetsResponse", "Data", "DataCategory"]


class DataCategory(BaseModel):
    """Generic id+name reference used across domain boundaries."""

    id: str

    name: str


class Data(BaseModel):
    id: str

    category: DataCategory
    """Generic id+name reference used across domain boundaries."""

    created_at: datetime

    is_owned: bool

    logo_url: str

    name: str

    website: str

    alternate_domains: Optional[List[str]] = None


class OrganizationListAssetsResponse(BaseModel):
    data: List[Data]
