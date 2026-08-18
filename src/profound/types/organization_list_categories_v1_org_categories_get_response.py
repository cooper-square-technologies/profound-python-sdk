# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

from .organization import Organization

__all__ = [
    "OrganizationListCategoriesV1OrgCategoriesGetResponse",
    "OrganizationListCategoriesV1OrgCategoriesGetResponseItem",
]


class OrganizationListCategoriesV1OrgCategoriesGetResponseItem(BaseModel):
    id: str

    name: str

    internal_name: Optional[str] = None

    organization: Organization


OrganizationListCategoriesV1OrgCategoriesGetResponse: TypeAlias = List[
    OrganizationListCategoriesV1OrgCategoriesGetResponseItem
]
