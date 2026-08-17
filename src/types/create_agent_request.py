# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CreateAgentRequest", "Graph"]


class Graph(BaseModel):
    pass



class CreateAgentRequest(BaseModel):
    """Request body for creating a draft agent."""

    organization_id: str
    """ID of the organization that will own the agent. Required — Profound API keys are user-scoped, so the owning organization must be chosen explicitly. The caller must be a member of this organization."""

    name: str
    """Display name for the agent. Must be non-empty."""

    description: Optional[str] = None
    """Short description of the agent."""

    graph: Optional[Graph] = None
    """Initial workflow graph for the agent's draft version. Optional — an agent can be created empty and have its graph filled in later."""
