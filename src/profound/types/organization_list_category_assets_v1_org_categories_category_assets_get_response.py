# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "OrganizationListCategoryAssetsV1OrgCategoriesCategoryAssetsGetResponse",
    "OrganizationListCategoryAssetsV1OrgCategoriesCategoryAssetsGetResponseItem",
]


class OrganizationListCategoryAssetsV1OrgCategoriesCategoryAssetsGetResponseItem(BaseModel):
    id: str

    name: str

    website: str

    alternate_domains: Optional[List[str]] = None

    is_owned: bool

    created_at: datetime

    logo_url: str


OrganizationListCategoryAssetsV1OrgCategoriesCategoryAssetsGetResponse: TypeAlias = List[
    OrganizationListCategoryAssetsV1OrgCategoriesCategoryAssetsGetResponseItem
]
