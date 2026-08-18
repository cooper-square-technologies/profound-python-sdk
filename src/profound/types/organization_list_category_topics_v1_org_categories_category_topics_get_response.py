# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "OrganizationListCategoryTopicsV1OrgCategoriesCategoryTopicsGetResponse",
    "OrganizationListCategoryTopicsV1OrgCategoriesCategoryTopicsGetResponseItem",
]


class OrganizationListCategoryTopicsV1OrgCategoriesCategoryTopicsGetResponseItem(BaseModel):
    id: str

    name: str

    status: Literal["active", "disabled"]


OrganizationListCategoryTopicsV1OrgCategoriesCategoryTopicsGetResponse: TypeAlias = List[
    OrganizationListCategoryTopicsV1OrgCategoriesCategoryTopicsGetResponseItem
]
