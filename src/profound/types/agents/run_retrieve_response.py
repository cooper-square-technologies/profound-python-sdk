# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RunRetrieveResponse"]


class RunRetrieveResponse(BaseModel):
    """Status and result details for an agent run."""

    id: str
    """Unique ID for the run."""

    agent_id: str
    """Unique ID of the agent for this run."""

    status: Literal["queued", "running", "succeeded", "failed", "cancelled", "skipped", "unknown"]
    """Current status of the run."""

    error: Optional[Dict[str, object]] = None
    """Error details, when the run fails and error information is available."""

    finished_at: Optional[datetime] = None
    """When the run finished, if it has completed."""

    outputs: Optional[Dict[str, object]] = None
    """Output values returned by the run, keyed by variable ID.

    This object conforms to `schema.output` from the agent detail response and is
    empty when no outputs are available.
    """

    started_at: Optional[datetime] = None
    """When the run started, if it has started."""
