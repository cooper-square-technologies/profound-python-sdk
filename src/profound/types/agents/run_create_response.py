# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RunCreateResponse"]


class RunCreateResponse(BaseModel):
    """Run details returned after a run request is accepted."""

    id: str
    """Unique ID for the accepted run."""

    agent_id: str
    """Unique ID of the agent for this run."""

    status: Literal["queued", "running", "succeeded", "failed", "cancelled", "skipped", "unknown"]
    """Initial status of the accepted run."""

    started_at: Optional[datetime] = None
    """When the run started, if execution began immediately."""
