# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types.reports import (
    ShoppingBrandsResponse,
    ShoppingProductsResponse,
    ShoppingMerchantsResponse,
    ShoppingTriggerRateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShopping:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_brands(self, client: Profound) -> None:
        shopping = client.reports.shopping.brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ShoppingBrandsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_brands_with_all_params(self, client: Profound) -> None:
        shopping = client.reports.shopping.brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            assets="string",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["visibility_score"],
            scope="owned",
        )
        assert_matches_type(ShoppingBrandsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_brands(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = response.parse()
        assert_matches_type(ShoppingBrandsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_brands(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingBrandsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_merchants(self, client: Profound) -> None:
        shopping = client.reports.shopping.merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ShoppingMerchantsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_merchants_with_all_params(self, client: Profound) -> None:
        shopping = client.reports.shopping.merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["merchant_share"],
        )
        assert_matches_type(ShoppingMerchantsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_merchants(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = response.parse()
        assert_matches_type(ShoppingMerchantsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_merchants(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingMerchantsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_products(self, client: Profound) -> None:
        shopping = client.reports.shopping.products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ShoppingProductsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_products_with_all_params(self, client: Profound) -> None:
        shopping = client.reports.shopping.products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            competitor_limit=1,
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            include_merchants=True,
            interval="day",
            limit=1,
            max_results=1,
            metrics=["visibility_score"],
            target_product="x",
        )
        assert_matches_type(ShoppingProductsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_products(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = response.parse()
        assert_matches_type(ShoppingProductsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_products(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingProductsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_brands(self, client: Profound) -> None:
        shopping_stream = client.reports.shopping.stream_brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        shopping_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_brands_with_all_params(self, client: Profound) -> None:
        shopping_stream = client.reports.shopping.stream_brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            assets="string",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["visibility_score"],
            scope="owned",
        )
        shopping_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_brands(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.stream_brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_brands(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.stream_brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_merchants(self, client: Profound) -> None:
        shopping_stream = client.reports.shopping.stream_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        shopping_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_merchants_with_all_params(self, client: Profound) -> None:
        shopping_stream = client.reports.shopping.stream_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["merchant_share"],
        )
        shopping_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_merchants(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.stream_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_merchants(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.stream_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_products(self, client: Profound) -> None:
        shopping_stream = client.reports.shopping.stream_products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        shopping_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_products_with_all_params(self, client: Profound) -> None:
        shopping_stream = client.reports.shopping.stream_products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            competitor_limit=1,
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            include_merchants=True,
            interval="day",
            limit=1,
            max_results=1,
            metrics=["visibility_score"],
            target_product="x",
        )
        shopping_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_products(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.stream_products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_products(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.stream_products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_trigger_rate(self, client: Profound) -> None:
        shopping_stream = client.reports.shopping.stream_trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        shopping_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_trigger_rate_with_all_params(self, client: Profound) -> None:
        shopping_stream = client.reports.shopping.stream_trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["total_runs"],
        )
        shopping_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_trigger_rate(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.stream_trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_trigger_rate(self, client: Profound) -> None:
        with client.reports.shopping.with_streaming_response.stream_trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_rate(self, client: Profound) -> None:
        shopping = client.reports.shopping.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_rate_with_all_params(self, client: Profound) -> None:
        shopping = client.reports.shopping.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["total_runs"],
        )
        assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_trigger_rate(self, client: Profound) -> None:
        response = client.reports.shopping.with_raw_response.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
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
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = response.parse()
            assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShopping:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_brands(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ShoppingBrandsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_brands_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            assets="string",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["visibility_score"],
            scope="owned",
        )
        assert_matches_type(ShoppingBrandsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_brands(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = await response.parse()
        assert_matches_type(ShoppingBrandsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_brands(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingBrandsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_merchants(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ShoppingMerchantsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_merchants_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["merchant_share"],
        )
        assert_matches_type(ShoppingMerchantsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_merchants(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = await response.parse()
        assert_matches_type(ShoppingMerchantsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_merchants(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingMerchantsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_products(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ShoppingProductsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_products_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            competitor_limit=1,
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            include_merchants=True,
            interval="day",
            limit=1,
            max_results=1,
            metrics=["visibility_score"],
            target_product="x",
        )
        assert_matches_type(ShoppingProductsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_products(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shopping = await response.parse()
        assert_matches_type(ShoppingProductsResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_products(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingProductsResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_brands(self, async_client: AsyncProfound) -> None:
        shopping_stream = await async_client.reports.shopping.stream_brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        await shopping_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_brands_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping_stream = await async_client.reports.shopping.stream_brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            assets="string",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["visibility_score"],
            scope="owned",
        )
        await shopping_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_brands(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.stream_brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_brands(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.stream_brands(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_merchants(self, async_client: AsyncProfound) -> None:
        shopping_stream = await async_client.reports.shopping.stream_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        await shopping_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_merchants_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping_stream = await async_client.reports.shopping.stream_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["merchant_share"],
        )
        await shopping_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_merchants(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.stream_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_merchants(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.stream_merchants(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_products(self, async_client: AsyncProfound) -> None:
        shopping_stream = await async_client.reports.shopping.stream_products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        await shopping_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_products_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping_stream = await async_client.reports.shopping.stream_products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            competitor_limit=1,
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            include_merchants=True,
            interval="day",
            limit=1,
            max_results=1,
            metrics=["visibility_score"],
            target_product="x",
        )
        await shopping_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_products(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.stream_products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_products(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.stream_products(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_trigger_rate(self, async_client: AsyncProfound) -> None:
        shopping_stream = await async_client.reports.shopping.stream_trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        await shopping_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_trigger_rate_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping_stream = await async_client.reports.shopping.stream_trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["total_runs"],
        )
        await shopping_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_trigger_rate(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.stream_trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_trigger_rate(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.shopping.with_streaming_response.stream_trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_rate(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_rate_with_all_params(self, async_client: AsyncProfound) -> None:
        shopping = await async_client.reports.shopping.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["total_runs"],
        )
        assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_trigger_rate(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.shopping.with_raw_response.trigger_rate(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
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
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shopping = await response.parse()
            assert_matches_type(ShoppingTriggerRateResponse, shopping, path=["response"])

        assert cast(Any, response.is_closed) is True
