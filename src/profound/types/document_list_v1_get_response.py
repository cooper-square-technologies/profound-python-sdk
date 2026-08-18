# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

from .shared.cursor_pagination import CursorPagination

__all__ = ["DocumentListV1GetResponse", "Data"]


class Data(BaseModel):
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


class DocumentListV1GetResponse(BaseModel):
    data: List[Data]
    """Documents on this page."""

    pagination: CursorPagination
    """Pagination state for fetching the next page."""
