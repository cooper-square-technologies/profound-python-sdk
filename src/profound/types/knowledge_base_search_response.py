# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

from .shared.cursor_pagination import CursorPagination

__all__ = ["KnowledgeBaseSearchResponse", "Data"]


class Data(BaseModel):
    id: str
    """Document or chunk path."""

    score: float
    """Relevance score."""

    metadata: Dict[str, object]
    """Result metadata, including folder path."""

    content: str
    """Matched content."""


class KnowledgeBaseSearchResponse(BaseModel):
    data: List[Data]
    """Knowledge base search results."""

    pagination: Optional[CursorPagination] = None
    """Pagination metadata."""
