# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["IDOrNameParam"]


class IDOrNameParam(TypedDict, total=False):
    """Reference by id, name, or both.

    Plain strings work too:
    UUIDs become id lookups, other strings become name lookups.
    """

    id: Optional[str]
    """UUID of the resource."""

    name: Optional[str]
    """Display name of the resource."""
