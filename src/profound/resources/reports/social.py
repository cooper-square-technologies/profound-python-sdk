# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional
from typing_extensions import Literal

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.reports.social_query_youtube_channels_v2_youtube_channels_post_response import (
    SocialQueryYoutubeChannelsV2YoutubeChannelsPostResponse,
)
from ...types.shared_params.filter_node import FilterNode
from ...types.reports import (
    social_query_youtube_channels_v2_youtube_channels_post_params,
    social_query_youtube_videos_v2_youtube_videos_post_params,
    social_query_youtube_summary_v2_youtube_summary_post_params,
)
from ...types.reports.social_query_youtube_videos_v2_youtube_videos_post_response import (
    SocialQueryYoutubeVideosV2YoutubeVideosPostResponse,
)
from ...types.reports.social_query_youtube_summary_v2_youtube_summary_post_response import (
    SocialQueryYoutubeSummaryV2YoutubeSummaryPostResponse,
)

__all__ = ["SocialResource", "AsyncSocialResource"]


class SocialResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SocialResourceWithRawResponse:
        return SocialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SocialResourceWithStreamingResponse:
        return SocialResourceWithStreamingResponse(self)

    def query_youtube_channels_v2_youtube_channels_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        source_types: Optional[List[Literal["video", "short", "channel", "playlist", "other"]]] | Omit = omit,
        group_by: List[Literal["channel", "video_category", "model", "source_type"]] | Omit = omit,
        interval: Optional[Literal["day", "week", "month"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialQueryYoutubeChannelsV2YoutubeChannelsPostResponse:
        """
        Rank the YouTube channels cited in a category, or the video categories they publish in.

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            filter: Advanced filter tree. Prompt-level dimensions are `model`, `topic`, `region`, `prompt`, `persona`, `tag`, `analysis_type`. `channel` covers both channel cases: `in` with a list of handles selects exactly those channels, resolving each handle to its channel so a renamed channel is never returned in pieces; `contains` matches a channel's title or handle by name. Combine with `and`/`or`/`not` up to 3 deep. An exact `channel` selection must be its own `and` clause, and a `channel` leaf cannot share an `or` or `not` with a prompt-level leaf, because those compile at different stages of the query. `domain` and `page` are rejected rather than approximated: every row here is one domain, and `page` is not a video id.
            limit: Page size; default 10, max 50.
            cursor: Body parameter.
            source_types: Limit results to YouTube source types: `video`, `short`, `channel`, `playlist`, or `other`. Omit to include `video`, `short`, `channel`, and `playlist`; `other` is excluded because those citations have no channel. Requests containing `other` are rejected.
            group_by: What each row represents. Empty or `["channel"]` ranks channels; `["video_category"]` ranks content categories; `["source_type"]` ranks source types; `["channel", "video_category"]`, `["channel", "source_type"]` and `["channel", "model"]` return cross-tabs — a row per channel per category, or per answer engine. `limit` counts leading channels in every case, so ten channels across nine engines is ten channels and ninety rows.
            interval: Return a time series instead of window totals: one row per entity per period, each carrying `date`. `citation_share` is then relative to that period, so the series is comparable across periods. Omit for window totals.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SocialQueryYoutubeChannelsV2YoutubeChannelsPostResponse: Successful Response

        Example:
            ```python
            social = client.reports.social.query_youtube_channels_v2_youtube_channels_post(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )
            ```
        """
        return self._post(
            "/v2/reports/social/youtube/channels",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "filter": filter,
                    "limit": limit,
                    "cursor": cursor,
                    "source_types": source_types,
                    "group_by": group_by,
                    "interval": interval,
                },
                social_query_youtube_channels_v2_youtube_channels_post_params.SocialQueryYoutubeChannelsV2YoutubeChannelsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialQueryYoutubeChannelsV2YoutubeChannelsPostResponse,
        )

    def query_youtube_videos_v2_youtube_videos_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        source_types: Optional[List[Literal["video", "short", "channel", "playlist", "other"]]] | Omit = omit,
        attribution: Literal["attributed", "unattributed", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialQueryYoutubeVideosV2YoutubeVideosPostResponse:
        """
        Rank cited YouTube videos, for one channel or across all of them.

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            filter: Advanced filter tree. Prompt-level dimensions are `model`, `topic`, `region`, `prompt`, `persona`, `tag`, `analysis_type`. `channel` covers both channel cases: `in` with a list of handles selects exactly those channels, resolving each handle to its channel so a renamed channel is never returned in pieces; `contains` matches a channel's title or handle by name. Combine with `and`/`or`/`not` up to 3 deep. An exact `channel` selection must be its own `and` clause, and a `channel` leaf cannot share an `or` or `not` with a prompt-level leaf, because those compile at different stages of the query. `domain` and `page` are rejected rather than approximated: every row here is one domain, and `page` is not a video id.
            limit: Page size; default 10, max 50.
            cursor: Body parameter.
            source_types: Limit results to YouTube source types: `video`, `short`, `channel`, `playlist`, or `other`. Omit to include `video` and `short` with the default `attribution='attributed'`; `unattributed` and `all` widen the default to all five source types. Requests containing `other` with `attribution='attributed'` are rejected.
            attribution: Choose attributed citations, unattributed citations, or all citations. An unattributed row has no channel: `source_type` is `other` for a search or feed URL that names no source, and any other type is a source we have no channel for.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SocialQueryYoutubeVideosV2YoutubeVideosPostResponse: Successful Response

        Example:
            ```python
            social = client.reports.social.query_youtube_videos_v2_youtube_videos_post(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                attribution="attributed",
            )
            ```
        """
        return self._post(
            "/v2/reports/social/youtube/videos",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "filter": filter,
                    "limit": limit,
                    "cursor": cursor,
                    "source_types": source_types,
                    "attribution": attribution,
                },
                social_query_youtube_videos_v2_youtube_videos_post_params.SocialQueryYoutubeVideosV2YoutubeVideosPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialQueryYoutubeVideosV2YoutubeVideosPostResponse,
        )

    def query_youtube_summary_v2_youtube_summary_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        filter: Optional[FilterNode] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialQueryYoutubeSummaryV2YoutubeSummaryPostResponse:
        """
        Report how much of youtube.com the channel and video rankings account for.

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            filter: Advanced filter tree. Prompt-level dimensions are `model`, `topic`, `region`, `prompt`, `persona`, `tag`, `analysis_type`. `channel` covers both channel cases: `in` with a list of handles selects exactly those channels, resolving each handle to its channel so a renamed channel is never returned in pieces; `contains` matches a channel's title or handle by name. Combine with `and`/`or`/`not` up to 3 deep. An exact `channel` selection must be its own `and` clause, and a `channel` leaf cannot share an `or` or `not` with a prompt-level leaf, because those compile at different stages of the query. `domain` and `page` are rejected rather than approximated: every row here is one domain, and `page` is not a video id.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SocialQueryYoutubeSummaryV2YoutubeSummaryPostResponse: Successful Response

        Example:
            ```python
            social = client.reports.social.query_youtube_summary_v2_youtube_summary_post(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )
            ```
        """
        return self._post(
            "/v2/reports/social/youtube/summary",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "filter": filter,
                },
                social_query_youtube_summary_v2_youtube_summary_post_params.SocialQueryYoutubeSummaryV2YoutubeSummaryPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialQueryYoutubeSummaryV2YoutubeSummaryPostResponse,
        )


class AsyncSocialResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSocialResourceWithRawResponse:
        return AsyncSocialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSocialResourceWithStreamingResponse:
        return AsyncSocialResourceWithStreamingResponse(self)

    async def query_youtube_channels_v2_youtube_channels_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        source_types: Optional[List[Literal["video", "short", "channel", "playlist", "other"]]] | Omit = omit,
        group_by: List[Literal["channel", "video_category", "model", "source_type"]] | Omit = omit,
        interval: Optional[Literal["day", "week", "month"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialQueryYoutubeChannelsV2YoutubeChannelsPostResponse:
        """
        Rank the YouTube channels cited in a category, or the video categories they publish in.

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            filter: Advanced filter tree. Prompt-level dimensions are `model`, `topic`, `region`, `prompt`, `persona`, `tag`, `analysis_type`. `channel` covers both channel cases: `in` with a list of handles selects exactly those channels, resolving each handle to its channel so a renamed channel is never returned in pieces; `contains` matches a channel's title or handle by name. Combine with `and`/`or`/`not` up to 3 deep. An exact `channel` selection must be its own `and` clause, and a `channel` leaf cannot share an `or` or `not` with a prompt-level leaf, because those compile at different stages of the query. `domain` and `page` are rejected rather than approximated: every row here is one domain, and `page` is not a video id.
            limit: Page size; default 10, max 50.
            cursor: Body parameter.
            source_types: Limit results to YouTube source types: `video`, `short`, `channel`, `playlist`, or `other`. Omit to include `video`, `short`, `channel`, and `playlist`; `other` is excluded because those citations have no channel. Requests containing `other` are rejected.
            group_by: What each row represents. Empty or `["channel"]` ranks channels; `["video_category"]` ranks content categories; `["source_type"]` ranks source types; `["channel", "video_category"]`, `["channel", "source_type"]` and `["channel", "model"]` return cross-tabs — a row per channel per category, or per answer engine. `limit` counts leading channels in every case, so ten channels across nine engines is ten channels and ninety rows.
            interval: Return a time series instead of window totals: one row per entity per period, each carrying `date`. `citation_share` is then relative to that period, so the series is comparable across periods. Omit for window totals.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SocialQueryYoutubeChannelsV2YoutubeChannelsPostResponse: Successful Response

        Example:
            ```python
            social = await client.reports.social.query_youtube_channels_v2_youtube_channels_post(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )
            ```
        """
        return await self._post(
            "/v2/reports/social/youtube/channels",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "filter": filter,
                    "limit": limit,
                    "cursor": cursor,
                    "source_types": source_types,
                    "group_by": group_by,
                    "interval": interval,
                },
                social_query_youtube_channels_v2_youtube_channels_post_params.SocialQueryYoutubeChannelsV2YoutubeChannelsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialQueryYoutubeChannelsV2YoutubeChannelsPostResponse,
        )

    async def query_youtube_videos_v2_youtube_videos_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        source_types: Optional[List[Literal["video", "short", "channel", "playlist", "other"]]] | Omit = omit,
        attribution: Literal["attributed", "unattributed", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialQueryYoutubeVideosV2YoutubeVideosPostResponse:
        """
        Rank cited YouTube videos, for one channel or across all of them.

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            filter: Advanced filter tree. Prompt-level dimensions are `model`, `topic`, `region`, `prompt`, `persona`, `tag`, `analysis_type`. `channel` covers both channel cases: `in` with a list of handles selects exactly those channels, resolving each handle to its channel so a renamed channel is never returned in pieces; `contains` matches a channel's title or handle by name. Combine with `and`/`or`/`not` up to 3 deep. An exact `channel` selection must be its own `and` clause, and a `channel` leaf cannot share an `or` or `not` with a prompt-level leaf, because those compile at different stages of the query. `domain` and `page` are rejected rather than approximated: every row here is one domain, and `page` is not a video id.
            limit: Page size; default 10, max 50.
            cursor: Body parameter.
            source_types: Limit results to YouTube source types: `video`, `short`, `channel`, `playlist`, or `other`. Omit to include `video` and `short` with the default `attribution='attributed'`; `unattributed` and `all` widen the default to all five source types. Requests containing `other` with `attribution='attributed'` are rejected.
            attribution: Choose attributed citations, unattributed citations, or all citations. An unattributed row has no channel: `source_type` is `other` for a search or feed URL that names no source, and any other type is a source we have no channel for.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SocialQueryYoutubeVideosV2YoutubeVideosPostResponse: Successful Response

        Example:
            ```python
            social = await client.reports.social.query_youtube_videos_v2_youtube_videos_post(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
                attribution="attributed",
            )
            ```
        """
        return await self._post(
            "/v2/reports/social/youtube/videos",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "filter": filter,
                    "limit": limit,
                    "cursor": cursor,
                    "source_types": source_types,
                    "attribution": attribution,
                },
                social_query_youtube_videos_v2_youtube_videos_post_params.SocialQueryYoutubeVideosV2YoutubeVideosPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialQueryYoutubeVideosV2YoutubeVideosPostResponse,
        )

    async def query_youtube_summary_v2_youtube_summary_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        filter: Optional[FilterNode] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialQueryYoutubeSummaryV2YoutubeSummaryPostResponse:
        """
        Report how much of youtube.com the channel and video rankings account for.

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            filter: Advanced filter tree. Prompt-level dimensions are `model`, `topic`, `region`, `prompt`, `persona`, `tag`, `analysis_type`. `channel` covers both channel cases: `in` with a list of handles selects exactly those channels, resolving each handle to its channel so a renamed channel is never returned in pieces; `contains` matches a channel's title or handle by name. Combine with `and`/`or`/`not` up to 3 deep. An exact `channel` selection must be its own `and` clause, and a `channel` leaf cannot share an `or` or `not` with a prompt-level leaf, because those compile at different stages of the query. `domain` and `page` are rejected rather than approximated: every row here is one domain, and `page` is not a video id.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SocialQueryYoutubeSummaryV2YoutubeSummaryPostResponse: Successful Response

        Example:
            ```python
            social = await client.reports.social.query_youtube_summary_v2_youtube_summary_post(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )
            ```
        """
        return await self._post(
            "/v2/reports/social/youtube/summary",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "filter": filter,
                },
                social_query_youtube_summary_v2_youtube_summary_post_params.SocialQueryYoutubeSummaryV2YoutubeSummaryPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialQueryYoutubeSummaryV2YoutubeSummaryPostResponse,
        )


class SocialResourceWithRawResponse:
    def __init__(self, social: SocialResource) -> None:
        self._social = social

        self.query_youtube_channels_v2_youtube_channels_post = to_raw_response_wrapper(
            social.query_youtube_channels_v2_youtube_channels_post,
        )
        self.query_youtube_videos_v2_youtube_videos_post = to_raw_response_wrapper(
            social.query_youtube_videos_v2_youtube_videos_post,
        )
        self.query_youtube_summary_v2_youtube_summary_post = to_raw_response_wrapper(
            social.query_youtube_summary_v2_youtube_summary_post,
        )


class AsyncSocialResourceWithRawResponse:
    def __init__(self, social: AsyncSocialResource) -> None:
        self._social = social

        self.query_youtube_channels_v2_youtube_channels_post = async_to_raw_response_wrapper(
            social.query_youtube_channels_v2_youtube_channels_post,
        )
        self.query_youtube_videos_v2_youtube_videos_post = async_to_raw_response_wrapper(
            social.query_youtube_videos_v2_youtube_videos_post,
        )
        self.query_youtube_summary_v2_youtube_summary_post = async_to_raw_response_wrapper(
            social.query_youtube_summary_v2_youtube_summary_post,
        )


class SocialResourceWithStreamingResponse:
    def __init__(self, social: SocialResource) -> None:
        self._social = social

        self.query_youtube_channels_v2_youtube_channels_post = to_streamed_response_wrapper(
            social.query_youtube_channels_v2_youtube_channels_post,
        )
        self.query_youtube_videos_v2_youtube_videos_post = to_streamed_response_wrapper(
            social.query_youtube_videos_v2_youtube_videos_post,
        )
        self.query_youtube_summary_v2_youtube_summary_post = to_streamed_response_wrapper(
            social.query_youtube_summary_v2_youtube_summary_post,
        )


class AsyncSocialResourceWithStreamingResponse:
    def __init__(self, social: AsyncSocialResource) -> None:
        self._social = social

        self.query_youtube_channels_v2_youtube_channels_post = async_to_streamed_response_wrapper(
            social.query_youtube_channels_v2_youtube_channels_post,
        )
        self.query_youtube_videos_v2_youtube_videos_post = async_to_streamed_response_wrapper(
            social.query_youtube_videos_v2_youtube_videos_post,
        )
        self.query_youtube_summary_v2_youtube_summary_post = async_to_streamed_response_wrapper(
            social.query_youtube_summary_v2_youtube_summary_post,
        )
