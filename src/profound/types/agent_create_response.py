# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AgentCreateResponse"]


class AgentCreateResponse(BaseModel):
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
