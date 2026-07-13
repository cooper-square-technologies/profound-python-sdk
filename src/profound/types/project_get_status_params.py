# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProjectGetStatusParams"]


class ProjectGetStatusParams(TypedDict, total=False):
    category_id: Required[str]
    """Category that owns the project."""
