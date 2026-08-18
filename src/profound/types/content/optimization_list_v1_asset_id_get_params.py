# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OptimizationListV1AssetIDGetParams"]


class OptimizationListV1AssetIDGetParams(TypedDict, total=False):
    limit: int
    """Maximum number of results to return"""

    offset: int
    """Offset for pagination"""
