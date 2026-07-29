# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ReportQueryVisibilityResponse",
    "Data",
    "DataAsset",
    "DataModel",
    "DataPersona",
    "DataPrompt",
    "DataRegion",
    "DataTopic",
    "Info",
]


class DataAsset(BaseModel):
    name: Optional[str] = None

    owned: Optional[bool] = None
    """Whether the asset is owned by the category."""


class DataModel(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


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


class DataTopic(BaseModel):
    """An ``{id, name}`` reference for a grouped dimension value."""

    id: Optional[str] = None

    name: Optional[str] = None


class Data(BaseModel):
    """One (asset x group) row.

    Group dimensions and metrics present depend on `group_by`/`metrics`.
    """

    asset: Optional[DataAsset] = None

    average_position: Optional[float] = None

    date: Optional[str] = None

    model: Optional[DataModel] = None
    """An `{id, name}` reference for a grouped dimension value."""

    persona: Optional[DataPersona] = None
    """An `{id, name}` reference for a grouped dimension value."""

    prompt: Optional[DataPrompt] = None
    """An `{id, name}` reference for a grouped dimension value."""

    rank: Optional[int] = None
    """Asset rank (only when not grouped)."""

    region: Optional[DataRegion] = None
    """An `{id, name}` reference for a grouped dimension value."""

    share_of_voice: Optional[float] = None

    topic: Optional[DataTopic] = None
    """An `{id, name}` reference for a grouped dimension value."""

    visibility_score: Optional[float] = None

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

    models: List[str]
    """Display names of the models the report covers."""

    scope: str
    """Asset scope: `all` or `owned`."""

    start_date: str
    """Echoed request start date (YYYY-MM-DD, ET)."""

    asset_filter: Union[Dict[str, object], List[str], str, None] = None
    """Echoed `assets` selection (filter clause, name, or list), or null."""

    filter: Optional[Dict[str, object]] = None
    """Echoed normalized filter tree, or null when no filter was sent."""

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


class ReportQueryVisibilityResponse(BaseModel):
    data: List[Data]

    info: Info
