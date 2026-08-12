# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ClaimQueryClaimsResponse",
    "Data",
    "DataCitationSource",
    "DataClaim",
    "DataClaimCitationSource",
    "DataClaimEvidence",
    "DataClaimModel",
    "DataEvidence",
    "DataModel",
    "DataPersona",
    "DataPrompt",
    "DataRegion",
    "DataTag",
    "DataTheme",
    "DataThemeDimensionRef",
    "DataTopic",
    "Info",
]


class DataCitationSource(BaseModel):
    citation_category: Optional[str] = None

    citation_share: Optional[float] = None

    domain_category: Optional[str] = None

    hostname: Optional[str] = None

    href: Optional[str] = None

    snippet: Optional[str] = None


class DataClaimCitationSource(BaseModel):
    citation_category: Optional[str] = None

    citation_share: Optional[float] = None

    domain_category: Optional[str] = None

    hostname: Optional[str] = None

    href: Optional[str] = None

    snippet: Optional[str] = None


class DataClaimEvidence(BaseModel):
    id: Optional[str] = None

    kb_path: Optional[str] = None

    kb_snippet: Optional[str] = None

    source_updated_at: Optional[str] = None


class DataClaimModel(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    occurrence: Optional[float] = None
    """Only populated for entries in `models`; omitted from grouped-section `model`."""


class DataClaim(BaseModel):
    """One inaccurate claim.

    `theme`/`reasoning`/`models`/`evidence`/`citation_sources` follow `include`.
    """

    citation_sources: Optional[List[DataClaimCitationSource]] = None

    claim: Optional[str] = None

    cluster_id: Optional[str] = None

    evidence: Optional[List[DataClaimEvidence]] = None

    models: Optional[List[DataClaimModel]] = None

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


class DataEvidence(BaseModel):
    id: Optional[str] = None

    kb_path: Optional[str] = None

    kb_snippet: Optional[str] = None

    source_updated_at: Optional[str] = None


class DataModel(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    occurrence: Optional[float] = None
    """Only populated for entries in `models`; omitted from grouped-section `model`."""


class DataPersona(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataPrompt(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataRegion(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataTag(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class DataThemeDimensionRef(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


DataTheme: TypeAlias = Union[str, DataThemeDimensionRef, None]


class DataTopic(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class Data(BaseModel):
    """
    A flat claim, or (with `group_by`) a section: a dimension + accuracy rollup + its `claims`.

    Present fields depend on `group_by`/`include`.
    """

    accuracy: Optional[float] = None

    accurate: Optional[int] = None

    citation_sources: Optional[List[DataCitationSource]] = None

    claim: Optional[str] = None

    claims: Optional[List[DataClaim]] = None

    cluster_id: Optional[str] = None

    evidence: Optional[List[DataEvidence]] = None

    inaccurate: Optional[int] = None

    model: Optional[DataModel] = None

    models: Optional[List[DataModel]] = None

    occurrence: Optional[float] = None

    persona: Optional[DataPersona] = None
    """An `{id, name}` reference for a grouped dimension value."""

    prompt: Optional[DataPrompt] = None
    """An `{id, name}` reference for a grouped dimension value."""

    reasoning: Optional[str] = None

    region: Optional[DataRegion] = None
    """An `{id, name}` reference for a grouped dimension value."""

    tag: Optional[DataTag] = None
    """An `{id, name}` reference for a grouped dimension value."""

    theme: Optional[DataTheme] = None
    """Claim theme (string), or an `{id, name}` ref when sectioning by `theme`."""

    topic: Optional[DataTopic] = None
    """An `{id, name}` reference for a grouped dimension value."""

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


class Info(BaseModel):
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


class ClaimQueryClaimsResponse(BaseModel):
    data: List[Data]

    info: Info
