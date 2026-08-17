# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List

from ..._models import BaseModel

from ..report_info import ReportInfo

__all__ = ["ShoppingProductMerchantURLsResponse"]


class ShoppingProductMerchantURLsResponse(BaseModel):
    info: ReportInfo
    """Base model for report information."""

    data: List[Dict[str, object]]
