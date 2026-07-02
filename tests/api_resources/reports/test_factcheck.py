# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types.reports import (
    FactcheckQueryScoresResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFactcheck:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_scores(self, client: Profound) -> None:
        factcheck = client.reports.factcheck.query_scores(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(FactcheckQueryScoresResponse, factcheck, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_scores_with_all_params(self, client: Profound) -> None:
        factcheck = client.reports.factcheck.query_scores(
            category_id="category_id",
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
            limit=1,
            max_results=1,
        )
        assert_matches_type(FactcheckQueryScoresResponse, factcheck, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query_scores(self, client: Profound) -> None:
        response = client.reports.factcheck.with_raw_response.query_scores(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        factcheck = response.parse()
        assert_matches_type(FactcheckQueryScoresResponse, factcheck, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query_scores(self, client: Profound) -> None:
        with client.reports.factcheck.with_streaming_response.query_scores(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            factcheck = response.parse()
            assert_matches_type(FactcheckQueryScoresResponse, factcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_scores(self, client: Profound) -> None:
        factcheck = client.reports.factcheck.stream_scores(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert factcheck is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_scores_with_all_params(self, client: Profound) -> None:
        factcheck = client.reports.factcheck.stream_scores(
            category_id="category_id",
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
            limit=1,
            max_results=1,
        )
        assert factcheck is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_scores(self, client: Profound) -> None:
        response = client.reports.factcheck.with_raw_response.stream_scores(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        factcheck = response.parse()
        assert factcheck is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_scores(self, client: Profound) -> None:
        with client.reports.factcheck.with_streaming_response.stream_scores(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            factcheck = response.parse()
            assert factcheck is None

        assert cast(Any, response.is_closed) is True


class TestAsyncFactcheck:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_scores(self, async_client: AsyncProfound) -> None:
        factcheck = await async_client.reports.factcheck.query_scores(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(FactcheckQueryScoresResponse, factcheck, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_scores_with_all_params(self, async_client: AsyncProfound) -> None:
        factcheck = await async_client.reports.factcheck.query_scores(
            category_id="category_id",
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
            limit=1,
            max_results=1,
        )
        assert_matches_type(FactcheckQueryScoresResponse, factcheck, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query_scores(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.factcheck.with_raw_response.query_scores(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        factcheck = await response.parse()
        assert_matches_type(FactcheckQueryScoresResponse, factcheck, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query_scores(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.factcheck.with_streaming_response.query_scores(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            factcheck = await response.parse()
            assert_matches_type(FactcheckQueryScoresResponse, factcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_scores(self, async_client: AsyncProfound) -> None:
        factcheck = await async_client.reports.factcheck.stream_scores(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert factcheck is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_scores_with_all_params(self, async_client: AsyncProfound) -> None:
        factcheck = await async_client.reports.factcheck.stream_scores(
            category_id="category_id",
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
            limit=1,
            max_results=1,
        )
        assert factcheck is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_scores(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.factcheck.with_raw_response.stream_scores(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        factcheck = await response.parse()
        assert factcheck is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_scores(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.factcheck.with_streaming_response.stream_scores(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            factcheck = await response.parse()
            assert factcheck is None

        assert cast(Any, response.is_closed) is True
