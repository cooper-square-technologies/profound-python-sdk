# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProjectListParams"]


class ProjectListParams(TypedDict, total=False):
    category_id: Required[str]
    """Category that owns the project."""

    status: Optional[str]
    """Comma-separated project statuses: suggested, tracked, retired."""

    limit: int

    offset: int
