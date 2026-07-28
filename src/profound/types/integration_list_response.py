# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IntegrationListResponse", "Data"]


class Data(BaseModel):
    """One connected integration installation visible to the caller."""

    id: str
    """Installation id to bind to a hub-backed node's `integration_id`."""

    account: Optional[str] = None
    """Connected account identity as the provider reports it, e.g.

    the Google account email or the WordPress site URL. This is what tells two
    connections of the same provider apart; `label` often repeats across them. Null
    when the provider reports no identity.
    """

    label: str
    """Human-readable account label for the connection."""

    level: Literal["org", "user"]
    """Installation scope: shared across the org, or user-owned."""

    provider: str
    """Canonical connector id, matching node contracts."""

    status: str
    """Connection lifecycle status."""


class IntegrationListResponse(BaseModel):
    """Connected integrations visible to the caller's org/user context."""

    data: List[Data]
    """Connected integrations."""
