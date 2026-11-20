# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestDocuments:
    @smoke_case(
        "knowledgeBases.documents.create:required",
        operation="create",
        path="/v1/knowledge-bases/{knowledge_base_id}/documents",
    )
    def test_method_create(self) -> None:
        document = client.knowledge_bases.documents.create(
            knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            name="x",
            text="x",
        )

    @smoke_case(
        "knowledgeBases.documents.create:all",
        operation="create",
        path="/v1/knowledge-bases/{knowledge_base_id}/documents",
    )
    def test_method_create_with_all_params(self) -> None:
        document = client.knowledge_bases.documents.create(
            knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            name="x",
            text="x",
            folder="x",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case(
        "knowledgeBases.documents.update:required",
        operation="update",
        path="/v1/knowledge-bases/{knowledge_base_id}/documents",
    )
    def test_method_update(self) -> None:
        document = client.knowledge_bases.documents.update(
            knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            name="x",
            text="x",
        )

    @smoke_case(
        "knowledgeBases.documents.update:all",
        operation="update",
        path="/v1/knowledge-bases/{knowledge_base_id}/documents",
    )
    def test_method_update_with_all_params(self) -> None:
        document = client.knowledge_bases.documents.update(
            knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            name="x",
            text="x",
            folder="x",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case(
        "knowledgeBases.documents.delete:required",
        operation="delete",
        path="/v1/knowledge-bases/{knowledge_base_id}/documents",
    )
    def test_method_delete(self) -> None:
        document = client.knowledge_bases.documents.delete(
            knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            name="x",
        )

    @smoke_case(
        "knowledgeBases.documents.delete:all",
        operation="delete",
        path="/v1/knowledge-bases/{knowledge_base_id}/documents",
    )
    def test_method_delete_with_all_params(self) -> None:
        document = client.knowledge_bases.documents.delete(
            knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            name="x",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )
