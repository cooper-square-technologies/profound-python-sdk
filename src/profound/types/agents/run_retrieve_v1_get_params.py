# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RunRetrieveV1GetParams"]


class RunRetrieveV1GetParams(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent that owns the run."""

    verbose: bool
    """Include each step's raw `outputs` payload in the execution trace."""
