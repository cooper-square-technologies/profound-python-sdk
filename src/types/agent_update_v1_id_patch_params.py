# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentUpdateV1IdPatchParams", "Graph"]


class AgentUpdateV1IdPatchParams(TypedDict, total=False):

    graph: Required[Graph]
    """New workflow graph for the agent's draft version. Replaces the current draft graph; the agent is iterated in place rather than re-created, so its ID is stable. Required — a null graph is rejected as a 422 here rather than as a relayed upstream error."""


class Graph(TypedDict, total=False):
    pass

