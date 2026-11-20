# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestIntegrations:
    @smoke_case("integrations.list:required", operation="list", path="/v1/integrations")
    def test_method_list(self) -> None:
        integrations = client.integrations.list()

    @smoke_case("integrations.list:all", operation="list", path="/v1/integrations")
    def test_method_list_with_all_params(self) -> None:
        integrations = client.integrations.list(
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            provider="provider",
            status_filter="active",
        )
