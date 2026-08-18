# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["OrganizationListCategoryCitationCategoriesV1OrgCategoriesCategoryCitationCategoriesGetResponse", "Data"]


class Data(BaseModel):
    value: str
    """Value to pass to the v2 citations `citation_category` filter."""

    name: str
    """Display name."""


class OrganizationListCategoryCitationCategoriesV1OrgCategoriesCategoryCitationCategoriesGetResponse(BaseModel):
    data: List[Data]
