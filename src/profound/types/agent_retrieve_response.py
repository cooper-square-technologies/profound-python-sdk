# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentRetrieveResponse", "Schema"]


class Schema(BaseModel):
    """Input and output schemas for this agent."""

    input: Dict[str, object]
    """JSON Schema for the agent's `inputs` object.

    Use the top-level property keys as input field names when starting a run.
    """

    output: Dict[str, object]
    """
    JSON Schema for the `outputs` object returned by
    `GET /v1/agents/{agent_id}/runs/{run_id}`.
    """


class AgentRetrieveResponse(BaseModel):
    """Detailed information for an agent."""

    id: str
    """Unique ID for the agent."""

    created_at: datetime
    """When the agent was created."""

    name: str
    """Display name of the agent."""

    organization_id: str
    """Unique ID of the organization that owns the agent."""

    schema_: Schema = FieldInfo(alias="schema")
    """Input and output schemas for this agent."""

    status: Literal["draft", "published", "unknown"]
    """Current status of the agent."""

    description: Optional[str] = None
    """Short description of the agent, if provided."""
