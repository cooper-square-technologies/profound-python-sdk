# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    organization_id: Required[str]
    """ID of the organization that will own the agent. Required — Profound API keys are user-scoped, so the owning organization must be chosen explicitly. The caller must be a member of this organization."""

    name: Required[str]
    """Display name for the agent. Must be non-empty."""

    description: Optional[str]
    """Short description of the agent."""

    graph: Optional[Dict[str, object]]
    """Initial workflow graph for the agent's draft version. Optional — an agent can be created empty and have its graph filled in later."""
