# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

from .organization import Organization

__all__ = ["OrganizationListAssetsV1OrgAssetsGetResponse", "Data", "DataCategory"]


class DataCategory(BaseModel):
    id: str

    name: str

    internal_name: Optional[str] = None


class Data(BaseModel):
    id: str

    name: str

    website: str

    alternate_domains: Optional[List[str]] = None

    is_owned: bool

    created_at: datetime

    logo_url: str

    category: DataCategory

    organization: Organization


class OrganizationListAssetsV1OrgAssetsGetResponse(BaseModel):
    data: List[Data]
