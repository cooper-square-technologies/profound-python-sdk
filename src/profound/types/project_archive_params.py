# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProjectArchiveParams"]


class ProjectArchiveParams(TypedDict, total=False):
    reason: Optional[str]

    category_id: Required[str]
    """Category that owns the project."""
