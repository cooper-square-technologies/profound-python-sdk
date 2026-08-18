# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ProjectGenerationContextItem"]


class ProjectGenerationContextItem(BaseModel):
    id: str

    name: str

    slug: Optional[str] = None
