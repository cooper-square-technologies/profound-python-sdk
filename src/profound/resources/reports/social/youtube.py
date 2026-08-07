# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.reports.social import youtube_get_videos_params, youtube_get_summary_params, youtube_get_channels_params
from ....types.reports.social.youtube_get_videos_response import YoutubeGetVideosResponse
from ....types.reports.social.youtube_get_summary_response import YoutubeGetSummaryResponse
from ....types.reports.social.youtube_get_channels_response import YoutubeGetChannelsResponse

__all__ = ["YoutubeResource", "AsyncYoutubeResource"]


class YoutubeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> YoutubeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return YoutubeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> YoutubeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return YoutubeResourceWithStreamingResponse(self)

    def get_channels(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[youtube_get_channels_params.Filter] | Omit = omit,
        group_by: List[Literal["channel", "video_category", "model", "source_type"]] | Omit = omit,
        interval: Optional[Literal["day", "week", "month"]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        source_types: Optional[List[Literal["video", "short", "channel", "playlist", "other"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetChannelsResponse:
        """
        Rank the YouTube channels cited in a category, or the video categories they
        publish in.

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: What each row represents. Empty or `["channel"]` ranks channels;
              `["video_category"]` ranks content categories; `["source_type"]` ranks source
              types; `["channel", "video_category"]`, `["channel", "source_type"]` and
              `["channel", "model"]` return cross-tabs — a row per channel per category, or
              per answer engine. `limit` counts leading channels in every case, so ten
              channels across nine engines is ten channels and ninety rows.

          interval: Return a time series instead of window totals: one row per entity per period,
              each carrying `date`. `citation_share` is then relative to that period, so the
              series is comparable across periods. Omit for window totals.

          limit: Page size; default 10, max 50.

          source_types: Limit results to YouTube source types: `video`, `short`, `channel`, `playlist`,
              or `other`. Omit to include `video`, `short`, `channel`, and `playlist`; `other`
              is excluded because those citations have no channel. Requests containing `other`
              are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/social/youtube/channels",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "source_types": source_types,
                },
                youtube_get_channels_params.YoutubeGetChannelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=YoutubeGetChannelsResponse,
        )

    def get_summary(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        filter: Optional[youtube_get_summary_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetSummaryResponse:
        """
        Report how much of youtube.com the channel and video rankings account for.

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/social/youtube/summary",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "filter": filter,
                },
                youtube_get_summary_params.YoutubeGetSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=YoutubeGetSummaryResponse,
        )

    def get_videos(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        attribution: Literal["attributed", "unattributed", "all"] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[youtube_get_videos_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        source_types: Optional[List[Literal["video", "short", "channel", "playlist", "other"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetVideosResponse:
        """
        Rank cited YouTube videos, for one channel or across all of them.

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          attribution: Choose attributed citations, unattributed citations, or all citations. An
              unattributed row has no channel: `source_type` is `other` for a search or feed
              URL that names no source, and any other type is a source we have no channel for.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          source_types: Limit results to YouTube source types: `video`, `short`, `channel`, `playlist`,
              or `other`. Omit to include `video` and `short` with the default
              `attribution='attributed'`; `unattributed` and `all` widen the default to all
              five source types. Requests containing `other` with `attribution='attributed'`
              are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/social/youtube/videos",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "attribution": attribution,
                    "cursor": cursor,
                    "filter": filter,
                    "limit": limit,
                    "source_types": source_types,
                },
                youtube_get_videos_params.YoutubeGetVideosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=YoutubeGetVideosResponse,
        )


class AsyncYoutubeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncYoutubeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncYoutubeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncYoutubeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncYoutubeResourceWithStreamingResponse(self)

    async def get_channels(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[youtube_get_channels_params.Filter] | Omit = omit,
        group_by: List[Literal["channel", "video_category", "model", "source_type"]] | Omit = omit,
        interval: Optional[Literal["day", "week", "month"]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        source_types: Optional[List[Literal["video", "short", "channel", "playlist", "other"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetChannelsResponse:
        """
        Rank the YouTube channels cited in a category, or the video categories they
        publish in.

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: What each row represents. Empty or `["channel"]` ranks channels;
              `["video_category"]` ranks content categories; `["source_type"]` ranks source
              types; `["channel", "video_category"]`, `["channel", "source_type"]` and
              `["channel", "model"]` return cross-tabs — a row per channel per category, or
              per answer engine. `limit` counts leading channels in every case, so ten
              channels across nine engines is ten channels and ninety rows.

          interval: Return a time series instead of window totals: one row per entity per period,
              each carrying `date`. `citation_share` is then relative to that period, so the
              series is comparable across periods. Omit for window totals.

          limit: Page size; default 10, max 50.

          source_types: Limit results to YouTube source types: `video`, `short`, `channel`, `playlist`,
              or `other`. Omit to include `video`, `short`, `channel`, and `playlist`; `other`
              is excluded because those citations have no channel. Requests containing `other`
              are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/social/youtube/channels",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "source_types": source_types,
                },
                youtube_get_channels_params.YoutubeGetChannelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=YoutubeGetChannelsResponse,
        )

    async def get_summary(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        filter: Optional[youtube_get_summary_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetSummaryResponse:
        """
        Report how much of youtube.com the channel and video rankings account for.

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/social/youtube/summary",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "filter": filter,
                },
                youtube_get_summary_params.YoutubeGetSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=YoutubeGetSummaryResponse,
        )

    async def get_videos(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        attribution: Literal["attributed", "unattributed", "all"] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[youtube_get_videos_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        source_types: Optional[List[Literal["video", "short", "channel", "playlist", "other"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetVideosResponse:
        """
        Rank cited YouTube videos, for one channel or across all of them.

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          attribution: Choose attributed citations, unattributed citations, or all citations. An
              unattributed row has no channel: `source_type` is `other` for a search or feed
              URL that names no source, and any other type is a source we have no channel for.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          source_types: Limit results to YouTube source types: `video`, `short`, `channel`, `playlist`,
              or `other`. Omit to include `video` and `short` with the default
              `attribution='attributed'`; `unattributed` and `all` widen the default to all
              five source types. Requests containing `other` with `attribution='attributed'`
              are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/social/youtube/videos",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "attribution": attribution,
                    "cursor": cursor,
                    "filter": filter,
                    "limit": limit,
                    "source_types": source_types,
                },
                youtube_get_videos_params.YoutubeGetVideosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=YoutubeGetVideosResponse,
        )


class YoutubeResourceWithRawResponse:
    def __init__(self, youtube: YoutubeResource) -> None:
        self._youtube = youtube

        self.get_channels = to_raw_response_wrapper(
            youtube.get_channels,
        )
        self.get_summary = to_raw_response_wrapper(
            youtube.get_summary,
        )
        self.get_videos = to_raw_response_wrapper(
            youtube.get_videos,
        )


class AsyncYoutubeResourceWithRawResponse:
    def __init__(self, youtube: AsyncYoutubeResource) -> None:
        self._youtube = youtube

        self.get_channels = async_to_raw_response_wrapper(
            youtube.get_channels,
        )
        self.get_summary = async_to_raw_response_wrapper(
            youtube.get_summary,
        )
        self.get_videos = async_to_raw_response_wrapper(
            youtube.get_videos,
        )


class YoutubeResourceWithStreamingResponse:
    def __init__(self, youtube: YoutubeResource) -> None:
        self._youtube = youtube

        self.get_channels = to_streamed_response_wrapper(
            youtube.get_channels,
        )
        self.get_summary = to_streamed_response_wrapper(
            youtube.get_summary,
        )
        self.get_videos = to_streamed_response_wrapper(
            youtube.get_videos,
        )


class AsyncYoutubeResourceWithStreamingResponse:
    def __init__(self, youtube: AsyncYoutubeResource) -> None:
        self._youtube = youtube

        self.get_channels = async_to_streamed_response_wrapper(
            youtube.get_channels,
        )
        self.get_summary = async_to_streamed_response_wrapper(
            youtube.get_summary,
        )
        self.get_videos = async_to_streamed_response_wrapper(
            youtube.get_videos,
        )
