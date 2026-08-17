# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RunCreateParams", "Inputs"]


class RunCreateParams(TypedDict, total=False):

    inputs: Inputs
    """Input values for the run. Keys should match the property names defined in `schema.input`. Omit the request body when the agent does not require inputs."""


class Inputs(TypedDict, total=False):
    pass

