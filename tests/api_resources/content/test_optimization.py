# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestOptimization:
    @smoke_case("content.optimization.list:single", operation="list", path="/v1/content/{asset_id}/optimization")
    def test_method_list(self) -> None:
        content_optimizations = client.content.optimization.list(
            asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            limit=10000,
            offset=0,
        )

    @smoke_case(
        "content.optimization.retrieve:single",
        operation="retrieve",
        path="/v1/content/{asset_id}/optimization/{content_id}",
    )
    def test_method_retrieve(self) -> None:
        optimization = client.content.optimization.retrieve(
            asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            content_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )
