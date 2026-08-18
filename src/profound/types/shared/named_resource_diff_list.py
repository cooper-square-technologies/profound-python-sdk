# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from .named_resource import NamedResource

__all__ = ["NamedResourceDiffList"]


class NamedResourceDiffList(BaseModel):
    """Shows which resources were added or removed."""

    added: Optional[List[NamedResource]] = None
    """Resources that were added."""

    removed: Optional[List[NamedResource]] = None
    """Resources that were removed."""
