# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, Required, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

__all__ = ["ShoppingProductMerchantURLsParams"]


class ShoppingProductMerchantURLsParams(TypedDict, total=False):
    category_id: Required[str]

    product_names: Required[SequenceNotStr[str]]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
