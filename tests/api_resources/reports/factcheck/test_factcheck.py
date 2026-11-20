# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestFactcheck:
    @smoke_case("reports.factcheck.queryScores:required", operation="queryScores", path="/v2/reports/factcheck")
    def test_method_query_scores(self) -> None:
        factcheck = client.reports.factcheck.query_scores(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
        )

    @smoke_case("reports.factcheck.queryScores:all", operation="queryScores", path="/v2/reports/factcheck")
    def test_method_query_scores_with_all_params(self) -> None:
        factcheck = client.reports.factcheck.query_scores(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

    @smoke_case(
        "reports.factcheck.streamScores:required", operation="streamScores", path="/v2/reports/factcheck/stream"
    )
    def test_method_stream_scores(self) -> None:
        stream = client.reports.factcheck.stream_scores(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
        )

        for event in stream:
            print(event)

    @smoke_case("reports.factcheck.streamScores:all", operation="streamScores", path="/v2/reports/factcheck/stream")
    def test_method_stream_scores_with_all_params(self) -> None:
        stream = client.reports.factcheck.stream_scores(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["date"],
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

        for event in stream:
            print(event)
