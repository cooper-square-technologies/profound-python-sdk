# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .cursor_pagination import CursorPagination

__all__ = ["KnowledgeBaseSearchResponse", "KnowledgeBaseSearchResult", "Metadata"]


class Metadata(BaseModel):
    pass

class KnowledgeBaseSearchResult(BaseModel):

    id: str
    """Document or chunk path."""

    score: float
    """Relevance score."""

    metadata: Metadata
    """Result metadata, including folder path."""

    content: str
    """Matched content."""



class KnowledgeBaseSearchResponse(BaseModel):

    data: List[KnowledgeBaseSearchResult]
    """Knowledge base search results."""

    pagination: Optional[CursorPagination] = None
    """Pagination metadata."""
