# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..report_response import ReportResponse

__all__ = ["RawLogsResponse", "LogVisitList"]


class LogVisitList(BaseModel):
    host: str

    ip: str

    method: str

    org_id: str

    path: str

    status_code: int

    timestamp: datetime

    user_agent: str

    bytes_sent: Optional[int] = None

    duration_ms: Optional[int] = None

    query_params: Optional[Dict[str, str]] = None

    referer: Optional[str] = None


RawLogsResponse: TypeAlias = Union[List[LogVisitList], ReportResponse]
