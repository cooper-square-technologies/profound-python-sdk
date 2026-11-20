# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestDocuments:
    @smoke_case("documents.create:single", operation="create", path="/v1/documents")
    def test_method_create(self) -> None:
        document = client.documents.create(
            id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            name="x",
            content_markdown="x",
        )

    @smoke_case("documents.list:required", operation="list", path="/v1/documents")
    def test_method_list(self) -> None:
        documents = client.documents.list(
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            limit=20,
        )

    @smoke_case("documents.list:all", operation="list", path="/v1/documents")
    def test_method_list_with_all_params(self) -> None:
        documents = client.documents.list(
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            q="q",
            sort="sort",
            limit=20,
            next_cursor="next_cursor",
        )

    @smoke_case("documents.retrieve:single", operation="retrieve", path="/v1/documents/{document_id}")
    def test_method_retrieve(self) -> None:
        document = client.documents.retrieve(
            document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            include_tabs=True,
            include_comments=True,
            preview=True,
        )

    @smoke_case("documents.update:required", operation="update", path="/v1/documents/{document_id}")
    def test_method_update(self) -> None:
        document = client.documents.update(
            document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("documents.update:all", operation="update", path="/v1/documents/{document_id}")
    def test_method_update_with_all_params(self) -> None:
        document = client.documents.update(
            document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            name="x",
            visibility="invited_only",
        )

    @smoke_case("documents.delete:single", operation="delete", path="/v1/documents/{document_id}")
    def test_method_delete(self) -> None:
        client.documents.delete(
            document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case(
        "documents.replaceContent:single", operation="replaceContent", path="/v1/documents/{document_id}/content"
    )
    def test_method_replace_content(self) -> None:
        document = client.documents.replace_content(
            document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            content_markdown="",
            skip_title_sync=False,
        )
