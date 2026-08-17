# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AgentListGraphV1GraphGetResponse", "Graph"]


class Graph(BaseModel):
    pass



class AgentListGraphV1GraphGetResponse(BaseModel):

    agent_id: str
    """Unique ID of the agent the graph belongs to."""

    version: Literal["published", "draft"]
    """Which version of the agent this graph is — `published` or `draft`."""

    graph: Graph
    """Workflow graph (`{nodes, edges}`) in the canonical dialect — the same shape `create` and `update` accept. Treat it as an opaque object: it is returned verbatim, so tool-backed nodes appear in their lowered `tool` form rather than the friendly v1 node types. Read it back to copy and edit a known-good agent."""
