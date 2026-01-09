# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OptimizationListParams"]


class OptimizationListParams(TypedDict, total=False):
    limit: int
    """Maximum number of results to return"""

    offset: int
    """Offset for pagination"""
