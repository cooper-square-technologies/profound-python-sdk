# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestYoutube:
    @smoke_case(
        "reports.social.youtube.getChannels:required",
        operation="getChannels",
        path="/v2/reports/social/youtube/channels",
    )
    def test_method_get_channels(self) -> None:
        youtube = client.reports.social.youtube.get_channels(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
        )

    @smoke_case(
        "reports.social.youtube.getChannels:all", operation="getChannels", path="/v2/reports/social/youtube/channels"
    )
    def test_method_get_channels_with_all_params(self) -> None:
        youtube = client.reports.social.youtube.get_channels(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            cursor="",
            source_types=["video"],
            group_by=["channel"],
            interval="day",
        )

    @smoke_case(
        "reports.social.youtube.getVideos:required", operation="getVideos", path="/v2/reports/social/youtube/videos"
    )
    def test_method_get_videos(self) -> None:
        youtube = client.reports.social.youtube.get_videos(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            attribution="attributed",
        )

    @smoke_case("reports.social.youtube.getVideos:all", operation="getVideos", path="/v2/reports/social/youtube/videos")
    def test_method_get_videos_with_all_params(self) -> None:
        youtube = client.reports.social.youtube.get_videos(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            cursor="",
            source_types=["video"],
            attribution="attributed",
        )

    @smoke_case(
        "reports.social.youtube.getSummary:required", operation="getSummary", path="/v2/reports/social/youtube/summary"
    )
    def test_method_get_summary(self) -> None:
        youtube = client.reports.social.youtube.get_summary(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
        )

    @smoke_case(
        "reports.social.youtube.getSummary:all", operation="getSummary", path="/v2/reports/social/youtube/summary"
    )
    def test_method_get_summary_with_all_params(self) -> None:
        youtube = client.reports.social.youtube.get_summary(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        )
