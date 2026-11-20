# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestRuns:
    @smoke_case("agents.runs.create:required", operation="create", path="/v1/agents/{agent_id}/runs")
    def test_method_create(self) -> None:
        run = client.agents.runs.create(
            agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("agents.runs.create:all", operation="create", path="/v1/agents/{agent_id}/runs")
    def test_method_create_with_all_params(self) -> None:
        run = client.agents.runs.create(
            agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            inputs={},
        )

    @smoke_case("agents.runs.retrieve:single", operation="retrieve", path="/v1/agents/{agent_id}/runs/{run_id}")
    def test_method_retrieve(self) -> None:
        run = client.agents.runs.retrieve(
            agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            verbose=False,
        )
