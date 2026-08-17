# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, TypedDict
from ..._types import SequenceNotStr

__all__ = ["ShoppingProductMerchantUrlsParams"]


class ShoppingProductMerchantUrlsParams(TypedDict, total=False):

    category_id: Required[str]

    product_names: Required[SequenceNotStr[str]]

    start_date: Required[Union[str, datetime]]

    end_date: Required[Union[str, datetime]]
