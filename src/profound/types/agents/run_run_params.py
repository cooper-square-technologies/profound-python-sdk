# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["RunRunParams"]


class RunRunParams(TypedDict, total=False):
    inputs: Dict[str, object]
    """Input values for the run.

    Keys should match the property names defined in `schema.input`.
    """
