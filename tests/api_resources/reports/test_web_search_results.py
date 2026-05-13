# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound._utils import parse_datetime
from profound.types.reports import (
    WebSearchResultQueryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebSearchResults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query(self, client: Profound) -> None:
        web_search_result = client.reports.web_search_results.query(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WebSearchResultQueryResponse, web_search_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: Profound) -> None:
        web_search_result = client.reports.web_search_results.query(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["hostname"],
            filters=[
                {
                    "field": "hostname",
                    "operator": "is",
                    "value": "string",
                }
            ],
            order_by={"date": "asc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(WebSearchResultQueryResponse, web_search_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Profound) -> None:
        response = client.reports.web_search_results.with_raw_response.query(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web_search_result = response.parse()
        assert_matches_type(WebSearchResultQueryResponse, web_search_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Profound) -> None:
        with client.reports.web_search_results.with_streaming_response.query(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web_search_result = response.parse()
            assert_matches_type(WebSearchResultQueryResponse, web_search_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream(self, client: Profound) -> None:
        web_search_result_stream = client.reports.web_search_results.stream(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        web_search_result_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_with_all_params(self, client: Profound) -> None:
        web_search_result_stream = client.reports.web_search_results.stream(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["hostname"],
            filters=[
                {
                    "field": "hostname",
                    "operator": "is",
                    "value": "string",
                }
            ],
            order_by={"date": "asc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        web_search_result_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream(self, client: Profound) -> None:
        response = client.reports.web_search_results.with_raw_response.stream(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream(self, client: Profound) -> None:
        with client.reports.web_search_results.with_streaming_response.stream(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncWebSearchResults:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncProfound) -> None:
        web_search_result = await async_client.reports.web_search_results.query(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WebSearchResultQueryResponse, web_search_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncProfound) -> None:
        web_search_result = await async_client.reports.web_search_results.query(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["hostname"],
            filters=[
                {
                    "field": "hostname",
                    "operator": "is",
                    "value": "string",
                }
            ],
            order_by={"date": "asc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(WebSearchResultQueryResponse, web_search_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.web_search_results.with_raw_response.query(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web_search_result = await response.parse()
        assert_matches_type(WebSearchResultQueryResponse, web_search_result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.web_search_results.with_streaming_response.query(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web_search_result = await response.parse()
            assert_matches_type(WebSearchResultQueryResponse, web_search_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream(self, async_client: AsyncProfound) -> None:
        web_search_result_stream = await async_client.reports.web_search_results.stream(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        await web_search_result_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncProfound) -> None:
        web_search_result_stream = await async_client.reports.web_search_results.stream(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["hostname"],
            filters=[
                {
                    "field": "hostname",
                    "operator": "is",
                    "value": "string",
                }
            ],
            order_by={"date": "asc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        await web_search_result_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.web_search_results.with_raw_response.stream(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.web_search_results.with_streaming_response.stream(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
