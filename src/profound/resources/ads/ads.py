# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .openai_ads.openai_ads import (
    OpenAIAdsResource,
    AsyncOpenAIAdsResource,
    OpenAIAdsResourceWithRawResponse,
    AsyncOpenAIAdsResourceWithRawResponse,
    OpenAIAdsResourceWithStreamingResponse,
    AsyncOpenAIAdsResourceWithStreamingResponse,
)

__all__ = ["AdsResource", "AsyncAdsResource"]


class AdsResource(SyncAPIResource):
    @cached_property
    def openai_ads(self) -> OpenAIAdsResource:
        return OpenAIAdsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AdsResourceWithStreamingResponse(self)


class AsyncAdsResource(AsyncAPIResource):
    @cached_property
    def openai_ads(self) -> AsyncOpenAIAdsResource:
        return AsyncOpenAIAdsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncAdsResourceWithStreamingResponse(self)


class AdsResourceWithRawResponse:
    def __init__(self, ads: AdsResource) -> None:
        self._ads = ads

    @cached_property
    def openai_ads(self) -> OpenAIAdsResourceWithRawResponse:
        return OpenAIAdsResourceWithRawResponse(self._ads.openai_ads)


class AsyncAdsResourceWithRawResponse:
    def __init__(self, ads: AsyncAdsResource) -> None:
        self._ads = ads

    @cached_property
    def openai_ads(self) -> AsyncOpenAIAdsResourceWithRawResponse:
        return AsyncOpenAIAdsResourceWithRawResponse(self._ads.openai_ads)


class AdsResourceWithStreamingResponse:
    def __init__(self, ads: AdsResource) -> None:
        self._ads = ads

    @cached_property
    def openai_ads(self) -> OpenAIAdsResourceWithStreamingResponse:
        return OpenAIAdsResourceWithStreamingResponse(self._ads.openai_ads)


class AsyncAdsResourceWithStreamingResponse:
    def __init__(self, ads: AsyncAdsResource) -> None:
        self._ads = ads

    @cached_property
    def openai_ads(self) -> AsyncOpenAIAdsResourceWithStreamingResponse:
        return AsyncOpenAIAdsResourceWithStreamingResponse(self._ads.openai_ads)
