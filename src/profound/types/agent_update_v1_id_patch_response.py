# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentUpdateV1IDPatchResponse", "Schema", "Validation", "ValidationIssue"]


class ValidationIssue(BaseModel):
    code: str
    """Stable machine-readable identifier for the kind of issue."""

    message: str
    """Human-readable description of the issue."""

    node_id: Optional[str] = None
    """ID of the node the issue applies to, if node-specific."""

    node_title: Optional[str] = None
    """Display title of the affected node, if available."""

    field: Optional[str] = None
    """Name of the offending field on the node, if field-specific."""

    field_title: Optional[str] = None
    """Display title of the affected field, if available."""

    violation: Optional[str] = None
    """The specific constraint that was violated, if available."""


class Validation(BaseModel):
    valid: bool
    """Whether the agent's graph is valid and ready to publish."""

    issues: Optional[List[ValidationIssue]] = None
    """Problems found while validating the graph. Empty when `valid` is true."""


class Schema(BaseModel):
    input: Dict[str, object]
    """JSON Schema for the agent's `inputs` object. Use the top-level property keys as input field names when starting a run."""

    output: Dict[str, object]
    """JSON Schema for the `outputs` object returned by `GET /v1/agents/{agent_id}/runs/{run_id}`."""


class AgentUpdateV1IDPatchResponse(BaseModel):
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

    schema_: Optional[Schema] = FieldInfo(alias="schema", default=None)
    """Input and output schemas for this agent. Omitted while the agent's graph cannot be previewed (e.g. an empty or structurally-invalid draft); check `validation` to see what needs fixing."""

    validation: Optional[Validation] = None
    """Validation report for the agent's graph, when available. Use `validation.valid` to check the agent is publishable."""
