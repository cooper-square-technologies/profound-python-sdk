# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .openai_ads import (
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
        return AdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdsResourceWithStreamingResponse:
        return AdsResourceWithStreamingResponse(self)


class AsyncAdsResource(AsyncAPIResource):
    @cached_property
    def openai_ads(self) -> AsyncOpenAIAdsResource:
        return AsyncOpenAIAdsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdsResourceWithRawResponse:
        return AsyncAdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdsResourceWithStreamingResponse:
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
