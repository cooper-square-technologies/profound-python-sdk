# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentRetrieveResponse", "Schema", "Validation", "ValidationIssue"]


class Schema(BaseModel):
    """Schema metadata for an agent."""

    input: Dict[str, object]
    """JSON Schema for the agent's `inputs` object.

    Use the top-level property keys as input field names when starting a run.
    """

    output: Dict[str, object]
    """
    JSON Schema for the `outputs` object returned by
    `GET /v1/agents/{agent_id}/runs/{run_id}`.
    """


class ValidationIssue(BaseModel):
    """A single problem found while validating an agent's graph."""

    code: str
    """Stable machine-readable identifier for the kind of issue."""

    message: str
    """Human-readable description of the issue."""

    field: Optional[str] = None
    """Name of the offending field on the node, if field-specific."""

    field_title: Optional[str] = None
    """Display title of the affected field, if available."""

    node_id: Optional[str] = None
    """ID of the node the issue applies to, if node-specific."""

    node_title: Optional[str] = None
    """Display title of the affected node, if available."""

    violation: Optional[str] = None
    """The specific constraint that was violated, if available."""


class Validation(BaseModel):
    """Result of validating an agent's graph.

    Mirrors the report computed on every read, so callers can confirm a draft
    is publishable before calling publish.
    """

    valid: bool
    """Whether the agent's graph is valid and ready to publish."""

    issues: Optional[List[ValidationIssue]] = None
    """Problems found while validating the graph. Empty when `valid` is true."""


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

    status: Literal["draft", "published", "unknown"]
    """Current status of the agent."""

    description: Optional[str] = None
    """Short description of the agent, if provided."""

    schema_: Optional[Schema] = FieldInfo(alias="schema", default=None)
    """Schema metadata for an agent."""

    validation: Optional[Validation] = None
    """Result of validating an agent's graph.

    Mirrors the report computed on every read, so callers can confirm a draft is
    publishable before calling publish.
    """
