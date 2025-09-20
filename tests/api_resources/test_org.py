# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types import OrgRetrieveModelsResponse, OrgRetrieveDomainsResponse, OrgRetrieveRegionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrg:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_domains(self, client: Profound) -> None:
        org = client.org.retrieve_domains()
        assert_matches_type(OrgRetrieveDomainsResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_domains(self, client: Profound) -> None:
        response = client.org.with_raw_response.retrieve_domains()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgRetrieveDomainsResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_domains(self, client: Profound) -> None:
        with client.org.with_streaming_response.retrieve_domains() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgRetrieveDomainsResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_models(self, client: Profound) -> None:
        org = client.org.retrieve_models()
        assert_matches_type(OrgRetrieveModelsResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_models(self, client: Profound) -> None:
        response = client.org.with_raw_response.retrieve_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgRetrieveModelsResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_models(self, client: Profound) -> None:
        with client.org.with_streaming_response.retrieve_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgRetrieveModelsResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_regions(self, client: Profound) -> None:
        org = client.org.retrieve_regions()
        assert_matches_type(OrgRetrieveRegionsResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_regions(self, client: Profound) -> None:
        response = client.org.with_raw_response.retrieve_regions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgRetrieveRegionsResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_regions(self, client: Profound) -> None:
        with client.org.with_streaming_response.retrieve_regions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgRetrieveRegionsResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrg:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_domains(self, async_client: AsyncProfound) -> None:
        org = await async_client.org.retrieve_domains()
        assert_matches_type(OrgRetrieveDomainsResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_domains(self, async_client: AsyncProfound) -> None:
        response = await async_client.org.with_raw_response.retrieve_domains()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgRetrieveDomainsResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_domains(self, async_client: AsyncProfound) -> None:
        async with async_client.org.with_streaming_response.retrieve_domains() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgRetrieveDomainsResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_models(self, async_client: AsyncProfound) -> None:
        org = await async_client.org.retrieve_models()
        assert_matches_type(OrgRetrieveModelsResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_models(self, async_client: AsyncProfound) -> None:
        response = await async_client.org.with_raw_response.retrieve_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgRetrieveModelsResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_models(self, async_client: AsyncProfound) -> None:
        async with async_client.org.with_streaming_response.retrieve_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgRetrieveModelsResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_regions(self, async_client: AsyncProfound) -> None:
        org = await async_client.org.retrieve_regions()
        assert_matches_type(OrgRetrieveRegionsResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_regions(self, async_client: AsyncProfound) -> None:
        response = await async_client.org.with_raw_response.retrieve_regions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgRetrieveRegionsResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_regions(self, async_client: AsyncProfound) -> None:
        async with async_client.org.with_streaming_response.retrieve_regions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgRetrieveRegionsResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True
