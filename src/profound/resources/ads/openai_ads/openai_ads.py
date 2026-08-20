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
from .ad_account import (
    AdAccountResource,
    AsyncAdAccountResource,
    AdAccountResourceWithRawResponse,
    AsyncAdAccountResourceWithRawResponse,
    AdAccountResourceWithStreamingResponse,
    AsyncAdAccountResourceWithStreamingResponse,
)

__all__ = ["OpenAIAdsResource", "AsyncOpenAIAdsResource"]


class OpenAIAdsResource(SyncAPIResource):
    @cached_property
    def ad_account(self) -> AdAccountResource:
        return AdAccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> OpenAIAdsResourceWithRawResponse:
        return OpenAIAdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpenAIAdsResourceWithStreamingResponse:
        return OpenAIAdsResourceWithStreamingResponse(self)


class AsyncOpenAIAdsResource(AsyncAPIResource):
    @cached_property
    def ad_account(self) -> AsyncAdAccountResource:
        return AsyncAdAccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOpenAIAdsResourceWithRawResponse:
        return AsyncOpenAIAdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpenAIAdsResourceWithStreamingResponse:
        return AsyncOpenAIAdsResourceWithStreamingResponse(self)


class OpenAIAdsResourceWithRawResponse:
    def __init__(self, openai_ads: OpenAIAdsResource) -> None:
        self._openai_ads = openai_ads

    @cached_property
    def ad_account(self) -> AdAccountResourceWithRawResponse:
        return AdAccountResourceWithRawResponse(self._openai_ads.ad_account)


class AsyncOpenAIAdsResourceWithRawResponse:
    def __init__(self, openai_ads: AsyncOpenAIAdsResource) -> None:
        self._openai_ads = openai_ads

    @cached_property
    def ad_account(self) -> AsyncAdAccountResourceWithRawResponse:
        return AsyncAdAccountResourceWithRawResponse(self._openai_ads.ad_account)


class OpenAIAdsResourceWithStreamingResponse:
    def __init__(self, openai_ads: OpenAIAdsResource) -> None:
        self._openai_ads = openai_ads

    @cached_property
    def ad_account(self) -> AdAccountResourceWithStreamingResponse:
        return AdAccountResourceWithStreamingResponse(self._openai_ads.ad_account)


class AsyncOpenAIAdsResourceWithStreamingResponse:
    def __init__(self, openai_ads: AsyncOpenAIAdsResource) -> None:
        self._openai_ads = openai_ads

    @cached_property
    def ad_account(self) -> AsyncAdAccountResourceWithStreamingResponse:
        return AsyncAdAccountResourceWithStreamingResponse(self._openai_ads.ad_account)
