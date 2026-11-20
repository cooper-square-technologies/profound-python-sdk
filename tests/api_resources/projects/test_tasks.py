# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestTasks:
    @smoke_case("projects.tasks.list:single", operation="list", path="/v1/projects/{project_id}/tasks")
    def test_method_list(self) -> None:
        project_tasks = client.projects.tasks.list(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("projects.tasks.create:required", operation="create", path="/v1/projects/{project_id}/tasks")
    def test_method_create(self) -> None:
        task = client.projects.tasks.create(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            title="x",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("projects.tasks.create:all", operation="create", path="/v1/projects/{project_id}/tasks")
    def test_method_create_with_all_params(self) -> None:
        task = client.projects.tasks.create(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            title="x",
            summary="x",
            brief="x",
            type="x",
            topic="x",
            impact=1,
            reference_url="x",
            reference_label="x",
            position=0,
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case(
        "projects.tasks.retrieve:single", operation="retrieve", path="/v1/projects/{project_id}/tasks/{task_id}"
    )
    def test_method_retrieve(self) -> None:
        task = client.projects.tasks.retrieve(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("projects.tasks.update:required", operation="update", path="/v1/projects/{project_id}/tasks/{task_id}")
    def test_method_update(self) -> None:
        task = client.projects.tasks.update(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("projects.tasks.update:all", operation="update", path="/v1/projects/{project_id}/tasks/{task_id}")
    def test_method_update_with_all_params(self) -> None:
        task = client.projects.tasks.update(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            title="x",
            summary="x",
            brief="x",
            type="x",
            topic="x",
            impact=1,
            reference_url="x",
            reference_label="x",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("projects.tasks.delete:single", operation="delete", path="/v1/projects/{project_id}/tasks/{task_id}")
    def test_method_delete(self) -> None:
        client.projects.tasks.delete(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case(
        "projects.tasks.updateStatus:required",
        operation="updateStatus",
        path="/v1/projects/{project_id}/tasks/{task_id}/status",
    )
    def test_method_update_status(self) -> None:
        task = client.projects.tasks.update_status(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            status="not_started",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case(
        "projects.tasks.updateStatus:all",
        operation="updateStatus",
        path="/v1/projects/{project_id}/tasks/{task_id}/status",
    )
    def test_method_update_status_with_all_params(self) -> None:
        task = client.projects.tasks.update_status(
            project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            status="not_started",
            note="x",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )
