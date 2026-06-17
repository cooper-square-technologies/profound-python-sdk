# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    graph: Required[Dict[str, object]]
    """New workflow graph for the agent's draft version.

    Replaces the current draft graph; the agent is iterated in place rather than
    re-created, so its ID is stable. Required — Magi rejects a null graph, so an
    empty update is a 422 here rather than a relayed upstream error.
    """
