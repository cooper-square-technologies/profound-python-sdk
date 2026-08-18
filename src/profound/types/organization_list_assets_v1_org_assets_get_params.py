# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict
from .._types import SequenceNotStr

__all__ = ["OrganizationListAssetsV1OrgAssetsGetParams"]


class OrganizationListAssetsV1OrgAssetsGetParams(TypedDict, total=False):
    organization_ids: Optional[SequenceNotStr[str]]
    """Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to."""
