# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Union
from datetime import date
from typing_extensions import Literal
from ..._types import SequenceNotStr

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
from ...types.prompt_volumes.intent_on_the_fly_response import IntentOnTheFlyResponse
from ...types.prompt_volumes import intent_on_the_fly_params

__all__ = ["IntentsResource", "AsyncIntentsResource"]


class IntentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntentsResourceWithRawResponse:
        return IntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntentsResourceWithStreamingResponse:
        return IntentsResourceWithStreamingResponse(self)

    def on_the_fly(
        self,
        *,
        keyword: str,
        matching_type: Literal["exact_match", "phrase_match"],
        start_date: Union[str, date],
        end_date: Union[str, date],
        regions: SequenceNotStr[str] | Omit = omit,
        platforms: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntentOnTheFlyResponse:
        """
        Intent shares for one keyword across the requested cohort weeks.

        Shares are fractions from 0 to 1 over classified matching conversations.
        Cohorts with at most two matching users are omitted for privacy. This
        endpoint shares the volume endpoint's burst limit but consumes no daily
        keyword quota.

        Args:
            keyword: Body parameter.
            matching_type: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            regions: Body parameter.
            platforms: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntentOnTheFlyResponse: Successful Response

        Example:
            ```python
            intent = client.prompt_volumes.intents.on_the_fly(
                keyword="",
                matching_type="exact_match",
                start_date="2024-01-01",
                end_date="2024-01-01",
            )
            ```
        """
        return self._post(
            "/v2/prompt-volumes/intents/on-the-fly",
            body=maybe_transform(
                {
                    "keyword": keyword,
                    "matching_type": matching_type,
                    "start_date": start_date,
                    "end_date": end_date,
                    "regions": regions,
                    "platforms": platforms,
                },
                intent_on_the_fly_params.IntentOnTheFlyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntentOnTheFlyResponse,
        )


class AsyncIntentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntentsResourceWithRawResponse:
        return AsyncIntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntentsResourceWithStreamingResponse:
        return AsyncIntentsResourceWithStreamingResponse(self)

    async def on_the_fly(
        self,
        *,
        keyword: str,
        matching_type: Literal["exact_match", "phrase_match"],
        start_date: Union[str, date],
        end_date: Union[str, date],
        regions: SequenceNotStr[str] | Omit = omit,
        platforms: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntentOnTheFlyResponse:
        """
        Intent shares for one keyword across the requested cohort weeks.

        Shares are fractions from 0 to 1 over classified matching conversations.
        Cohorts with at most two matching users are omitted for privacy. This
        endpoint shares the volume endpoint's burst limit but consumes no daily
        keyword quota.

        Args:
            keyword: Body parameter.
            matching_type: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            regions: Body parameter.
            platforms: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntentOnTheFlyResponse: Successful Response

        Example:
            ```python
            intent = await client.prompt_volumes.intents.on_the_fly(
                keyword="",
                matching_type="exact_match",
                start_date="2024-01-01",
                end_date="2024-01-01",
            )
            ```
        """
        return await self._post(
            "/v2/prompt-volumes/intents/on-the-fly",
            body=await async_maybe_transform(
                {
                    "keyword": keyword,
                    "matching_type": matching_type,
                    "start_date": start_date,
                    "end_date": end_date,
                    "regions": regions,
                    "platforms": platforms,
                },
                intent_on_the_fly_params.IntentOnTheFlyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntentOnTheFlyResponse,
        )


class IntentsResourceWithRawResponse:
    def __init__(self, intents: IntentsResource) -> None:
        self._intents = intents

        self.on_the_fly = to_raw_response_wrapper(
            intents.on_the_fly,
        )


class AsyncIntentsResourceWithRawResponse:
    def __init__(self, intents: AsyncIntentsResource) -> None:
        self._intents = intents

        self.on_the_fly = async_to_raw_response_wrapper(
            intents.on_the_fly,
        )


class IntentsResourceWithStreamingResponse:
    def __init__(self, intents: IntentsResource) -> None:
        self._intents = intents

        self.on_the_fly = to_streamed_response_wrapper(
            intents.on_the_fly,
        )


class AsyncIntentsResourceWithStreamingResponse:
    def __init__(self, intents: AsyncIntentsResource) -> None:
        self._intents = intents

        self.on_the_fly = async_to_streamed_response_wrapper(
            intents.on_the_fly,
        )
