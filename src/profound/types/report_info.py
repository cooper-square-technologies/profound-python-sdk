# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ReportInfo"]


class ReportInfo(BaseModel):
    """Base model for report information."""

    total_rows: int

    query: Optional[Dict[str, object]] = None
