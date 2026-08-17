# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AgentRetrieveParams"]


class AgentRetrieveParams(TypedDict, total=False):
    version: Literal["published", "draft"]
    """Version of the agent to retrieve. Use `published` for the live version, or `draft` for the latest unpublished changes for the same agent. Defaults to `published`."""
