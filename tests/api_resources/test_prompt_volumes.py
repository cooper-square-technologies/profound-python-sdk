# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPromptVolumes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_volume(self, client: Profound) -> None:
        prompt_volume = client.prompt_volumes.create_volume(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["volume"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, prompt_volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_volume_with_all_params(self, client: Profound) -> None:
        prompt_volume = client.prompt_volumes.create_volume(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["volume"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["keyword"],
            filters=[
                {
                    "field": "country_code",
                    "operator": "is",
                    "value": "string",
                }
            ],
            order_by={"date": "asc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(object, prompt_volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_volume(self, client: Profound) -> None:
        response = client.prompt_volumes.with_raw_response.create_volume(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["volume"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_volume = response.parse()
        assert_matches_type(object, prompt_volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_volume(self, client: Profound) -> None:
        with client.prompt_volumes.with_streaming_response.create_volume(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["volume"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_volume = response.parse()
            assert_matches_type(object, prompt_volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_citation_prompts(self, client: Profound) -> None:
        prompt_volume = client.prompt_volumes.list_citation_prompts(
            input_domain="xxx",
        )
        assert_matches_type(object, prompt_volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_citation_prompts(self, client: Profound) -> None:
        response = client.prompt_volumes.with_raw_response.list_citation_prompts(
            input_domain="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_volume = response.parse()
        assert_matches_type(object, prompt_volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_citation_prompts(self, client: Profound) -> None:
        with client.prompt_volumes.with_streaming_response.list_citation_prompts(
            input_domain="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_volume = response.parse()
            assert_matches_type(object, prompt_volume, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPromptVolumes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_volume(self, async_client: AsyncProfound) -> None:
        prompt_volume = await async_client.prompt_volumes.create_volume(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["volume"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, prompt_volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_volume_with_all_params(self, async_client: AsyncProfound) -> None:
        prompt_volume = await async_client.prompt_volumes.create_volume(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["volume"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_interval="hour",
            dimensions=["keyword"],
            filters=[
                {
                    "field": "country_code",
                    "operator": "is",
                    "value": "string",
                }
            ],
            order_by={"date": "asc"},
            pagination={
                "limit": 1,
                "offset": 0,
            },
        )
        assert_matches_type(object, prompt_volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_volume(self, async_client: AsyncProfound) -> None:
        response = await async_client.prompt_volumes.with_raw_response.create_volume(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["volume"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_volume = await response.parse()
        assert_matches_type(object, prompt_volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_volume(self, async_client: AsyncProfound) -> None:
        async with async_client.prompt_volumes.with_streaming_response.create_volume(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            metrics=["volume"],
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_volume = await response.parse()
            assert_matches_type(object, prompt_volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_citation_prompts(self, async_client: AsyncProfound) -> None:
        prompt_volume = await async_client.prompt_volumes.list_citation_prompts(
            input_domain="xxx",
        )
        assert_matches_type(object, prompt_volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_citation_prompts(self, async_client: AsyncProfound) -> None:
        response = await async_client.prompt_volumes.with_raw_response.list_citation_prompts(
            input_domain="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_volume = await response.parse()
        assert_matches_type(object, prompt_volume, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_citation_prompts(self, async_client: AsyncProfound) -> None:
        async with async_client.prompt_volumes.with_streaming_response.list_citation_prompts(
            input_domain="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_volume = await response.parse()
            assert_matches_type(object, prompt_volume, path=["response"])

        assert cast(Any, response.is_closed) is True
