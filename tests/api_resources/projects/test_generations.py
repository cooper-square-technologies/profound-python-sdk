# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestGenerations:
    @smoke_case("projects.generations.list:single", operation="list", path="/v1/projects/generations")
    def test_method_list(self) -> None:
        generation = client.projects.generations.list()

    @smoke_case("projects.generations.retrieve:single", operation="retrieve", path="/v1/projects/generations/{run_id}")
    def test_method_retrieve(self) -> None:
        generation = client.projects.generations.retrieve(
            run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )
