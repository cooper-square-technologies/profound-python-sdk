# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

from .category import Category
from .organization import Organization

__all__ = ["OrganizationListAssetsResponse", "Data"]


class Data(BaseModel):
    id: str

    name: str

    website: str

    alternate_domains: Optional[List[str]] = None

    is_owned: bool

    created_at: datetime

    logo_url: str

    category: Category

    organization: Organization


class OrganizationListAssetsResponse(BaseModel):
    data: List[Data]
