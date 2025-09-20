# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types.org import (
    CategoryListResponse,
    CategoryRetrieveTagsResponse,
    CategoryRetrieveTopicsResponse,
    CategoryRetrievePromptsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Profound) -> None:
        category = client.org.categories.list()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Profound) -> None:
        response = client.org.categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Profound) -> None:
        with client.org.categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryListResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_prompts(self, client: Profound) -> None:
        category = client.org.categories.retrieve_prompts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CategoryRetrievePromptsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_prompts(self, client: Profound) -> None:
        response = client.org.categories.with_raw_response.retrieve_prompts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryRetrievePromptsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_prompts(self, client: Profound) -> None:
        with client.org.categories.with_streaming_response.retrieve_prompts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryRetrievePromptsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_prompts(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.org.categories.with_raw_response.retrieve_prompts(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_tags(self, client: Profound) -> None:
        category = client.org.categories.retrieve_tags(
            "category_id",
        )
        assert_matches_type(CategoryRetrieveTagsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_tags(self, client: Profound) -> None:
        response = client.org.categories.with_raw_response.retrieve_tags(
            "category_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryRetrieveTagsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_tags(self, client: Profound) -> None:
        with client.org.categories.with_streaming_response.retrieve_tags(
            "category_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryRetrieveTagsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_tags(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.org.categories.with_raw_response.retrieve_tags(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_topics(self, client: Profound) -> None:
        category = client.org.categories.retrieve_topics(
            "category_id",
        )
        assert_matches_type(CategoryRetrieveTopicsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_topics(self, client: Profound) -> None:
        response = client.org.categories.with_raw_response.retrieve_topics(
            "category_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryRetrieveTopicsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_topics(self, client: Profound) -> None:
        with client.org.categories.with_streaming_response.retrieve_topics(
            "category_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryRetrieveTopicsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_topics(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.org.categories.with_raw_response.retrieve_topics(
                "",
            )


class TestAsyncCategories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncProfound) -> None:
        category = await async_client.org.categories.list()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncProfound) -> None:
        response = await async_client.org.categories.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncProfound) -> None:
        async with async_client.org.categories.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryListResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_prompts(self, async_client: AsyncProfound) -> None:
        category = await async_client.org.categories.retrieve_prompts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CategoryRetrievePromptsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_prompts(self, async_client: AsyncProfound) -> None:
        response = await async_client.org.categories.with_raw_response.retrieve_prompts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryRetrievePromptsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_prompts(self, async_client: AsyncProfound) -> None:
        async with async_client.org.categories.with_streaming_response.retrieve_prompts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryRetrievePromptsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_prompts(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.org.categories.with_raw_response.retrieve_prompts(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_tags(self, async_client: AsyncProfound) -> None:
        category = await async_client.org.categories.retrieve_tags(
            "category_id",
        )
        assert_matches_type(CategoryRetrieveTagsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_tags(self, async_client: AsyncProfound) -> None:
        response = await async_client.org.categories.with_raw_response.retrieve_tags(
            "category_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryRetrieveTagsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_tags(self, async_client: AsyncProfound) -> None:
        async with async_client.org.categories.with_streaming_response.retrieve_tags(
            "category_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryRetrieveTagsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_tags(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.org.categories.with_raw_response.retrieve_tags(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_topics(self, async_client: AsyncProfound) -> None:
        category = await async_client.org.categories.retrieve_topics(
            "category_id",
        )
        assert_matches_type(CategoryRetrieveTopicsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_topics(self, async_client: AsyncProfound) -> None:
        response = await async_client.org.categories.with_raw_response.retrieve_topics(
            "category_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryRetrieveTopicsResponse, category, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_topics(self, async_client: AsyncProfound) -> None:
        async with async_client.org.categories.with_streaming_response.retrieve_topics(
            "category_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryRetrieveTopicsResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_topics(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.org.categories.with_raw_response.retrieve_topics(
                "",
            )
