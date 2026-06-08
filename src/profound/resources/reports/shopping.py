# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
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
from ..._base_client import make_request_options
from ...types.reports import (
    shopping_executions_params,
    shopping_visibility_params,
    shopping_trigger_rate_params,
    shopping_merchant_share_params,
    shopping_item_visibility_params,
    shopping_merchant_by_items_params,
    shopping_merchant_distribution_params,
    shopping_product_merchant_urls_params,
    shopping_all_items_with_merchants_params,
    shopping_merchant_visibility_by_brand_params,
)
from ...types.shared_params.pagination import Pagination
from ...types.reports.shopping_executions_response import ShoppingExecutionsResponse
from ...types.reports.shopping_visibility_response import ShoppingVisibilityResponse
from ...types.reports.shopping_trigger_rate_response import ShoppingTriggerRateResponse
from ...types.reports.shopping_merchant_share_response import ShoppingMerchantShareResponse
from ...types.reports.shopping_item_visibility_response import ShoppingItemVisibilityResponse
from ...types.reports.shopping_merchant_by_items_response import ShoppingMerchantByItemsResponse
from ...types.reports.shopping_merchant_distribution_response import ShoppingMerchantDistributionResponse
from ...types.reports.shopping_product_merchant_urls_response import ShoppingProductMerchantURLsResponse
from ...types.reports.shopping_all_items_with_merchants_response import ShoppingAllItemsWithMerchantsResponse
from ...types.reports.shopping_merchant_visibility_by_brand_response import ShoppingMerchantVisibilityByBrandResponse

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

    def all_items_with_merchants(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "period",
                "product_name",
                "brand_name",
                "product_url",
                "product_image_urls",
                "product_price",
                "merchant_names",
                "merchant_prices",
            ]
        ]
        | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_all_items_with_merchants_params.Filter] | Omit = omit,
        include_count: bool | Omit = omit,
        include_items: SequenceNotStr[str] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        merchant_filter_type: Literal["any", "all"] | Omit = omit,
        metrics: List[
            Literal[
                "visibility_score",
                "share_of_voice",
                "average_position",
                "visibility_rank",
                "product_rating",
                "product_num_reviews",
                "total_count",
            ]
        ]
        | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        rank_by: Literal["visibility", "average_position", "name"] | Omit = omit,
        search_item: Optional[str] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingAllItemsWithMerchantsResponse:
        """Shopping All Items With Merchants

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/shopping/all-items-with-merchants",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_count": include_count,
                    "include_items": include_items,
                    "include_no_tag": include_no_tag,
                    "merchant_filter_type": merchant_filter_type,
                    "metrics": metrics,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "rank_by": rank_by,
                    "search_item": search_item,
                    "sort_order": sort_order,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_all_items_with_merchants_params.ShoppingAllItemsWithMerchantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingAllItemsWithMerchantsResponse,
        )

    def executions(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        analysis_filter_type: Literal["any", "all"] | Omit = omit,
        analysis_types: List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]] | Omit = omit,
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_executions_params.Filter] | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingExecutionsResponse:
        """Shopping Executions

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/shopping/executions",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "analysis_filter_type": analysis_filter_type,
                    "analysis_types": analysis_types,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_executions_params.ShoppingExecutionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingExecutionsResponse,
        )

    def item_visibility(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        competitor_limit: int | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "period",
                "product_name",
                "brand_name",
                "date",
                "topic_id",
                "prompt_id",
                "prompt",
                "product_url",
                "product_image_urls",
                "product_price",
            ]
        ]
        | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_item_visibility_params.Filter] | Omit = omit,
        include_competitors: bool | Omit = omit,
        include_count: bool | Omit = omit,
        include_items: SequenceNotStr[str] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        include_position_frequency: bool | Omit = omit,
        merchant_filter_type: Literal["any", "all"] | Omit = omit,
        metrics: List[
            Literal[
                "visibility_score",
                "share_of_voice",
                "average_position",
                "visibility_rank",
                "position1_percentage",
                "position2_percentage",
                "position3_percentage",
                "position_above3_percentage",
                "product_rating",
                "product_num_reviews",
                "total_count",
            ]
        ]
        | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        search_item: Optional[str] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        target_product: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingItemVisibilityResponse:
        """Shopping Item Visibility

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/shopping/item-visibility",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "competitor_limit": competitor_limit,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_competitors": include_competitors,
                    "include_count": include_count,
                    "include_items": include_items,
                    "include_no_tag": include_no_tag,
                    "include_position_frequency": include_position_frequency,
                    "merchant_filter_type": merchant_filter_type,
                    "metrics": metrics,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "search_item": search_item,
                    "tag_filter_type": tag_filter_type,
                    "target_product": target_product,
                },
                shopping_item_visibility_params.ShoppingItemVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingItemVisibilityResponse,
        )

    def merchant_by_items(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "period",
                "merchant_name",
                "product_name",
                "brand_name",
                "product_image_urls",
                "product_price",
                "merchant_prices",
                "has_instant_checkout",
                "delivery_options",
                "merchant_url",
            ]
        ]
        | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_merchant_by_items_params.Filter] | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        metrics: List[
            Literal["merchant_visibility", "product_visibility", "product_rank", "avg_position", "total_count"]
        ]
        | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        product_name: Optional[str] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantByItemsResponse:
        """Shopping Merchant By Items

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/shopping/merchant-by-items",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "metrics": metrics,
                    "order_by": order_by,
                    "pagination": pagination,
                    "product_name": product_name,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_merchant_by_items_params.ShoppingMerchantByItemsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantByItemsResponse,
        )

    def merchant_distribution(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["period", "merchant_name", "date", "owned_asset_name"]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_merchant_distribution_params.Filter] | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        metrics: List[
            Literal["offer_count", "product_count", "average_rank", "share_of_offers", "visibility_rank", "total_count"]
        ]
        | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        search_merchant: Optional[str] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantDistributionResponse:
        """Shopping Merchant Distribution

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/shopping/merchant-distribution",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "metrics": metrics,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "search_merchant": search_merchant,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_merchant_distribution_params.ShoppingMerchantDistributionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantDistributionResponse,
        )

    def merchant_share(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["period", "topic_id", "prompt_id"]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_merchant_share_params.Filter] | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        metrics: List[Literal["merchant_share"]] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        target_asset_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantShareResponse:
        """Shopping Merchant Share

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/shopping/merchant-share",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "metrics": metrics,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "tag_filter_type": tag_filter_type,
                    "target_asset_names": target_asset_names,
                },
                shopping_merchant_share_params.ShoppingMerchantShareParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantShareResponse,
        )

    def merchant_visibility_by_brand(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["period", "merchant_name", "brand_name"]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_merchant_visibility_by_brand_params.Filter] | Omit = omit,
        include_brand: Optional[str] | Omit = omit,
        include_brand_only: bool | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        metrics: List[
            Literal["visibility_score", "share_of_voice", "average_position", "visibility_rank", "total_count"]
        ]
        | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        search_brand: Optional[str] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantVisibilityByBrandResponse:
        """Shopping Merchant Visibility By Brand

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/shopping/merchant-visibility-by-brand",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_brand": include_brand,
                    "include_brand_only": include_brand_only,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "metrics": metrics,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "search_brand": search_brand,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_merchant_visibility_by_brand_params.ShoppingMerchantVisibilityByBrandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantVisibilityByBrandResponse,
        )

    def product_merchant_urls(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        product_names: SequenceNotStr[str],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingProductMerchantURLsResponse:
        """
        Shopping Product Merchant Urls

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/shopping/product-merchant-urls",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "product_names": product_names,
                    "start_date": start_date,
                },
                shopping_product_merchant_urls_params.ShoppingProductMerchantURLsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingProductMerchantURLsResponse,
        )

    def trigger_rate(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal["period", "date", "model_id", "topic_id", "region_id", "persona_id", "prompt_id", "prompt"]
        ]
        | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_trigger_rate_params.Filter] | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        metrics: List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingTriggerRateResponse:
        """Shopping Trigger Rate

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/shopping/trigger-rate",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "metrics": metrics,
                    "order_by": order_by,
                    "pagination": pagination,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_trigger_rate_params.ShoppingTriggerRateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingTriggerRateResponse,
        )

    def visibility(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal["period", "asset_name", "date", "model_id", "topic_id", "region_id", "prompt_id", "prompt"]
        ]
        | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_visibility_params.Filter] | Omit = omit,
        include_asset: Optional[str] | Omit = omit,
        include_asset_only: bool | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        include_position_frequency: bool | Omit = omit,
        metrics: List[
            Literal[
                "visibility_score",
                "share_of_voice",
                "average_position",
                "visibility_rank",
                "average_position_rank",
                "position1_percentage",
                "position2_percentage",
                "position3_percentage",
                "position_above3_percentage",
                "total_count",
            ]
        ]
        | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        rank_by: Literal["visibility_score", "average_position"] | Omit = omit,
        search_asset: Optional[str] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingVisibilityResponse:
        """Shopping Visibility

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/shopping/visibility",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_asset": include_asset,
                    "include_asset_only": include_asset_only,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "include_position_frequency": include_position_frequency,
                    "metrics": metrics,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "rank_by": rank_by,
                    "search_asset": search_asset,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_visibility_params.ShoppingVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingVisibilityResponse,
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

    async def all_items_with_merchants(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "period",
                "product_name",
                "brand_name",
                "product_url",
                "product_image_urls",
                "product_price",
                "merchant_names",
                "merchant_prices",
            ]
        ]
        | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_all_items_with_merchants_params.Filter] | Omit = omit,
        include_count: bool | Omit = omit,
        include_items: SequenceNotStr[str] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        merchant_filter_type: Literal["any", "all"] | Omit = omit,
        metrics: List[
            Literal[
                "visibility_score",
                "share_of_voice",
                "average_position",
                "visibility_rank",
                "product_rating",
                "product_num_reviews",
                "total_count",
            ]
        ]
        | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        rank_by: Literal["visibility", "average_position", "name"] | Omit = omit,
        search_item: Optional[str] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingAllItemsWithMerchantsResponse:
        """Shopping All Items With Merchants

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/shopping/all-items-with-merchants",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_count": include_count,
                    "include_items": include_items,
                    "include_no_tag": include_no_tag,
                    "merchant_filter_type": merchant_filter_type,
                    "metrics": metrics,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "rank_by": rank_by,
                    "search_item": search_item,
                    "sort_order": sort_order,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_all_items_with_merchants_params.ShoppingAllItemsWithMerchantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingAllItemsWithMerchantsResponse,
        )

    async def executions(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        analysis_filter_type: Literal["any", "all"] | Omit = omit,
        analysis_types: List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]] | Omit = omit,
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_executions_params.Filter] | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingExecutionsResponse:
        """Shopping Executions

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/shopping/executions",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "analysis_filter_type": analysis_filter_type,
                    "analysis_types": analysis_types,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_executions_params.ShoppingExecutionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingExecutionsResponse,
        )

    async def item_visibility(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        competitor_limit: int | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "period",
                "product_name",
                "brand_name",
                "date",
                "topic_id",
                "prompt_id",
                "prompt",
                "product_url",
                "product_image_urls",
                "product_price",
            ]
        ]
        | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_item_visibility_params.Filter] | Omit = omit,
        include_competitors: bool | Omit = omit,
        include_count: bool | Omit = omit,
        include_items: SequenceNotStr[str] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        include_position_frequency: bool | Omit = omit,
        merchant_filter_type: Literal["any", "all"] | Omit = omit,
        metrics: List[
            Literal[
                "visibility_score",
                "share_of_voice",
                "average_position",
                "visibility_rank",
                "position1_percentage",
                "position2_percentage",
                "position3_percentage",
                "position_above3_percentage",
                "product_rating",
                "product_num_reviews",
                "total_count",
            ]
        ]
        | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        search_item: Optional[str] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        target_product: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingItemVisibilityResponse:
        """Shopping Item Visibility

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/shopping/item-visibility",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "competitor_limit": competitor_limit,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_competitors": include_competitors,
                    "include_count": include_count,
                    "include_items": include_items,
                    "include_no_tag": include_no_tag,
                    "include_position_frequency": include_position_frequency,
                    "merchant_filter_type": merchant_filter_type,
                    "metrics": metrics,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "search_item": search_item,
                    "tag_filter_type": tag_filter_type,
                    "target_product": target_product,
                },
                shopping_item_visibility_params.ShoppingItemVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingItemVisibilityResponse,
        )

    async def merchant_by_items(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "period",
                "merchant_name",
                "product_name",
                "brand_name",
                "product_image_urls",
                "product_price",
                "merchant_prices",
                "has_instant_checkout",
                "delivery_options",
                "merchant_url",
            ]
        ]
        | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_merchant_by_items_params.Filter] | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        metrics: List[
            Literal["merchant_visibility", "product_visibility", "product_rank", "avg_position", "total_count"]
        ]
        | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        product_name: Optional[str] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantByItemsResponse:
        """Shopping Merchant By Items

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/shopping/merchant-by-items",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "metrics": metrics,
                    "order_by": order_by,
                    "pagination": pagination,
                    "product_name": product_name,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_merchant_by_items_params.ShoppingMerchantByItemsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantByItemsResponse,
        )

    async def merchant_distribution(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["period", "merchant_name", "date", "owned_asset_name"]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_merchant_distribution_params.Filter] | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        metrics: List[
            Literal["offer_count", "product_count", "average_rank", "share_of_offers", "visibility_rank", "total_count"]
        ]
        | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        search_merchant: Optional[str] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantDistributionResponse:
        """Shopping Merchant Distribution

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/shopping/merchant-distribution",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "metrics": metrics,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "search_merchant": search_merchant,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_merchant_distribution_params.ShoppingMerchantDistributionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantDistributionResponse,
        )

    async def merchant_share(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["period", "topic_id", "prompt_id"]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_merchant_share_params.Filter] | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        metrics: List[Literal["merchant_share"]] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        target_asset_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantShareResponse:
        """Shopping Merchant Share

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/shopping/merchant-share",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "metrics": metrics,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "tag_filter_type": tag_filter_type,
                    "target_asset_names": target_asset_names,
                },
                shopping_merchant_share_params.ShoppingMerchantShareParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantShareResponse,
        )

    async def merchant_visibility_by_brand(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["period", "merchant_name", "brand_name"]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_merchant_visibility_by_brand_params.Filter] | Omit = omit,
        include_brand: Optional[str] | Omit = omit,
        include_brand_only: bool | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        metrics: List[
            Literal["visibility_score", "share_of_voice", "average_position", "visibility_rank", "total_count"]
        ]
        | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        search_brand: Optional[str] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantVisibilityByBrandResponse:
        """Shopping Merchant Visibility By Brand

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/shopping/merchant-visibility-by-brand",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_brand": include_brand,
                    "include_brand_only": include_brand_only,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "metrics": metrics,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "search_brand": search_brand,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_merchant_visibility_by_brand_params.ShoppingMerchantVisibilityByBrandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantVisibilityByBrandResponse,
        )

    async def product_merchant_urls(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        product_names: SequenceNotStr[str],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingProductMerchantURLsResponse:
        """
        Shopping Product Merchant Urls

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/shopping/product-merchant-urls",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "product_names": product_names,
                    "start_date": start_date,
                },
                shopping_product_merchant_urls_params.ShoppingProductMerchantURLsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingProductMerchantURLsResponse,
        )

    async def trigger_rate(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal["period", "date", "model_id", "topic_id", "region_id", "persona_id", "prompt_id", "prompt"]
        ]
        | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_trigger_rate_params.Filter] | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        metrics: List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingTriggerRateResponse:
        """Shopping Trigger Rate

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/shopping/trigger-rate",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "metrics": metrics,
                    "order_by": order_by,
                    "pagination": pagination,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_trigger_rate_params.ShoppingTriggerRateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingTriggerRateResponse,
        )

    async def visibility(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal["period", "asset_name", "date", "model_id", "topic_id", "region_id", "prompt_id", "prompt"]
        ]
        | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        filters: Iterable[shopping_visibility_params.Filter] | Omit = omit,
        include_asset: Optional[str] | Omit = omit,
        include_asset_only: bool | Omit = omit,
        include_count: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        include_position_frequency: bool | Omit = omit,
        metrics: List[
            Literal[
                "visibility_score",
                "share_of_voice",
                "average_position",
                "visibility_rank",
                "average_position_rank",
                "position1_percentage",
                "position2_percentage",
                "position3_percentage",
                "position_above3_percentage",
                "total_count",
            ]
        ]
        | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        rank_by: Literal["visibility_score", "average_position"] | Omit = omit,
        search_asset: Optional[str] | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingVisibilityResponse:
        """Shopping Visibility

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/shopping/visibility",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "exclude_topic_ids": exclude_topic_ids,
                    "filters": filters,
                    "include_asset": include_asset,
                    "include_asset_only": include_asset_only,
                    "include_count": include_count,
                    "include_no_tag": include_no_tag,
                    "include_position_frequency": include_position_frequency,
                    "metrics": metrics,
                    "order_by": order_by,
                    "owned_asset_names": owned_asset_names,
                    "pagination": pagination,
                    "rank_by": rank_by,
                    "search_asset": search_asset,
                    "tag_filter_type": tag_filter_type,
                },
                shopping_visibility_params.ShoppingVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingVisibilityResponse,
        )


class ShoppingResourceWithRawResponse:
    def __init__(self, shopping: ShoppingResource) -> None:
        self._shopping = shopping

        self.all_items_with_merchants = to_raw_response_wrapper(
            shopping.all_items_with_merchants,
        )
        self.executions = to_raw_response_wrapper(
            shopping.executions,
        )
        self.item_visibility = to_raw_response_wrapper(
            shopping.item_visibility,
        )
        self.merchant_by_items = to_raw_response_wrapper(
            shopping.merchant_by_items,
        )
        self.merchant_distribution = to_raw_response_wrapper(
            shopping.merchant_distribution,
        )
        self.merchant_share = to_raw_response_wrapper(
            shopping.merchant_share,
        )
        self.merchant_visibility_by_brand = to_raw_response_wrapper(
            shopping.merchant_visibility_by_brand,
        )
        self.product_merchant_urls = to_raw_response_wrapper(
            shopping.product_merchant_urls,
        )
        self.trigger_rate = to_raw_response_wrapper(
            shopping.trigger_rate,
        )
        self.visibility = to_raw_response_wrapper(
            shopping.visibility,
        )


class AsyncShoppingResourceWithRawResponse:
    def __init__(self, shopping: AsyncShoppingResource) -> None:
        self._shopping = shopping

        self.all_items_with_merchants = async_to_raw_response_wrapper(
            shopping.all_items_with_merchants,
        )
        self.executions = async_to_raw_response_wrapper(
            shopping.executions,
        )
        self.item_visibility = async_to_raw_response_wrapper(
            shopping.item_visibility,
        )
        self.merchant_by_items = async_to_raw_response_wrapper(
            shopping.merchant_by_items,
        )
        self.merchant_distribution = async_to_raw_response_wrapper(
            shopping.merchant_distribution,
        )
        self.merchant_share = async_to_raw_response_wrapper(
            shopping.merchant_share,
        )
        self.merchant_visibility_by_brand = async_to_raw_response_wrapper(
            shopping.merchant_visibility_by_brand,
        )
        self.product_merchant_urls = async_to_raw_response_wrapper(
            shopping.product_merchant_urls,
        )
        self.trigger_rate = async_to_raw_response_wrapper(
            shopping.trigger_rate,
        )
        self.visibility = async_to_raw_response_wrapper(
            shopping.visibility,
        )


class ShoppingResourceWithStreamingResponse:
    def __init__(self, shopping: ShoppingResource) -> None:
        self._shopping = shopping

        self.all_items_with_merchants = to_streamed_response_wrapper(
            shopping.all_items_with_merchants,
        )
        self.executions = to_streamed_response_wrapper(
            shopping.executions,
        )
        self.item_visibility = to_streamed_response_wrapper(
            shopping.item_visibility,
        )
        self.merchant_by_items = to_streamed_response_wrapper(
            shopping.merchant_by_items,
        )
        self.merchant_distribution = to_streamed_response_wrapper(
            shopping.merchant_distribution,
        )
        self.merchant_share = to_streamed_response_wrapper(
            shopping.merchant_share,
        )
        self.merchant_visibility_by_brand = to_streamed_response_wrapper(
            shopping.merchant_visibility_by_brand,
        )
        self.product_merchant_urls = to_streamed_response_wrapper(
            shopping.product_merchant_urls,
        )
        self.trigger_rate = to_streamed_response_wrapper(
            shopping.trigger_rate,
        )
        self.visibility = to_streamed_response_wrapper(
            shopping.visibility,
        )


class AsyncShoppingResourceWithStreamingResponse:
    def __init__(self, shopping: AsyncShoppingResource) -> None:
        self._shopping = shopping

        self.all_items_with_merchants = async_to_streamed_response_wrapper(
            shopping.all_items_with_merchants,
        )
        self.executions = async_to_streamed_response_wrapper(
            shopping.executions,
        )
        self.item_visibility = async_to_streamed_response_wrapper(
            shopping.item_visibility,
        )
        self.merchant_by_items = async_to_streamed_response_wrapper(
            shopping.merchant_by_items,
        )
        self.merchant_distribution = async_to_streamed_response_wrapper(
            shopping.merchant_distribution,
        )
        self.merchant_share = async_to_streamed_response_wrapper(
            shopping.merchant_share,
        )
        self.merchant_visibility_by_brand = async_to_streamed_response_wrapper(
            shopping.merchant_visibility_by_brand,
        )
        self.product_merchant_urls = async_to_streamed_response_wrapper(
            shopping.product_merchant_urls,
        )
        self.trigger_rate = async_to_streamed_response_wrapper(
            shopping.trigger_rate,
        )
        self.visibility = async_to_streamed_response_wrapper(
            shopping.visibility,
        )
