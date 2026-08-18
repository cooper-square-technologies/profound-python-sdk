# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DocumentCreateV1PostParams"]


class DocumentCreateV1PostParams(TypedDict, total=False):
    id: Required[str]
    """ID for the new document, chosen by you. Creation is idempotent on this ID: repeating a request with the same ID returns the existing document instead of creating a second one, so a retry after a network error is safe."""

    organization_id: Required[str]
    """ID of the organization that will own the document. Required — Profound API keys are user-scoped, so the owning organization must be chosen explicitly. The caller must be a member of this organization."""

    name: Required[str]
    """Title for the document. Must be non-empty."""

    content_markdown: Required[str]
    """Initial document body as markdown. Must be non-empty. Rendered into the collaborative editor, so the result is real editable content, not a stored blob."""
