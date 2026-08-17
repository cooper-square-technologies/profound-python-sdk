# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .cursor_pagination import CursorPagination

__all__ = ["AgentListResponse", "Agent"]


class Agent(BaseModel):

    id: str
    """Unique ID for the agent."""

    organization_id: str
    """Unique ID of the organization that owns the agent."""

    name: str
    """Display name of the agent."""

    status: Literal["draft", "published", "unknown"]
    """Current status of the agent."""

    created_at: datetime
    """When the agent was created."""

    description: Optional[str] = None
    """Short description of the agent, if provided."""



class AgentListResponse(BaseModel):

    data: List[Agent]
    """Agents returned for this page."""

    pagination: Optional[CursorPagination] = None
    """Cursor pagination details for this response."""
