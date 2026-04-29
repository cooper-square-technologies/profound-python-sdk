# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types import (
    KnowledgeBaseListResponse,
    KnowledgeBaseSearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledgeBases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Profound) -> None:
        knowledge_base = client.knowledge_bases.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Profound) -> None:
        knowledge_base = client.knowledge_bases.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Profound) -> None:
        response = client.knowledge_bases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Profound) -> None:
        with client.knowledge_bases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Profound) -> None:
        knowledge_base = client.knowledge_bases.search(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
            top_k=1,
        )
        assert_matches_type(KnowledgeBaseSearchResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Profound) -> None:
        knowledge_base = client.knowledge_bases.search(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
            top_k=1,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filters={
                "folders": ["x"],
                "tags": ["x"],
            },
            return_full_page=True,
        )
        assert_matches_type(KnowledgeBaseSearchResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Profound) -> None:
        response = client.knowledge_bases.with_raw_response.search(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
            top_k=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseSearchResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Profound) -> None:
        with client.knowledge_bases.with_streaming_response.search(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
            top_k=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseSearchResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_search(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            client.knowledge_bases.with_raw_response.search(
                knowledge_base_id="",
                query="x",
                top_k=1,
            )


class TestAsyncKnowledgeBases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncProfound) -> None:
        knowledge_base = await async_client.knowledge_bases.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncProfound) -> None:
        knowledge_base = await async_client.knowledge_bases.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncProfound) -> None:
        response = await async_client.knowledge_bases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncProfound) -> None:
        async with async_client.knowledge_bases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncProfound) -> None:
        knowledge_base = await async_client.knowledge_bases.search(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
            top_k=1,
        )
        assert_matches_type(KnowledgeBaseSearchResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncProfound) -> None:
        knowledge_base = await async_client.knowledge_bases.search(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
            top_k=1,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filters={
                "folders": ["x"],
                "tags": ["x"],
            },
            return_full_page=True,
        )
        assert_matches_type(KnowledgeBaseSearchResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncProfound) -> None:
        response = await async_client.knowledge_bases.with_raw_response.search(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
            top_k=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseSearchResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncProfound) -> None:
        async with async_client.knowledge_bases.with_streaming_response.search(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
            top_k=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseSearchResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_search(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            await async_client.knowledge_bases.with_raw_response.search(
                knowledge_base_id="",
                query="x",
                top_k=1,
            )
