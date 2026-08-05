# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentCreateResponse"]


class DocumentCreateResponse(BaseModel):
    """
    The document that was created, plus the change-detection token minted for this write.
    """

    id: str
    """The document's ID."""

    app_delegate: Optional[str] = None
    """
    Which integration created the document, derived server-side from the credential
    that authenticated the write. `null` for documents created outside any
    integration. An open-ended value, not a fixed set — known values today include
    `external-api` and `context-manager`, and more are added as new integrations
    ship.
    """

    author_type: Literal["user", "agent"]
    """Whether the document's owner is a person (`user`) or an agent (`agent`)."""

    category_name: Optional[str] = None
    """Name of the brand category set on the document, if any.

    Paired with `company_name`; writable only on create.
    """

    company_name: Optional[str] = None
    """Name of the brand/company set on the document, if any.

    Paired with `category_name`; writable only on create.
    """

    created_at: datetime
    """When the document was created."""

    name: str
    """The document's title."""

    owner_email: Optional[str] = None
    """Email of the document's owner.

    `null` when the owning profile has been deleted or could not be resolved.
    """

    owner_user_id: str
    """ID of the document's owner."""

    updated_at: datetime
    """When the document was last modified.

    Seeding the initial content counts, so a freshly created document is normally
    modified a moment after it was created.
    """

    url: str
    """Link to open the document in the Profound app."""

    version_hash: Optional[str] = None
    """Opaque token that changes whenever the document's content changes.

    `null` when this call found an existing document with the same id (idempotent
    create) rather than creating one, or when the token could not be minted. Bare
    hex, up to 128 characters, with no fixed prefix — treat it as opaque and do not
    parse it. It detects change; it is not a precondition, and a matching token is
    not licence to overwrite blindly.
    """

    visibility: Literal["invited_only", "organization"]
    """General access scope. New documents are `invited_only`."""
