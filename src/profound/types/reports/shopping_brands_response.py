# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ShoppingBrandsResponse", "Data", "DataPrompt", "DataRegion", "DataTopic", "Info"]


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

    Group dims/metrics present depend on `group_by`/`metrics`.
    """

    asset: Optional[Dict[str, object]] = None

    average_position: Optional[float] = None

    date: Optional[str] = None

    prompt: Optional[DataPrompt] = None
    """An `{id, name}` reference for a grouped dimension value."""

    rank: Optional[int] = None
    """Asset visibility rank as a top-level field (ungrouped only)."""

    region: Optional[DataRegion] = None
    """An `{id, name}` reference for a grouped dimension value."""

    topic: Optional[DataTopic] = None
    """An `{id, name}` reference for a grouped dimension value."""

    visibility_rank: Optional[int] = None
    """Asset visibility rank (present on grouped rows)."""

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
    """Number of assets on this page.

    When grouped by `date`, `data` holds one row per asset x bucket, so `len(data)`
    can exceed `count`.
    """

    end_date: str
    """Echoed request end date (YYYY-MM-DD, ET)."""

    metrics: List[str]
    """Metrics returned per row."""

    models: List[str]
    """Display names of the models the report covers."""

    scope: str
    """Asset scope: `all`, `owned`, or `custom` when `assets` was given."""

    start_date: str
    """Echoed request start date (YYYY-MM-DD, ET)."""

    assets: Union[str, List[str], None] = None
    """Echoed `assets` selection; when set it overrides `scope`."""

    filter: Optional[Dict[str, object]] = None
    """Echoed normalized filter tree, or null when no filter was sent."""

    next_cursor: Optional[str] = None
    """Opaque cursor for the next page; null on the last page."""

    total_results: Optional[int] = None
    """Total assets matching the query before pagination."""

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


class ShoppingBrandsResponse(BaseModel):
    data: List[Data]

    info: Info
