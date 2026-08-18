# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .shared.agent_version import AgentVersion

__all__ = ["AgentRetrieveV1GetParams"]


class AgentRetrieveV1GetParams(TypedDict, total=False):
    version: AgentVersion
    """Version of the agent to retrieve. Use `published` for the live version, or `draft` for the latest unpublished changes for the same agent. Defaults to `published`."""
