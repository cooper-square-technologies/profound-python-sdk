# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["OrganizationListCategoryCitationTagsV1OrgCategoriesCategoryCitationTagsGetResponse", "Data"]


class Data(BaseModel):
    value: str
    """Value to pass to the v2 citations `citation_tag` filter."""

    name: str
    """Display name."""


class OrganizationListCategoryCitationTagsV1OrgCategoriesCategoryCitationTagsGetResponse(BaseModel):
    data: List[Data]
