# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DocumentListV1GetParams"]


class DocumentListV1GetParams(TypedDict, total=False):
    organization_id: Required[str]
    """ID of the organization whose documents to list. Required. The caller must be a member of this organization."""

    q: Optional[str]
    """Filter to documents whose name contains this text, case-insensitively. Matches only the document's name, never its content — a query that finds nothing does not mean the topic is unwritten, only that no title mentions it. Blank or omitted returns every document. Ignored when sent alongside `next_cursor`, which carries the filter the walk started with. Matching is name-only as of this release; broader matching may follow if upstream changes how it indexes the name column."""

    sort: Optional[str]
    """Documents are always ordered newest-modified-first (`updated_at DESC`, then `created_at DESC`, then `id DESC`); there is no parameter that changes this. `recency` is the only accepted value, and passing it is a no-op that names the guarantee rather than altering it — any other value is rejected outright rather than silently ignored. Ordering is never re-applied to a returned page either: that would only be consistent within the page, not across a paginated walk."""

    limit: int

    next_cursor: Optional[str]
