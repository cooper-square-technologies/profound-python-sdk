# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .youtube import (
    YoutubeResource,
    AsyncYoutubeResource,
    YoutubeResourceWithRawResponse,
    AsyncYoutubeResourceWithRawResponse,
    YoutubeResourceWithStreamingResponse,
    AsyncYoutubeResourceWithStreamingResponse,
)

__all__ = ["SocialResource", "AsyncSocialResource"]


class SocialResource(SyncAPIResource):
    @cached_property
    def youtube(self) -> YoutubeResource:
        return YoutubeResource(self._client)

    @cached_property
    def with_raw_response(self) -> SocialResourceWithRawResponse:
        return SocialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SocialResourceWithStreamingResponse:
        return SocialResourceWithStreamingResponse(self)


class AsyncSocialResource(AsyncAPIResource):
    @cached_property
    def youtube(self) -> AsyncYoutubeResource:
        return AsyncYoutubeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSocialResourceWithRawResponse:
        return AsyncSocialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSocialResourceWithStreamingResponse:
        return AsyncSocialResourceWithStreamingResponse(self)


class SocialResourceWithRawResponse:
    def __init__(self, social: SocialResource) -> None:
        self._social = social

    @cached_property
    def youtube(self) -> YoutubeResourceWithRawResponse:
        return YoutubeResourceWithRawResponse(self._social.youtube)


class AsyncSocialResourceWithRawResponse:
    def __init__(self, social: AsyncSocialResource) -> None:
        self._social = social

    @cached_property
    def youtube(self) -> AsyncYoutubeResourceWithRawResponse:
        return AsyncYoutubeResourceWithRawResponse(self._social.youtube)


class SocialResourceWithStreamingResponse:
    def __init__(self, social: SocialResource) -> None:
        self._social = social

    @cached_property
    def youtube(self) -> YoutubeResourceWithStreamingResponse:
        return YoutubeResourceWithStreamingResponse(self._social.youtube)


class AsyncSocialResourceWithStreamingResponse:
    def __init__(self, social: AsyncSocialResource) -> None:
        self._social = social

    @cached_property
    def youtube(self) -> AsyncYoutubeResourceWithStreamingResponse:
        return AsyncYoutubeResourceWithStreamingResponse(self._social.youtube)
