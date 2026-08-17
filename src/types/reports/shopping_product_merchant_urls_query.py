# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ShoppingProductMerchantUrlsQuery"]


class ShoppingProductMerchantUrlsQuery(BaseModel):

    category_id: str

    product_names: List[str]

    start_date: datetime

    end_date: datetime
