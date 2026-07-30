# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.reports import (
    shopping_brands_params,
    shopping_products_params,
    shopping_merchants_params,
    shopping_trigger_rate_params,
    shopping_stream_brands_params,
    shopping_stream_products_params,
    shopping_stream_merchants_params,
    shopping_stream_trigger_rate_params,
)
from ...types.reports.shopping_brands_response import ShoppingBrandsResponse
from ...types.reports.shopping_products_response import ShoppingProductsResponse
from ...types.reports.shopping_merchants_response import ShoppingMerchantsResponse
from ...types.reports.shopping_trigger_rate_response import ShoppingTriggerRateResponse
from ...types.reports.shopping_stream_brands_response import ShoppingStreamBrandsResponse
from ...types.reports.shopping_stream_products_response import ShoppingStreamProductsResponse
from ...types.reports.shopping_stream_merchants_response import ShoppingStreamMerchantsResponse
from ...types.reports.shopping_stream_trigger_rate_response import ShoppingStreamTriggerRateResponse

__all__ = ["ShoppingResource", "AsyncShoppingResource"]


class ShoppingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShoppingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ShoppingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShoppingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return ShoppingResourceWithStreamingResponse(self)

    def brands(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        assets: Union[str, SequenceNotStr[str], None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_brands_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "topic", "region", "prompt"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["visibility_score", "average_position", "visibility_rank"]]] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingBrandsResponse:
        """
        Query Shopping Brands V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          assets: Restrict to these asset names (a name or list). Overrides `scope`.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size for scope=all; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/shopping/brands",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "assets": assets,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "scope": scope,
                },
                shopping_brands_params.ShoppingBrandsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingBrandsResponse,
        )

    def merchants(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_merchants_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "brand", "product"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[
            List[
                Literal[
                    "merchant_share",
                    "merchant_share_rank",
                    "merchant_visibility",
                    "merchant_visibility_rank",
                    "visibility_rank",
                    "brand_share",
                    "product_visibility",
                    "product_rank",
                ]
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantsResponse:
        """
        Query Shopping Merchants V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: `[]` = distribution; `[brand]` = brand share within each merchant; `[product]` =
              top products per merchant. `date` (distribution only) adds a time series.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap streamed rows.

          metrics: Defaults to the chosen view's metrics; must be valid for that view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/shopping/merchants",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                },
                shopping_merchants_params.ShoppingMerchantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantsResponse,
        )

    def products(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        competitor_limit: int | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_products_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "topic", "prompt"]] | Omit = omit,
        include_merchants: bool | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[
            List[
                Literal[
                    "visibility_score",
                    "average_position",
                    "visibility_rank",
                    "position1_percentage",
                    "position2_percentage",
                    "position3_percentage",
                    "position_above3_percentage",
                    "product_rating",
                    "product_num_reviews",
                ]
            ]
        ]
        | Omit = omit,
        target_product: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingProductsResponse:
        """
        Query Shopping Products V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          competitor_limit: Competitors returned when `target_product` is set.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          include_merchants: Include per-product merchant offers (names, prices, urls, images).

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap streamed rows.

          target_product: Return this product plus its top competitors (item view only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/shopping/products",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "competitor_limit": competitor_limit,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "include_merchants": include_merchants,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "target_product": target_product,
                },
                shopping_products_params.ShoppingProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingProductsResponse,
        )

    def stream_brands(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        assets: Union[str, SequenceNotStr[str], None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_stream_brands_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "topic", "region", "prompt"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["visibility_score", "average_position", "visibility_rank"]]] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ShoppingStreamBrandsResponse]:
        """
        Stream Shopping Brands V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          assets: Restrict to these asset names (a name or list). Overrides `scope`.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size for scope=all; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/shopping/brands/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "assets": assets,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "scope": scope,
                },
                shopping_stream_brands_params.ShoppingStreamBrandsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ShoppingStreamBrandsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[ShoppingStreamBrandsResponse],
        )

    def stream_merchants(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_stream_merchants_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "brand", "product"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[
            List[
                Literal[
                    "merchant_share",
                    "merchant_share_rank",
                    "merchant_visibility",
                    "merchant_visibility_rank",
                    "visibility_rank",
                    "brand_share",
                    "product_visibility",
                    "product_rank",
                ]
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ShoppingStreamMerchantsResponse]:
        """
        Stream Shopping Merchants V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: `[]` = distribution; `[brand]` = brand share within each merchant; `[product]` =
              top products per merchant. `date` (distribution only) adds a time series.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap streamed rows.

          metrics: Defaults to the chosen view's metrics; must be valid for that view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/shopping/merchants/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                },
                shopping_stream_merchants_params.ShoppingStreamMerchantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ShoppingStreamMerchantsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[ShoppingStreamMerchantsResponse],
        )

    def stream_products(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        competitor_limit: int | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_stream_products_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "topic", "prompt"]] | Omit = omit,
        include_merchants: bool | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[
            List[
                Literal[
                    "visibility_score",
                    "average_position",
                    "visibility_rank",
                    "position1_percentage",
                    "position2_percentage",
                    "position3_percentage",
                    "position_above3_percentage",
                    "product_rating",
                    "product_num_reviews",
                ]
            ]
        ]
        | Omit = omit,
        target_product: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ShoppingStreamProductsResponse]:
        """
        Stream Shopping Products V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          competitor_limit: Competitors returned when `target_product` is set.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          include_merchants: Include per-product merchant offers (names, prices, urls, images).

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap streamed rows.

          target_product: Return this product plus its top competitors (item view only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/shopping/products/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "competitor_limit": competitor_limit,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "include_merchants": include_merchants,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "target_product": target_product,
                },
                shopping_stream_products_params.ShoppingStreamProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ShoppingStreamProductsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[ShoppingStreamProductsResponse],
        )

    def stream_trigger_rate(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_stream_trigger_rate_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "topic", "region", "persona", "prompt"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ShoppingStreamTriggerRateResponse]:
        """
        Stream Shopping Trigger Rate V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: Group by `prompt`/`topic` for the per-prompt/-topic trigger rate.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap streamed rows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/shopping/trigger-rate/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                },
                shopping_stream_trigger_rate_params.ShoppingStreamTriggerRateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ShoppingStreamTriggerRateResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[ShoppingStreamTriggerRateResponse],
        )

    def trigger_rate(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_trigger_rate_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "topic", "region", "persona", "prompt"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingTriggerRateResponse:
        """
        Query Shopping Trigger Rate V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: Group by `prompt`/`topic` for the per-prompt/-topic trigger rate.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap streamed rows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/shopping/trigger-rate",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                },
                shopping_trigger_rate_params.ShoppingTriggerRateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingTriggerRateResponse,
        )


class AsyncShoppingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShoppingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncShoppingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShoppingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncShoppingResourceWithStreamingResponse(self)

    async def brands(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        assets: Union[str, SequenceNotStr[str], None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_brands_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "topic", "region", "prompt"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["visibility_score", "average_position", "visibility_rank"]]] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingBrandsResponse:
        """
        Query Shopping Brands V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          assets: Restrict to these asset names (a name or list). Overrides `scope`.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size for scope=all; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/shopping/brands",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "assets": assets,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "scope": scope,
                },
                shopping_brands_params.ShoppingBrandsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingBrandsResponse,
        )

    async def merchants(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_merchants_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "brand", "product"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[
            List[
                Literal[
                    "merchant_share",
                    "merchant_share_rank",
                    "merchant_visibility",
                    "merchant_visibility_rank",
                    "visibility_rank",
                    "brand_share",
                    "product_visibility",
                    "product_rank",
                ]
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantsResponse:
        """
        Query Shopping Merchants V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: `[]` = distribution; `[brand]` = brand share within each merchant; `[product]` =
              top products per merchant. `date` (distribution only) adds a time series.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap streamed rows.

          metrics: Defaults to the chosen view's metrics; must be valid for that view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/shopping/merchants",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                },
                shopping_merchants_params.ShoppingMerchantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantsResponse,
        )

    async def products(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        competitor_limit: int | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_products_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "topic", "prompt"]] | Omit = omit,
        include_merchants: bool | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[
            List[
                Literal[
                    "visibility_score",
                    "average_position",
                    "visibility_rank",
                    "position1_percentage",
                    "position2_percentage",
                    "position3_percentage",
                    "position_above3_percentage",
                    "product_rating",
                    "product_num_reviews",
                ]
            ]
        ]
        | Omit = omit,
        target_product: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingProductsResponse:
        """
        Query Shopping Products V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          competitor_limit: Competitors returned when `target_product` is set.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          include_merchants: Include per-product merchant offers (names, prices, urls, images).

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap streamed rows.

          target_product: Return this product plus its top competitors (item view only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/shopping/products",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "competitor_limit": competitor_limit,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "include_merchants": include_merchants,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "target_product": target_product,
                },
                shopping_products_params.ShoppingProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingProductsResponse,
        )

    async def stream_brands(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        assets: Union[str, SequenceNotStr[str], None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_stream_brands_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "topic", "region", "prompt"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["visibility_score", "average_position", "visibility_rank"]]] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ShoppingStreamBrandsResponse]:
        """
        Stream Shopping Brands V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          assets: Restrict to these asset names (a name or list). Overrides `scope`.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size for scope=all; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/shopping/brands/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "assets": assets,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "scope": scope,
                },
                shopping_stream_brands_params.ShoppingStreamBrandsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ShoppingStreamBrandsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[ShoppingStreamBrandsResponse],
        )

    async def stream_merchants(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_stream_merchants_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "brand", "product"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[
            List[
                Literal[
                    "merchant_share",
                    "merchant_share_rank",
                    "merchant_visibility",
                    "merchant_visibility_rank",
                    "visibility_rank",
                    "brand_share",
                    "product_visibility",
                    "product_rank",
                ]
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ShoppingStreamMerchantsResponse]:
        """
        Stream Shopping Merchants V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: `[]` = distribution; `[brand]` = brand share within each merchant; `[product]` =
              top products per merchant. `date` (distribution only) adds a time series.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap streamed rows.

          metrics: Defaults to the chosen view's metrics; must be valid for that view.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/shopping/merchants/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                },
                shopping_stream_merchants_params.ShoppingStreamMerchantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ShoppingStreamMerchantsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[ShoppingStreamMerchantsResponse],
        )

    async def stream_products(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        competitor_limit: int | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_stream_products_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "topic", "prompt"]] | Omit = omit,
        include_merchants: bool | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[
            List[
                Literal[
                    "visibility_score",
                    "average_position",
                    "visibility_rank",
                    "position1_percentage",
                    "position2_percentage",
                    "position3_percentage",
                    "position_above3_percentage",
                    "product_rating",
                    "product_num_reviews",
                ]
            ]
        ]
        | Omit = omit,
        target_product: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ShoppingStreamProductsResponse]:
        """
        Stream Shopping Products V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          competitor_limit: Competitors returned when `target_product` is set.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          include_merchants: Include per-product merchant offers (names, prices, urls, images).

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap streamed rows.

          target_product: Return this product plus its top competitors (item view only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/shopping/products/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "competitor_limit": competitor_limit,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "include_merchants": include_merchants,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "target_product": target_product,
                },
                shopping_stream_products_params.ShoppingStreamProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ShoppingStreamProductsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[ShoppingStreamProductsResponse],
        )

    async def stream_trigger_rate(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_stream_trigger_rate_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "topic", "region", "persona", "prompt"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ShoppingStreamTriggerRateResponse]:
        """
        Stream Shopping Trigger Rate V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: Group by `prompt`/`topic` for the per-prompt/-topic trigger rate.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap streamed rows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/shopping/trigger-rate/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                },
                shopping_stream_trigger_rate_params.ShoppingStreamTriggerRateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ShoppingStreamTriggerRateResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[ShoppingStreamTriggerRateResponse],
        )

    async def trigger_rate(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[shopping_trigger_rate_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "topic", "region", "persona", "prompt"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingTriggerRateResponse:
        """
        Query Shopping Trigger Rate V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: Group by `prompt`/`topic` for the per-prompt/-topic trigger rate.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap streamed rows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/shopping/trigger-rate",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                },
                shopping_trigger_rate_params.ShoppingTriggerRateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingTriggerRateResponse,
        )


class ShoppingResourceWithRawResponse:
    def __init__(self, shopping: ShoppingResource) -> None:
        self._shopping = shopping

        self.brands = to_raw_response_wrapper(
            shopping.brands,
        )
        self.merchants = to_raw_response_wrapper(
            shopping.merchants,
        )
        self.products = to_raw_response_wrapper(
            shopping.products,
        )
        self.stream_brands = to_raw_response_wrapper(
            shopping.stream_brands,
        )
        self.stream_merchants = to_raw_response_wrapper(
            shopping.stream_merchants,
        )
        self.stream_products = to_raw_response_wrapper(
            shopping.stream_products,
        )
        self.stream_trigger_rate = to_raw_response_wrapper(
            shopping.stream_trigger_rate,
        )
        self.trigger_rate = to_raw_response_wrapper(
            shopping.trigger_rate,
        )


class AsyncShoppingResourceWithRawResponse:
    def __init__(self, shopping: AsyncShoppingResource) -> None:
        self._shopping = shopping

        self.brands = async_to_raw_response_wrapper(
            shopping.brands,
        )
        self.merchants = async_to_raw_response_wrapper(
            shopping.merchants,
        )
        self.products = async_to_raw_response_wrapper(
            shopping.products,
        )
        self.stream_brands = async_to_raw_response_wrapper(
            shopping.stream_brands,
        )
        self.stream_merchants = async_to_raw_response_wrapper(
            shopping.stream_merchants,
        )
        self.stream_products = async_to_raw_response_wrapper(
            shopping.stream_products,
        )
        self.stream_trigger_rate = async_to_raw_response_wrapper(
            shopping.stream_trigger_rate,
        )
        self.trigger_rate = async_to_raw_response_wrapper(
            shopping.trigger_rate,
        )


class ShoppingResourceWithStreamingResponse:
    def __init__(self, shopping: ShoppingResource) -> None:
        self._shopping = shopping

        self.brands = to_streamed_response_wrapper(
            shopping.brands,
        )
        self.merchants = to_streamed_response_wrapper(
            shopping.merchants,
        )
        self.products = to_streamed_response_wrapper(
            shopping.products,
        )
        self.stream_brands = to_streamed_response_wrapper(
            shopping.stream_brands,
        )
        self.stream_merchants = to_streamed_response_wrapper(
            shopping.stream_merchants,
        )
        self.stream_products = to_streamed_response_wrapper(
            shopping.stream_products,
        )
        self.stream_trigger_rate = to_streamed_response_wrapper(
            shopping.stream_trigger_rate,
        )
        self.trigger_rate = to_streamed_response_wrapper(
            shopping.trigger_rate,
        )


class AsyncShoppingResourceWithStreamingResponse:
    def __init__(self, shopping: AsyncShoppingResource) -> None:
        self._shopping = shopping

        self.brands = async_to_streamed_response_wrapper(
            shopping.brands,
        )
        self.merchants = async_to_streamed_response_wrapper(
            shopping.merchants,
        )
        self.products = async_to_streamed_response_wrapper(
            shopping.products,
        )
        self.stream_brands = async_to_streamed_response_wrapper(
            shopping.stream_brands,
        )
        self.stream_merchants = async_to_streamed_response_wrapper(
            shopping.stream_merchants,
        )
        self.stream_products = async_to_streamed_response_wrapper(
            shopping.stream_products,
        )
        self.stream_trigger_rate = async_to_streamed_response_wrapper(
            shopping.stream_trigger_rate,
        )
        self.trigger_rate = async_to_streamed_response_wrapper(
            shopping.trigger_rate,
        )
