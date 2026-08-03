# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentCreateResponse"]


class DocumentCreateResponse(BaseModel):
    """A Profound document."""

    id: str
    """The document's ID."""

    created_at: datetime
    """When the document was created."""

    name: str
    """The document's title."""

    updated_at: datetime
    """When the document was last modified.

    Seeding the initial content counts, so a freshly created document is normally
    modified a moment after it was created.
    """

    url: str
    """Link to open the document in the Profound app."""

    visibility: Literal["invited_only", "organization"]
    """General access scope. New documents are `invited_only`."""
