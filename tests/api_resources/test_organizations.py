# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types import (
    OrganizationModelsResponse,
    OrganizationDomainsResponse,
    OrganizationRegionsResponse,
    OrganizationListAssetsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_domains(self, client: Profound) -> None:
        organization = client.organizations.domains()
        assert_matches_type(OrganizationDomainsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_domains(self, client: Profound) -> None:
        response = client.organizations.with_raw_response.domains()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationDomainsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_domains(self, client: Profound) -> None:
        with client.organizations.with_streaming_response.domains() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationDomainsResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_assets(self, client: Profound) -> None:
        organization = client.organizations.list_assets()
        assert_matches_type(OrganizationListAssetsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_assets(self, client: Profound) -> None:
        response = client.organizations.with_raw_response.list_assets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationListAssetsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_assets(self, client: Profound) -> None:
        with client.organizations.with_streaming_response.list_assets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationListAssetsResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_models(self, client: Profound) -> None:
        organization = client.organizations.models()
        assert_matches_type(OrganizationModelsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_models(self, client: Profound) -> None:
        response = client.organizations.with_raw_response.models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationModelsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_models(self, client: Profound) -> None:
        with client.organizations.with_streaming_response.models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationModelsResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_regions(self, client: Profound) -> None:
        organization = client.organizations.regions()
        assert_matches_type(OrganizationRegionsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_regions(self, client: Profound) -> None:
        response = client.organizations.with_raw_response.regions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationRegionsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_regions(self, client: Profound) -> None:
        with client.organizations.with_streaming_response.regions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationRegionsResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_domains(self, async_client: AsyncProfound) -> None:
        organization = await async_client.organizations.domains()
        assert_matches_type(OrganizationDomainsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_domains(self, async_client: AsyncProfound) -> None:
        response = await async_client.organizations.with_raw_response.domains()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationDomainsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_domains(self, async_client: AsyncProfound) -> None:
        async with async_client.organizations.with_streaming_response.domains() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationDomainsResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_assets(self, async_client: AsyncProfound) -> None:
        organization = await async_client.organizations.list_assets()
        assert_matches_type(OrganizationListAssetsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_assets(self, async_client: AsyncProfound) -> None:
        response = await async_client.organizations.with_raw_response.list_assets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationListAssetsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_assets(self, async_client: AsyncProfound) -> None:
        async with async_client.organizations.with_streaming_response.list_assets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationListAssetsResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_models(self, async_client: AsyncProfound) -> None:
        organization = await async_client.organizations.models()
        assert_matches_type(OrganizationModelsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_models(self, async_client: AsyncProfound) -> None:
        response = await async_client.organizations.with_raw_response.models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationModelsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_models(self, async_client: AsyncProfound) -> None:
        async with async_client.organizations.with_streaming_response.models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationModelsResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_regions(self, async_client: AsyncProfound) -> None:
        organization = await async_client.organizations.regions()
        assert_matches_type(OrganizationRegionsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_regions(self, async_client: AsyncProfound) -> None:
        response = await async_client.organizations.with_raw_response.regions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationRegionsResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_regions(self, async_client: AsyncProfound) -> None:
        async with async_client.organizations.with_streaming_response.regions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationRegionsResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True
