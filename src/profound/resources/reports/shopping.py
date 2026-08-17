# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, Iterable, List, Optional, Union
from datetime import datetime
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
from ...types.reports.shopping_visibility_response import ShoppingVisibilityResponse
from ...types.shared_params.pagination import Pagination
from ...types.reports import (
    shopping_visibility_params,
    shopping_item_visibility_params,
    shopping_merchant_distribution_params,
    shopping_merchant_visibility_by_brand_params,
    shopping_merchant_by_items_params,
    shopping_all_items_with_merchants_params,
    shopping_trigger_rate_params,
    shopping_merchant_share_params,
    shopping_product_merchant_urls_params,
    shopping_executions_params,
)
from ...types.reports.shopping_item_visibility_response import ShoppingItemVisibilityResponse
from ...types.reports.shopping_merchant_distribution_response import ShoppingMerchantDistributionResponse
from ...types.reports.shopping_merchant_visibility_by_brand_response import ShoppingMerchantVisibilityByBrandResponse
from ...types.reports.shopping_merchant_by_items_response import ShoppingMerchantByItemsResponse
from ...types.reports.shopping_all_items_with_merchants_response import ShoppingAllItemsWithMerchantsResponse
from ...types.reports.shopping_trigger_rate_response import ShoppingTriggerRateResponse
from ...types.reports.shopping_merchant_share_response import ShoppingMerchantShareResponse
from ...types.reports.shopping_product_merchant_urls_response import ShoppingProductMerchantURLsResponse
from ...types.reports.shopping_executions_response import ShoppingExecutionsResponse

__all__ = ["ShoppingResource", "AsyncShoppingResource"]


class ShoppingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShoppingResourceWithRawResponse:
        return ShoppingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShoppingResourceWithStreamingResponse:
        return ShoppingResourceWithStreamingResponse(self)

    def visibility(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_visibility_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        dimensions: List[
            Literal["period", "asset_name", "date", "model_id", "topic_id", "region_id", "prompt_id", "prompt"]
        ]
        | Omit = omit,
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
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        search_asset: Optional[str] | Omit = omit,
        include_asset: Optional[str] | Omit = omit,
        include_asset_only: bool | Omit = omit,
        include_assets_only: SequenceNotStr[str] | Omit = omit,
        rank_by: Literal["visibility_score", "average_position"] | Omit = omit,
        include_position_frequency: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingVisibilityResponse:
        """
        Shopping Visibility

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            owned_asset_names: Body parameter.
            search_asset: Body parameter.
            include_asset: Body parameter.
            include_asset_only: Body parameter.
            include_assets_only: Body parameter.
            rank_by: Body parameter.
            include_position_frequency: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingVisibilityResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.visibility(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
                include_asset_only=False,
                rank_by="visibility_score",
                include_position_frequency=False,
            )
            ```
        """
        return self._post(
            "/v1/reports/shopping/visibility",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "owned_asset_names": owned_asset_names,
                    "search_asset": search_asset,
                    "include_asset": include_asset,
                    "include_asset_only": include_asset_only,
                    "include_assets_only": include_assets_only,
                    "rank_by": rank_by,
                    "include_position_frequency": include_position_frequency,
                },
                shopping_visibility_params.ShoppingVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingVisibilityResponse,
        )

    def item_visibility(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_item_visibility_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        dimensions: List[
            Literal[
                "period",
                "product_key",
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
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        include_items: SequenceNotStr[str] | Omit = omit,
        search_item: Optional[str] | Omit = omit,
        merchant_filter_type: Literal["any", "all"] | Omit = omit,
        include_competitors: bool | Omit = omit,
        target_product: Optional[str] | Omit = omit,
        competitor_limit: int | Omit = omit,
        include_position_frequency: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingItemVisibilityResponse:
        """
        Shopping Item Visibility

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            owned_asset_names: Body parameter.
            include_items: Body parameter.
            search_item: Body parameter.
            merchant_filter_type: Body parameter.
            include_competitors: Body parameter.
            target_product: Body parameter.
            competitor_limit: Body parameter.
            include_position_frequency: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingItemVisibilityResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.item_visibility(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
                merchant_filter_type="any",
                include_competitors=False,
                competitor_limit=5,
                include_position_frequency=False,
            )
            ```
        """
        return self._post(
            "/v1/reports/shopping/item-visibility",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "owned_asset_names": owned_asset_names,
                    "include_items": include_items,
                    "search_item": search_item,
                    "merchant_filter_type": merchant_filter_type,
                    "include_competitors": include_competitors,
                    "target_product": target_product,
                    "competitor_limit": competitor_limit,
                    "include_position_frequency": include_position_frequency,
                },
                shopping_item_visibility_params.ShoppingItemVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingItemVisibilityResponse,
        )

    def merchant_distribution(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_distribution_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        dimensions: List[Literal["period", "merchant_name", "date", "owned_asset_name"]] | Omit = omit,
        metrics: List[
            Literal["offer_count", "product_count", "average_rank", "share_of_offers", "visibility_rank", "total_count"]
        ]
        | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        search_merchant: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantDistributionResponse:
        """
        Shopping Merchant Distribution

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            owned_asset_names: Body parameter.
            search_merchant: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingMerchantDistributionResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.merchant_distribution(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
            )
            ```
        """
        return self._post(
            "/v1/reports/shopping/merchant-distribution",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "owned_asset_names": owned_asset_names,
                    "search_merchant": search_merchant,
                },
                shopping_merchant_distribution_params.ShoppingMerchantDistributionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantDistributionResponse,
        )

    def merchant_visibility_by_brand(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_visibility_by_brand_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        dimensions: List[Literal["period", "merchant_name", "brand_name"]] | Omit = omit,
        metrics: List[
            Literal["visibility_score", "share_of_voice", "average_position", "visibility_rank", "total_count"]
        ]
        | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        search_brand: Optional[str] | Omit = omit,
        include_brand: Optional[str] | Omit = omit,
        include_brand_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantVisibilityByBrandResponse:
        """
        Shopping Merchant Visibility By Brand

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            owned_asset_names: Body parameter.
            search_brand: Body parameter.
            include_brand: Body parameter.
            include_brand_only: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingMerchantVisibilityByBrandResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.merchant_visibility_by_brand(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
                include_brand_only=False,
            )
            ```
        """
        return self._post(
            "/v1/reports/shopping/merchant-visibility-by-brand",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "owned_asset_names": owned_asset_names,
                    "search_brand": search_brand,
                    "include_brand": include_brand,
                    "include_brand_only": include_brand_only,
                },
                shopping_merchant_visibility_by_brand_params.ShoppingMerchantVisibilityByBrandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantVisibilityByBrandResponse,
        )

    def merchant_by_items(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_by_items_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
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
        metrics: List[
            Literal["merchant_visibility", "product_visibility", "product_rank", "avg_position", "total_count"]
        ]
        | Omit = omit,
        product_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantByItemsResponse:
        """
        Shopping Merchant By Items

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            product_name: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingMerchantByItemsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.merchant_by_items(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
            )
            ```
        """
        return self._post(
            "/v1/reports/shopping/merchant-by-items",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "product_name": product_name,
                },
                shopping_merchant_by_items_params.ShoppingMerchantByItemsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantByItemsResponse,
        )

    def all_items_with_merchants(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_all_items_with_merchants_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
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
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        include_items: SequenceNotStr[str] | Omit = omit,
        search_item: Optional[str] | Omit = omit,
        merchant_filter_type: Literal["any", "all"] | Omit = omit,
        rank_by: Literal["visibility", "average_position", "name"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingAllItemsWithMerchantsResponse:
        """
        Shopping All Items With Merchants

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            owned_asset_names: Body parameter.
            include_items: Body parameter.
            search_item: Body parameter.
            merchant_filter_type: Body parameter.
            rank_by: Body parameter.
            sort_order: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingAllItemsWithMerchantsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.all_items_with_merchants(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
                merchant_filter_type="any",
                rank_by="visibility",
                sort_order="desc",
            )
            ```
        """
        return self._post(
            "/v1/reports/shopping/all-items-with-merchants",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "owned_asset_names": owned_asset_names,
                    "include_items": include_items,
                    "search_item": search_item,
                    "merchant_filter_type": merchant_filter_type,
                    "rank_by": rank_by,
                    "sort_order": sort_order,
                },
                shopping_all_items_with_merchants_params.ShoppingAllItemsWithMerchantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingAllItemsWithMerchantsResponse,
        )

    def trigger_rate(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_trigger_rate_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        dimensions: List[
            Literal["period", "date", "model_id", "topic_id", "region_id", "persona_id", "prompt_id", "prompt"]
        ]
        | Omit = omit,
        metrics: List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingTriggerRateResponse:
        """
        Shopping Trigger Rate

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
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
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
            )
            ```
        """
        return self._post(
            "/v1/reports/shopping/trigger-rate",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                },
                shopping_trigger_rate_params.ShoppingTriggerRateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingTriggerRateResponse,
        )

    def merchant_share(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_share_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        dimensions: List[Literal["period", "topic_id", "prompt_id"]] | Omit = omit,
        metrics: List[Literal["merchant_share"]] | Omit = omit,
        target_asset_names: SequenceNotStr[str] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantShareResponse:
        """
        Shopping Merchant Share

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            target_asset_names: Body parameter.
            owned_asset_names: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingMerchantShareResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.merchant_share(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
            )
            ```
        """
        return self._post(
            "/v1/reports/shopping/merchant-share",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "target_asset_names": target_asset_names,
                    "owned_asset_names": owned_asset_names,
                },
                shopping_merchant_share_params.ShoppingMerchantShareParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantShareResponse,
        )

    def product_merchant_urls(
        self,
        *,
        category_id: str,
        product_names: SequenceNotStr[str],
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
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
            category_id: Body parameter.
            product_names: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingProductMerchantURLsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.product_merchant_urls(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                product_names=[],
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )
            ```
        """
        return self._post(
            "/v1/reports/shopping/product-merchant-urls",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "product_names": product_names,
                    "start_date": start_date,
                    "end_date": end_date,
                },
                shopping_product_merchant_urls_params.ShoppingProductMerchantURLsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingProductMerchantURLsResponse,
        )

    def executions(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_executions_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        analysis_types: List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]] | Omit = omit,
        analysis_filter_type: Literal["any", "all"] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingExecutionsResponse:
        """
        Shopping Executions

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            analysis_types: Body parameter.
            analysis_filter_type: Body parameter.
            owned_asset_names: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingExecutionsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.executions(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
                analysis_filter_type="any",
            )
            ```
        """
        return self._post(
            "/v1/reports/shopping/executions",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "analysis_types": analysis_types,
                    "analysis_filter_type": analysis_filter_type,
                    "owned_asset_names": owned_asset_names,
                },
                shopping_executions_params.ShoppingExecutionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingExecutionsResponse,
        )


class AsyncShoppingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShoppingResourceWithRawResponse:
        return AsyncShoppingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShoppingResourceWithStreamingResponse:
        return AsyncShoppingResourceWithStreamingResponse(self)

    async def visibility(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_visibility_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        dimensions: List[
            Literal["period", "asset_name", "date", "model_id", "topic_id", "region_id", "prompt_id", "prompt"]
        ]
        | Omit = omit,
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
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        search_asset: Optional[str] | Omit = omit,
        include_asset: Optional[str] | Omit = omit,
        include_asset_only: bool | Omit = omit,
        include_assets_only: SequenceNotStr[str] | Omit = omit,
        rank_by: Literal["visibility_score", "average_position"] | Omit = omit,
        include_position_frequency: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingVisibilityResponse:
        """
        Shopping Visibility

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            owned_asset_names: Body parameter.
            search_asset: Body parameter.
            include_asset: Body parameter.
            include_asset_only: Body parameter.
            include_assets_only: Body parameter.
            rank_by: Body parameter.
            include_position_frequency: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingVisibilityResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.visibility(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
                include_asset_only=False,
                rank_by="visibility_score",
                include_position_frequency=False,
            )
            ```
        """
        return await self._post(
            "/v1/reports/shopping/visibility",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "owned_asset_names": owned_asset_names,
                    "search_asset": search_asset,
                    "include_asset": include_asset,
                    "include_asset_only": include_asset_only,
                    "include_assets_only": include_assets_only,
                    "rank_by": rank_by,
                    "include_position_frequency": include_position_frequency,
                },
                shopping_visibility_params.ShoppingVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingVisibilityResponse,
        )

    async def item_visibility(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_item_visibility_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        dimensions: List[
            Literal[
                "period",
                "product_key",
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
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        include_items: SequenceNotStr[str] | Omit = omit,
        search_item: Optional[str] | Omit = omit,
        merchant_filter_type: Literal["any", "all"] | Omit = omit,
        include_competitors: bool | Omit = omit,
        target_product: Optional[str] | Omit = omit,
        competitor_limit: int | Omit = omit,
        include_position_frequency: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingItemVisibilityResponse:
        """
        Shopping Item Visibility

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            owned_asset_names: Body parameter.
            include_items: Body parameter.
            search_item: Body parameter.
            merchant_filter_type: Body parameter.
            include_competitors: Body parameter.
            target_product: Body parameter.
            competitor_limit: Body parameter.
            include_position_frequency: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingItemVisibilityResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.item_visibility(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
                merchant_filter_type="any",
                include_competitors=False,
                competitor_limit=5,
                include_position_frequency=False,
            )
            ```
        """
        return await self._post(
            "/v1/reports/shopping/item-visibility",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "owned_asset_names": owned_asset_names,
                    "include_items": include_items,
                    "search_item": search_item,
                    "merchant_filter_type": merchant_filter_type,
                    "include_competitors": include_competitors,
                    "target_product": target_product,
                    "competitor_limit": competitor_limit,
                    "include_position_frequency": include_position_frequency,
                },
                shopping_item_visibility_params.ShoppingItemVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingItemVisibilityResponse,
        )

    async def merchant_distribution(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_distribution_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        dimensions: List[Literal["period", "merchant_name", "date", "owned_asset_name"]] | Omit = omit,
        metrics: List[
            Literal["offer_count", "product_count", "average_rank", "share_of_offers", "visibility_rank", "total_count"]
        ]
        | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        search_merchant: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantDistributionResponse:
        """
        Shopping Merchant Distribution

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            owned_asset_names: Body parameter.
            search_merchant: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingMerchantDistributionResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.merchant_distribution(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
            )
            ```
        """
        return await self._post(
            "/v1/reports/shopping/merchant-distribution",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "owned_asset_names": owned_asset_names,
                    "search_merchant": search_merchant,
                },
                shopping_merchant_distribution_params.ShoppingMerchantDistributionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantDistributionResponse,
        )

    async def merchant_visibility_by_brand(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_visibility_by_brand_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        dimensions: List[Literal["period", "merchant_name", "brand_name"]] | Omit = omit,
        metrics: List[
            Literal["visibility_score", "share_of_voice", "average_position", "visibility_rank", "total_count"]
        ]
        | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        search_brand: Optional[str] | Omit = omit,
        include_brand: Optional[str] | Omit = omit,
        include_brand_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantVisibilityByBrandResponse:
        """
        Shopping Merchant Visibility By Brand

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            owned_asset_names: Body parameter.
            search_brand: Body parameter.
            include_brand: Body parameter.
            include_brand_only: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingMerchantVisibilityByBrandResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.merchant_visibility_by_brand(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
                include_brand_only=False,
            )
            ```
        """
        return await self._post(
            "/v1/reports/shopping/merchant-visibility-by-brand",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "owned_asset_names": owned_asset_names,
                    "search_brand": search_brand,
                    "include_brand": include_brand,
                    "include_brand_only": include_brand_only,
                },
                shopping_merchant_visibility_by_brand_params.ShoppingMerchantVisibilityByBrandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantVisibilityByBrandResponse,
        )

    async def merchant_by_items(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_by_items_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
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
        metrics: List[
            Literal["merchant_visibility", "product_visibility", "product_rank", "avg_position", "total_count"]
        ]
        | Omit = omit,
        product_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantByItemsResponse:
        """
        Shopping Merchant By Items

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            product_name: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingMerchantByItemsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.merchant_by_items(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
            )
            ```
        """
        return await self._post(
            "/v1/reports/shopping/merchant-by-items",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "product_name": product_name,
                },
                shopping_merchant_by_items_params.ShoppingMerchantByItemsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantByItemsResponse,
        )

    async def all_items_with_merchants(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_all_items_with_merchants_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
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
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        include_items: SequenceNotStr[str] | Omit = omit,
        search_item: Optional[str] | Omit = omit,
        merchant_filter_type: Literal["any", "all"] | Omit = omit,
        rank_by: Literal["visibility", "average_position", "name"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingAllItemsWithMerchantsResponse:
        """
        Shopping All Items With Merchants

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            owned_asset_names: Body parameter.
            include_items: Body parameter.
            search_item: Body parameter.
            merchant_filter_type: Body parameter.
            rank_by: Body parameter.
            sort_order: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingAllItemsWithMerchantsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.all_items_with_merchants(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
                merchant_filter_type="any",
                rank_by="visibility",
                sort_order="desc",
            )
            ```
        """
        return await self._post(
            "/v1/reports/shopping/all-items-with-merchants",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "owned_asset_names": owned_asset_names,
                    "include_items": include_items,
                    "search_item": search_item,
                    "merchant_filter_type": merchant_filter_type,
                    "rank_by": rank_by,
                    "sort_order": sort_order,
                },
                shopping_all_items_with_merchants_params.ShoppingAllItemsWithMerchantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingAllItemsWithMerchantsResponse,
        )

    async def trigger_rate(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_trigger_rate_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        dimensions: List[
            Literal["period", "date", "model_id", "topic_id", "region_id", "persona_id", "prompt_id", "prompt"]
        ]
        | Omit = omit,
        metrics: List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingTriggerRateResponse:
        """
        Shopping Trigger Rate

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
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
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
            )
            ```
        """
        return await self._post(
            "/v1/reports/shopping/trigger-rate",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                },
                shopping_trigger_rate_params.ShoppingTriggerRateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingTriggerRateResponse,
        )

    async def merchant_share(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_share_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        dimensions: List[Literal["period", "topic_id", "prompt_id"]] | Omit = omit,
        metrics: List[Literal["merchant_share"]] | Omit = omit,
        target_asset_names: SequenceNotStr[str] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingMerchantShareResponse:
        """
        Shopping Merchant Share

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            dimensions: Body parameter.
            metrics: Body parameter.
            target_asset_names: Body parameter.
            owned_asset_names: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingMerchantShareResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.merchant_share(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
            )
            ```
        """
        return await self._post(
            "/v1/reports/shopping/merchant-share",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "dimensions": dimensions,
                    "metrics": metrics,
                    "target_asset_names": target_asset_names,
                    "owned_asset_names": owned_asset_names,
                },
                shopping_merchant_share_params.ShoppingMerchantShareParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingMerchantShareResponse,
        )

    async def product_merchant_urls(
        self,
        *,
        category_id: str,
        product_names: SequenceNotStr[str],
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
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
            category_id: Body parameter.
            product_names: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingProductMerchantURLsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.product_merchant_urls(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                product_names=[],
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )
            ```
        """
        return await self._post(
            "/v1/reports/shopping/product-merchant-urls",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "product_names": product_names,
                    "start_date": start_date,
                    "end_date": end_date,
                },
                shopping_product_merchant_urls_params.ShoppingProductMerchantURLsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingProductMerchantURLsResponse,
        )

    async def executions(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_executions_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        analysis_types: List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]] | Omit = omit,
        analysis_filter_type: Literal["any", "all"] | Omit = omit,
        owned_asset_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingExecutionsResponse:
        """
        Shopping Executions

        Args:
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            date_interval: Body parameter.
            filters: Body parameter.
            order_by: Body parameter.
            pagination: Body parameter.
            include_count: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            exclude_topic_ids: Body parameter.
            analysis_types: Body parameter.
            analysis_filter_type: Body parameter.
            owned_asset_names: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingExecutionsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.executions(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
                date_interval="day",
                include_count=False,
                tag_filter_type="any",
                include_no_tag=False,
                exclude_topic_ids=False,
                analysis_filter_type="any",
            )
            ```
        """
        return await self._post(
            "/v1/reports/shopping/executions",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "comparison_start_date": comparison_start_date,
                    "comparison_end_date": comparison_end_date,
                    "date_interval": date_interval,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                    "include_count": include_count,
                    "tag_filter_type": tag_filter_type,
                    "include_no_tag": include_no_tag,
                    "exclude_topic_ids": exclude_topic_ids,
                    "analysis_types": analysis_types,
                    "analysis_filter_type": analysis_filter_type,
                    "owned_asset_names": owned_asset_names,
                },
                shopping_executions_params.ShoppingExecutionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingExecutionsResponse,
        )


class ShoppingResourceWithRawResponse:
    def __init__(self, shopping: ShoppingResource) -> None:
        self._shopping = shopping

        self.visibility = to_raw_response_wrapper(
            shopping.visibility,
        )
        self.item_visibility = to_raw_response_wrapper(
            shopping.item_visibility,
        )
        self.merchant_distribution = to_raw_response_wrapper(
            shopping.merchant_distribution,
        )
        self.merchant_visibility_by_brand = to_raw_response_wrapper(
            shopping.merchant_visibility_by_brand,
        )
        self.merchant_by_items = to_raw_response_wrapper(
            shopping.merchant_by_items,
        )
        self.all_items_with_merchants = to_raw_response_wrapper(
            shopping.all_items_with_merchants,
        )
        self.trigger_rate = to_raw_response_wrapper(
            shopping.trigger_rate,
        )
        self.merchant_share = to_raw_response_wrapper(
            shopping.merchant_share,
        )
        self.product_merchant_urls = to_raw_response_wrapper(
            shopping.product_merchant_urls,
        )
        self.executions = to_raw_response_wrapper(
            shopping.executions,
        )


class AsyncShoppingResourceWithRawResponse:
    def __init__(self, shopping: AsyncShoppingResource) -> None:
        self._shopping = shopping

        self.visibility = async_to_raw_response_wrapper(
            shopping.visibility,
        )
        self.item_visibility = async_to_raw_response_wrapper(
            shopping.item_visibility,
        )
        self.merchant_distribution = async_to_raw_response_wrapper(
            shopping.merchant_distribution,
        )
        self.merchant_visibility_by_brand = async_to_raw_response_wrapper(
            shopping.merchant_visibility_by_brand,
        )
        self.merchant_by_items = async_to_raw_response_wrapper(
            shopping.merchant_by_items,
        )
        self.all_items_with_merchants = async_to_raw_response_wrapper(
            shopping.all_items_with_merchants,
        )
        self.trigger_rate = async_to_raw_response_wrapper(
            shopping.trigger_rate,
        )
        self.merchant_share = async_to_raw_response_wrapper(
            shopping.merchant_share,
        )
        self.product_merchant_urls = async_to_raw_response_wrapper(
            shopping.product_merchant_urls,
        )
        self.executions = async_to_raw_response_wrapper(
            shopping.executions,
        )


class ShoppingResourceWithStreamingResponse:
    def __init__(self, shopping: ShoppingResource) -> None:
        self._shopping = shopping

        self.visibility = to_streamed_response_wrapper(
            shopping.visibility,
        )
        self.item_visibility = to_streamed_response_wrapper(
            shopping.item_visibility,
        )
        self.merchant_distribution = to_streamed_response_wrapper(
            shopping.merchant_distribution,
        )
        self.merchant_visibility_by_brand = to_streamed_response_wrapper(
            shopping.merchant_visibility_by_brand,
        )
        self.merchant_by_items = to_streamed_response_wrapper(
            shopping.merchant_by_items,
        )
        self.all_items_with_merchants = to_streamed_response_wrapper(
            shopping.all_items_with_merchants,
        )
        self.trigger_rate = to_streamed_response_wrapper(
            shopping.trigger_rate,
        )
        self.merchant_share = to_streamed_response_wrapper(
            shopping.merchant_share,
        )
        self.product_merchant_urls = to_streamed_response_wrapper(
            shopping.product_merchant_urls,
        )
        self.executions = to_streamed_response_wrapper(
            shopping.executions,
        )


class AsyncShoppingResourceWithStreamingResponse:
    def __init__(self, shopping: AsyncShoppingResource) -> None:
        self._shopping = shopping

        self.visibility = async_to_streamed_response_wrapper(
            shopping.visibility,
        )
        self.item_visibility = async_to_streamed_response_wrapper(
            shopping.item_visibility,
        )
        self.merchant_distribution = async_to_streamed_response_wrapper(
            shopping.merchant_distribution,
        )
        self.merchant_visibility_by_brand = async_to_streamed_response_wrapper(
            shopping.merchant_visibility_by_brand,
        )
        self.merchant_by_items = async_to_streamed_response_wrapper(
            shopping.merchant_by_items,
        )
        self.all_items_with_merchants = async_to_streamed_response_wrapper(
            shopping.all_items_with_merchants,
        )
        self.trigger_rate = async_to_streamed_response_wrapper(
            shopping.trigger_rate,
        )
        self.merchant_share = async_to_streamed_response_wrapper(
            shopping.merchant_share,
        )
        self.product_merchant_urls = async_to_streamed_response_wrapper(
            shopping.product_merchant_urls,
        )
        self.executions = async_to_streamed_response_wrapper(
            shopping.executions,
        )
