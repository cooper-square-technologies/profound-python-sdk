# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["CategoryListParams"]


class CategoryListParams(TypedDict, total=False):

    organization_ids: Optional[Iterable[str]]
    """Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to."""
