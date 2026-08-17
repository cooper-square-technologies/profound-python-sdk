# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["NodeTypeListV1AgentsGetResponse", "NodeTypeSummary"]


class NodeTypeSummary(BaseModel):

    node_type: str
    """Stable identifier for the node type, e.g. `llm`."""

    display_name: str
    """Human-readable name for the node type."""

    description: Optional[str] = None
    """Short description of what the node type does, if provided."""



class NodeTypeListV1AgentsGetResponse(BaseModel):

    data: List[NodeTypeSummary]
    """Allowlisted node types, returned as thin summaries."""
