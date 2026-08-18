# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TaskRetrieveV1GetParams"]


class TaskRetrieveV1GetParams(TypedDict, total=False):
    project_id: Required[str]
    """Unique project ID."""

    category_id: Required[str]
    """Category that owns the project."""
