# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestReports:
    @smoke_case("reports.citations:required", operation="citations", path="/v1/reports/citations")
    def test_method_citations(self) -> None:
        report = client.reports.citations(
            date_interval="day",
            dimensions=[],
            metrics=["count"],
            order_by={},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
        )

    @smoke_case("reports.citations:all", operation="citations", path="/v1/reports/citations")
    def test_method_citations_with_all_params(self) -> None:
        report = client.reports.citations(
            date_interval="day",
            dimensions=[],
            metrics=["count"],
            order_by={},
            pagination={"limit": 10000, "offset": 0},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            filters=[{"field": "hostname", "operator": "is", "value": ""}],
        )

    @smoke_case("reports.visibility:required", operation="visibility", path="/v1/reports/visibility")
    def test_method_visibility(self) -> None:
        report = client.reports.visibility(
            date_interval="day",
            dimensions=[],
            metrics=["share_of_voice"],
            order_by={},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
        )

    @smoke_case("reports.visibility:all", operation="visibility", path="/v1/reports/visibility")
    def test_method_visibility_with_all_params(self) -> None:
        report = client.reports.visibility(
            date_interval="day",
            dimensions=[],
            metrics=["share_of_voice"],
            order_by={},
            pagination={"limit": 10000, "offset": 0},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            filters=[{"field": "region_id", "operator": "is", "value": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
        )

    @smoke_case("reports.sentiment:required", operation="sentiment", path="/v1/reports/sentiment")
    def test_method_sentiment(self) -> None:
        report = client.reports.sentiment(
            date_interval="day",
            dimensions=[],
            metrics=["positive"],
            order_by={},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
        )

    @smoke_case("reports.sentiment:all", operation="sentiment", path="/v1/reports/sentiment")
    def test_method_sentiment_with_all_params(self) -> None:
        report = client.reports.sentiment(
            date_interval="day",
            dimensions=[],
            metrics=["positive"],
            order_by={},
            pagination={"limit": 10000, "offset": 0},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            filters=[{"field": "asset_id", "operator": "is", "value": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
        )

    @smoke_case("reports.sentimentV2:required", operation="sentimentV2", path="/v1/reports/sentiment-v2")
    def test_method_sentiment_v2(self) -> None:
        report = client.reports.sentiment_v2(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            asset_name="",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            date_bucket="day",
            metrics=["sentiment"],
        )

    @smoke_case("reports.sentimentV2:all", operation="sentimentV2", path="/v1/reports/sentiment-v2")
    def test_method_sentiment_v2_with_all_params(self) -> None:
        report = client.reports.sentiment_v2(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            asset_name="",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            comparison_start_date="2024-01-01T00:00:00.000Z",
            comparison_end_date="2024-01-01T00:00:00.000Z",
            date_bucket="day",
            dimensions=["date"],
            metrics=["sentiment"],
            filters=[{"field": "model_id", "operator": "is", "value": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
            order_by={"occurrence": "desc"},
            pagination={"limit": 10000, "offset": 0},
        )

    @smoke_case("reports.getReferralsReport:required", operation="getReferralsReport", path="/v1/reports/referrals")
    def test_method_get_referrals_report(self) -> None:
        report = client.reports.get_referrals_report(
            date_interval="day",
            dimensions=[],
            metrics=["visits"],
            order_by={},
            domain="",
            start_date="2024-01-01T00:00:00.000Z",
        )

    @smoke_case("reports.getReferralsReport:all", operation="getReferralsReport", path="/v1/reports/referrals")
    def test_method_get_referrals_report_with_all_params(self) -> None:
        report = client.reports.get_referrals_report(
            date_interval="day",
            dimensions=[],
            metrics=["visits"],
            order_by={},
            pagination={"limit": 10000, "offset": 0},
            domain="",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            metric_filters=[{"field": "", "operator": ">", "value": 0}],
            filters=[{"field": "path", "operator": "is", "value": ""}],
        )

    @smoke_case("reports.getBotsReport:required", operation="getBotsReport", path="/v1/reports/bots")
    def test_method_get_bots_report(self) -> None:
        report = client.reports.get_bots_report(
            date_interval="day",
            dimensions=[],
            metrics=["count"],
            order_by={},
            domain="",
            start_date="2024-01-01T00:00:00.000Z",
        )

    @smoke_case("reports.getBotsReport:all", operation="getBotsReport", path="/v1/reports/bots")
    def test_method_get_bots_report_with_all_params(self) -> None:
        report = client.reports.get_bots_report(
            date_interval="day",
            dimensions=[],
            metrics=["count"],
            order_by={},
            pagination={"limit": 10000, "offset": 0},
            domain="",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            metric_filters=[{"field": "", "operator": ">", "value": 0}],
            filters=[{"field": "path", "operator": "is", "value": ""}],
        )

    @smoke_case("reports.queryFanouts:required", operation="queryFanouts", path="/v1/reports/query-fanouts")
    def test_method_query_fanouts(self) -> None:
        report = client.reports.query_fanouts(
            date_interval="day",
            dimensions=[],
            metrics=["fanouts_per_execution"],
            order_by={},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
        )

    @smoke_case("reports.queryFanouts:all", operation="queryFanouts", path="/v1/reports/query-fanouts")
    def test_method_query_fanouts_with_all_params(self) -> None:
        report = client.reports.query_fanouts(
            date_interval="day",
            dimensions=[],
            metrics=["fanouts_per_execution"],
            order_by={},
            pagination={"limit": 10000, "offset": 0},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            filters=[{"field": "region_id", "operator": "is", "value": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
        )

    @smoke_case("reports.streamCitations:required", operation="streamCitations", path="/v1/reports/citations/stream")
    def test_method_stream_citations(self) -> None:
        stream = client.reports.stream_citations(
            date_interval="day",
            dimensions=[],
            metrics=["count"],
            order_by={},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
        )

        for event in stream:
            print(event)

    @smoke_case("reports.streamCitations:all", operation="streamCitations", path="/v1/reports/citations/stream")
    def test_method_stream_citations_with_all_params(self) -> None:
        stream = client.reports.stream_citations(
            date_interval="day",
            dimensions=[],
            metrics=["count"],
            order_by={},
            pagination={"limit": 10000, "offset": 0},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            filters=[{"field": "hostname", "operator": "is", "value": ""}],
        )

        for event in stream:
            print(event)

    @smoke_case("reports.streamVisibility:required", operation="streamVisibility", path="/v1/reports/visibility/stream")
    def test_method_stream_visibility(self) -> None:
        stream = client.reports.stream_visibility(
            date_interval="day",
            dimensions=[],
            metrics=["share_of_voice"],
            order_by={},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
        )

        for event in stream:
            print(event)

    @smoke_case("reports.streamVisibility:all", operation="streamVisibility", path="/v1/reports/visibility/stream")
    def test_method_stream_visibility_with_all_params(self) -> None:
        stream = client.reports.stream_visibility(
            date_interval="day",
            dimensions=[],
            metrics=["share_of_voice"],
            order_by={},
            pagination={"limit": 10000, "offset": 0},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            filters=[{"field": "region_id", "operator": "is", "value": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
        )

        for event in stream:
            print(event)

    @smoke_case("reports.streamSentiment:required", operation="streamSentiment", path="/v1/reports/sentiment/stream")
    def test_method_stream_sentiment(self) -> None:
        stream = client.reports.stream_sentiment(
            date_interval="day",
            dimensions=[],
            metrics=["positive"],
            order_by={},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
        )

        for event in stream:
            print(event)

    @smoke_case("reports.streamSentiment:all", operation="streamSentiment", path="/v1/reports/sentiment/stream")
    def test_method_stream_sentiment_with_all_params(self) -> None:
        stream = client.reports.stream_sentiment(
            date_interval="day",
            dimensions=[],
            metrics=["positive"],
            order_by={},
            pagination={"limit": 10000, "offset": 0},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            filters=[{"field": "asset_id", "operator": "is", "value": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
        )

        for event in stream:
            print(event)

    @smoke_case(
        "reports.streamCitationsV2:required", operation="streamCitationsV2", path="/v2/reports/citations/stream"
    )
    def test_method_stream_citations_v2(self) -> None:
        stream = client.reports.stream_citations_v2(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            entity="domain",
            interval="day",
            scope="all",
        )

        for event in stream:
            print(event)

    @smoke_case("reports.streamCitationsV2:all", operation="streamCitationsV2", path="/v2/reports/citations/stream")
    def test_method_stream_citations_v2_with_all_params(self) -> None:
        stream = client.reports.stream_citations_v2(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            entity="domain",
            group_by=["page"],
            metrics=["count"],
            interval="day",
            scope="all",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

        for event in stream:
            print(event)

    @smoke_case(
        "reports.streamVisibilityV2:required", operation="streamVisibilityV2", path="/v2/reports/visibility/stream"
    )
    def test_method_stream_visibility_v2(self) -> None:
        stream = client.reports.stream_visibility_v2(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            interval="day",
            scope="owned",
        )

        for event in stream:
            print(event)

    @smoke_case("reports.streamVisibilityV2:all", operation="streamVisibilityV2", path="/v2/reports/visibility/stream")
    def test_method_stream_visibility_v2_with_all_params(self) -> None:
        stream = client.reports.stream_visibility_v2(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            metrics=["visibility_score"],
            interval="day",
            scope="owned",
            assets="",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            sort={"field": "visibility_score"},
            limit=1,
            max_results=1,
            cursor="",
        )

        for event in stream:
            print(event)

    @smoke_case(
        "reports.streamSentimentV2:required", operation="streamSentimentV2", path="/v2/reports/sentiment/stream"
    )
    def test_method_stream_sentiment_v2(self) -> None:
        stream = client.reports.stream_sentiment_v2(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            asset="",
            start_date="",
            end_date="",
            source="response",
            interval="day",
            include_cited_websites=False,
        )

        for event in stream:
            print(event)

    @smoke_case("reports.streamSentimentV2:all", operation="streamSentimentV2", path="/v2/reports/sentiment/stream")
    def test_method_stream_sentiment_v2_with_all_params(self) -> None:
        stream = client.reports.stream_sentiment_v2(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            asset="",
            start_date="",
            end_date="",
            comparison_start_date="",
            comparison_end_date="",
            source="response",
            group_by=["date"],
            metrics=["positive_sentiment"],
            interval="day",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            sort={"field": "positive_sentiment", "dir": "desc"},
            include_cited_websites=False,
            limit=1,
            max_results=1,
            cursor="",
        )

        for event in stream:
            print(event)

    @smoke_case(
        "reports.streamQueryFanouts:required", operation="streamQueryFanouts", path="/v2/reports/query-fanouts/stream"
    )
    def test_method_stream_query_fanouts(self) -> None:
        stream = client.reports.stream_query_fanouts(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            interval="day",
        )

        for event in stream:
            print(event)

    @smoke_case(
        "reports.streamQueryFanouts:all", operation="streamQueryFanouts", path="/v2/reports/query-fanouts/stream"
    )
    def test_method_stream_query_fanouts_with_all_params(self) -> None:
        stream = client.reports.stream_query_fanouts(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            metrics=["fanouts_per_execution"],
            interval="day",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            sort={"field": "", "dir": "desc"},
            limit=1,
            max_results=1,
            cursor="",
        )

        for event in stream:
            print(event)

    @smoke_case("reports.getReferralsReportV2:required", operation="getReferralsReportV2", path="/v2/reports/referrals")
    def test_method_get_referrals_report_v2(self) -> None:
        report = client.reports.get_referrals_report_v2(
            date_interval="day",
            dimensions=[],
            metrics=["visits"],
            order_by={},
            domain="",
            start_date="2024-01-01T00:00:00.000Z",
            timezone="UTC",
        )

    @smoke_case("reports.getReferralsReportV2:all", operation="getReferralsReportV2", path="/v2/reports/referrals")
    def test_method_get_referrals_report_v2_with_all_params(self) -> None:
        report = client.reports.get_referrals_report_v2(
            date_interval="day",
            dimensions=[],
            metrics=["visits"],
            order_by={},
            pagination={"limit": 10000, "offset": 0},
            domain="",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            timezone="UTC",
            view_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            metric_filters=[{"field": "", "operator": ">", "value": 0}],
            filters=[{"field": "path", "operator": "is", "value": ""}],
        )

    @smoke_case("reports.getBotsReportV2:required", operation="getBotsReportV2", path="/v2/reports/bots")
    def test_method_get_bots_report_v2(self) -> None:
        report = client.reports.get_bots_report_v2(
            date_interval="day",
            dimensions=[],
            metrics=["count"],
            order_by={},
            domain="",
            start_date="2024-01-01T00:00:00.000Z",
            timezone="UTC",
        )

    @smoke_case("reports.getBotsReportV2:all", operation="getBotsReportV2", path="/v2/reports/bots")
    def test_method_get_bots_report_v2_with_all_params(self) -> None:
        report = client.reports.get_bots_report_v2(
            date_interval="day",
            dimensions=[],
            metrics=["count"],
            order_by={},
            pagination={"limit": 10000, "offset": 0},
            domain="",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            timezone="UTC",
            view_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            metric_filters=[{"field": "", "operator": ">", "value": 0}],
            filters=[{"field": "path", "operator": "is", "value": ""}],
            domain_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            tags=[""],
        )

    @smoke_case("reports.queryVisibility:required", operation="queryVisibility", path="/v2/reports/visibility")
    def test_method_query_visibility(self) -> None:
        report = client.reports.query_visibility(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            interval="day",
            scope="owned",
        )

    @smoke_case("reports.queryVisibility:all", operation="queryVisibility", path="/v2/reports/visibility")
    def test_method_query_visibility_with_all_params(self) -> None:
        report = client.reports.query_visibility(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            metrics=["visibility_score"],
            interval="day",
            scope="owned",
            assets="",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            sort={"field": "visibility_score"},
            limit=1,
            max_results=1,
            cursor="",
        )

    @smoke_case("reports.queryCitations:required", operation="queryCitations", path="/v2/reports/citations")
    def test_method_query_citations(self) -> None:
        report = client.reports.query_citations(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            entity="domain",
            interval="day",
            scope="all",
        )

    @smoke_case("reports.queryCitations:all", operation="queryCitations", path="/v2/reports/citations")
    def test_method_query_citations_with_all_params(self) -> None:
        report = client.reports.query_citations(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            entity="domain",
            group_by=["page"],
            metrics=["count"],
            interval="day",
            scope="all",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

    @smoke_case("reports.querySentiment:required", operation="querySentiment", path="/v2/reports/sentiment")
    def test_method_query_sentiment(self) -> None:
        report = client.reports.query_sentiment(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            asset="",
            start_date="",
            end_date="",
            source="response",
            interval="day",
            include_cited_websites=False,
        )

    @smoke_case("reports.querySentiment:all", operation="querySentiment", path="/v2/reports/sentiment")
    def test_method_query_sentiment_with_all_params(self) -> None:
        report = client.reports.query_sentiment(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            asset="",
            start_date="",
            end_date="",
            comparison_start_date="",
            comparison_end_date="",
            source="response",
            group_by=["date"],
            metrics=["positive_sentiment"],
            interval="day",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            sort={"field": "positive_sentiment", "dir": "desc"},
            include_cited_websites=False,
            limit=1,
            max_results=1,
            cursor="",
        )

    @smoke_case("reports.queryQueryFanouts:required", operation="queryQueryFanouts", path="/v2/reports/query-fanouts")
    def test_method_query_query_fanouts(self) -> None:
        report = client.reports.query_query_fanouts(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            interval="day",
        )

    @smoke_case("reports.queryQueryFanouts:all", operation="queryQueryFanouts", path="/v2/reports/query-fanouts")
    def test_method_query_query_fanouts_with_all_params(self) -> None:
        report = client.reports.query_query_fanouts(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            metrics=["fanouts_per_execution"],
            interval="day",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            sort={"field": "", "dir": "desc"},
            limit=1,
            max_results=1,
            cursor="",
        )
