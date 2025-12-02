# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types import PromptAnswersResponse
from profound._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_answers(self, client: Profound) -> None:
        prompt = client.prompts.answers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PromptAnswersResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_answers_with_all_params(self, client: Profound) -> None:
        prompt = client.prompts.answers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include={
                "asset": True,
                "citations": True,
                "created_at": True,
                "mentions": True,
                "model": True,
                "persona": True,
                "prompt": True,
                "prompt_id": True,
                "prompt_type": True,
                "region": True,
                "response": True,
                "run_id": True,
                "search_queries": True,
                "tags": True,
                "themes": True,
                "topic": True,
            },
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(PromptAnswersResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_answers(self, client: Profound) -> None:
        response = client.prompts.with_raw_response.answers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptAnswersResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_answers(self, client: Profound) -> None:
        with client.prompts.with_streaming_response.answers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptAnswersResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrompts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_answers(self, async_client: AsyncProfound) -> None:
        prompt = await async_client.prompts.answers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PromptAnswersResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_answers_with_all_params(self, async_client: AsyncProfound) -> None:
        prompt = await async_client.prompts.answers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            filters=[
                {
                    "field": "region_id",
                    "operator": "is",
                    "value": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            include={
                "asset": True,
                "citations": True,
                "created_at": True,
                "mentions": True,
                "model": True,
                "persona": True,
                "prompt": True,
                "prompt_id": True,
                "prompt_type": True,
                "region": True,
                "response": True,
                "run_id": True,
                "search_queries": True,
                "tags": True,
                "themes": True,
                "topic": True,
            },
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(PromptAnswersResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_answers(self, async_client: AsyncProfound) -> None:
        response = await async_client.prompts.with_raw_response.answers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptAnswersResponse, prompt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_answers(self, async_client: AsyncProfound) -> None:
        async with async_client.prompts.with_streaming_response.answers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptAnswersResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True
