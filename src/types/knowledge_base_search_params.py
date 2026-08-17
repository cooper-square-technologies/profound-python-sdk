# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict
from .._types import SequenceNotStr

__all__ = ["KnowledgeBaseSearchParams", "SearchKnowledgeBaseFilters"]


class KnowledgeBaseSearchParams(TypedDict, total=False):

    query: Required[str]
    """Search query."""

    top_k: Required[int]
    """Maximum number of results to return."""

    return_full_page: bool
    """Return full page content instead of snippets."""

    filters: Optional[SearchKnowledgeBaseFilters]
    """Optional search filters."""

    organization_id: Optional[str]
    """Organization scope for API keys that can access multiple organizations."""


class SearchKnowledgeBaseFilters(TypedDict, total=False):

    tags: Optional[SequenceNotStr[str]]
    """Optional tags to match. Documents with any matching tag are included."""

    folders: Optional[SequenceNotStr[str]]
    """Optional folder paths to search within. Currently limited to one folder."""

