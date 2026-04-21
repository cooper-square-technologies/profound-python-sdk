# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["OrganizationListAssetsResponse", "Data", "DataCategory", "DataOrganization"]


class DataCategory(BaseModel):
    id: str

    name: str


class DataOrganization(BaseModel):
    id: str

    name: Optional[str] = None


class Data(BaseModel):
    id: str

    category: DataCategory

    created_at: datetime

    is_owned: bool

    logo_url: str

    name: str

    organization: DataOrganization

    website: str

    alternate_domains: Optional[List[str]] = None


class OrganizationListAssetsResponse(BaseModel):
    data: List[Data]
