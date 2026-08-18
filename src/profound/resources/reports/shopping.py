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
from ..._streaming import Stream, AsyncStream
from ...types.shared.shopping_rows_response import ShoppingRowsResponse
from ...types.shared_params.pagination import Pagination
from ...types.reports import (
    shopping_visibility_v1_visibility_post_params,
    shopping_item_visibility_v1_item_visibility_post_params,
    shopping_merchant_distribution_v1_merchant_distribution_post_params,
    shopping_merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post_params,
    shopping_merchant_by_items_v1_merchant_by_items_post_params,
    shopping_all_items_with_merchants_v1_all_items_with_merchants_post_params,
    shopping_trigger_rate_v1_trigger_rate_post_params,
    shopping_triggered_prompts_v1_triggered_prompts_post_params,
    shopping_triggered_topics_v1_triggered_topics_post_params,
    shopping_merchant_share_v1_merchant_share_post_params,
    shopping_product_merchant_urls_v1_product_merchant_urls_post_params,
    shopping_executions_v1_executions_post_params,
    shopping_query_brands_v2_v2_brands_post_params,
    shopping_stream_brands_v2_v2_brands_stream_post_params,
    shopping_query_products_v2_v2_products_post_params,
    shopping_stream_products_v2_v2_products_stream_post_params,
    shopping_query_merchants_v2_v2_merchants_post_params,
    shopping_stream_merchants_v2_v2_merchants_stream_post_params,
    shopping_query_trigger_rate_v2_v2_trigger_rate_post_params,
    shopping_stream_trigger_rate_v2_v2_trigger_rate_stream_post_params,
)
from ...types.reports.shopping_query_brands_v2_v2_brands_post_response import ShoppingQueryBrandsV2V2BrandsPostResponse
from ...types.shared_params.filter_node import FilterNode
from ...types.reports.shopping_stream_brands_v2_v2_brands_stream_post_response import (
    ShoppingStreamBrandsV2V2BrandsStreamPostResponse,
)
from ...types.reports.shopping_query_products_v2_v2_products_post_response import (
    ShoppingQueryProductsV2V2ProductsPostResponse,
)
from ...types.reports.shopping_stream_products_v2_v2_products_stream_post_response import (
    ShoppingStreamProductsV2V2ProductsStreamPostResponse,
)
from ...types.reports.shopping_query_merchants_v2_v2_merchants_post_response import (
    ShoppingQueryMerchantsV2V2MerchantsPostResponse,
)
from ...types.reports.shopping_stream_merchants_v2_v2_merchants_stream_post_response import (
    ShoppingStreamMerchantsV2V2MerchantsStreamPostResponse,
)
from ...types.reports.shopping_query_trigger_rate_v2_v2_trigger_rate_post_response import (
    ShoppingQueryTriggerRateV2V2TriggerRatePostResponse,
)
from ...types.reports.shopping_stream_trigger_rate_v2_v2_trigger_rate_stream_post_response import (
    ShoppingStreamTriggerRateV2V2TriggerRateStreamPostResponse,
)

__all__ = ["ShoppingResource", "AsyncShoppingResource"]


class ShoppingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShoppingResourceWithRawResponse:
        return ShoppingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShoppingResourceWithStreamingResponse:
        return ShoppingResourceWithStreamingResponse(self)

    def visibility_v1_visibility_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_visibility_v1_visibility_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.visibility_v1_visibility_post(
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
                shopping_visibility_v1_visibility_post_params.ShoppingVisibilityV1VisibilityPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    def item_visibility_v1_item_visibility_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_item_visibility_v1_item_visibility_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.item_visibility_v1_item_visibility_post(
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
                shopping_item_visibility_v1_item_visibility_post_params.ShoppingItemVisibilityV1ItemVisibilityPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    def merchant_distribution_v1_merchant_distribution_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_distribution_v1_merchant_distribution_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.merchant_distribution_v1_merchant_distribution_post(
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
                shopping_merchant_distribution_v1_merchant_distribution_post_params.ShoppingMerchantDistributionV1MerchantDistributionPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    def merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post_params.Filter]
        | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post(
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
                shopping_merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post_params.ShoppingMerchantVisibilityByBrandV1MerchantVisibilityByBrandPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    def merchant_by_items_v1_merchant_by_items_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_by_items_v1_merchant_by_items_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.merchant_by_items_v1_merchant_by_items_post(
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
                shopping_merchant_by_items_v1_merchant_by_items_post_params.ShoppingMerchantByItemsV1MerchantByItemsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    def all_items_with_merchants_v1_all_items_with_merchants_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_all_items_with_merchants_v1_all_items_with_merchants_post_params.Filter]
        | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.all_items_with_merchants_v1_all_items_with_merchants_post(
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
                shopping_all_items_with_merchants_v1_all_items_with_merchants_post_params.ShoppingAllItemsWithMerchantsV1AllItemsWithMerchantsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    def trigger_rate_v1_trigger_rate_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_trigger_rate_v1_trigger_rate_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.trigger_rate_v1_trigger_rate_post(
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
                shopping_trigger_rate_v1_trigger_rate_post_params.ShoppingTriggerRateV1TriggerRatePostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    def triggered_prompts_v1_triggered_prompts_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_triggered_prompts_v1_triggered_prompts_post_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: None | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingRowsResponse:
        """
        Shopping Triggered Prompts

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
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.triggered_prompts_v1_triggered_prompts_post(
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
            "/v1/reports/shopping/triggered-prompts",
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
                },
                shopping_triggered_prompts_v1_triggered_prompts_post_params.ShoppingTriggeredPromptsV1TriggeredPromptsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    def triggered_topics_v1_triggered_topics_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_triggered_topics_v1_triggered_topics_post_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: None | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingRowsResponse:
        """
        Shopping Triggered Topics

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
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.triggered_topics_v1_triggered_topics_post(
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
            "/v1/reports/shopping/triggered-topics",
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
                },
                shopping_triggered_topics_v1_triggered_topics_post_params.ShoppingTriggeredTopicsV1TriggeredTopicsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    def merchant_share_v1_merchant_share_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_share_v1_merchant_share_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.merchant_share_v1_merchant_share_post(
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
                shopping_merchant_share_v1_merchant_share_post_params.ShoppingMerchantShareV1MerchantSharePostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    def product_merchant_urls_v1_product_merchant_urls_post(
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.product_merchant_urls_v1_product_merchant_urls_post(
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
                shopping_product_merchant_urls_v1_product_merchant_urls_post_params.ShoppingProductMerchantURLsV1ProductMerchantURLsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    def executions_v1_executions_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_executions_v1_executions_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.executions_v1_executions_post(
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
                shopping_executions_v1_executions_post_params.ShoppingExecutionsV1ExecutionsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    def query_brands_v2_v2_brands_post(
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
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingQueryBrandsV2V2BrandsPostResponse:
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
            ShoppingQueryBrandsV2V2BrandsPostResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.query_brands_v2_v2_brands_post(
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
                shopping_query_brands_v2_v2_brands_post_params.ShoppingQueryBrandsV2V2BrandsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingQueryBrandsV2V2BrandsPostResponse,
        )

    def stream_brands_v2_v2_brands_stream_post(
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
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ShoppingStreamBrandsV2V2BrandsStreamPostResponse]:
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
            Stream[ShoppingStreamBrandsV2V2BrandsStreamPostResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = client.reports.shopping.stream_brands_v2_v2_brands_stream_post(
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
                shopping_stream_brands_v2_v2_brands_stream_post_params.ShoppingStreamBrandsV2V2BrandsStreamPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamBrandsV2V2BrandsStreamPostResponse,
            stream=True,
            stream_cls=Stream[ShoppingStreamBrandsV2V2BrandsStreamPostResponse],
        )

    def query_products_v2_v2_products_post(
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
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingQueryProductsV2V2ProductsPostResponse:
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
            ShoppingQueryProductsV2V2ProductsPostResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.query_products_v2_v2_products_post(
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
                shopping_query_products_v2_v2_products_post_params.ShoppingQueryProductsV2V2ProductsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingQueryProductsV2V2ProductsPostResponse,
        )

    def stream_products_v2_v2_products_stream_post(
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
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ShoppingStreamProductsV2V2ProductsStreamPostResponse]:
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
            Stream[ShoppingStreamProductsV2V2ProductsStreamPostResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = client.reports.shopping.stream_products_v2_v2_products_stream_post(
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
                shopping_stream_products_v2_v2_products_stream_post_params.ShoppingStreamProductsV2V2ProductsStreamPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamProductsV2V2ProductsStreamPostResponse,
            stream=True,
            stream_cls=Stream[ShoppingStreamProductsV2V2ProductsStreamPostResponse],
        )

    def query_merchants_v2_v2_merchants_post(
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
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingQueryMerchantsV2V2MerchantsPostResponse:
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
            ShoppingQueryMerchantsV2V2MerchantsPostResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.query_merchants_v2_v2_merchants_post(
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
                shopping_query_merchants_v2_v2_merchants_post_params.ShoppingQueryMerchantsV2V2MerchantsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingQueryMerchantsV2V2MerchantsPostResponse,
        )

    def stream_merchants_v2_v2_merchants_stream_post(
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
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ShoppingStreamMerchantsV2V2MerchantsStreamPostResponse]:
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
            Stream[ShoppingStreamMerchantsV2V2MerchantsStreamPostResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = client.reports.shopping.stream_merchants_v2_v2_merchants_stream_post(
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
                shopping_stream_merchants_v2_v2_merchants_stream_post_params.ShoppingStreamMerchantsV2V2MerchantsStreamPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamMerchantsV2V2MerchantsStreamPostResponse,
            stream=True,
            stream_cls=Stream[ShoppingStreamMerchantsV2V2MerchantsStreamPostResponse],
        )

    def query_trigger_rate_v2_v2_trigger_rate_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "region", "persona", "prompt"]] | Omit = omit,
        metrics: Optional[List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]]]
        | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingQueryTriggerRateV2V2TriggerRatePostResponse:
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
            ShoppingQueryTriggerRateV2V2TriggerRatePostResponse: Successful Response

        Example:
            ```python
            shopping = client.reports.shopping.query_trigger_rate_v2_v2_trigger_rate_post(
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
                shopping_query_trigger_rate_v2_v2_trigger_rate_post_params.ShoppingQueryTriggerRateV2V2TriggerRatePostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingQueryTriggerRateV2V2TriggerRatePostResponse,
        )

    def stream_trigger_rate_v2_v2_trigger_rate_stream_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "region", "persona", "prompt"]] | Omit = omit,
        metrics: Optional[List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]]]
        | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ShoppingStreamTriggerRateV2V2TriggerRateStreamPostResponse]:
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
            Stream[ShoppingStreamTriggerRateV2V2TriggerRateStreamPostResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = client.reports.shopping.stream_trigger_rate_v2_v2_trigger_rate_stream_post(
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
                shopping_stream_trigger_rate_v2_v2_trigger_rate_stream_post_params.ShoppingStreamTriggerRateV2V2TriggerRateStreamPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamTriggerRateV2V2TriggerRateStreamPostResponse,
            stream=True,
            stream_cls=Stream[ShoppingStreamTriggerRateV2V2TriggerRateStreamPostResponse],
        )


class AsyncShoppingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShoppingResourceWithRawResponse:
        return AsyncShoppingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShoppingResourceWithStreamingResponse:
        return AsyncShoppingResourceWithStreamingResponse(self)

    async def visibility_v1_visibility_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_visibility_v1_visibility_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.visibility_v1_visibility_post(
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
                shopping_visibility_v1_visibility_post_params.ShoppingVisibilityV1VisibilityPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    async def item_visibility_v1_item_visibility_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_item_visibility_v1_item_visibility_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.item_visibility_v1_item_visibility_post(
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
                shopping_item_visibility_v1_item_visibility_post_params.ShoppingItemVisibilityV1ItemVisibilityPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    async def merchant_distribution_v1_merchant_distribution_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_distribution_v1_merchant_distribution_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.merchant_distribution_v1_merchant_distribution_post(
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
                shopping_merchant_distribution_v1_merchant_distribution_post_params.ShoppingMerchantDistributionV1MerchantDistributionPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    async def merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post_params.Filter]
        | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post(
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
                shopping_merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post_params.ShoppingMerchantVisibilityByBrandV1MerchantVisibilityByBrandPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    async def merchant_by_items_v1_merchant_by_items_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_by_items_v1_merchant_by_items_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.merchant_by_items_v1_merchant_by_items_post(
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
                shopping_merchant_by_items_v1_merchant_by_items_post_params.ShoppingMerchantByItemsV1MerchantByItemsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    async def all_items_with_merchants_v1_all_items_with_merchants_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_all_items_with_merchants_v1_all_items_with_merchants_post_params.Filter]
        | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.all_items_with_merchants_v1_all_items_with_merchants_post(
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
                shopping_all_items_with_merchants_v1_all_items_with_merchants_post_params.ShoppingAllItemsWithMerchantsV1AllItemsWithMerchantsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    async def trigger_rate_v1_trigger_rate_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_trigger_rate_v1_trigger_rate_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.trigger_rate_v1_trigger_rate_post(
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
                shopping_trigger_rate_v1_trigger_rate_post_params.ShoppingTriggerRateV1TriggerRatePostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    async def triggered_prompts_v1_triggered_prompts_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_triggered_prompts_v1_triggered_prompts_post_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: None | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingRowsResponse:
        """
        Shopping Triggered Prompts

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
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.triggered_prompts_v1_triggered_prompts_post(
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
            "/v1/reports/shopping/triggered-prompts",
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
                },
                shopping_triggered_prompts_v1_triggered_prompts_post_params.ShoppingTriggeredPromptsV1TriggeredPromptsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    async def triggered_topics_v1_triggered_topics_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_triggered_topics_v1_triggered_topics_post_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: None | Omit = omit,
        include_count: bool | Omit = omit,
        tag_filter_type: Literal["any", "all"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingRowsResponse:
        """
        Shopping Triggered Topics

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
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.triggered_topics_v1_triggered_topics_post(
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
            "/v1/reports/shopping/triggered-topics",
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
                },
                shopping_triggered_topics_v1_triggered_topics_post_params.ShoppingTriggeredTopicsV1TriggeredTopicsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    async def merchant_share_v1_merchant_share_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_merchant_share_v1_merchant_share_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.merchant_share_v1_merchant_share_post(
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
                shopping_merchant_share_v1_merchant_share_post_params.ShoppingMerchantShareV1MerchantSharePostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    async def product_merchant_urls_v1_product_merchant_urls_post(
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.product_merchant_urls_v1_product_merchant_urls_post(
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
                shopping_product_merchant_urls_v1_product_merchant_urls_post_params.ShoppingProductMerchantURLsV1ProductMerchantURLsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    async def executions_v1_executions_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        filters: Iterable[shopping_executions_v1_executions_post_params.Filter] | Omit = omit,
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
    ) -> ShoppingRowsResponse:
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
            ShoppingRowsResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.executions_v1_executions_post(
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
                shopping_executions_v1_executions_post_params.ShoppingExecutionsV1ExecutionsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingRowsResponse,
        )

    async def query_brands_v2_v2_brands_post(
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
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingQueryBrandsV2V2BrandsPostResponse:
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
            ShoppingQueryBrandsV2V2BrandsPostResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.query_brands_v2_v2_brands_post(
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
                shopping_query_brands_v2_v2_brands_post_params.ShoppingQueryBrandsV2V2BrandsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingQueryBrandsV2V2BrandsPostResponse,
        )

    async def stream_brands_v2_v2_brands_stream_post(
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
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ShoppingStreamBrandsV2V2BrandsStreamPostResponse]:
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
            AsyncStream[ShoppingStreamBrandsV2V2BrandsStreamPostResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = await client.reports.shopping.stream_brands_v2_v2_brands_stream_post(
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
                shopping_stream_brands_v2_v2_brands_stream_post_params.ShoppingStreamBrandsV2V2BrandsStreamPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamBrandsV2V2BrandsStreamPostResponse,
            stream=True,
            stream_cls=AsyncStream[ShoppingStreamBrandsV2V2BrandsStreamPostResponse],
        )

    async def query_products_v2_v2_products_post(
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
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingQueryProductsV2V2ProductsPostResponse:
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
            ShoppingQueryProductsV2V2ProductsPostResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.query_products_v2_v2_products_post(
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
                shopping_query_products_v2_v2_products_post_params.ShoppingQueryProductsV2V2ProductsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingQueryProductsV2V2ProductsPostResponse,
        )

    async def stream_products_v2_v2_products_stream_post(
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
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ShoppingStreamProductsV2V2ProductsStreamPostResponse]:
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
            AsyncStream[ShoppingStreamProductsV2V2ProductsStreamPostResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = await client.reports.shopping.stream_products_v2_v2_products_stream_post(
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
                shopping_stream_products_v2_v2_products_stream_post_params.ShoppingStreamProductsV2V2ProductsStreamPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamProductsV2V2ProductsStreamPostResponse,
            stream=True,
            stream_cls=AsyncStream[ShoppingStreamProductsV2V2ProductsStreamPostResponse],
        )

    async def query_merchants_v2_v2_merchants_post(
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
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingQueryMerchantsV2V2MerchantsPostResponse:
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
            ShoppingQueryMerchantsV2V2MerchantsPostResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.query_merchants_v2_v2_merchants_post(
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
                shopping_query_merchants_v2_v2_merchants_post_params.ShoppingQueryMerchantsV2V2MerchantsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingQueryMerchantsV2V2MerchantsPostResponse,
        )

    async def stream_merchants_v2_v2_merchants_stream_post(
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
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ShoppingStreamMerchantsV2V2MerchantsStreamPostResponse]:
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
            AsyncStream[ShoppingStreamMerchantsV2V2MerchantsStreamPostResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = await client.reports.shopping.stream_merchants_v2_v2_merchants_stream_post(
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
                shopping_stream_merchants_v2_v2_merchants_stream_post_params.ShoppingStreamMerchantsV2V2MerchantsStreamPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamMerchantsV2V2MerchantsStreamPostResponse,
            stream=True,
            stream_cls=AsyncStream[ShoppingStreamMerchantsV2V2MerchantsStreamPostResponse],
        )

    async def query_trigger_rate_v2_v2_trigger_rate_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "region", "persona", "prompt"]] | Omit = omit,
        metrics: Optional[List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]]]
        | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShoppingQueryTriggerRateV2V2TriggerRatePostResponse:
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
            ShoppingQueryTriggerRateV2V2TriggerRatePostResponse: Successful Response

        Example:
            ```python
            shopping = await client.reports.shopping.query_trigger_rate_v2_v2_trigger_rate_post(
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
                shopping_query_trigger_rate_v2_v2_trigger_rate_post_params.ShoppingQueryTriggerRateV2V2TriggerRatePostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingQueryTriggerRateV2V2TriggerRatePostResponse,
        )

    async def stream_trigger_rate_v2_v2_trigger_rate_stream_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "topic", "region", "persona", "prompt"]] | Omit = omit,
        metrics: Optional[List[Literal["total_runs", "shopping_triggered_runs", "trigger_rate_percentage"]]]
        | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ShoppingStreamTriggerRateV2V2TriggerRateStreamPostResponse]:
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
            AsyncStream[ShoppingStreamTriggerRateV2V2TriggerRateStreamPostResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = await client.reports.shopping.stream_trigger_rate_v2_v2_trigger_rate_stream_post(
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
                shopping_stream_trigger_rate_v2_v2_trigger_rate_stream_post_params.ShoppingStreamTriggerRateV2V2TriggerRateStreamPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShoppingStreamTriggerRateV2V2TriggerRateStreamPostResponse,
            stream=True,
            stream_cls=AsyncStream[ShoppingStreamTriggerRateV2V2TriggerRateStreamPostResponse],
        )


class ShoppingResourceWithRawResponse:
    def __init__(self, shopping: ShoppingResource) -> None:
        self._shopping = shopping

        self.visibility_v1_visibility_post = to_raw_response_wrapper(
            shopping.visibility_v1_visibility_post,
        )
        self.item_visibility_v1_item_visibility_post = to_raw_response_wrapper(
            shopping.item_visibility_v1_item_visibility_post,
        )
        self.merchant_distribution_v1_merchant_distribution_post = to_raw_response_wrapper(
            shopping.merchant_distribution_v1_merchant_distribution_post,
        )
        self.merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post = to_raw_response_wrapper(
            shopping.merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post,
        )
        self.merchant_by_items_v1_merchant_by_items_post = to_raw_response_wrapper(
            shopping.merchant_by_items_v1_merchant_by_items_post,
        )
        self.all_items_with_merchants_v1_all_items_with_merchants_post = to_raw_response_wrapper(
            shopping.all_items_with_merchants_v1_all_items_with_merchants_post,
        )
        self.trigger_rate_v1_trigger_rate_post = to_raw_response_wrapper(
            shopping.trigger_rate_v1_trigger_rate_post,
        )
        self.triggered_prompts_v1_triggered_prompts_post = to_raw_response_wrapper(
            shopping.triggered_prompts_v1_triggered_prompts_post,
        )
        self.triggered_topics_v1_triggered_topics_post = to_raw_response_wrapper(
            shopping.triggered_topics_v1_triggered_topics_post,
        )
        self.merchant_share_v1_merchant_share_post = to_raw_response_wrapper(
            shopping.merchant_share_v1_merchant_share_post,
        )
        self.product_merchant_urls_v1_product_merchant_urls_post = to_raw_response_wrapper(
            shopping.product_merchant_urls_v1_product_merchant_urls_post,
        )
        self.executions_v1_executions_post = to_raw_response_wrapper(
            shopping.executions_v1_executions_post,
        )
        self.query_brands_v2_v2_brands_post = to_raw_response_wrapper(
            shopping.query_brands_v2_v2_brands_post,
        )
        self.stream_brands_v2_v2_brands_stream_post = to_raw_response_wrapper(
            shopping.stream_brands_v2_v2_brands_stream_post,
        )
        self.query_products_v2_v2_products_post = to_raw_response_wrapper(
            shopping.query_products_v2_v2_products_post,
        )
        self.stream_products_v2_v2_products_stream_post = to_raw_response_wrapper(
            shopping.stream_products_v2_v2_products_stream_post,
        )
        self.query_merchants_v2_v2_merchants_post = to_raw_response_wrapper(
            shopping.query_merchants_v2_v2_merchants_post,
        )
        self.stream_merchants_v2_v2_merchants_stream_post = to_raw_response_wrapper(
            shopping.stream_merchants_v2_v2_merchants_stream_post,
        )
        self.query_trigger_rate_v2_v2_trigger_rate_post = to_raw_response_wrapper(
            shopping.query_trigger_rate_v2_v2_trigger_rate_post,
        )
        self.stream_trigger_rate_v2_v2_trigger_rate_stream_post = to_raw_response_wrapper(
            shopping.stream_trigger_rate_v2_v2_trigger_rate_stream_post,
        )


class AsyncShoppingResourceWithRawResponse:
    def __init__(self, shopping: AsyncShoppingResource) -> None:
        self._shopping = shopping

        self.visibility_v1_visibility_post = async_to_raw_response_wrapper(
            shopping.visibility_v1_visibility_post,
        )
        self.item_visibility_v1_item_visibility_post = async_to_raw_response_wrapper(
            shopping.item_visibility_v1_item_visibility_post,
        )
        self.merchant_distribution_v1_merchant_distribution_post = async_to_raw_response_wrapper(
            shopping.merchant_distribution_v1_merchant_distribution_post,
        )
        self.merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post = async_to_raw_response_wrapper(
            shopping.merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post,
        )
        self.merchant_by_items_v1_merchant_by_items_post = async_to_raw_response_wrapper(
            shopping.merchant_by_items_v1_merchant_by_items_post,
        )
        self.all_items_with_merchants_v1_all_items_with_merchants_post = async_to_raw_response_wrapper(
            shopping.all_items_with_merchants_v1_all_items_with_merchants_post,
        )
        self.trigger_rate_v1_trigger_rate_post = async_to_raw_response_wrapper(
            shopping.trigger_rate_v1_trigger_rate_post,
        )
        self.triggered_prompts_v1_triggered_prompts_post = async_to_raw_response_wrapper(
            shopping.triggered_prompts_v1_triggered_prompts_post,
        )
        self.triggered_topics_v1_triggered_topics_post = async_to_raw_response_wrapper(
            shopping.triggered_topics_v1_triggered_topics_post,
        )
        self.merchant_share_v1_merchant_share_post = async_to_raw_response_wrapper(
            shopping.merchant_share_v1_merchant_share_post,
        )
        self.product_merchant_urls_v1_product_merchant_urls_post = async_to_raw_response_wrapper(
            shopping.product_merchant_urls_v1_product_merchant_urls_post,
        )
        self.executions_v1_executions_post = async_to_raw_response_wrapper(
            shopping.executions_v1_executions_post,
        )
        self.query_brands_v2_v2_brands_post = async_to_raw_response_wrapper(
            shopping.query_brands_v2_v2_brands_post,
        )
        self.stream_brands_v2_v2_brands_stream_post = async_to_raw_response_wrapper(
            shopping.stream_brands_v2_v2_brands_stream_post,
        )
        self.query_products_v2_v2_products_post = async_to_raw_response_wrapper(
            shopping.query_products_v2_v2_products_post,
        )
        self.stream_products_v2_v2_products_stream_post = async_to_raw_response_wrapper(
            shopping.stream_products_v2_v2_products_stream_post,
        )
        self.query_merchants_v2_v2_merchants_post = async_to_raw_response_wrapper(
            shopping.query_merchants_v2_v2_merchants_post,
        )
        self.stream_merchants_v2_v2_merchants_stream_post = async_to_raw_response_wrapper(
            shopping.stream_merchants_v2_v2_merchants_stream_post,
        )
        self.query_trigger_rate_v2_v2_trigger_rate_post = async_to_raw_response_wrapper(
            shopping.query_trigger_rate_v2_v2_trigger_rate_post,
        )
        self.stream_trigger_rate_v2_v2_trigger_rate_stream_post = async_to_raw_response_wrapper(
            shopping.stream_trigger_rate_v2_v2_trigger_rate_stream_post,
        )


class ShoppingResourceWithStreamingResponse:
    def __init__(self, shopping: ShoppingResource) -> None:
        self._shopping = shopping

        self.visibility_v1_visibility_post = to_streamed_response_wrapper(
            shopping.visibility_v1_visibility_post,
        )
        self.item_visibility_v1_item_visibility_post = to_streamed_response_wrapper(
            shopping.item_visibility_v1_item_visibility_post,
        )
        self.merchant_distribution_v1_merchant_distribution_post = to_streamed_response_wrapper(
            shopping.merchant_distribution_v1_merchant_distribution_post,
        )
        self.merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post = to_streamed_response_wrapper(
            shopping.merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post,
        )
        self.merchant_by_items_v1_merchant_by_items_post = to_streamed_response_wrapper(
            shopping.merchant_by_items_v1_merchant_by_items_post,
        )
        self.all_items_with_merchants_v1_all_items_with_merchants_post = to_streamed_response_wrapper(
            shopping.all_items_with_merchants_v1_all_items_with_merchants_post,
        )
        self.trigger_rate_v1_trigger_rate_post = to_streamed_response_wrapper(
            shopping.trigger_rate_v1_trigger_rate_post,
        )
        self.triggered_prompts_v1_triggered_prompts_post = to_streamed_response_wrapper(
            shopping.triggered_prompts_v1_triggered_prompts_post,
        )
        self.triggered_topics_v1_triggered_topics_post = to_streamed_response_wrapper(
            shopping.triggered_topics_v1_triggered_topics_post,
        )
        self.merchant_share_v1_merchant_share_post = to_streamed_response_wrapper(
            shopping.merchant_share_v1_merchant_share_post,
        )
        self.product_merchant_urls_v1_product_merchant_urls_post = to_streamed_response_wrapper(
            shopping.product_merchant_urls_v1_product_merchant_urls_post,
        )
        self.executions_v1_executions_post = to_streamed_response_wrapper(
            shopping.executions_v1_executions_post,
        )
        self.query_brands_v2_v2_brands_post = to_streamed_response_wrapper(
            shopping.query_brands_v2_v2_brands_post,
        )
        self.stream_brands_v2_v2_brands_stream_post = to_streamed_response_wrapper(
            shopping.stream_brands_v2_v2_brands_stream_post,
        )
        self.query_products_v2_v2_products_post = to_streamed_response_wrapper(
            shopping.query_products_v2_v2_products_post,
        )
        self.stream_products_v2_v2_products_stream_post = to_streamed_response_wrapper(
            shopping.stream_products_v2_v2_products_stream_post,
        )
        self.query_merchants_v2_v2_merchants_post = to_streamed_response_wrapper(
            shopping.query_merchants_v2_v2_merchants_post,
        )
        self.stream_merchants_v2_v2_merchants_stream_post = to_streamed_response_wrapper(
            shopping.stream_merchants_v2_v2_merchants_stream_post,
        )
        self.query_trigger_rate_v2_v2_trigger_rate_post = to_streamed_response_wrapper(
            shopping.query_trigger_rate_v2_v2_trigger_rate_post,
        )
        self.stream_trigger_rate_v2_v2_trigger_rate_stream_post = to_streamed_response_wrapper(
            shopping.stream_trigger_rate_v2_v2_trigger_rate_stream_post,
        )


class AsyncShoppingResourceWithStreamingResponse:
    def __init__(self, shopping: AsyncShoppingResource) -> None:
        self._shopping = shopping

        self.visibility_v1_visibility_post = async_to_streamed_response_wrapper(
            shopping.visibility_v1_visibility_post,
        )
        self.item_visibility_v1_item_visibility_post = async_to_streamed_response_wrapper(
            shopping.item_visibility_v1_item_visibility_post,
        )
        self.merchant_distribution_v1_merchant_distribution_post = async_to_streamed_response_wrapper(
            shopping.merchant_distribution_v1_merchant_distribution_post,
        )
        self.merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post = async_to_streamed_response_wrapper(
            shopping.merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post,
        )
        self.merchant_by_items_v1_merchant_by_items_post = async_to_streamed_response_wrapper(
            shopping.merchant_by_items_v1_merchant_by_items_post,
        )
        self.all_items_with_merchants_v1_all_items_with_merchants_post = async_to_streamed_response_wrapper(
            shopping.all_items_with_merchants_v1_all_items_with_merchants_post,
        )
        self.trigger_rate_v1_trigger_rate_post = async_to_streamed_response_wrapper(
            shopping.trigger_rate_v1_trigger_rate_post,
        )
        self.triggered_prompts_v1_triggered_prompts_post = async_to_streamed_response_wrapper(
            shopping.triggered_prompts_v1_triggered_prompts_post,
        )
        self.triggered_topics_v1_triggered_topics_post = async_to_streamed_response_wrapper(
            shopping.triggered_topics_v1_triggered_topics_post,
        )
        self.merchant_share_v1_merchant_share_post = async_to_streamed_response_wrapper(
            shopping.merchant_share_v1_merchant_share_post,
        )
        self.product_merchant_urls_v1_product_merchant_urls_post = async_to_streamed_response_wrapper(
            shopping.product_merchant_urls_v1_product_merchant_urls_post,
        )
        self.executions_v1_executions_post = async_to_streamed_response_wrapper(
            shopping.executions_v1_executions_post,
        )
        self.query_brands_v2_v2_brands_post = async_to_streamed_response_wrapper(
            shopping.query_brands_v2_v2_brands_post,
        )
        self.stream_brands_v2_v2_brands_stream_post = async_to_streamed_response_wrapper(
            shopping.stream_brands_v2_v2_brands_stream_post,
        )
        self.query_products_v2_v2_products_post = async_to_streamed_response_wrapper(
            shopping.query_products_v2_v2_products_post,
        )
        self.stream_products_v2_v2_products_stream_post = async_to_streamed_response_wrapper(
            shopping.stream_products_v2_v2_products_stream_post,
        )
        self.query_merchants_v2_v2_merchants_post = async_to_streamed_response_wrapper(
            shopping.query_merchants_v2_v2_merchants_post,
        )
        self.stream_merchants_v2_v2_merchants_stream_post = async_to_streamed_response_wrapper(
            shopping.stream_merchants_v2_v2_merchants_stream_post,
        )
        self.query_trigger_rate_v2_v2_trigger_rate_post = async_to_streamed_response_wrapper(
            shopping.query_trigger_rate_v2_v2_trigger_rate_post,
        )
        self.stream_trigger_rate_v2_v2_trigger_rate_stream_post = async_to_streamed_response_wrapper(
            shopping.stream_trigger_rate_v2_v2_trigger_rate_stream_post,
        )
