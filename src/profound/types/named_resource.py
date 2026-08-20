# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["NamedResource"]


class NamedResource(BaseModel):
    """Generic id+name reference used across domain boundaries."""

    id: str

    name: str
