# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestProjects:
    @smoke_case("projects.list:required", operation="list", path="/v1/projects")
    def test_method_list(self) -> None:
        project = client.projects.list(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            limit=100,
            offset=0,
        )

    @smoke_case("projects.list:all", operation="list", path="/v1/projects")
    def test_method_list_with_all_params(self) -> None:
        project = client.projects.list(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            status="status",
            limit=100,
            offset=0,
        )

    @smoke_case("projects.create:single", operation="create", path="/v1/projects")
    def test_method_create(self) -> None:
        project = client.projects.create()

    @smoke_case("projects.retrieve:single", operation="retrieve", path="/v1/projects/{project_id}")
    def test_method_retrieve(self) -> None:
        project = client.projects.retrieve(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("projects.delete:single", operation="delete", path="/v1/projects/{project_id}")
    def test_method_delete(self) -> None:
        client.projects.delete(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("projects.getStatus:single", operation="getStatus", path="/v1/projects/{project_id}/status")
    def test_method_get_status(self) -> None:
        project = client.projects.get_status(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("projects.archive:required", operation="archive", path="/v1/projects/{project_id}/archive")
    def test_method_archive(self) -> None:
        project = client.projects.archive(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("projects.archive:all", operation="archive", path="/v1/projects/{project_id}/archive")
    def test_method_archive_with_all_params(self) -> None:
        project = client.projects.archive(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            reason="x",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("projects.unarchive:single", operation="unarchive", path="/v1/projects/{project_id}/unarchive")
    def test_method_unarchive(self) -> None:
        project = client.projects.unarchive(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )
