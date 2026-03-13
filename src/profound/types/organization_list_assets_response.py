# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .named_resource import NamedResource

__all__ = ["OrganizationListAssetsResponse", "Data"]


class Data(BaseModel):
    id: str

    category: NamedResource
    """Generic id+name reference used across domain boundaries."""

    created_at: datetime

    is_owned: bool

    logo_url: str

    name: str

    website: str

    alternate_domains: Optional[List[str]] = None


class OrganizationListAssetsResponse(BaseModel):
    data: List[Data]
