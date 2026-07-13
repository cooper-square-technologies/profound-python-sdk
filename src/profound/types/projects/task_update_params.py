# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TaskUpdateParams"]


class TaskUpdateParams(TypedDict, total=False):
    project_id: Required[str]
    """Unique project ID."""

    category_id: Required[str]
    """Category that owns the project."""

    brief: Optional[str]

    impact: Optional[int]

    reference_label: Optional[str]

    reference_url: Optional[str]

    summary: Optional[str]

    title: Optional[str]

    topic: Optional[str]

    type: Optional[str]
