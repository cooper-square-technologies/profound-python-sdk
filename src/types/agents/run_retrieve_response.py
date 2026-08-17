# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RunRetrieveResponse", "Error", "Outputs"]


class Outputs(BaseModel):
    pass

class Error(BaseModel):
    pass



class RunRetrieveResponse(BaseModel):

    id: str
    """Unique ID for the run."""

    agent_id: str
    """Unique ID of the agent for this run."""

    status: Literal["queued", "running", "succeeded", "failed", "cancelled", "skipped", "unknown"]
    """Current status of the run."""

    started_at: Optional[datetime] = None
    """When the run started, if it has started."""

    finished_at: Optional[datetime] = None
    """When the run finished, if it has completed."""

    error: Optional[Error] = None
    """Error details, when the run fails and error information is available."""

    outputs: Optional[Outputs] = None
    """Output values returned by the run, keyed by variable ID. This object conforms to `schema.output` from the agent detail response and is empty when no outputs are available."""
