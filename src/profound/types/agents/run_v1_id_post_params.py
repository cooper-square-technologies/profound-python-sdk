# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["RunV1IDPostParams"]


class RunV1IDPostParams(TypedDict, total=False):
    inputs: Dict[str, object]
    """Input values for the run. Keys should match the property names defined in `schema.input`. Omit the request body when the agent does not require inputs."""
