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

    docs_version: Optional[str] = None
    """
    Opaque version string for `documentation`/`examples`, independent of
    `schema_version`. Bumps when the authoring guidance changes even if the
    underlying machine `schema` did not. When it trails the live `schema_version`,
    treat `documentation`/`examples` as guidance that may be stale and validate
    against the live `schema`.
    """

    documentation: Optional[Dict[str, object]] = None
    """
    Opaque, human-oriented authoring guidance for the node type — purpose,
    constraints, enum values, and variable-flow notes that the machine `schema` does
    not always express (e.g. a conditional's else-branch rule, or an iteration's
    sub-graph shape). Treat as an arbitrary object; use `docs_version` as its cache
    key.
    """

    examples: Optional[List[Dict[str, object]]] = None
    """Worked example configurations for the node type, in the canonical graph dialect.

    These are curated guidance maintained by external-api, versioned by
    `docs_version` (NOT `schema_version`): they illustrate a valid shape at curation
    time but are a starting point, not the contract — they may lag the validator.
    The authoritative contract is `schema`, and the only authoritative check that a
    graph is valid is publishing it (or the agent-validation endpoint). Do not parse
    `examples` as the schema.
    """
