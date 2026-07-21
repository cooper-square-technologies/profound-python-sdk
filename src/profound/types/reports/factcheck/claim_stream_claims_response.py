# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ClaimStreamClaimsResponse",
    "FactcheckClaimsInfo",
    "FactcheckClaimsRow",
    "FactcheckClaimsRowCitationSource",
    "FactcheckClaimsRowClaim",
    "FactcheckClaimsRowClaimCitationSource",
    "FactcheckClaimsRowClaimEvidence",
    "FactcheckClaimsRowClaimModel",
    "FactcheckClaimsRowEvidence",
    "FactcheckClaimsRowModel",
    "FactcheckClaimsRowPersona",
    "FactcheckClaimsRowPrompt",
    "FactcheckClaimsRowRegion",
    "FactcheckClaimsRowTag",
    "FactcheckClaimsRowTheme",
    "FactcheckClaimsRowThemeDimensionRef",
    "FactcheckClaimsRowTopic",
]


class FactcheckClaimsInfo(BaseModel):
    """`summary` event payload (the report `info` block)."""

    count: int
    """Number of rows returned in `data` for this page."""

    end_date: str
    """Echoed request end date (YYYY-MM-DD, ET)."""

    group_by: List[str]
    """Dimension the claims are sectioned by (empty → one flat list)."""

    models: List[str]
    """Display names of the models the report covers."""

    start_date: str
    """Echoed request start date (YYYY-MM-DD, ET)."""

    filter: Optional[Dict[str, object]] = None
    """Echoed normalized filter tree, or null when no filter was sent."""

    include: Optional[List[str]] = None
    """Per-claim detail fields requested."""

    next_cursor: Optional[str] = None
    """Opaque cursor for the next page; null on the last page."""

    total_results: Optional[int] = None
    """Total rows matching the query before pagination (null when not computed)."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FactcheckClaimsRowCitationSource(BaseModel):
    citation_category: Optional[str] = None

    citation_share: Optional[float] = None

    domain_category: Optional[str] = None

    hostname: Optional[str] = None

    href: Optional[str] = None

    snippet: Optional[str] = None


class FactcheckClaimsRowClaimCitationSource(BaseModel):
    citation_category: Optional[str] = None

    citation_share: Optional[float] = None

    domain_category: Optional[str] = None

    hostname: Optional[str] = None

    href: Optional[str] = None

    snippet: Optional[str] = None


class FactcheckClaimsRowClaimEvidence(BaseModel):
    id: Optional[str] = None

    kb_path: Optional[str] = None

    kb_snippet: Optional[str] = None

    source_updated_at: Optional[str] = None


class FactcheckClaimsRowClaimModel(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    occurrence: Optional[float] = None


class FactcheckClaimsRowClaim(BaseModel):
    """One inaccurate claim.

    `theme`/`reasoning`/`models`/`evidence`/`citation_sources` follow `include`.
    """

    citation_sources: Optional[List[FactcheckClaimsRowClaimCitationSource]] = None

    claim: Optional[str] = None

    cluster_id: Optional[str] = None

    evidence: Optional[List[FactcheckClaimsRowClaimEvidence]] = None

    models: Optional[List[FactcheckClaimsRowClaimModel]] = None

    occurrence: Optional[float] = None

    reasoning: Optional[str] = None

    theme: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class FactcheckClaimsRowEvidence(BaseModel):
    id: Optional[str] = None

    kb_path: Optional[str] = None

    kb_snippet: Optional[str] = None

    source_updated_at: Optional[str] = None


class FactcheckClaimsRowModel(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class FactcheckClaimsRowPersona(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class FactcheckClaimsRowPrompt(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class FactcheckClaimsRowRegion(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class FactcheckClaimsRowTag(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class FactcheckClaimsRowThemeDimensionRef(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


FactcheckClaimsRowTheme: TypeAlias = Union[str, FactcheckClaimsRowThemeDimensionRef, None]


class FactcheckClaimsRowTopic(BaseModel):
    """
    An ``{id, name}`` reference for a grouped dimension value (model, topic, region, …).
    """

    id: Optional[str] = None

    name: Optional[str] = None


class FactcheckClaimsRow(BaseModel):
    """`result` event payload — one inaccurate claim."""

    accuracy: Optional[float] = None

    accurate: Optional[int] = None

    citation_sources: Optional[List[FactcheckClaimsRowCitationSource]] = None

    claim: Optional[str] = None

    claims: Optional[List[FactcheckClaimsRowClaim]] = None

    cluster_id: Optional[str] = None

    evidence: Optional[List[FactcheckClaimsRowEvidence]] = None

    inaccurate: Optional[int] = None

    model: Optional[FactcheckClaimsRowModel] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    models: Optional[List[FactcheckClaimsRowModel]] = None

    occurrence: Optional[float] = None

    persona: Optional[FactcheckClaimsRowPersona] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    prompt: Optional[FactcheckClaimsRowPrompt] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    reasoning: Optional[str] = None

    region: Optional[FactcheckClaimsRowRegion] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    tag: Optional[FactcheckClaimsRowTag] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    theme: Optional[FactcheckClaimsRowTheme] = None
    """Claim theme (string), or an `{id, name}` ref when sectioning by `theme`."""

    topic: Optional[FactcheckClaimsRowTopic] = None
    """
    An `{id, name}` reference for a grouped dimension value (model, topic, region,
    …).
    """

    total_claims: Optional[int] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


ClaimStreamClaimsResponse: TypeAlias = Union[FactcheckClaimsInfo, FactcheckClaimsRow]
