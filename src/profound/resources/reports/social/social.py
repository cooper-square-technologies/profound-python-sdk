# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .youtube import (
    YoutubeResource,
    AsyncYoutubeResource,
    YoutubeResourceWithRawResponse,
    AsyncYoutubeResourceWithRawResponse,
    YoutubeResourceWithStreamingResponse,
    AsyncYoutubeResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SocialResource", "AsyncSocialResource"]


class SocialResource(SyncAPIResource):
    @cached_property
    def youtube(self) -> YoutubeResource:
        return YoutubeResource(self._client)

    @cached_property
    def with_raw_response(self) -> SocialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SocialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SocialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return SocialResourceWithStreamingResponse(self)


class AsyncSocialResource(AsyncAPIResource):
    @cached_property
    def youtube(self) -> AsyncYoutubeResource:
        return AsyncYoutubeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSocialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSocialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSocialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
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
