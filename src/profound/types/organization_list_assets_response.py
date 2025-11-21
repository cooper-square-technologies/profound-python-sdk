# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .organizations.org_item import OrgItem

__all__ = ["OrganizationListAssetsResponse", "Data"]


class Data(BaseModel):
    id: str

    category: OrgItem

    created_at: datetime

    is_owned: bool

    name: str

    website: str

    alternate_domains: Optional[List[str]] = None


class OrganizationListAssetsResponse(BaseModel):
    data: List[Data]
