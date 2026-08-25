# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional, Union
from typing_extensions import Literal
from ..._types import SequenceNotStr

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ..._streaming import Stream, AsyncStream
from ...types.reports.shopping_brands_response import ShoppingBrandsResponse
from ...types.reports import (
    shopping_brands_params,
    shopping_stream_brands_params,
    shopping_products_params,
    shopping_stream_products_params,
    shopping_merchants_params,
    shopping_stream_merchants_params,
    shopping_trigger_rate_params,
    shopping_stream_trigger_rate_params,
)
from ...types.reports.shopping_stream_brands_response import ShoppingStreamBrandsResponse
from ...types.reports.shopping_products_response import ShoppingProductsResponse
from ...types.reports.shopping_stream_products_response import ShoppingStreamProductsResponse
from ...types.reports.shopping_merchants_response import ShoppingMerchantsResponse
from ...types.reports.shopping_stream_merchants_response import ShoppingStreamMerchantsResponse
from ...types.reports.shopping_trigger_rate_response import ShoppingTriggerRateResponse
from ...types.reports.shopping_stream_trigger_rate_response import ShoppingStreamTriggerRateResponse

__all__ = ["ShoppingResource", "AsyncShoppingResource"]


class ShoppingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShoppingResourceWithRawResponse:
        return ShoppingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShoppingResourceWithStreamingResponse:
        return ShoppingResourceWithStreamingResponse(self)

    def brands(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "region", "prompt"]] | Omit = omit,
        metrics: Optional[List[Literal["visibility_score", "average_position", "visibility_rank"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        assets: Optional[Union[str, SequenceNotStr[str]]] | Omit = omit,
        filter: Optional[shopping_brands_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            scope: Body parameter.
            assets: Restrict to these asset names (a name or list). Overrides `scope`.
            filter: Body parameter.
            limit: Page size for scope=all; default 10, max 50.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingBrandsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.brands(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
                scope="owned",
            )
            ```
        """
        return self._post(
            "/v2/reports/shopping/brands",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "scope": scope,
                    "assets": assets,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_brands_params.ShoppingBrandsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingBrandsResponse,
        )

    def stream_brands(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "region", "prompt"]] | Omit = omit,
        metrics: Optional[List[Literal["visibility_score", "average_position", "visibility_rank"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        assets: Optional[Union[str, SequenceNotStr[str]]] | Omit = omit,
        filter: Optional[shopping_stream_brands_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            scope: Body parameter.
            assets: Restrict to these asset names (a name or list). Overrides `scope`.
            filter: Body parameter.
            limit: Page size for scope=all; default 10, max 50.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Stream[ShoppingStreamBrandsResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = client.reports.shopping.stream_brands(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
                scope="owned",
            )

            for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/shopping/brands/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "scope": scope,
                    "assets": assets,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_stream_brands_params.ShoppingStreamBrandsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamBrandsResponse,
            stream=True,
            stream_cls=Stream[ShoppingStreamBrandsResponse],
        )

    def products(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "prompt"]] | Omit = omit,
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
        interval: Literal["day", "week", "month"] | Omit = omit,
        include_merchants: bool | Omit = omit,
        target_product: Optional[str] | Omit = omit,
        competitor_limit: int | Omit = omit,
        filter: Optional[shopping_products_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            include_merchants: Include per-product merchant offers (names, prices, urls, images).
            target_product: Return this product plus its top competitors (item view only).
            competitor_limit: Competitors returned when `target_product` is set.
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap streamed rows.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingProductsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.products(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
                include_merchants=False,
                competitor_limit=5,
            )
            ```
        """
        return self._post(
            "/v2/reports/shopping/products",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "include_merchants": include_merchants,
                    "target_product": target_product,
                    "competitor_limit": competitor_limit,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_products_params.ShoppingProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingProductsResponse,
        )

    def stream_products(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "prompt"]] | Omit = omit,
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
        interval: Literal["day", "week", "month"] | Omit = omit,
        include_merchants: bool | Omit = omit,
        target_product: Optional[str] | Omit = omit,
        competitor_limit: int | Omit = omit,
        filter: Optional[shopping_stream_products_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            include_merchants: Include per-product merchant offers (names, prices, urls, images).
            target_product: Return this product plus its top competitors (item view only).
            competitor_limit: Competitors returned when `target_product` is set.
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap streamed rows.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Stream[ShoppingStreamProductsResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = client.reports.shopping.stream_products(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
                include_merchants=False,
                competitor_limit=5,
            )

            for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/shopping/products/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "include_merchants": include_merchants,
                    "target_product": target_product,
                    "competitor_limit": competitor_limit,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_stream_products_params.ShoppingStreamProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamProductsResponse,
            stream=True,
            stream_cls=Stream[ShoppingStreamProductsResponse],
        )

    def merchants(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "brand", "product"]] | Omit = omit,
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
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[shopping_merchants_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: `[]` = distribution; `[brand]` = brand share within each merchant; `[product]` = top products per merchant. `date` (distribution only) adds a time series.
            metrics: Defaults to the chosen view's metrics; must be valid for that view.
            interval: Body parameter.
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap streamed rows.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingMerchantsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.merchants(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
            )
            ```
        """
        return self._post(
            "/v2/reports/shopping/merchants",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_merchants_params.ShoppingMerchantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantsResponse,
        )

    def stream_merchants(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "brand", "product"]] | Omit = omit,
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
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[shopping_stream_merchants_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: `[]` = distribution; `[brand]` = brand share within each merchant; `[product]` = top products per merchant. `date` (distribution only) adds a time series.
            metrics: Defaults to the chosen view's metrics; must be valid for that view.
            interval: Body parameter.
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap streamed rows.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Stream[ShoppingStreamMerchantsResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = client.reports.shopping.stream_merchants(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
            )

            for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/shopping/merchants/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_stream_merchants_params.ShoppingStreamMerchantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamMerchantsResponse,
            stream=True,
            stream_cls=Stream[ShoppingStreamMerchantsResponse],
        )

    def trigger_rate(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "region", "persona", "prompt"]] | Omit = omit,
        metrics: Optional[List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]]]
        | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[shopping_trigger_rate_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Group by `prompt`/`topic` for the per-prompt/-topic trigger rate.
            metrics: Body parameter.
            interval: Body parameter.
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap streamed rows.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingTriggerRateResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.trigger_rate(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
            )
            ```
        """
        return self._post(
            "/v2/reports/shopping/trigger-rate",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_trigger_rate_params.ShoppingTriggerRateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingTriggerRateResponse,
        )

    def stream_trigger_rate(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "region", "persona", "prompt"]] | Omit = omit,
        metrics: Optional[List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]]]
        | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[shopping_stream_trigger_rate_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Group by `prompt`/`topic` for the per-prompt/-topic trigger rate.
            metrics: Body parameter.
            interval: Body parameter.
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap streamed rows.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Stream[ShoppingStreamTriggerRateResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = client.reports.shopping.stream_trigger_rate(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
            )

            for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/shopping/trigger-rate/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_stream_trigger_rate_params.ShoppingStreamTriggerRateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamTriggerRateResponse,
            stream=True,
            stream_cls=Stream[ShoppingStreamTriggerRateResponse],
        )


class AsyncShoppingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShoppingResourceWithRawResponse:
        return AsyncShoppingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShoppingResourceWithStreamingResponse:
        return AsyncShoppingResourceWithStreamingResponse(self)

    async def brands(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "region", "prompt"]] | Omit = omit,
        metrics: Optional[List[Literal["visibility_score", "average_position", "visibility_rank"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        assets: Optional[Union[str, SequenceNotStr[str]]] | Omit = omit,
        filter: Optional[shopping_brands_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            scope: Body parameter.
            assets: Restrict to these asset names (a name or list). Overrides `scope`.
            filter: Body parameter.
            limit: Page size for scope=all; default 10, max 50.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingBrandsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.brands(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
                scope="owned",
            )
            ```
        """
        return await self._post(
            "/v2/reports/shopping/brands",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "scope": scope,
                    "assets": assets,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_brands_params.ShoppingBrandsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingBrandsResponse,
        )

    async def stream_brands(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "region", "prompt"]] | Omit = omit,
        metrics: Optional[List[Literal["visibility_score", "average_position", "visibility_rank"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        assets: Optional[Union[str, SequenceNotStr[str]]] | Omit = omit,
        filter: Optional[shopping_stream_brands_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            scope: Body parameter.
            assets: Restrict to these asset names (a name or list). Overrides `scope`.
            filter: Body parameter.
            limit: Page size for scope=all; default 10, max 50.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncStream[ShoppingStreamBrandsResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = await client.reports.shopping.stream_brands(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
                scope="owned",
            )

            async for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/shopping/brands/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "scope": scope,
                    "assets": assets,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_stream_brands_params.ShoppingStreamBrandsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamBrandsResponse,
            stream=True,
            stream_cls=AsyncStream[ShoppingStreamBrandsResponse],
        )

    async def products(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "prompt"]] | Omit = omit,
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
        interval: Literal["day", "week", "month"] | Omit = omit,
        include_merchants: bool | Omit = omit,
        target_product: Optional[str] | Omit = omit,
        competitor_limit: int | Omit = omit,
        filter: Optional[shopping_products_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            include_merchants: Include per-product merchant offers (names, prices, urls, images).
            target_product: Return this product plus its top competitors (item view only).
            competitor_limit: Competitors returned when `target_product` is set.
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap streamed rows.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingProductsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.products(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
                include_merchants=False,
                competitor_limit=5,
            )
            ```
        """
        return await self._post(
            "/v2/reports/shopping/products",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "include_merchants": include_merchants,
                    "target_product": target_product,
                    "competitor_limit": competitor_limit,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_products_params.ShoppingProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingProductsResponse,
        )

    async def stream_products(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "prompt"]] | Omit = omit,
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
        interval: Literal["day", "week", "month"] | Omit = omit,
        include_merchants: bool | Omit = omit,
        target_product: Optional[str] | Omit = omit,
        competitor_limit: int | Omit = omit,
        filter: Optional[shopping_stream_products_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            include_merchants: Include per-product merchant offers (names, prices, urls, images).
            target_product: Return this product plus its top competitors (item view only).
            competitor_limit: Competitors returned when `target_product` is set.
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap streamed rows.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncStream[ShoppingStreamProductsResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = await client.reports.shopping.stream_products(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
                include_merchants=False,
                competitor_limit=5,
            )

            async for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/shopping/products/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "include_merchants": include_merchants,
                    "target_product": target_product,
                    "competitor_limit": competitor_limit,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_stream_products_params.ShoppingStreamProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamProductsResponse,
            stream=True,
            stream_cls=AsyncStream[ShoppingStreamProductsResponse],
        )

    async def merchants(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "brand", "product"]] | Omit = omit,
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
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[shopping_merchants_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: `[]` = distribution; `[brand]` = brand share within each merchant; `[product]` = top products per merchant. `date` (distribution only) adds a time series.
            metrics: Defaults to the chosen view's metrics; must be valid for that view.
            interval: Body parameter.
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap streamed rows.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingMerchantsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.merchants(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
            )
            ```
        """
        return await self._post(
            "/v2/reports/shopping/merchants",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_merchants_params.ShoppingMerchantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantsResponse,
        )

    async def stream_merchants(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "brand", "product"]] | Omit = omit,
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
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[shopping_stream_merchants_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: `[]` = distribution; `[brand]` = brand share within each merchant; `[product]` = top products per merchant. `date` (distribution only) adds a time series.
            metrics: Defaults to the chosen view's metrics; must be valid for that view.
            interval: Body parameter.
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap streamed rows.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncStream[ShoppingStreamMerchantsResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = await client.reports.shopping.stream_merchants(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
            )

            async for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/shopping/merchants/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_stream_merchants_params.ShoppingStreamMerchantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamMerchantsResponse,
            stream=True,
            stream_cls=AsyncStream[ShoppingStreamMerchantsResponse],
        )

    async def trigger_rate(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "region", "persona", "prompt"]] | Omit = omit,
        metrics: Optional[List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]]]
        | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[shopping_trigger_rate_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Group by `prompt`/`topic` for the per-prompt/-topic trigger rate.
            metrics: Body parameter.
            interval: Body parameter.
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap streamed rows.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingTriggerRateResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.trigger_rate(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
            )
            ```
        """
        return await self._post(
            "/v2/reports/shopping/trigger-rate",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_trigger_rate_params.ShoppingTriggerRateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingTriggerRateResponse,
        )

    async def stream_trigger_rate(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "region", "persona", "prompt"]] | Omit = omit,
        metrics: Optional[List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]]]
        | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[shopping_stream_trigger_rate_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
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
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Group by `prompt`/`topic` for the per-prompt/-topic trigger rate.
            metrics: Body parameter.
            interval: Body parameter.
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap streamed rows.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncStream[ShoppingStreamTriggerRateResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = await client.reports.shopping.stream_trigger_rate(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                interval="day",
            )

            async for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/shopping/trigger-rate/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "metrics": metrics,
                    "interval": interval,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                shopping_stream_trigger_rate_params.ShoppingStreamTriggerRateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamTriggerRateResponse,
            stream=True,
            stream_cls=AsyncStream[ShoppingStreamTriggerRateResponse],
        )


class ShoppingResourceWithRawResponse:
    def __init__(self, shopping: ShoppingResource) -> None:
        self._shopping = shopping

        self.brands = to_raw_response_wrapper(
            shopping.brands,
        )
        self.stream_brands = to_raw_response_wrapper(
            shopping.stream_brands,
        )
        self.products = to_raw_response_wrapper(
            shopping.products,
        )
        self.stream_products = to_raw_response_wrapper(
            shopping.stream_products,
        )
        self.merchants = to_raw_response_wrapper(
            shopping.merchants,
        )
        self.stream_merchants = to_raw_response_wrapper(
            shopping.stream_merchants,
        )
        self.trigger_rate = to_raw_response_wrapper(
            shopping.trigger_rate,
        )
        self.stream_trigger_rate = to_raw_response_wrapper(
            shopping.stream_trigger_rate,
        )


class AsyncShoppingResourceWithRawResponse:
    def __init__(self, shopping: AsyncShoppingResource) -> None:
        self._shopping = shopping

        self.brands = async_to_raw_response_wrapper(
            shopping.brands,
        )
        self.stream_brands = async_to_raw_response_wrapper(
            shopping.stream_brands,
        )
        self.products = async_to_raw_response_wrapper(
            shopping.products,
        )
        self.stream_products = async_to_raw_response_wrapper(
            shopping.stream_products,
        )
        self.merchants = async_to_raw_response_wrapper(
            shopping.merchants,
        )
        self.stream_merchants = async_to_raw_response_wrapper(
            shopping.stream_merchants,
        )
        self.trigger_rate = async_to_raw_response_wrapper(
            shopping.trigger_rate,
        )
        self.stream_trigger_rate = async_to_raw_response_wrapper(
            shopping.stream_trigger_rate,
        )


class ShoppingResourceWithStreamingResponse:
    def __init__(self, shopping: ShoppingResource) -> None:
        self._shopping = shopping

        self.brands = to_streamed_response_wrapper(
            shopping.brands,
        )
        self.stream_brands = to_streamed_response_wrapper(
            shopping.stream_brands,
        )
        self.products = to_streamed_response_wrapper(
            shopping.products,
        )
        self.stream_products = to_streamed_response_wrapper(
            shopping.stream_products,
        )
        self.merchants = to_streamed_response_wrapper(
            shopping.merchants,
        )
        self.stream_merchants = to_streamed_response_wrapper(
            shopping.stream_merchants,
        )
        self.trigger_rate = to_streamed_response_wrapper(
            shopping.trigger_rate,
        )
        self.stream_trigger_rate = to_streamed_response_wrapper(
            shopping.stream_trigger_rate,
        )


class AsyncShoppingResourceWithStreamingResponse:
    def __init__(self, shopping: AsyncShoppingResource) -> None:
        self._shopping = shopping

        self.brands = async_to_streamed_response_wrapper(
            shopping.brands,
        )
        self.stream_brands = async_to_streamed_response_wrapper(
            shopping.stream_brands,
        )
        self.products = async_to_streamed_response_wrapper(
            shopping.products,
        )
        self.stream_products = async_to_streamed_response_wrapper(
            shopping.stream_products,
        )
        self.merchants = async_to_streamed_response_wrapper(
            shopping.merchants,
        )
        self.stream_merchants = async_to_streamed_response_wrapper(
            shopping.stream_merchants,
        )
        self.trigger_rate = async_to_streamed_response_wrapper(
            shopping.trigger_rate,
        )
        self.stream_trigger_rate = async_to_streamed_response_wrapper(
            shopping.stream_trigger_rate,
        )
