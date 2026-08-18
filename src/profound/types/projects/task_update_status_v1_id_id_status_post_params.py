# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TaskUpdateStatusV1IDIDStatusPostParams"]


class TaskUpdateStatusV1IDIDStatusPostParams(TypedDict, total=False):
    project_id: Required[str]
    """Unique project ID."""

    status: Required[Literal["not_started", "in_progress", "done", "abandoned"]]

    note: Optional[str]

    category_id: Required[str]
    """Category that owns the project."""
