# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentReadV1IDGetResponse", "AdditionalTab", "Comment"]


class Comment(BaseModel):
    content: str
    """The comment's text."""

    context: Optional[str] = None
    """Text the comment was left on. `null` for a comment on no specific text, never an empty string."""


class AdditionalTab(BaseModel):
    title: str
    """The tab's title as authored. Not unique within a document, and a placeholder when the tab was never titled."""

    content_markdown: str
    """This tab's body as markdown."""


class DocumentReadV1IDGetResponse(BaseModel):
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

    content_markdown: str
    """The default tab's body as markdown. Empty string for a document with no content — never absent, so you can read it without a presence check."""

    additional_tabs: Optional[List[AdditionalTab]] = None
    """Every tab beyond the default one, in document order, each as `{title, content_markdown}`. Upstream allows up to twenty. Omitted from the response entirely when `include_tabs=false`; an empty list is a real answer meaning this document has no other tabs, and the two are never confused. Tabs are readable through this API but not writable: create cannot make one, and replacing this document's content does not preserve them."""

    comments: Optional[List[Comment]] = None
    """Review comments left on the document, each mapped to `{content, context}` — the comment's text and, if any, the text it was left on. Omitted from the response entirely when `include_comments=false`; an empty list is a real answer meaning this document has no comments. Mapped from upstream's own open, unvalidated shape — commenter identity, reply threads and resolution state are dropped, never relayed. A comment whose shape this mapping cannot read is dropped from the list rather than failing the read, so this list can be shorter than the document's real thread count."""

    version_hash: Optional[str] = None
    """Opaque token that changes whenever the document's content changes, sampled before this body was read — so it names this body or an older state, never a newer one. `null` when the collaboration service could not be asked for it; the read itself still succeeded, only the token is missing. Bare hex, up to 128 characters, with no fixed prefix — treat it as opaque and do not parse it. It detects change; it is not a precondition, and a matching token is not licence to overwrite blindly. Omitted entirely — not `null` — on a `preview=true` read: a hash next to a body you have not fully seen invites replacing content you never read. Ask for `preview=false` before you intend to write."""

    content_truncated: Optional[bool] = None
    """Whether any body in this response was cut short — `content_markdown` or any tab's. `true` only on a `preview=true` read where one of them exceeded the preview length; a short document, or a `preview=false` read, always gets `false` and every body whole. It does not say which one was cut. Preview truncation saves your context, not upstream cost — the full round trip through the collaborative editor happens either way."""
