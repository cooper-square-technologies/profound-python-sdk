# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DocumentReplaceContentParams"]


class DocumentReplaceContentParams(TypedDict, total=False):
    organization_id: Required[str]
    """ID of the organization that owns the document. Required — Profound API keys are user-scoped, so the owning organization must be chosen explicitly. The caller must be a member of this organization."""

    content_markdown: Required[str]
    """New markdown body for the document, replacing everything it held before. An empty string is valid and clears the document — nothing else warns you before that happens, so treat sending one as deliberate. Whole-body replace only: send the complete new text, not just the part that changed. Capped at 1,000,000 bytes; the upstream router separately caps the entire request at 2 MiB, so a body near this cap can still be refused in transit rather than by this field."""

    skip_title_sync: bool
    """Off by default, matching the Profound app: the document's title follows the new content's first heading, so a replace silently renames the document whenever that heading differs from the current title. Set true to keep the current title regardless of what the new content's first heading says."""
