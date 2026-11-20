# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestClaims:
    @smoke_case(
        "reports.factcheck.claims.queryClaims:required", operation="queryClaims", path="/v2/reports/factcheck/claims"
    )
    def test_method_query_claims(self) -> None:
        claim = client.reports.factcheck.claims.query_claims(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
        )

    @smoke_case(
        "reports.factcheck.claims.queryClaims:all", operation="queryClaims", path="/v2/reports/factcheck/claims"
    )
    def test_method_query_claims_with_all_params(self) -> None:
        claim = client.reports.factcheck.claims.query_claims(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["model"],
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            include=["theme"],
            limit=1,
            max_results=1,
            cursor="",
        )

    @smoke_case(
        "reports.factcheck.claims.streamClaims:required",
        operation="streamClaims",
        path="/v2/reports/factcheck/claims/stream",
    )
    def test_method_stream_claims(self) -> None:
        stream = client.reports.factcheck.claims.stream_claims(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
        )

        for event in stream:
            print(event)

    @smoke_case(
        "reports.factcheck.claims.streamClaims:all",
        operation="streamClaims",
        path="/v2/reports/factcheck/claims/stream",
    )
    def test_method_stream_claims_with_all_params(self) -> None:
        stream = client.reports.factcheck.claims.stream_claims(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            group_by=["model"],
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            include=["theme"],
            limit=1,
            max_results=1,
            cursor="",
        )

        for event in stream:
            print(event)
