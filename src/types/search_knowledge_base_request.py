# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SearchKnowledgeBaseRequest", "SearchKnowledgeBaseFilters"]


class SearchKnowledgeBaseFilters(BaseModel):

    tags: Optional[List[str]] = None
    """Optional tags to match. Documents with any matching tag are included."""

    folders: Optional[List[str]] = None
    """Optional folder paths to search within. Currently limited to one folder."""



class SearchKnowledgeBaseRequest(BaseModel):

    query: str
    """Search query."""

    top_k: int
    """Maximum number of results to return."""

    return_full_page: Optional[bool] = None
    """Return full page content instead of snippets."""

    filters: Optional[SearchKnowledgeBaseFilters] = None
    """Optional search filters."""
