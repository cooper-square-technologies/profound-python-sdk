# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "OrganizationDomainsResponse",
    "OrganizationDomainsResponseItem",
    "OrganizationDomainsResponseItemOrganization",
]


class OrganizationDomainsResponseItemOrganization(BaseModel):
    id: str

    name: Optional[str] = None


class OrganizationDomainsResponseItem(BaseModel):
    """A domain paired with the organization edge it belongs to."""

    id: str

    created_at: datetime

    name: str

    organization: OrganizationDomainsResponseItemOrganization


OrganizationDomainsResponse: TypeAlias = List[OrganizationDomainsResponseItem]
