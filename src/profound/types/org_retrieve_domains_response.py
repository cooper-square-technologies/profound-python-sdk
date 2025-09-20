# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["OrgRetrieveDomainsResponse", "OrgRetrieveDomainsResponseItem"]


class OrgRetrieveDomainsResponseItem(BaseModel):
    id: str

    created_at: datetime

    name: str


OrgRetrieveDomainsResponse: TypeAlias = List[OrgRetrieveDomainsResponseItem]
