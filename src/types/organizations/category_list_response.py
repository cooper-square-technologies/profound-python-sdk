# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias
from ..._models import BaseModel
from ..organization import Organization

__all__ = ["CategoryListResponse", "CategoryWithOrganization"]

class CategoryWithOrganization(BaseModel):

    id: str

    name: str

    organization: Organization



CategoryListResponse: TypeAlias = List[CategoryWithOrganization]
