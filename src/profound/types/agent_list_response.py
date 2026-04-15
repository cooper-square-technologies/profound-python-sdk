# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AgentListResponse", "Data", "Pagination"]


class Data(BaseModel):
    """Summary information for an agent."""

    id: str
    """Unique ID for the agent."""

    created_at: datetime
    """When the agent was created."""

    name: str
    """Display name of the agent."""

    organization_id: str
    """Unique ID of the organization that owns the agent."""

    status: Literal["draft", "published", "unknown"]
    """Current status of the agent."""

    description: Optional[str] = None
    """Short description of the agent, if provided."""


class Pagination(BaseModel):
    """Cursor pagination details for this response."""

    limit: Optional[int] = None
    """Maximum number of results to return. Default is 10,000, maximum is 50,000."""

    next_cursor: Optional[str] = None
    """Token for the next page, if more results are available."""


class AgentListResponse(BaseModel):
    """Paginated list of agents."""

    data: List[Data]
    """Agents returned for this page."""

    pagination: Optional[Pagination] = None
    """Cursor pagination details for this response."""
