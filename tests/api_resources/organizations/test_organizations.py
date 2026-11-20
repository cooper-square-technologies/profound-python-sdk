# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestOrganizations:
    @smoke_case("organizations.regions:required", operation="regions", path="/v1/org/regions")
    def test_method_regions(self) -> None:
        organization = client.organizations.regions()

    @smoke_case("organizations.regions:all", operation="regions", path="/v1/org/regions")
    def test_method_regions_with_all_params(self) -> None:
        organization = client.organizations.regions(
            organization_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        )

    @smoke_case("organizations.models:single", operation="models", path="/v1/org/models")
    def test_method_models(self) -> None:
        organization = client.organizations.models()

    @smoke_case("organizations.domains:required", operation="domains", path="/v1/org/domains")
    def test_method_domains(self) -> None:
        organization = client.organizations.domains()

    @smoke_case("organizations.domains:all", operation="domains", path="/v1/org/domains")
    def test_method_domains_with_all_params(self) -> None:
        organization = client.organizations.domains(
            organization_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        )

    @smoke_case("organizations.listAssets:required", operation="listAssets", path="/v1/org/assets")
    def test_method_list_assets(self) -> None:
        organization = client.organizations.list_assets()

    @smoke_case("organizations.listAssets:all", operation="listAssets", path="/v1/org/assets")
    def test_method_list_assets_with_all_params(self) -> None:
        organization = client.organizations.list_assets(
            organization_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        )

    @smoke_case("organizations.getPersonas:required", operation="getPersonas", path="/v1/org/personas")
    def test_method_get_personas(self) -> None:
        organization_personas_with_categories = client.organizations.get_personas()

    @smoke_case("organizations.getPersonas:all", operation="getPersonas", path="/v1/org/personas")
    def test_method_get_personas_with_all_params(self) -> None:
        organization_personas_with_categories = client.organizations.get_personas(
            organization_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        )

    @smoke_case("organizations.list:single", operation="list", path="/v1/org")
    def test_method_list(self) -> None:
        organization = client.organizations.list()
