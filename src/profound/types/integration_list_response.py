# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IntegrationListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Installation id to bind to a hub-backed node's `integration_id`."""

    provider: str
    """Canonical connector id, matching node contracts."""

    label: str
    """Human-readable account label for the connection."""

    account: Optional[str] = None
    """Connected account identity as the provider reports it, e.g. the Google account email or the WordPress site URL. This is what tells two connections of the same provider apart; `label` often repeats across them. Null when the provider reports no identity."""

    status: str
    """Connection lifecycle status."""

    level: Literal["org", "user"]
    """Installation scope: shared across the org, or user-owned."""


class IntegrationListResponse(BaseModel):
    data: List[Data]
    """Connected integrations."""
