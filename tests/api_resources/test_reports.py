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
    ReportSentimentV2Response,
    ReportQueryCitationsResponse,
    ReportQuerySentimentResponse,
    ReportQueryVisibilityResponse,
    ReportQueryQueryFanoutsResponse,
)
from profound._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_citations(self, client: Profound) -> None:
        report = client.reports.citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_citations_with_all_params(self, client: Profound) -> None:
        report = client.reports.citations(
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
        assert_matches_type(ReportCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_bots_report(self, client: Profound) -> None:
        report = client.reports.get_bots_report(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_bots_report_with_all_params(self, client: Profound) -> None:
        report = client.reports.get_bots_report(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["date"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "path",
                    "operator": "is",
                    "value": "string",
                }
            ],
            metric_filters=[
                {
                    "field": "field",
                    "operator": ">",
                    "value": 0,
                }
            ],
            order_by={"date": "asc"},
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_bots_report(self, client: Profound) -> None:
        response = client.reports.with_raw_response.get_bots_report(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_bots_report(self, client: Profound) -> None:
        with client.reports.with_streaming_response.get_bots_report(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_bots_report_v2(self, client: Profound) -> None:
        report = client.reports.get_bots_report_v2(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_bots_report_v2_with_all_params(self, client: Profound) -> None:
        report = client.reports.get_bots_report_v2(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["date"],
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "path",
                    "operator": "is",
                    "value": "string",
                }
            ],
            metric_filters=[
                {
                    "field": "field",
                    "operator": ">",
                    "value": 0,
                }
            ],
            order_by={"date": "asc"},
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "limit": 1,
                "offset": 0,
            },
            tags=["string"],
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_bots_report_v2(self, client: Profound) -> None:
        response = client.reports.with_raw_response.get_bots_report_v2(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_bots_report_v2(self, client: Profound) -> None:
        with client.reports.with_streaming_response.get_bots_report_v2(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_referrals_report(self, client: Profound) -> None:
        report = client.reports.get_referrals_report(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_referrals_report_with_all_params(self, client: Profound) -> None:
        report = client.reports.get_referrals_report(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["date"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "path",
                    "operator": "is",
                    "value": "string",
                }
            ],
            metric_filters=[
                {
                    "field": "field",
                    "operator": ">",
                    "value": 0,
                }
            ],
            order_by={"date": "asc"},
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_referrals_report(self, client: Profound) -> None:
        response = client.reports.with_raw_response.get_referrals_report(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_referrals_report(self, client: Profound) -> None:
        with client.reports.with_streaming_response.get_referrals_report(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_referrals_report_v2(self, client: Profound) -> None:
        report = client.reports.get_referrals_report_v2(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_referrals_report_v2_with_all_params(self, client: Profound) -> None:
        report = client.reports.get_referrals_report_v2(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["date"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "path",
                    "operator": "is",
                    "value": "string",
                }
            ],
            metric_filters=[
                {
                    "field": "field",
                    "operator": ">",
                    "value": 0,
                }
            ],
            order_by={"date": "asc"},
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_referrals_report_v2(self, client: Profound) -> None:
        response = client.reports.with_raw_response.get_referrals_report_v2(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_referrals_report_v2(self, client: Profound) -> None:
        with client.reports.with_streaming_response.get_referrals_report_v2(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_citations(self, client: Profound) -> None:
        report = client.reports.query_citations(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ReportQueryCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_citations_with_all_params(self, client: Profound) -> None:
        report = client.reports.query_citations(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            entity="domain",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["page"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["count"],
            scope="all",
        )
        assert_matches_type(ReportQueryCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query_citations(self, client: Profound) -> None:
        response = client.reports.with_raw_response.query_citations(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportQueryCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query_citations(self, client: Profound) -> None:
        with client.reports.with_streaming_response.query_citations(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportQueryCitationsResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_fanouts(self, client: Profound) -> None:
        report = client.reports.query_fanouts(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["fanouts_per_execution"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_fanouts_with_all_params(self, client: Profound) -> None:
        report = client.reports.query_fanouts(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["fanouts_per_execution"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["prompt"],
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            order_by={"fanouts_per_execution": "desc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query_fanouts(self, client: Profound) -> None:
        response = client.reports.with_raw_response.query_fanouts(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["fanouts_per_execution"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query_fanouts(self, client: Profound) -> None:
        with client.reports.with_streaming_response.query_fanouts(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["fanouts_per_execution"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_query_fanouts(self, client: Profound) -> None:
        report = client.reports.query_query_fanouts(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ReportQueryQueryFanoutsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_query_fanouts_with_all_params(self, client: Profound) -> None:
        report = client.reports.query_query_fanouts(
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
            interval="day",
            limit=1,
            max_results=1,
            metrics=["fanouts_per_execution"],
            sort={
                "field": "field",
                "dir": "asc",
            },
        )
        assert_matches_type(ReportQueryQueryFanoutsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query_query_fanouts(self, client: Profound) -> None:
        response = client.reports.with_raw_response.query_query_fanouts(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportQueryQueryFanoutsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query_query_fanouts(self, client: Profound) -> None:
        with client.reports.with_streaming_response.query_query_fanouts(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportQueryQueryFanoutsResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_sentiment(self, client: Profound) -> None:
        report = client.reports.query_sentiment(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ReportQuerySentimentResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_sentiment_with_all_params(self, client: Profound) -> None:
        report = client.reports.query_sentiment(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            include_cited_websites=True,
            interval="day",
            limit=1,
            max_results=1,
            metrics=["positive_sentiment"],
            sort={
                "dir": "asc",
                "field": "occurrence",
            },
        )
        assert_matches_type(ReportQuerySentimentResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query_sentiment(self, client: Profound) -> None:
        response = client.reports.with_raw_response.query_sentiment(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportQuerySentimentResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query_sentiment(self, client: Profound) -> None:
        with client.reports.with_streaming_response.query_sentiment(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportQuerySentimentResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_visibility(self, client: Profound) -> None:
        report = client.reports.query_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ReportQueryVisibilityResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_visibility_with_all_params(self, client: Profound) -> None:
        report = client.reports.query_visibility(
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
            sort={"field": "visibility_score"},
        )
        assert_matches_type(ReportQueryVisibilityResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query_visibility(self, client: Profound) -> None:
        response = client.reports.with_raw_response.query_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportQueryVisibilityResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query_visibility(self, client: Profound) -> None:
        with client.reports.with_streaming_response.query_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportQueryVisibilityResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sentiment(self, client: Profound) -> None:
        report = client.reports.sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sentiment_with_all_params(self, client: Profound) -> None:
        report = client.reports.sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["theme"],
            filters=[
                {
                    "field": "asset_id",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sentiment_v2(self, client: Profound) -> None:
        report = client.reports.sentiment_v2(
            asset_name="asset_name",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["sentiment"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportSentimentV2Response, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sentiment_v2_with_all_params(self, client: Profound) -> None:
        report = client.reports.sentiment_v2(
            asset_name="asset_name",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["sentiment"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_bucket="day",
            dimensions=["date"],
            filters=[
                {
                    "field": "model_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            order_by={"occurrence": "desc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(ReportSentimentV2Response, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sentiment_v2(self, client: Profound) -> None:
        response = client.reports.with_raw_response.sentiment_v2(
            asset_name="asset_name",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["sentiment"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportSentimentV2Response, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sentiment_v2(self, client: Profound) -> None:
        with client.reports.with_streaming_response.sentiment_v2(
            asset_name="asset_name",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["sentiment"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportSentimentV2Response, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_citations(self, client: Profound) -> None:
        report_stream = client.reports.stream_citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        report_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_citations_with_all_params(self, client: Profound) -> None:
        report_stream = client.reports.stream_citations(
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
        report_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_citations(self, client: Profound) -> None:
        response = client.reports.with_raw_response.stream_citations(
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
    def test_streaming_response_stream_citations(self, client: Profound) -> None:
        with client.reports.with_streaming_response.stream_citations(
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_citations_v2(self, client: Profound) -> None:
        report = client.reports.stream_citations_v2(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_citations_v2_with_all_params(self, client: Profound) -> None:
        report = client.reports.stream_citations_v2(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            entity="domain",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["page"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["count"],
            scope="all",
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_citations_v2(self, client: Profound) -> None:
        response = client.reports.with_raw_response.stream_citations_v2(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_citations_v2(self, client: Profound) -> None:
        with client.reports.with_streaming_response.stream_citations_v2(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert report is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_query_fanouts(self, client: Profound) -> None:
        report = client.reports.stream_query_fanouts(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_query_fanouts_with_all_params(self, client: Profound) -> None:
        report = client.reports.stream_query_fanouts(
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
            interval="day",
            limit=1,
            max_results=1,
            metrics=["fanouts_per_execution"],
            sort={
                "field": "field",
                "dir": "asc",
            },
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_query_fanouts(self, client: Profound) -> None:
        response = client.reports.with_raw_response.stream_query_fanouts(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_query_fanouts(self, client: Profound) -> None:
        with client.reports.with_streaming_response.stream_query_fanouts(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert report is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_sentiment(self, client: Profound) -> None:
        report_stream = client.reports.stream_sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        report_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_sentiment_with_all_params(self, client: Profound) -> None:
        report_stream = client.reports.stream_sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["theme"],
            filters=[
                {
                    "field": "asset_id",
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
        report_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_sentiment(self, client: Profound) -> None:
        response = client.reports.with_raw_response.stream_sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_sentiment(self, client: Profound) -> None:
        with client.reports.with_streaming_response.stream_sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_sentiment_v2(self, client: Profound) -> None:
        report = client.reports.stream_sentiment_v2(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_sentiment_v2_with_all_params(self, client: Profound) -> None:
        report = client.reports.stream_sentiment_v2(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            include_cited_websites=True,
            interval="day",
            limit=1,
            max_results=1,
            metrics=["positive_sentiment"],
            sort={
                "dir": "asc",
                "field": "occurrence",
            },
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_sentiment_v2(self, client: Profound) -> None:
        response = client.reports.with_raw_response.stream_sentiment_v2(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_sentiment_v2(self, client: Profound) -> None:
        with client.reports.with_streaming_response.stream_sentiment_v2(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert report is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_visibility(self, client: Profound) -> None:
        report_stream = client.reports.stream_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        report_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_visibility_with_all_params(self, client: Profound) -> None:
        report_stream = client.reports.stream_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
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
        report_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_visibility(self, client: Profound) -> None:
        response = client.reports.with_raw_response.stream_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_visibility(self, client: Profound) -> None:
        with client.reports.with_streaming_response.stream_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_visibility_v2(self, client: Profound) -> None:
        report = client.reports.stream_visibility_v2(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_visibility_v2_with_all_params(self, client: Profound) -> None:
        report = client.reports.stream_visibility_v2(
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
            sort={"field": "visibility_score"},
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_visibility_v2(self, client: Profound) -> None:
        response = client.reports.with_raw_response.stream_visibility_v2(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_visibility_v2(self, client: Profound) -> None:
        with client.reports.with_streaming_response.stream_visibility_v2(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert report is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_visibility(self, client: Profound) -> None:
        report = client.reports.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_visibility_with_all_params(self, client: Profound) -> None:
        report = client.reports.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_citations(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_citations_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.citations(
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
        assert_matches_type(ReportCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_bots_report(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.get_bots_report(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_bots_report_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.get_bots_report(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["date"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "path",
                    "operator": "is",
                    "value": "string",
                }
            ],
            metric_filters=[
                {
                    "field": "field",
                    "operator": ">",
                    "value": 0,
                }
            ],
            order_by={"date": "asc"},
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_bots_report(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.get_bots_report(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_bots_report(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.get_bots_report(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_bots_report_v2(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.get_bots_report_v2(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_bots_report_v2_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.get_bots_report_v2(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["date"],
            domain_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "path",
                    "operator": "is",
                    "value": "string",
                }
            ],
            metric_filters=[
                {
                    "field": "field",
                    "operator": ">",
                    "value": 0,
                }
            ],
            order_by={"date": "asc"},
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "limit": 1,
                "offset": 0,
            },
            tags=["string"],
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_bots_report_v2(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.get_bots_report_v2(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_bots_report_v2(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.get_bots_report_v2(
            domain="domain",
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_referrals_report(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.get_referrals_report(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_referrals_report_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.get_referrals_report(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["date"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "path",
                    "operator": "is",
                    "value": "string",
                }
            ],
            metric_filters=[
                {
                    "field": "field",
                    "operator": ">",
                    "value": 0,
                }
            ],
            order_by={"date": "asc"},
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_referrals_report(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.get_referrals_report(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_referrals_report(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.get_referrals_report(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_referrals_report_v2(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.get_referrals_report_v2(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_referrals_report_v2_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.get_referrals_report_v2(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["date"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "path",
                    "operator": "is",
                    "value": "string",
                }
            ],
            metric_filters=[
                {
                    "field": "field",
                    "operator": ">",
                    "value": 0,
                }
            ],
            order_by={"date": "asc"},
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_referrals_report_v2(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.get_referrals_report_v2(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_referrals_report_v2(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.get_referrals_report_v2(
            domain="domain",
            metrics=["visits"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_citations(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.query_citations(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ReportQueryCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_citations_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.query_citations(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            entity="domain",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["page"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["count"],
            scope="all",
        )
        assert_matches_type(ReportQueryCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query_citations(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.query_citations(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportQueryCitationsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query_citations(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.query_citations(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportQueryCitationsResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_fanouts(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.query_fanouts(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["fanouts_per_execution"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_fanouts_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.query_fanouts(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["fanouts_per_execution"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["prompt"],
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            order_by={"fanouts_per_execution": "desc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query_fanouts(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.query_fanouts(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["fanouts_per_execution"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query_fanouts(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.query_fanouts(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["fanouts_per_execution"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_query_fanouts(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.query_query_fanouts(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ReportQueryQueryFanoutsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_query_fanouts_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.query_query_fanouts(
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
            interval="day",
            limit=1,
            max_results=1,
            metrics=["fanouts_per_execution"],
            sort={
                "field": "field",
                "dir": "asc",
            },
        )
        assert_matches_type(ReportQueryQueryFanoutsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query_query_fanouts(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.query_query_fanouts(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportQueryQueryFanoutsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query_query_fanouts(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.query_query_fanouts(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportQueryQueryFanoutsResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_sentiment(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.query_sentiment(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ReportQuerySentimentResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_sentiment_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.query_sentiment(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            include_cited_websites=True,
            interval="day",
            limit=1,
            max_results=1,
            metrics=["positive_sentiment"],
            sort={
                "dir": "asc",
                "field": "occurrence",
            },
        )
        assert_matches_type(ReportQuerySentimentResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query_sentiment(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.query_sentiment(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportQuerySentimentResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query_sentiment(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.query_sentiment(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportQuerySentimentResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_visibility(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.query_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(ReportQueryVisibilityResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_visibility_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.query_visibility(
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
            sort={"field": "visibility_score"},
        )
        assert_matches_type(ReportQueryVisibilityResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query_visibility(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.query_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportQueryVisibilityResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query_visibility(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.query_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportQueryVisibilityResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sentiment(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sentiment_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["theme"],
            filters=[
                {
                    "field": "asset_id",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sentiment_v2(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.sentiment_v2(
            asset_name="asset_name",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["sentiment"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportSentimentV2Response, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sentiment_v2_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.sentiment_v2(
            asset_name="asset_name",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["sentiment"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comparison_start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_bucket="day",
            dimensions=["date"],
            filters=[
                {
                    "field": "model_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            order_by={"occurrence": "desc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(ReportSentimentV2Response, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sentiment_v2(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.sentiment_v2(
            asset_name="asset_name",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["sentiment"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportSentimentV2Response, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sentiment_v2(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.sentiment_v2(
            asset_name="asset_name",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["sentiment"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportSentimentV2Response, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_citations(self, async_client: AsyncProfound) -> None:
        report_stream = await async_client.reports.stream_citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["count"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        await report_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_citations_with_all_params(self, async_client: AsyncProfound) -> None:
        report_stream = await async_client.reports.stream_citations(
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
        await report_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_citations(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.stream_citations(
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
    async def test_streaming_response_stream_citations(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.stream_citations(
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_citations_v2(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.stream_citations_v2(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_citations_v2_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.stream_citations_v2(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            entity="domain",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["page"],
            interval="day",
            limit=1,
            max_results=1,
            metrics=["count"],
            scope="all",
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_citations_v2(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.stream_citations_v2(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_citations_v2(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.stream_citations_v2(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert report is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_query_fanouts(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.stream_query_fanouts(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_query_fanouts_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.stream_query_fanouts(
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
            interval="day",
            limit=1,
            max_results=1,
            metrics=["fanouts_per_execution"],
            sort={
                "field": "field",
                "dir": "asc",
            },
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_query_fanouts(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.stream_query_fanouts(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_query_fanouts(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.stream_query_fanouts(
            category_id="category_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert report is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_sentiment(self, async_client: AsyncProfound) -> None:
        report_stream = await async_client.reports.stream_sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        await report_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_sentiment_with_all_params(self, async_client: AsyncProfound) -> None:
        report_stream = await async_client.reports.stream_sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["theme"],
            filters=[
                {
                    "field": "asset_id",
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
        await report_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_sentiment(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.stream_sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_sentiment(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.stream_sentiment(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["positive"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_sentiment_v2(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.stream_sentiment_v2(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_sentiment_v2_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.stream_sentiment_v2(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["date"],
            include_cited_websites=True,
            interval="day",
            limit=1,
            max_results=1,
            metrics=["positive_sentiment"],
            sort={
                "dir": "asc",
                "field": "occurrence",
            },
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_sentiment_v2(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.stream_sentiment_v2(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_sentiment_v2(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.stream_sentiment_v2(
            asset="asset",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert report is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_visibility(self, async_client: AsyncProfound) -> None:
        report_stream = await async_client.reports.stream_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        await report_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_visibility_with_all_params(self, async_client: AsyncProfound) -> None:
        report_stream = await async_client.reports.stream_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
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
        await report_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_visibility(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.stream_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_visibility(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.stream_visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_visibility_v2(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.stream_visibility_v2(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_visibility_v2_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.stream_visibility_v2(
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
            sort={"field": "visibility_score"},
        )
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_visibility_v2(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.with_raw_response.stream_visibility_v2(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert report is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_visibility_v2(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.with_streaming_response.stream_visibility_v2(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert report is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_visibility(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ReportResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_visibility_with_all_params(self, async_client: AsyncProfound) -> None:
        report = await async_client.reports.visibility(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["share_of_voice"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
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
