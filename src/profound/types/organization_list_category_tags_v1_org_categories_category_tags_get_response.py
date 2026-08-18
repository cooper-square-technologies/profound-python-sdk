# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "OrganizationListCategoryTagsV1OrgCategoriesCategoryTagsGetResponse",
    "OrganizationListCategoryTagsV1OrgCategoriesCategoryTagsGetResponseItem",
]


class OrganizationListCategoryTagsV1OrgCategoriesCategoryTagsGetResponseItem(BaseModel):
    id: str

    name: str


OrganizationListCategoryTagsV1OrgCategoriesCategoryTagsGetResponse: TypeAlias = List[
    OrganizationListCategoryTagsV1OrgCategoriesCategoryTagsGetResponseItem
]
