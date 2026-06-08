# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ..._models import BaseModel
from ..report_info import ReportInfo

__all__ = ["ShoppingTriggerRateResponse"]


class ShoppingTriggerRateResponse(BaseModel):
    data: List[Dict[str, object]]

    info: ReportInfo
    """Base model for report information."""
