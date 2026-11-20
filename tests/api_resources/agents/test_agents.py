# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestAgents:
    @smoke_case("agents.list:required", operation="list", path="/v1/agents")
    def test_method_list(self) -> None:
        agents = client.agents.list(
            limit=100,
        )

    @smoke_case("agents.list:all", operation="list", path="/v1/agents")
    def test_method_list_with_all_params(self) -> None:
        agents = client.agents.list(
            statuses=["published"],
            limit=100,
            next_cursor="next_cursor",
        )

    @smoke_case("agents.retrieve:single", operation="retrieve", path="/v1/agents/{agent_id}")
    def test_method_retrieve(self) -> None:
        agent = client.agents.retrieve(
            agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            version="published",
        )

    @smoke_case("agents.create:required", operation="create", path="/v1/agents")
    def test_method_create(self) -> None:
        agent = client.agents.create(
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            name="x",
        )

    @smoke_case("agents.create:all", operation="create", path="/v1/agents")
    def test_method_create_with_all_params(self) -> None:
        agent = client.agents.create(
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            name="x",
            description="",
            graph={},
        )

    @smoke_case("agents.publish:single", operation="publish", path="/v1/agents/{agent_id}/publish")
    def test_method_publish(self) -> None:
        agent = client.agents.publish(
            agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("agents.update:single", operation="update", path="/v1/agents/{agent_id}")
    def test_method_update(self) -> None:
        agent = client.agents.update(
            agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            graph={},
        )

    @smoke_case("agents.retrieveGraph:single", operation="retrieveGraph", path="/v1/agents/{agent_id}/graph")
    def test_method_retrieve_graph(self) -> None:
        agent = client.agents.retrieve_graph(
            agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            version="published",
        )
