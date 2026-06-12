# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["NodeTypeListResponse", "Data"]


class Data(BaseModel):
    """Thin summary for a node type available to v1 agent authors."""

    display_name: str
    """Human-readable name for the node type."""

    node_type: str
    """Stable identifier for the node type, e.g. `llm`."""

    description: Optional[str] = None
    """Short description of what the node type does, if provided."""


class NodeTypeListResponse(BaseModel):
    """List of node types available to v1 agent authors."""

    data: List[Data]
    """Allowlisted node types, returned as thin summaries."""
