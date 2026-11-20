# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestFolders:
    @smoke_case(
        "knowledgeBases.folders.create:required",
        operation="create",
        path="/v1/knowledge-bases/{knowledge_base_id}/folders",
    )
    def test_method_create(self) -> None:
        folder = client.knowledge_bases.folders.create(
            knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            path="x",
        )

    @smoke_case(
        "knowledgeBases.folders.create:all", operation="create", path="/v1/knowledge-bases/{knowledge_base_id}/folders"
    )
    def test_method_create_with_all_params(self) -> None:
        folder = client.knowledge_bases.folders.create(
            knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            path="x",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case(
        "knowledgeBases.folders.delete:required",
        operation="delete",
        path="/v1/knowledge-bases/{knowledge_base_id}/folders",
    )
    def test_method_delete(self) -> None:
        folder = client.knowledge_bases.folders.delete(
            knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            path="x",
            recursive=False,
        )

    @smoke_case(
        "knowledgeBases.folders.delete:all", operation="delete", path="/v1/knowledge-bases/{knowledge_base_id}/folders"
    )
    def test_method_delete_with_all_params(self) -> None:
        folder = client.knowledge_bases.folders.delete(
            knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            path="x",
            recursive=False,
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )
