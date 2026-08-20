# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["IntegrationListParams"]


class IntegrationListParams(TypedDict, total=False):
    organization_id: Optional[str]
    """Organization scope for API keys that can access multiple organizations."""

    provider: Optional[str]
    """Filter to a single connector/provider id, e.g. `google_drive`."""

    status_filter: Optional[Literal["active", "pending", "needs_reauth", "revoking", "revoked"]]
    """Filter to one lifecycle status. Omitted returns all statuses."""
