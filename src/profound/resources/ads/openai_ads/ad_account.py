# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.ads.openai_ads import ad_account_retrieve_insights_params
from ....types.ads.openai_ads.ad_account_retrieve_insights_response import AdAccountRetrieveInsightsResponse

__all__ = ["AdAccountResource", "AsyncAdAccountResource"]


class AdAccountResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdAccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AdAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AdAccountResourceWithStreamingResponse(self)

    def retrieve_insights(
        self,
        *,
        after: Optional[str] | Omit = omit,
        aggregation_level: Optional[Literal["ad_account", "campaign", "ad_group", "ad"]] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        time_granularity: Optional[Literal["hourly", "daily", "monthly", "none"]] | Omit = omit,
        time_ranges: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdAccountRetrieveInsightsResponse:
        """
        Get ad account insights for the organization's OpenAI Ads partner brand.

        `aggregation_level=campaign` returns one row per campaign (with `campaign_id` /
        `campaign_name` and all metrics), so every campaign's insights come back in a
        single call; `time_granularity=daily` gives per-day rows (e.g. daily spend).

        Args:
          after: Return items after this ID (forward pagination).

          aggregation_level: Row entity for the insights breakdown. `campaign` returns one row per campaign.

          before: Return items before this ID (backward pagination).

          limit: Maximum rows to return.

          organization_id: Organization scope for API keys that can access multiple organizations.

          time_granularity: Time bucket for the rows; `none` or omitted returns totals over the whole range.

          time_ranges: Time ranges as JSON objects, e.g.
              `{"type": "date_range", "since": "2026-07-01", "until": "2026-07-18"}`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/ads/openai-ads/ad-account/insights",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "aggregation_level": aggregation_level,
                        "before": before,
                        "limit": limit,
                        "organization_id": organization_id,
                        "time_granularity": time_granularity,
                        "time_ranges": time_ranges,
                    },
                    ad_account_retrieve_insights_params.AdAccountRetrieveInsightsParams,
                ),
            ),
            cast_to=AdAccountRetrieveInsightsResponse,
        )


class AsyncAdAccountResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdAccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAdAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncAdAccountResourceWithStreamingResponse(self)

    async def retrieve_insights(
        self,
        *,
        after: Optional[str] | Omit = omit,
        aggregation_level: Optional[Literal["ad_account", "campaign", "ad_group", "ad"]] | Omit = omit,
        before: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        time_granularity: Optional[Literal["hourly", "daily", "monthly", "none"]] | Omit = omit,
        time_ranges: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdAccountRetrieveInsightsResponse:
        """
        Get ad account insights for the organization's OpenAI Ads partner brand.

        `aggregation_level=campaign` returns one row per campaign (with `campaign_id` /
        `campaign_name` and all metrics), so every campaign's insights come back in a
        single call; `time_granularity=daily` gives per-day rows (e.g. daily spend).

        Args:
          after: Return items after this ID (forward pagination).

          aggregation_level: Row entity for the insights breakdown. `campaign` returns one row per campaign.

          before: Return items before this ID (backward pagination).

          limit: Maximum rows to return.

          organization_id: Organization scope for API keys that can access multiple organizations.

          time_granularity: Time bucket for the rows; `none` or omitted returns totals over the whole range.

          time_ranges: Time ranges as JSON objects, e.g.
              `{"type": "date_range", "since": "2026-07-01", "until": "2026-07-18"}`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/ads/openai-ads/ad-account/insights",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "aggregation_level": aggregation_level,
                        "before": before,
                        "limit": limit,
                        "organization_id": organization_id,
                        "time_granularity": time_granularity,
                        "time_ranges": time_ranges,
                    },
                    ad_account_retrieve_insights_params.AdAccountRetrieveInsightsParams,
                ),
            ),
            cast_to=AdAccountRetrieveInsightsResponse,
        )


class AdAccountResourceWithRawResponse:
    def __init__(self, ad_account: AdAccountResource) -> None:
        self._ad_account = ad_account

        self.retrieve_insights = to_raw_response_wrapper(
            ad_account.retrieve_insights,
        )


class AsyncAdAccountResourceWithRawResponse:
    def __init__(self, ad_account: AsyncAdAccountResource) -> None:
        self._ad_account = ad_account

        self.retrieve_insights = async_to_raw_response_wrapper(
            ad_account.retrieve_insights,
        )


class AdAccountResourceWithStreamingResponse:
    def __init__(self, ad_account: AdAccountResource) -> None:
        self._ad_account = ad_account

        self.retrieve_insights = to_streamed_response_wrapper(
            ad_account.retrieve_insights,
        )


class AsyncAdAccountResourceWithStreamingResponse:
    def __init__(self, ad_account: AsyncAdAccountResource) -> None:
        self._ad_account = ad_account

        self.retrieve_insights = async_to_streamed_response_wrapper(
            ad_account.retrieve_insights,
        )
