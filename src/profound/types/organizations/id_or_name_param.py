# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["IDOrNameParam"]


class IDOrNameParam(TypedDict, total=False):
    id: Optional[str]
    """UUID of the resource."""

    name: Optional[str]
    """Display name of the resource."""
