# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .category import Category
from .organization import Organization

__all__ = ["OrganizationListAssetsResponse", "Data"]


class Data(BaseModel):
    id: str

    category: Category

    created_at: datetime

    is_owned: bool

    logo_url: str

    name: str

    organization: Organization

    website: str

    alternate_domains: Optional[List[str]] = None


class OrganizationListAssetsResponse(BaseModel):
    data: List[Data]
