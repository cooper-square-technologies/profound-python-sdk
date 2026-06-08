# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound._utils import parse_datetime
from profound.types.reports import (
    ShoppingExecutionsResponse,
    ShoppingVisibilityResponse,
    ShoppingTriggerRateResponse,
    ShoppingMerchantShareResponse,
    ShoppingItemVisibilityResponse,
    ShoppingMerchantByItemsResponse,
    ShoppingProductMerchantURLsResponse,
    ShoppingMerchantDistributionResponse,
    ShoppingAllItemsWithMerchantsResponse,
    ShoppingMerchantVisibilityByBrandResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShopping:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_all_items_with_merchants(self, client: Profound) -> None:
        shopping = client.reports.shopping.all_items_with_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingAllItemsWithMerchantsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_all_items_with_merchants_with_all_params(self, client: Profound) -> None:
        shopping = client.reports.shopping.all_items_with_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_count=True,
            include_items=["string"],
            include_no_tag=True,
            merchant_filter_type="any",
            metrics=["visibility_score"],
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            rank_by="visibility",
            search_item="search_item",
            sort_order="asc",
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingAllItemsWithMerchantsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_all_items_with_merchants(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.all_items_with_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = response.parse()
        assert_matches_type(ShoppingAllItemsWithMerchantsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_all_items_with_merchants(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.all_items_with_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingAllItemsWithMerchantsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_executions(self, client: Profound) -> None:
        shopping = client.reports.shopping.executions(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingExecutionsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_executions_with_all_params(self, client: Profound) -> None:
        shopping = client.reports.shopping.executions(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            analysis_filter_type="any",
            analysis_types=["visibility"],
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_count=True,
            include_no_tag=True,
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingExecutionsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_executions(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.executions(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = response.parse()
        assert_matches_type(ShoppingExecutionsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_executions(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.executions(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingExecutionsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_item_visibility(self, client: Profound) -> None:
        shopping = client.reports.shopping.item_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingItemVisibilityResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_item_visibility_with_all_params(self, client: Profound) -> None:
        shopping = client.reports.shopping.item_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            competitor_limit=1,
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_competitors=True,
            include_count=True,
            include_items=["string"],
            include_no_tag=True,
            include_position_frequency=True,
            merchant_filter_type="any",
            metrics=["visibility_score"],
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            search_item="search_item",
            tag_filter_type="any",
            target_product="target_product",
        )
        assert_matches_type(ShoppingItemVisibilityResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_item_visibility(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.item_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = response.parse()
        assert_matches_type(ShoppingItemVisibilityResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_item_visibility(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.item_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingItemVisibilityResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_merchant_by_items(self, client: Profound) -> None:
        shopping = client.reports.shopping.merchant_by_items(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingMerchantByItemsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_merchant_by_items_with_all_params(self, client: Profound) -> None:
        shopping = client.reports.shopping.merchant_by_items(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_count=True,
            include_no_tag=True,
            metrics=["merchant_visibility"],
            order_by={"foo": "asc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
            product_name="product_name",
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingMerchantByItemsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_merchant_by_items(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.merchant_by_items(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = response.parse()
        assert_matches_type(ShoppingMerchantByItemsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_merchant_by_items(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.merchant_by_items(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingMerchantByItemsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_merchant_distribution(self, client: Profound) -> None:
        shopping = client.reports.shopping.merchant_distribution(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingMerchantDistributionResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_merchant_distribution_with_all_params(self, client: Profound) -> None:
        shopping = client.reports.shopping.merchant_distribution(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_count=True,
            include_no_tag=True,
            metrics=["offer_count"],
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            search_merchant="search_merchant",
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingMerchantDistributionResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_merchant_distribution(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.merchant_distribution(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = response.parse()
        assert_matches_type(ShoppingMerchantDistributionResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_merchant_distribution(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.merchant_distribution(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingMerchantDistributionResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_merchant_share(self, client: Profound) -> None:
        shopping = client.reports.shopping.merchant_share(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingMerchantShareResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_merchant_share_with_all_params(self, client: Profound) -> None:
        shopping = client.reports.shopping.merchant_share(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_count=True,
            include_no_tag=True,
            metrics=["merchant_share"],
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            tag_filter_type="any",
            target_asset_names=["string"],
        )
        assert_matches_type(ShoppingMerchantShareResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_merchant_share(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.merchant_share(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = response.parse()
        assert_matches_type(ShoppingMerchantShareResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_merchant_share(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.merchant_share(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingMerchantShareResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_merchant_visibility_by_brand(self, client: Profound) -> None:
        shopping = client.reports.shopping.merchant_visibility_by_brand(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingMerchantVisibilityByBrandResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_merchant_visibility_by_brand_with_all_params(self, client: Profound) -> None:
        shopping = client.reports.shopping.merchant_visibility_by_brand(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_brand="include_brand",
            include_brand_only=True,
            include_count=True,
            include_no_tag=True,
            metrics=["visibility_score"],
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            search_brand="search_brand",
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingMerchantVisibilityByBrandResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_merchant_visibility_by_brand(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.merchant_visibility_by_brand(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = response.parse()
        assert_matches_type(ShoppingMerchantVisibilityByBrandResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_merchant_visibility_by_brand(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.merchant_visibility_by_brand(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingMerchantVisibilityByBrandResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_product_merchant_urls(self, client: Profound) -> None:
        shopping = client.reports.shopping.product_merchant_urls(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            product_names=["string"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingProductMerchantURLsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_product_merchant_urls(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.product_merchant_urls(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            product_names=["string"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = response.parse()
        assert_matches_type(ShoppingProductMerchantURLsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_product_merchant_urls(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.product_merchant_urls(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            product_names=["string"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingProductMerchantURLsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_rate(self, client: Profound) -> None:
        shopping = client.reports.shopping.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_rate_with_all_params(self, client: Profound) -> None:
        shopping = client.reports.shopping.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_count=True,
            include_no_tag=True,
            metrics=["total_runs"],
            order_by={"foo": "asc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_trigger_rate(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = response.parse()
        assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_trigger_rate(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_visibility(self, client: Profound) -> None:
        shopping = client.reports.shopping.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingVisibilityResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_visibility_with_all_params(self, client: Profound) -> None:
        shopping = client.reports.shopping.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_asset="include_asset",
            include_asset_only=True,
            include_count=True,
            include_no_tag=True,
            include_position_frequency=True,
            metrics=["visibility_score"],
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            rank_by="visibility_score",
            search_asset="search_asset",
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingVisibilityResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_visibility(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = response.parse()
        assert_matches_type(ShoppingVisibilityResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_visibility(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingVisibilityResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShopping:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_all_items_with_merchants(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.all_items_with_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingAllItemsWithMerchantsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_all_items_with_merchants_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.all_items_with_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_count=True,
            include_items=["string"],
            include_no_tag=True,
            merchant_filter_type="any",
            metrics=["visibility_score"],
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            rank_by="visibility",
            search_item="search_item",
            sort_order="asc",
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingAllItemsWithMerchantsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_all_items_with_merchants(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.all_items_with_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = await response.parse()
        assert_matches_type(ShoppingAllItemsWithMerchantsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_all_items_with_merchants(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.all_items_with_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingAllItemsWithMerchantsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_executions(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.executions(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingExecutionsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_executions_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.executions(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            analysis_filter_type="any",
            analysis_types=["visibility"],
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_count=True,
            include_no_tag=True,
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingExecutionsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_executions(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.executions(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = await response.parse()
        assert_matches_type(ShoppingExecutionsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_executions(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.executions(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingExecutionsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_item_visibility(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.item_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingItemVisibilityResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_item_visibility_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.item_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            competitor_limit=1,
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_competitors=True,
            include_count=True,
            include_items=["string"],
            include_no_tag=True,
            include_position_frequency=True,
            merchant_filter_type="any",
            metrics=["visibility_score"],
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            search_item="search_item",
            tag_filter_type="any",
            target_product="target_product",
        )
        assert_matches_type(ShoppingItemVisibilityResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_item_visibility(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.item_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = await response.parse()
        assert_matches_type(ShoppingItemVisibilityResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_item_visibility(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.item_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingItemVisibilityResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_merchant_by_items(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.merchant_by_items(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingMerchantByItemsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_merchant_by_items_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.merchant_by_items(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_count=True,
            include_no_tag=True,
            metrics=["merchant_visibility"],
            order_by={"foo": "asc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
            product_name="product_name",
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingMerchantByItemsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_merchant_by_items(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.merchant_by_items(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = await response.parse()
        assert_matches_type(ShoppingMerchantByItemsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_merchant_by_items(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.merchant_by_items(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingMerchantByItemsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_merchant_distribution(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.merchant_distribution(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingMerchantDistributionResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_merchant_distribution_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.merchant_distribution(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_count=True,
            include_no_tag=True,
            metrics=["offer_count"],
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            search_merchant="search_merchant",
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingMerchantDistributionResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_merchant_distribution(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.merchant_distribution(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = await response.parse()
        assert_matches_type(ShoppingMerchantDistributionResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_merchant_distribution(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.merchant_distribution(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingMerchantDistributionResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_merchant_share(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.merchant_share(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingMerchantShareResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_merchant_share_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.merchant_share(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_count=True,
            include_no_tag=True,
            metrics=["merchant_share"],
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            tag_filter_type="any",
            target_asset_names=["string"],
        )
        assert_matches_type(ShoppingMerchantShareResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_merchant_share(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.merchant_share(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = await response.parse()
        assert_matches_type(ShoppingMerchantShareResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_merchant_share(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.merchant_share(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingMerchantShareResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_merchant_visibility_by_brand(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.merchant_visibility_by_brand(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingMerchantVisibilityByBrandResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_merchant_visibility_by_brand_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.merchant_visibility_by_brand(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_brand="include_brand",
            include_brand_only=True,
            include_count=True,
            include_no_tag=True,
            metrics=["visibility_score"],
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            search_brand="search_brand",
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingMerchantVisibilityByBrandResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_merchant_visibility_by_brand(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.merchant_visibility_by_brand(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = await response.parse()
        assert_matches_type(ShoppingMerchantVisibilityByBrandResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_merchant_visibility_by_brand(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.merchant_visibility_by_brand(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingMerchantVisibilityByBrandResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_product_merchant_urls(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.product_merchant_urls(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            product_names=["string"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingProductMerchantURLsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_product_merchant_urls(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.product_merchant_urls(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            product_names=["string"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = await response.parse()
        assert_matches_type(ShoppingProductMerchantURLsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_product_merchant_urls(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.product_merchant_urls(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            product_names=["string"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingProductMerchantURLsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_rate(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_rate_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_count=True,
            include_no_tag=True,
            metrics=["total_runs"],
            order_by={"foo": "asc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_trigger_rate(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = await response.parse()
        assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_trigger_rate(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_visibility(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ShoppingVisibilityResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_visibility_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["period"],
            exclude_topic_ids=True,
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include_asset="include_asset",
            include_asset_only=True,
            include_count=True,
            include_no_tag=True,
            include_position_frequency=True,
            metrics=["visibility_score"],
            order_by={"foo": "asc"},
            owned_asset_names=["string"],
            pagination={
                "limit": 1,
                "offset": 0,
            },
            rank_by="visibility_score",
            search_asset="search_asset",
            tag_filter_type="any",
        )
        assert_matches_type(ShoppingVisibilityResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_visibility(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = await response.parse()
        assert_matches_type(ShoppingVisibilityResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_visibility(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingVisibilityResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True
