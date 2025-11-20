# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types.organizations import (
    CategoryListResponse,
    CategoryTagsResponse,
    CategoryAssetsResponse,
    CategoryTopicsResponse,
    CategoryPromptsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Profound) -> None:
        category = client.organizations.categories.list()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Profound) -> None:
        response = client.organizations.categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Profound) -> None:
        with client.organizations.categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryListResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_assets(self, client: Profound) -> None:
        category = client.organizations.categories.assets(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CategoryAssetsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_assets(self, client: Profound) -> None:
        response = client.organizations.categories.with_raw_response.assets(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryAssetsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_assets(self, client: Profound) -> None:
        with client.organizations.categories.with_streaming_response.assets(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryAssetsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_assets(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.organizations.categories.with_raw_response.assets(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_prompts(self, client: Profound) -> None:
        category = client.organizations.categories.prompts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CategoryPromptsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_prompts(self, client: Profound) -> None:
        response = client.organizations.categories.with_raw_response.prompts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryPromptsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_prompts(self, client: Profound) -> None:
        with client.organizations.categories.with_streaming_response.prompts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryPromptsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_prompts(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.organizations.categories.with_raw_response.prompts(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_tags(self, client: Profound) -> None:
        category = client.organizations.categories.tags(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CategoryTagsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_tags(self, client: Profound) -> None:
        response = client.organizations.categories.with_raw_response.tags(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryTagsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_tags(self, client: Profound) -> None:
        with client.organizations.categories.with_streaming_response.tags(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryTagsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_tags(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.organizations.categories.with_raw_response.tags(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_topics(self, client: Profound) -> None:
        category = client.organizations.categories.topics(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CategoryTopicsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_topics(self, client: Profound) -> None:
        response = client.organizations.categories.with_raw_response.topics(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryTopicsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_topics(self, client: Profound) -> None:
        with client.organizations.categories.with_streaming_response.topics(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryTopicsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_topics(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.organizations.categories.with_raw_response.topics(
                "",
            )


class TestAsyncCategories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncProfound) -> None:
        category = await async_client.organizations.categories.list()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncProfound) -> None:
        response = await async_client.organizations.categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncProfound) -> None:
        async with async_client.organizations.categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryListResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_assets(self, async_client: AsyncProfound) -> None:
        category = await async_client.organizations.categories.assets(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CategoryAssetsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_assets(self, async_client: AsyncProfound) -> None:
        response = await async_client.organizations.categories.with_raw_response.assets(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryAssetsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_assets(self, async_client: AsyncProfound) -> None:
        async with async_client.organizations.categories.with_streaming_response.assets(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryAssetsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_assets(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.organizations.categories.with_raw_response.assets(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_prompts(self, async_client: AsyncProfound) -> None:
        category = await async_client.organizations.categories.prompts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CategoryPromptsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_prompts(self, async_client: AsyncProfound) -> None:
        response = await async_client.organizations.categories.with_raw_response.prompts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryPromptsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_prompts(self, async_client: AsyncProfound) -> None:
        async with async_client.organizations.categories.with_streaming_response.prompts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryPromptsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_prompts(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.organizations.categories.with_raw_response.prompts(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_tags(self, async_client: AsyncProfound) -> None:
        category = await async_client.organizations.categories.tags(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CategoryTagsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_tags(self, async_client: AsyncProfound) -> None:
        response = await async_client.organizations.categories.with_raw_response.tags(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryTagsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_tags(self, async_client: AsyncProfound) -> None:
        async with async_client.organizations.categories.with_streaming_response.tags(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryTagsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_tags(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.organizations.categories.with_raw_response.tags(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_topics(self, async_client: AsyncProfound) -> None:
        category = await async_client.organizations.categories.topics(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CategoryTopicsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_topics(self, async_client: AsyncProfound) -> None:
        response = await async_client.organizations.categories.with_raw_response.topics(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryTopicsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_topics(self, async_client: AsyncProfound) -> None:
        async with async_client.organizations.categories.with_streaming_response.topics(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryTopicsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_topics(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.organizations.categories.with_raw_response.topics(
                "",
            )
