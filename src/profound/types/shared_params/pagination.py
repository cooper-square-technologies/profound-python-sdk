# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["Pagination"]


class Pagination(TypedDict, total=False):
    limit: int
    """Maximum number of results to return. Default is 10,000, maximum is 50,000."""

    offset: int
    """Offset for the results. Used for pagination."""
