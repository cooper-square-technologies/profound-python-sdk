# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound._utils import parse_datetime
from profound.types.logs import RawBotsResponse, RawLogsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRaw:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bots(self, client: Profound) -> None:
        raw = client.logs.raw.bots(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RawBotsResponse, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bots_with_all_params(self, client: Profound) -> None:
        raw = client.logs.raw.bots(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="day",
            dimensions=["method"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "bot_name",
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
        assert_matches_type(RawBotsResponse, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bots(self, client: Profound) -> None:
        response = client.logs.raw.with_raw_response.bots(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(RawBotsResponse, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bots(self, client: Profound) -> None:
        with client.logs.raw.with_streaming_response.bots(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(RawBotsResponse, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_logs(self, client: Profound) -> None:
        raw = client.logs.raw.logs(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RawLogsResponse, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_logs_with_all_params(self, client: Profound) -> None:
        raw = client.logs.raw.logs(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="day",
            dimensions=["timestamp"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "method",
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
        assert_matches_type(RawLogsResponse, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_logs(self, client: Profound) -> None:
        response = client.logs.raw.with_raw_response.logs(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = response.parse()
        assert_matches_type(RawLogsResponse, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_logs(self, client: Profound) -> None:
        with client.logs.raw.with_streaming_response.logs(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = response.parse()
            assert_matches_type(RawLogsResponse, raw, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRaw:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bots(self, async_client: AsyncProfound) -> None:
        raw = await async_client.logs.raw.bots(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RawBotsResponse, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bots_with_all_params(self, async_client: AsyncProfound) -> None:
        raw = await async_client.logs.raw.bots(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="day",
            dimensions=["method"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "bot_name",
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
        assert_matches_type(RawBotsResponse, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bots(self, async_client: AsyncProfound) -> None:
        response = await async_client.logs.raw.with_raw_response.bots(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(RawBotsResponse, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bots(self, async_client: AsyncProfound) -> None:
        async with async_client.logs.raw.with_streaming_response.bots(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(RawBotsResponse, raw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_logs(self, async_client: AsyncProfound) -> None:
        raw = await async_client.logs.raw.logs(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RawLogsResponse, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_logs_with_all_params(self, async_client: AsyncProfound) -> None:
        raw = await async_client.logs.raw.logs(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="day",
            dimensions=["timestamp"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "method",
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
        assert_matches_type(RawLogsResponse, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_logs(self, async_client: AsyncProfound) -> None:
        response = await async_client.logs.raw.with_raw_response.logs(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        raw = await response.parse()
        assert_matches_type(RawLogsResponse, raw, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_logs(self, async_client: AsyncProfound) -> None:
        async with async_client.logs.raw.with_streaming_response.logs(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            raw = await response.parse()
            assert_matches_type(RawLogsResponse, raw, path=["response"])

        assert cast(Any, response.is_closed) is True
