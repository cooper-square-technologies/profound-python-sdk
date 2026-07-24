# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IntegrationListResponse", "Data"]


class Data(BaseModel):
    """One connected integration installation visible to the caller."""

    id: str
    """Installation id to bind to a hub-backed node's `integration_id`."""

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
