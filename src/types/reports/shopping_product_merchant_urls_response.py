# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from ..._models import BaseModel
from ..report_info import ReportInfo

__all__ = ["ShoppingProductMerchantUrlsResponse", "Data"]


class Data(BaseModel):
    pass



class ShoppingProductMerchantUrlsResponse(BaseModel):

    info: ReportInfo
    """Base model for report information."""

    data: List[Data]
