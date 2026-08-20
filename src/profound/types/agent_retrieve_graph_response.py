# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict

from .._models import BaseModel

from .shared.agent_version import AgentVersion

__all__ = ["AgentRetrieveGraphResponse"]


class AgentRetrieveGraphResponse(BaseModel):
    agent_id: str
    """Unique ID of the agent the graph belongs to."""

    version: AgentVersion
    """Which version of the agent this graph is — `published` or `draft`."""

    graph: Dict[str, object]
    """Workflow graph (`{nodes, edges}`) in the canonical dialect — the same shape `create` and `update` accept. Treat it as an opaque object: it is returned verbatim, so tool-backed nodes appear in their lowered `tool` form rather than the friendly v1 node types. Read it back to copy and edit a known-good agent."""
