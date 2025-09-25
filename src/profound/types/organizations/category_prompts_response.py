# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .org_item import OrgItem
from ..._models import BaseModel

__all__ = ["CategoryPromptsResponse", "Data"]


class Data(BaseModel):
    id: str

    created_at: datetime

    platforms: List[OrgItem]

    prompt: str

    prompt_type: str

    regions: List[OrgItem]

    topic: OrgItem

    tags: Optional[List[OrgItem]] = None


class CategoryPromptsResponse(BaseModel):
    data: List[Data]
