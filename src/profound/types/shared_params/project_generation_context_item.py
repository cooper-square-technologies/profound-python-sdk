# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProjectGenerationContextItem"]


class ProjectGenerationContextItem(TypedDict, total=False):
    id: Required[str]

    name: Required[str]

    slug: Optional[str]
