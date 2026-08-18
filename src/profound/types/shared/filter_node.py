# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FilterNode"]


class FilterNode(BaseModel):
    """A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group."""

    and_: Optional[List["FilterNode"]] = FieldInfo(alias="and", default=None)

    or_: Optional[List["FilterNode"]] = FieldInfo(alias="or", default=None)

    not_: Optional["FilterNode"] = FieldInfo(alias="not", default=None)

    field: Optional[str] = None

    op: Optional[str] = None

    value: Optional[object] = None
