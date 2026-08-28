# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, TYPE_CHECKING, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ShoppingStreamProductsResponse",
    "ShoppingProductsV2Info",
    "ShoppingProductRow",
    "ShoppingProductRowTopic",
    "ShoppingProductRowPrompt",
]


class ShoppingProductRowPrompt(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class ShoppingProductRowTopic(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class ShoppingProductRow(BaseModel):
    product: Optional[Dict[str, object]] = None

    date: Optional[str] = None

    topic: Optional[ShoppingProductRowTopic] = None

    prompt: Optional[ShoppingProductRowPrompt] = None

    visibility_score: Optional[float] = None

    average_position: Optional[float] = None

    visibility_rank: Optional[int] = None

    position1_percentage: Optional[float] = None

    position2_percentage: Optional[float] = None

    position3_percentage: Optional[float] = None

    position_above3_percentage: Optional[float] = None

    product_rating: Optional[float] = None

    product_num_reviews: Optional[int] = None

    product_url: Optional[str] = None

    product_image_urls: Optional[List[str]] = None

    merchants: Optional[List[Dict[str, object]]] = None
    """Per-product merchant offers `{name, price}` (only with `include_merchants`)."""

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


class ShoppingProductsV2Info(BaseModel):
    total_results: Optional[int] = None
    """Total products matching the query before pagination."""

    count: int
    """Number of products on this page. When grouped by `date`/`topic`/`prompt`, `data` holds one row per product x bucket, so `len(data)` can exceed `count`."""

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

    include_merchants: bool
    """Whether merchant offers are included in each row."""

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


ShoppingStreamProductsResponse: TypeAlias = Union[ShoppingProductsV2Info, ShoppingProductRow]
