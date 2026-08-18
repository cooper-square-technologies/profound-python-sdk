# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

from .organization import Organization

__all__ = ["OrganizationListDomainsV1OrgDomainsGetResponse", "OrganizationListDomainsV1OrgDomainsGetResponseItem"]


class OrganizationListDomainsV1OrgDomainsGetResponseItem(BaseModel):
    created_at: datetime

    id: str

    name: str

    organization: Organization


OrganizationListDomainsV1OrgDomainsGetResponse: TypeAlias = List[OrganizationListDomainsV1OrgDomainsGetResponseItem]
