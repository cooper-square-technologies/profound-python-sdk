# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, TYPE_CHECKING, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..shared.claim_model_occurrence import ClaimModelOccurrence
from ..shared.dimension_ref import DimensionRef

__all__ = [
    "FactcheckStreamClaimsV2ClaimsStreamPostResponse",
    "FactcheckClaimsInfo",
    "FactcheckClaimsRow",
    "FactcheckClaimsRowEvidence",
    "FactcheckClaimsRowCitationSource",
    "FactcheckClaimsRowTheme",
    "FactcheckClaimsRowClaim",
    "FactcheckClaimsRowClaimEvidence",
    "FactcheckClaimsRowClaimCitationSource",
]


class FactcheckClaimsRowClaimCitationSource(BaseModel):
    href: Optional[str] = None

    hostname: Optional[str] = None

    citation_category: Optional[str] = None

    domain_category: Optional[str] = None

    snippet: Optional[str] = None

    citation_share: Optional[float] = None


class FactcheckClaimsRowClaimEvidence(BaseModel):
    id: Optional[str] = None

    kb_path: Optional[str] = None

    kb_snippet: Optional[str] = None

    source_updated_at: Optional[str] = None


class FactcheckClaimsRowClaim(BaseModel):
    cluster_id: Optional[str] = None

    claim: Optional[str] = None

    occurrence: Optional[float] = None

    theme: Optional[str] = None

    reasoning: Optional[str] = None

    models: Optional[List[ClaimModelOccurrence]] = None

    evidence: Optional[List[FactcheckClaimsRowClaimEvidence]] = None

    citation_sources: Optional[List[FactcheckClaimsRowClaimCitationSource]] = None

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


FactcheckClaimsRowTheme: TypeAlias = Union[str, DimensionRef]


class FactcheckClaimsRowCitationSource(BaseModel):
    href: Optional[str] = None

    hostname: Optional[str] = None

    citation_category: Optional[str] = None

    domain_category: Optional[str] = None

    snippet: Optional[str] = None

    citation_share: Optional[float] = None


class FactcheckClaimsRowEvidence(BaseModel):
    id: Optional[str] = None

    kb_path: Optional[str] = None

    kb_snippet: Optional[str] = None

    source_updated_at: Optional[str] = None


class FactcheckClaimsRow(BaseModel):
    cluster_id: Optional[str] = None

    claim: Optional[str] = None

    occurrence: Optional[float] = None

    reasoning: Optional[str] = None

    models: Optional[List[ClaimModelOccurrence]] = None

    evidence: Optional[List[FactcheckClaimsRowEvidence]] = None

    citation_sources: Optional[List[FactcheckClaimsRowCitationSource]] = None

    model: Optional[ClaimModelOccurrence] = None

    region: Optional[DimensionRef] = None

    persona: Optional[DimensionRef] = None

    prompt: Optional[DimensionRef] = None

    topic: Optional[DimensionRef] = None

    tag: Optional[DimensionRef] = None

    theme: Optional[FactcheckClaimsRowTheme] = None
    """Claim theme (string), or an `{id, name}` ref when sectioning by `theme`."""

    accuracy: Optional[float] = None

    accurate: Optional[int] = None

    inaccurate: Optional[int] = None

    total_claims: Optional[int] = None

    claims: Optional[List[FactcheckClaimsRowClaim]] = None

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


class FactcheckClaimsInfo(BaseModel):
    total_results: Optional[int] = None
    """Total rows matching the query before pagination (null when not computed)."""

    count: int
    """Number of rows returned in `data` for this page."""

    next_cursor: Optional[str] = None
    """Opaque cursor for the next page; null on the last page."""

    models: List[str]
    """Display names of the models the report covers."""

    start_date: str
    """Echoed request start date (YYYY-MM-DD, ET)."""

    end_date: str
    """Echoed request end date (YYYY-MM-DD, ET)."""

    filter: Optional[Dict[str, object]] = None
    """Echoed normalized filter tree, or null when no filter was sent."""

    group_by: List[str]
    """Dimension the claims are sectioned by (empty → one flat list)."""

    include: Optional[List[str]] = None
    """Per-claim detail fields requested."""

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


FactcheckStreamClaimsV2ClaimsStreamPostResponse: TypeAlias = Union[FactcheckClaimsInfo, FactcheckClaimsRow]
