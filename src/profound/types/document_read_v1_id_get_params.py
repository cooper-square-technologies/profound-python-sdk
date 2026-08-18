# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DocumentReadV1IDGetParams"]


class DocumentReadV1IDGetParams(TypedDict, total=False):
    organization_id: Required[str]
    """ID of the organization that owns the document. Required — Profound API keys are user-scoped, so the owning organization must be named explicitly. The caller must be a member of this organization."""

    include_tabs: bool
    """Include the document's other tabs. On by default — a tab body is part of the document, not an aside. Off, `additional_tabs` is omitted from the response rather than returned as an empty list."""

    include_comments: bool
    """Include the document's review comments, each mapped to `{content, context}`. On by default — a comment is part of the document's review state, not an aside. Turn it off to skip the comment-thread walk upstream; off, `comments` is omitted from the response rather than returned as an empty list."""

    preview: bool
    """Bound every body in the response — `content_markdown` and each tab's — and set `content_truncated` if any was cut. On by default. Upstream has no partial-read of its own — every read is a full round trip through the collaborative editor — so this saves your context, not upstream cost. A preview read also omits `version_hash`, on purpose: a hash returned next to a body you have not fully seen invites replacing content you never read. Pass `preview=false` before you intend to write, to get the whole body, `content_truncated: false`, and the hash."""
