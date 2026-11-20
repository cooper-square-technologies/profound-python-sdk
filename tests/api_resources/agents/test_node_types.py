# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestNodeTypes:
    @smoke_case("agents.nodeTypes.list:single", operation="list", path="/v1/agents/node-types")
    def test_method_list(self) -> None:
        node_type = client.agents.node_types.list()

    @smoke_case(
        "agents.nodeTypes.retrieveSchema:single",
        operation="retrieveSchema",
        path="/v1/agents/node-types/{node_type}/schema",
    )
    def test_method_retrieve_schema(self) -> None:
        node_type = client.agents.node_types.retrieve_schema(
            node_type="nodeType",
        )
