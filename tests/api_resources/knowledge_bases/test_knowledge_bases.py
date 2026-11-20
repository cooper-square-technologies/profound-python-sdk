# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestKnowledgeBases:
    @smoke_case("knowledgeBases.list:required", operation="list", path="/v1/knowledge-bases")
    def test_method_list(self) -> None:
        knowledge_base = client.knowledge_bases.list()

    @smoke_case("knowledgeBases.list:all", operation="list", path="/v1/knowledge-bases")
    def test_method_list_with_all_params(self) -> None:
        knowledge_base = client.knowledge_bases.list(
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case(
        "knowledgeBases.search:required", operation="search", path="/v1/knowledge-bases/{knowledge_base_id}/search"
    )
    def test_method_search(self) -> None:
        knowledge_base = client.knowledge_bases.search(
            knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            query="x",
            top_k=1,
            return_full_page=False,
        )

    @smoke_case("knowledgeBases.search:all", operation="search", path="/v1/knowledge-bases/{knowledge_base_id}/search")
    def test_method_search_with_all_params(self) -> None:
        knowledge_base = client.knowledge_bases.search(
            knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            query="x",
            top_k=1,
            return_full_page=False,
            filters={"tags": ["x"], "folders": ["x"]},
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )
