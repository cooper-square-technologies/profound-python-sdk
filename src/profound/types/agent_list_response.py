# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from .._models import BaseModel

from .shared.agent import Agent
from .shared.cursor_pagination import CursorPagination

__all__ = ["AgentListResponse"]


class AgentListResponse(BaseModel):
    data: List[Agent]
    """Agents returned for this page."""

    pagination: Optional[CursorPagination] = None
    """Cursor pagination details for this response."""
