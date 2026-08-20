# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .shared.agent_version import AgentVersion

__all__ = ["AgentRetrieveGraphParams"]


class AgentRetrieveGraphParams(TypedDict, total=False):
    version: AgentVersion
    """Version of the agent whose graph to retrieve. Use `published` for the live version, or `draft` for the latest unpublished changes. Defaults to `published`."""
