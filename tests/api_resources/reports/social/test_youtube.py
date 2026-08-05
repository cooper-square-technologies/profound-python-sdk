# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types.reports.social import (
    YoutubeGetVideosResponse,
    YoutubeGetSummaryResponse,
    YoutubeGetChannelsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestYoutube:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_channels(self, client: Profound) -> None:
        youtube = client.reports.social.youtube.get_channels(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(YoutubeGetChannelsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_channels_with_all_params(self, client: Profound) -> None:
        youtube = client.reports.social.youtube.get_channels(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["channel"],
            interval="day",
            limit=1,
            source_types=["video"],
        )
        assert_matches_type(YoutubeGetChannelsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_channels(self, client: Profound) -> None:
        response = client.reports.social.youtube.with_raw_response.get_channels(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = response.parse()
        assert_matches_type(YoutubeGetChannelsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_channels(self, client: Profound) -> None:
        with client.reports.social.youtube.with_streaming_response.get_channels(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = response.parse()
            assert_matches_type(YoutubeGetChannelsResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_summary(self, client: Profound) -> None:
        youtube = client.reports.social.youtube.get_summary(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(YoutubeGetSummaryResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_summary_with_all_params(self, client: Profound) -> None:
        youtube = client.reports.social.youtube.get_summary(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
        )
        assert_matches_type(YoutubeGetSummaryResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_summary(self, client: Profound) -> None:
        response = client.reports.social.youtube.with_raw_response.get_summary(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = response.parse()
        assert_matches_type(YoutubeGetSummaryResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_summary(self, client: Profound) -> None:
        with client.reports.social.youtube.with_streaming_response.get_summary(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = response.parse()
            assert_matches_type(YoutubeGetSummaryResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_videos(self, client: Profound) -> None:
        youtube = client.reports.social.youtube.get_videos(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(YoutubeGetVideosResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_videos_with_all_params(self, client: Profound) -> None:
        youtube = client.reports.social.youtube.get_videos(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            attribution="attributed",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            limit=1,
            source_types=["video"],
        )
        assert_matches_type(YoutubeGetVideosResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_videos(self, client: Profound) -> None:
        response = client.reports.social.youtube.with_raw_response.get_videos(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = response.parse()
        assert_matches_type(YoutubeGetVideosResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_videos(self, client: Profound) -> None:
        with client.reports.social.youtube.with_streaming_response.get_videos(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = response.parse()
            assert_matches_type(YoutubeGetVideosResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncYoutube:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_channels(self, async_client: AsyncProfound) -> None:
        youtube = await async_client.reports.social.youtube.get_channels(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(YoutubeGetChannelsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_channels_with_all_params(self, async_client: AsyncProfound) -> None:
        youtube = await async_client.reports.social.youtube.get_channels(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            group_by=["channel"],
            interval="day",
            limit=1,
            source_types=["video"],
        )
        assert_matches_type(YoutubeGetChannelsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_channels(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.social.youtube.with_raw_response.get_channels(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = await response.parse()
        assert_matches_type(YoutubeGetChannelsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_channels(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.social.youtube.with_streaming_response.get_channels(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = await response.parse()
            assert_matches_type(YoutubeGetChannelsResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_summary(self, async_client: AsyncProfound) -> None:
        youtube = await async_client.reports.social.youtube.get_summary(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(YoutubeGetSummaryResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_summary_with_all_params(self, async_client: AsyncProfound) -> None:
        youtube = await async_client.reports.social.youtube.get_summary(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
        )
        assert_matches_type(YoutubeGetSummaryResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_summary(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.social.youtube.with_raw_response.get_summary(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = await response.parse()
        assert_matches_type(YoutubeGetSummaryResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_summary(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.social.youtube.with_streaming_response.get_summary(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = await response.parse()
            assert_matches_type(YoutubeGetSummaryResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_videos(self, async_client: AsyncProfound) -> None:
        youtube = await async_client.reports.social.youtube.get_videos(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(YoutubeGetVideosResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_videos_with_all_params(self, async_client: AsyncProfound) -> None:
        youtube = await async_client.reports.social.youtube.get_videos(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            attribution="attributed",
            cursor="cursor",
            filter={
                "and": [],
                "field": "field",
                "op": "op",
                "or": [],
                "value": {},
            },
            limit=1,
            source_types=["video"],
        )
        assert_matches_type(YoutubeGetVideosResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_videos(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.social.youtube.with_raw_response.get_videos(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = await response.parse()
        assert_matches_type(YoutubeGetVideosResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_videos(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.social.youtube.with_streaming_response.get_videos(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = await response.parse()
            assert_matches_type(YoutubeGetVideosResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True
