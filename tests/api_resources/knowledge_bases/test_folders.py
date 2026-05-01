# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types.knowledge_bases import (
    FolderCreateResponse,
    FolderDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Profound) -> None:
        folder = client.knowledge_bases.folders.create(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Profound) -> None:
        folder = client.knowledge_bases.folders.create(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Profound) -> None:
        response = client.knowledge_bases.folders.with_raw_response.create(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Profound) -> None:
        with client.knowledge_bases.folders.with_streaming_response.create(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderCreateResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            client.knowledge_bases.folders.with_raw_response.create(
                knowledge_base_id="",
                path="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Profound) -> None:
        folder = client.knowledge_bases.folders.delete(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
        )
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Profound) -> None:
        folder = client.knowledge_bases.folders.delete(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recursive=True,
        )
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Profound) -> None:
        response = client.knowledge_bases.folders.with_raw_response.delete(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Profound) -> None:
        with client.knowledge_bases.folders.with_streaming_response.delete(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderDeleteResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            client.knowledge_bases.folders.with_raw_response.delete(
                knowledge_base_id="",
                path="x",
            )


class TestAsyncFolders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncProfound) -> None:
        folder = await async_client.knowledge_bases.folders.create(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncProfound) -> None:
        folder = await async_client.knowledge_bases.folders.create(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncProfound) -> None:
        response = await async_client.knowledge_bases.folders.with_raw_response.create(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncProfound) -> None:
        async with async_client.knowledge_bases.folders.with_streaming_response.create(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderCreateResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            await async_client.knowledge_bases.folders.with_raw_response.create(
                knowledge_base_id="",
                path="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncProfound) -> None:
        folder = await async_client.knowledge_bases.folders.delete(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
        )
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncProfound) -> None:
        folder = await async_client.knowledge_bases.folders.delete(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            recursive=True,
        )
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncProfound) -> None:
        response = await async_client.knowledge_bases.folders.with_raw_response.delete(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncProfound) -> None:
        async with async_client.knowledge_bases.folders.with_streaming_response.delete(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            path="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderDeleteResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            await async_client.knowledge_bases.folders.with_raw_response.delete(
                knowledge_base_id="",
                path="x",
            )
