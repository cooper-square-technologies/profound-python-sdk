# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DomainSegmentListV2GetParams"]


class DomainSegmentListV2GetParams(TypedDict, total=False):
    organization_id: Optional[str]
    """Organization UUID to list segments for. Required when the caller belongs to multiple organizations."""
