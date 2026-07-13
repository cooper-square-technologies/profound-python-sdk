# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TaskUpdateStatusParams"]


class TaskUpdateStatusParams(TypedDict, total=False):
    project_id: Required[str]
    """Unique project ID."""

    category_id: Required[str]
    """Category that owns the project."""

    status: Required[Literal["not_started", "in_progress", "done", "abandoned"]]

    note: Optional[str]
