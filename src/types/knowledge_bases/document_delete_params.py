# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DocumentDeleteParams"]


class DocumentDeleteParams(TypedDict, total=False):

    name: Required[str]
    """Document path to delete."""

    organization_id: Optional[str]
    """Organization scope for API keys that can access multiple organizations."""
