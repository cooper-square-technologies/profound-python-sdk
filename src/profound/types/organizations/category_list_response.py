# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..organization import Organization

__all__ = ["CategoryListResponse", "CategoryListResponseItem"]


class CategoryListResponseItem(BaseModel):
    """A category annotated with the organization that owns it."""

    id: str

    name: str

    organization: Organization

    internal_name: Optional[str] = None


CategoryListResponse: TypeAlias = List[CategoryListResponseItem]
