# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProjectListParams"]


class ProjectListParams(TypedDict, total=False):
    category_id: Required[str]
    """Category that owns the project."""

    limit: int

    offset: int

    status: Optional[str]
    """Comma-separated project statuses: suggested, tracked, retired."""
