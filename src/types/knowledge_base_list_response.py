# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .cursor_pagination import CursorPagination

__all__ = ["KnowledgeBaseListResponse", "KnowledgeBaseItem"]


class KnowledgeBaseItem(BaseModel):

    id: str
    """Unique knowledge base ID."""

    name: str
    """Knowledge base name."""

    slug: Optional[str] = None
    """Knowledge base slug."""

    description: Optional[str] = None
    """Knowledge base description."""

    created_at: datetime
    """Creation timestamp."""



class KnowledgeBaseListResponse(BaseModel):

    data: List[KnowledgeBaseItem]
    """Knowledge bases accessible to the API key."""

    pagination: Optional[CursorPagination] = None
    """Pagination metadata."""
