# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    category_id: Required[str]
    """Category that owns the project."""

    title: Required[str]

    brief: Optional[str]

    impact: Optional[int]

    position: Optional[int]

    reference_label: Optional[str]

    reference_url: Optional[str]

    summary: Optional[str]

    topic: Optional[str]

    type: Optional[str]
