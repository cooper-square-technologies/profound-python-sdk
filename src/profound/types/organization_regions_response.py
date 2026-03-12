# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["OrganizationRegionsResponse", "OrganizationRegionsResponseItem"]


class OrganizationRegionsResponseItem(BaseModel):
    """Generic id+name reference used across domain boundaries."""

    id: str

    name: str


OrganizationRegionsResponse: TypeAlias = List[OrganizationRegionsResponseItem]
