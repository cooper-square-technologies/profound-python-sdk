# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.cursor_pagination import CursorPagination

__all__ = ["KnowledgeBaseListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Unique knowledge base ID."""

    created_at: datetime
    """Creation timestamp."""

    name: str
    """Knowledge base name."""

    description: Optional[str] = None
    """Knowledge base description."""

    slug: Optional[str] = None
    """Knowledge base slug."""


class KnowledgeBaseListResponse(BaseModel):
    data: List[Data]
    """Knowledge bases accessible to the API key."""

    pagination: Optional[CursorPagination] = None
    """Pagination metadata."""
