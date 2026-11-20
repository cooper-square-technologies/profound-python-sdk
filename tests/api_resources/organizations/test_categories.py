# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestCategories:
    @smoke_case("organizations.categories.list:required", operation="list", path="/v1/org/categories")
    def test_method_list(self) -> None:
        category = client.organizations.categories.list()

    @smoke_case("organizations.categories.list:all", operation="list", path="/v1/org/categories")
    def test_method_list_with_all_params(self) -> None:
        category = client.organizations.categories.list(
            organization_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        )

    @smoke_case(
        "organizations.categories.topics:single", operation="topics", path="/v1/org/categories/{category_id}/topics"
    )
    def test_method_topics(self) -> None:
        category = client.organizations.categories.topics(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case("organizations.categories.tags:single", operation="tags", path="/v1/org/categories/{category_id}/tags")
    def test_method_tags(self) -> None:
        category = client.organizations.categories.tags(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case(
        "organizations.categories.prompts:required",
        operation="prompts",
        path="/v1/org/categories/{category_id}/prompts",
    )
    def test_method_prompts(self) -> None:
        category = client.organizations.categories.prompts(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            limit=10000,
            order_by="created_at",
            order_dir="desc",
            status=["active"],
        )

    @smoke_case(
        "organizations.categories.prompts:all", operation="prompts", path="/v1/org/categories/{category_id}/prompts"
    )
    def test_method_prompts_with_all_params(self) -> None:
        category = client.organizations.categories.prompts(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            limit=10000,
            cursor="cursor",
            order_by="created_at",
            order_dir="desc",
            analysis_type=["visibility"],
            prompt_type=["visibility"],
            status=["active"],
            topic_id=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            tag_id=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            region_id=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            platform_id=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            persona_id=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        )

    @smoke_case(
        "organizations.categories.assets:single", operation="assets", path="/v1/org/categories/{category_id}/assets"
    )
    def test_method_assets(self) -> None:
        category = client.organizations.categories.assets(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case(
        "organizations.categories.getCategoryPersonas:single",
        operation="getCategoryPersonas",
        path="/v1/org/categories/{category_id}/personas",
    )
    def test_method_get_category_personas(self) -> None:
        category_personas = client.organizations.categories.get_category_personas(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case(
        "organizations.categories.createPrompts:single",
        operation="createPrompts",
        path="/v1/org/categories/{category_id}/prompts",
    )
    def test_method_create_prompts(self) -> None:
        category = client.organizations.categories.create_prompts(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            prompts=[
                {
                    "prompt": "x",
                    "topic": {},
                    "language": "",
                    "tags": [],
                    "regions": [{}],
                    "platforms": [{}],
                    "personas": [],
                }
            ],
            dry_run=False,
        )

    @smoke_case(
        "organizations.categories.updatePrompts:single",
        operation="updatePrompts",
        path="/v1/org/categories/{category_id}/prompts",
    )
    def test_method_update_prompts(self) -> None:
        category = client.organizations.categories.update_prompts(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            prompts=[{"id": ""}],
            dry_run=False,
        )

    @smoke_case(
        "organizations.categories.updatePromptStatus:single",
        operation="updatePromptStatus",
        path="/v1/org/categories/{category_id}/prompts/status",
    )
    def test_method_update_prompt_status(self) -> None:
        category = client.organizations.categories.update_prompt_status(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            prompt_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            status="active",
            dry_run=False,
        )

    @smoke_case(
        "organizations.categories.retrieveRegions:single",
        operation="retrieveRegions",
        path="/v1/org/categories/{category_id}/regions",
    )
    def test_method_retrieve_regions(self) -> None:
        category = client.organizations.categories.retrieve_regions(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case(
        "organizations.categories.getCitationCategories:single",
        operation="getCitationCategories",
        path="/v1/org/categories/{category_id}/citation-categories",
    )
    def test_method_get_citation_categories(self) -> None:
        citation_categories = client.organizations.categories.get_citation_categories(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )
