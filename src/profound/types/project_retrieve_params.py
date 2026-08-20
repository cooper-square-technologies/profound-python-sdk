# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProjectRetrieveParams"]


class ProjectRetrieveParams(TypedDict, total=False):
    category_id: Required[str]
    """Category that owns the project."""
