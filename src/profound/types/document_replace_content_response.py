# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentReplaceContentResponse"]


class DocumentReplaceContentResponse(BaseModel):
    id: str
    """The document's ID."""

    name: str
    """The document's title."""

    url: str
    """Link to open the document in the Profound app."""

    visibility: Literal["invited_only", "organization"]
    """General access scope. New documents are `invited_only`."""

    created_at: datetime
    """When the document was created."""

    updated_at: datetime
    """When the document was last modified. Seeding the initial content counts, so a freshly created document is normally modified a moment after it was created."""

    owner_user_id: str
    """ID of the document's owner."""

    owner_email: Optional[str] = None
    """Email of the document's owner. `null` when the owning profile has been deleted or could not be resolved."""

    author_type: Literal["user", "agent"]
    """Whether the document's owner is a person (`user`) or an agent (`agent`)."""

    app_delegate: Optional[str] = None
    """Which integration created the document, derived server-side from the credential that authenticated the write. `null` for documents created outside any integration. An open-ended value, not a fixed set — known values today include `external-api` and `context-manager`, and more are added as new integrations ship."""

    category_name: Optional[str] = None
    """Name of the brand category set on the document, if any. Paired with `company_name`; writable only on create."""

    company_name: Optional[str] = None
    """Name of the brand/company set on the document, if any. Paired with `category_name`; writable only on create."""

    version_hash: Optional[str] = None
    """Opaque token that changes whenever the document's collaborative-editing snapshot changes — a digest over that snapshot, not over the markdown. It moves on a comment reply, because a comment changes the snapshot, and it does not move on a rename, because metadata sits outside the snapshot. Bare hex, up to 128 characters, with no fixed prefix — treat it as opaque and do not parse it. `null` when no token could be minted; never omitted. It is a change detector, not a precondition: a caller must not treat a matching token as licence to overwrite blindly, because it names the room at a moment cortex observed and not the moment its own write lands."""

    content_chars: int
    """Character count of the markdown that landed — 0 when this call cleared the document. The only confirmation of how much was written, on the most destructive operation this surface exposes."""
