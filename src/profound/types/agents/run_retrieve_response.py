# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RunRetrieveResponse", "Step"]


class Step(BaseModel):
    """One executed node in a run's step trace, in execution order.

    The lightweight fields always ship; ``outputs`` is populated only when the
    run-retrieve request asks for ``verbose``.
    """

    node_id: str
    """ID of the node that ran, within its agent graph."""

    node_type: str
    """Kind of node, e.g. "profound_visibility", "llm", "conditional"."""

    status: str
    """Terminal status of this node execution."""

    title: str
    """Human-readable title of the node."""

    elapsed_time: Optional[float] = None
    """Wall-clock seconds the node took, if recorded."""

    error_message: Optional[str] = None
    """Failure detail for this node, when it failed."""

    finished_at: Optional[datetime] = None
    """When the node finished, if it has."""

    outputs: Optional[Dict[str, object]] = None
    """Raw output payload this node produced.

    Included only when the request asks for `verbose`.
    """


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

    steps: Optional[List[Step]] = None
    """
    Ordered step-by-step execution trace — one entry per node that ran, in execution
    order. Always present once the run has executed a node; per-node `outputs`
    inside each step are included only when the request asks for `verbose`.
    """
