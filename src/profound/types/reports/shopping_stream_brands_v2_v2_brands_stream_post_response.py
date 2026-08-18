# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional, TYPE_CHECKING, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..shared.dimension_ref import DimensionRef

__all__ = ["ShoppingStreamBrandsV2V2BrandsStreamPostResponse", "ShoppingBrandsV2Info", "ShoppingBrandRow"]


class ShoppingBrandRow(BaseModel):
    asset: Optional[Dict[str, object]] = None

    rank: Optional[int] = None
    """Asset visibility rank as a top-level field (ungrouped only)."""

    date: Optional[str] = None

    topic: Optional[DimensionRef] = None

    region: Optional[DimensionRef] = None

    prompt: Optional[DimensionRef] = None

    visibility_score: Optional[float] = None

    average_position: Optional[float] = None

    visibility_rank: Optional[int] = None
    """Asset visibility rank (present on grouped rows)."""

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


class ShoppingBrandsV2Info(BaseModel):
    total_results: Optional[int] = None
    """Total assets matching the query before pagination."""

    count: int
    """Number of assets on this page. When grouped by `date`, `data` holds one row per asset x bucket, so `len(data)` can exceed `count`."""

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
    """Asset scope: `all`, `owned`, or `custom` when `assets` was given."""

    assets: Optional[Union[str, List[str]]] = None
    """Echoed `assets` selection; when set it overrides `scope`."""

    metrics: List[str]
    """Metrics returned per row."""

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


ShoppingStreamBrandsV2V2BrandsStreamPostResponse: TypeAlias = Union[ShoppingBrandsV2Info, ShoppingBrandRow]
