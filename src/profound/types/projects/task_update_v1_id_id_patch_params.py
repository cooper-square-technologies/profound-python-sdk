# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TaskUpdateV1IDIDPatchParams"]


class TaskUpdateV1IDIDPatchParams(TypedDict, total=False):
    project_id: Required[str]
    """Unique project ID."""

    title: Optional[str]

    summary: Optional[str]

    brief: Optional[str]

    type: Optional[str]

    topic: Optional[str]

    impact: Optional[int]

    reference_url: Optional[str]

    reference_label: Optional[str]

    category_id: Required[str]
    """Category that owns the project."""
