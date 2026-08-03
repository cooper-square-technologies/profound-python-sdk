# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .ad_account import (
    AdAccountResource,
    AsyncAdAccountResource,
    AdAccountResourceWithRawResponse,
    AsyncAdAccountResourceWithRawResponse,
    AdAccountResourceWithStreamingResponse,
    AsyncAdAccountResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OpenAIAdsResource", "AsyncOpenAIAdsResource"]


class OpenAIAdsResource(SyncAPIResource):
    @cached_property
    def ad_account(self) -> AdAccountResource:
        return AdAccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> OpenAIAdsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OpenAIAdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpenAIAdsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return OpenAIAdsResourceWithStreamingResponse(self)


class AsyncOpenAIAdsResource(AsyncAPIResource):
    @cached_property
    def ad_account(self) -> AsyncAdAccountResource:
        return AsyncAdAccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOpenAIAdsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOpenAIAdsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpenAIAdsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
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
