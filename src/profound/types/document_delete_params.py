# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DocumentDeleteParams"]


class DocumentDeleteParams(TypedDict, total=False):
    organization_id: Required[str]
    """ID of the organization that owns the document. You must be a member of it."""
