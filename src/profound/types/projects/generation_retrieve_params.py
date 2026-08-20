# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GenerationRetrieveParams"]


class GenerationRetrieveParams(TypedDict, total=False):
    category_id: Required[str]
    """Category that owns the project."""
