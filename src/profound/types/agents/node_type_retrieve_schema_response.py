# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NodeTypeRetrieveSchemaResponse"]


class NodeTypeRetrieveSchemaResponse(BaseModel):
    """JSON schema and worked examples for a single node type."""

    node_type: str
    """Stable identifier for the node type, e.g. `llm`."""

    schema_: Dict[str, object] = FieldInfo(alias="schema")
    """Opaque JSON Schema for the node's configuration.

    Treat this as an arbitrary object; its internal shape can change between
    `schema_version` bumps.
    """

    schema_version: str
    """Opaque version string for the node schema.

    Bumps whenever the underlying schema changes, so it can be used as a client-side
    cache key.
    """

    description: Optional[str] = None
    """Short description of what the node type does, if provided."""

    examples: Optional[List[Dict[str, object]]] = None
    """Worked example configurations for the node type that conform to `schema`."""
