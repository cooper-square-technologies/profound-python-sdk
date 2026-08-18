# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, TYPE_CHECKING, Union

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..shared.dimension_ref import DimensionRef

__all__ = ["VisibilityQueryV2V2PostResponse", "Info", "Data", "DataAsset"]


class DataAsset(BaseModel):
    name: Optional[str] = None

    owned: Optional[bool] = None
    """Whether the asset is owned by the category."""


class Data(BaseModel):
    asset: Optional[DataAsset] = None

    rank: Optional[int] = None
    """Asset rank (only when not grouped)."""

    date: Optional[str] = None

    model: Optional[DimensionRef] = None

    topic: Optional[DimensionRef] = None

    region: Optional[DimensionRef] = None

    prompt: Optional[DimensionRef] = None

    persona: Optional[DimensionRef] = None

    visibility_score: Optional[float] = None

    share_of_voice: Optional[float] = None

    average_position: Optional[float] = None

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

    scope: str
    """Asset scope: `all` or `owned`."""

    asset_filter: Optional[Union[Dict[str, object], List[str], str]] = None
    """Echoed `assets` selection (filter clause, name, or list), or null."""

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


class VisibilityQueryV2V2PostResponse(BaseModel):
    info: Info

    data: List[Data]
