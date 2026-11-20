# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestWebSearchResults:
    @smoke_case("reports.webSearchResults.query:required", operation="query", path="/v1/reports/web-search-results")
    def test_method_query(self) -> None:
        web_search_result = client.reports.web_search_results.query(
            date_interval="day",
            dimensions=[],
            metrics=["count"],
            order_by={},
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
        )

    @smoke_case("reports.webSearchResults.query:all", operation="query", path="/v1/reports/web-search-results")
    def test_method_query_with_all_params(self) -> None:
        web_search_result = client.reports.web_search_results.query(
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

    @smoke_case(
        "reports.webSearchResults.stream:required", operation="stream", path="/v1/reports/web-search-results/stream"
    )
    def test_method_stream(self) -> None:
        stream = client.reports.web_search_results.stream(
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

    @smoke_case("reports.webSearchResults.stream:all", operation="stream", path="/v1/reports/web-search-results/stream")
    def test_method_stream_with_all_params(self) -> None:
        stream = client.reports.web_search_results.stream(
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
