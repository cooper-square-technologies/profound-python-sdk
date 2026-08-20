# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

from .organization import Organization

__all__ = ["OrganizationDomainsResponse", "OrganizationDomainsResponseItem"]


class OrganizationDomainsResponseItem(BaseModel):
    created_at: datetime

    id: str

    name: str

    organization: Organization


OrganizationDomainsResponse: TypeAlias = List[OrganizationDomainsResponseItem]
