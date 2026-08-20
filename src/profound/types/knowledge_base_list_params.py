# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["KnowledgeBaseListParams"]


class KnowledgeBaseListParams(TypedDict, total=False):
    organization_id: Optional[str]
    """Organization scope for API keys that can access multiple organizations."""
