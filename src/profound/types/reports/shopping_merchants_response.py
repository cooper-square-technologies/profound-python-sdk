# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ShoppingMerchantsResponse", "Data", "Info"]


class Data(BaseModel):
    """One merchant row.

    `brand_name`/`brand_share` appear in the brand-share view; `product`/product
    metrics in the top-products view; metrics vary by view.
    """

    brand_name: Optional[str] = None

    brand_share: Optional[float] = None

    date: Optional[str] = None

    merchant_name: Optional[str] = None

    merchant_share: Optional[float] = None

    merchant_share_rank: Optional[int] = None

    merchant_visibility: Optional[float] = None

    merchant_visibility_rank: Optional[int] = None

    product: Optional[Dict[str, object]] = None

    product_rank: Optional[int] = None

    product_visibility: Optional[float] = None

    visibility_rank: Optional[int] = None

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

    metrics: List[str]
    """Metrics returned per row."""

    models: List[str]
    """Display names of the models the report covers."""

    start_date: str
    """Echoed request start date (YYYY-MM-DD, ET)."""

    view: str
    """`distribution`, `brand_share`, or `top_products`."""

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


class ShoppingMerchantsResponse(BaseModel):
    data: List[Data]

    info: Info
