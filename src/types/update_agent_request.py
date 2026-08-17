# File generated from our OpenAPI spec by Scalar. See README.md for details.


from .._models import BaseModel

__all__ = ["UpdateAgentRequest", "Graph"]


class Graph(BaseModel):
    pass



class UpdateAgentRequest(BaseModel):
    """Request body for updating a draft agent's graph in place."""

    graph: Graph
    """New workflow graph for the agent's draft version. Replaces the current draft graph; the agent is iterated in place rather than re-created, so its ID is stable. Required — a null graph is rejected as a 422 here rather than as a relayed upstream error."""
