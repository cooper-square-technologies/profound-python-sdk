# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["CategoryListResponse", "CategoryListResponseItem", "CategoryListResponseItemOrganization"]


class CategoryListResponseItemOrganization(BaseModel):
    id: str

    name: Optional[str] = None


class CategoryListResponseItem(BaseModel):
    """A category annotated with the organization that owns it."""

    id: str

    name: str

    organization: CategoryListResponseItemOrganization


CategoryListResponse: TypeAlias = List[CategoryListResponseItem]
