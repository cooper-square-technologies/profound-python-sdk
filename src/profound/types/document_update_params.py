# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DocumentUpdateParams"]


class DocumentUpdateParams(TypedDict, total=False):
    organization_id: Required[str]
    """ID of the organization that owns the document. Required — Profound API keys are user-scoped, so the owning organization must be named explicitly. The caller must be a member of this organization."""

    name: Optional[str]
    """New title for the document. Renaming sets a permanent lock: once a document is renamed through this route, its title stops following the first heading of its content, for the rest of the document's life, and no route can undo the lock. Omit to leave the title as it is."""

    visibility: Optional[Literal["invited_only", "organization"]]
    """New sharing scope: `invited_only` for only the people invited to the document, or `organization` for everyone in the owning organization. Only the document's creator can change this; omit to leave sharing as it is. Three things worth knowing before you set it: `organization` visibility grants view only — there is no value here that grants the organization edit access. Setting `invited_only` removes the organization's access entirely. And re-asserting `organization` on a document whose organization grant is already `edit` silently downgrades the whole organization to view — upstream replays the access sync whenever this field is sent, and that sync always upserts view, even when the value you sent matches the one already stored."""
