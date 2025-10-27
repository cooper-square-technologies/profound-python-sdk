# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types import (
    ReportResponse,
    ReportCitationsResponse,
)
from profound._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_citations(self, client: Profound) -> None:
        report = client.reports.citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_citations_with_all_params(self, client: Profound) -> None:
        report = client.reports.citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="day",
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
        assert_matches_type(ReportCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_citations(self, client: Profound) -> None:
        response = client.reports.with_raw_response.citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_citations(self, client: Profound) -> None:
        with client.reports.with_streaming_response.citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportCitationsResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_sentiment(self, client: Profound) -> None:
        report = client.reports.sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_sentiment_with_all_params(self, client: Profound) -> None:
        report = client.reports.sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="day",
            dimensions=["theme"],
            filters=[
                {
                    "field": "asset_name",
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
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_sentiment(self, client: Profound) -> None:
        response = client.reports.with_raw_response.sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_sentiment(self, client: Profound) -> None:
        with client.reports.with_streaming_response.sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_visibility(self, client: Profound) -> None:
        report = client.reports.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_visibility_with_all_params(self, client: Profound) -> None:
        report = client.reports.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="day",
            dimensions=["date"],
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            order_by={"date": "asc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_visibility(self, client: Profound) -> None:
        response = client.reports.with_raw_response.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_visibility(self, client: Profound) -> None:
        with client.reports.with_streaming_response.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_citations(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_citations_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="day",
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
        assert_matches_type(ReportCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_citations(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_citations(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportCitationsResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_sentiment(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_sentiment_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="day",
            dimensions=["theme"],
            filters=[
                {
                    "field": "asset_name",
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
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_sentiment(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_sentiment(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_visibility(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_visibility_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="day",
            dimensions=["date"],
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            order_by={"date": "asc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_visibility(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_visibility(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True
