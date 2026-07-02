# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types.reports.factcheck import (
    ClaimQueryClaimsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClaims:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_claims(self, client: Profound) -> None:
        claim = client.reports.factcheck.claims.query_claims(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ClaimQueryClaimsResponse, claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_claims_with_all_params(self, client: Profound) -> None:
        claim = client.reports.factcheck.claims.query_claims(
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
            group_by=["model"],
            include=["theme"],
            limit=1,
            max_results=1,
        )
        assert_matches_type(ClaimQueryClaimsResponse, claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query_claims(self, client: Profound) -> None:
        response = client.reports.factcheck.claims.with_raw_response.query_claims(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        claim = response.parse()
        assert_matches_type(ClaimQueryClaimsResponse, claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query_claims(self, client: Profound) -> None:
        with client.reports.factcheck.claims.with_streaming_response.query_claims(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            claim = response.parse()
            assert_matches_type(ClaimQueryClaimsResponse, claim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_claims(self, client: Profound) -> None:
        claim = client.reports.factcheck.claims.stream_claims(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert claim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_claims_with_all_params(self, client: Profound) -> None:
        claim = client.reports.factcheck.claims.stream_claims(
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
            group_by=["model"],
            include=["theme"],
            limit=1,
            max_results=1,
        )
        assert claim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_claims(self, client: Profound) -> None:
        response = client.reports.factcheck.claims.with_raw_response.stream_claims(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        claim = response.parse()
        assert claim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_claims(self, client: Profound) -> None:
        with client.reports.factcheck.claims.with_streaming_response.stream_claims(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            claim = response.parse()
            assert claim is None

        assert cast(Any, response.is_closed) is True


class TestAsyncClaims:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_claims(self, async_client: AsyncProfound) -> None:
        claim = await async_client.reports.factcheck.claims.query_claims(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ClaimQueryClaimsResponse, claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_claims_with_all_params(self, async_client: AsyncProfound) -> None:
        claim = await async_client.reports.factcheck.claims.query_claims(
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
            group_by=["model"],
            include=["theme"],
            limit=1,
            max_results=1,
        )
        assert_matches_type(ClaimQueryClaimsResponse, claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query_claims(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.factcheck.claims.with_raw_response.query_claims(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        claim = await response.parse()
        assert_matches_type(ClaimQueryClaimsResponse, claim, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query_claims(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.factcheck.claims.with_streaming_response.query_claims(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            claim = await response.parse()
            assert_matches_type(ClaimQueryClaimsResponse, claim, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_claims(self, async_client: AsyncProfound) -> None:
        claim = await async_client.reports.factcheck.claims.stream_claims(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert claim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_claims_with_all_params(self, async_client: AsyncProfound) -> None:
        claim = await async_client.reports.factcheck.claims.stream_claims(
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
            group_by=["model"],
            include=["theme"],
            limit=1,
            max_results=1,
        )
        assert claim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_claims(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.factcheck.claims.with_raw_response.stream_claims(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        claim = await response.parse()
        assert claim is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_claims(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.factcheck.claims.with_streaming_response.stream_claims(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            claim = await response.parse()
            assert claim is None

        assert cast(Any, response.is_closed) is True
