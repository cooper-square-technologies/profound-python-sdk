# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional, Union
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
from ...types.prompt_volumes.volume_on_the_fly_response import VolumeOnTheFlyResponse
from ...types.prompt_volumes import volume_on_the_fly_params

__all__ = ["VolumeResource", "AsyncVolumeResource"]


class VolumeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VolumeResourceWithRawResponse:
        return VolumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VolumeResourceWithStreamingResponse:
        return VolumeResourceWithStreamingResponse(self)

    def on_the_fly(
        self,
        *,
        keyword: str,
        matching_type: Literal["exact_match", "phrase_match"],
        start_date: Union[str, date],
        end_date: Union[str, date],
        regions: SequenceNotStr[str] | Omit = omit,
        platforms: SequenceNotStr[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeOnTheFlyResponse:
        """
        Weekly and monthly volume projections for one keyword.

        Each organization can look up 1,000 distinct normalized keywords per UTC
        day. Repeats consume no additional allowance. New keywords over the cap
        return 429 with X-KeywordQuota-* and Retry-After headers. Quota admission
        requires Redis (503 when unavailable); empty results and query failures
        retain the reservation. Slices with at most two users are omitted.

        Args:
            keyword: Body parameter.
            matching_type: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            regions: Body parameter.
            platforms: Body parameter.
            organization_id: Organization whose daily keyword allowance is used. Required in the JSON request body for API keys with multiple organizations that have API access. If omitted or null, defaults to the API key's sole organization with API access or the token's active organization. For OAuth/M2M tokens, any supplied organization_id must match the token's organization.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VolumeOnTheFlyResponse: Successful Response

        Example:
            ```python
            volume = client.prompt_volumes.volume.on_the_fly(
                keyword="",
                matching_type="exact_match",
                start_date="2024-01-01",
                end_date="2024-01-01",
            )
            ```
        """
        return self._post(
            "/v2/prompt-volumes/volume/on-the-fly",
            body=maybe_transform(
                {
                    "keyword": keyword,
                    "matching_type": matching_type,
                    "start_date": start_date,
                    "end_date": end_date,
                    "regions": regions,
                    "platforms": platforms,
                    "organization_id": organization_id,
                },
                volume_on_the_fly_params.VolumeOnTheFlyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeOnTheFlyResponse,
        )


class AsyncVolumeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVolumeResourceWithRawResponse:
        return AsyncVolumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVolumeResourceWithStreamingResponse:
        return AsyncVolumeResourceWithStreamingResponse(self)

    async def on_the_fly(
        self,
        *,
        keyword: str,
        matching_type: Literal["exact_match", "phrase_match"],
        start_date: Union[str, date],
        end_date: Union[str, date],
        regions: SequenceNotStr[str] | Omit = omit,
        platforms: SequenceNotStr[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VolumeOnTheFlyResponse:
        """
        Weekly and monthly volume projections for one keyword.

        Each organization can look up 1,000 distinct normalized keywords per UTC
        day. Repeats consume no additional allowance. New keywords over the cap
        return 429 with X-KeywordQuota-* and Retry-After headers. Quota admission
        requires Redis (503 when unavailable); empty results and query failures
        retain the reservation. Slices with at most two users are omitted.

        Args:
            keyword: Body parameter.
            matching_type: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            regions: Body parameter.
            platforms: Body parameter.
            organization_id: Organization whose daily keyword allowance is used. Required in the JSON request body for API keys with multiple organizations that have API access. If omitted or null, defaults to the API key's sole organization with API access or the token's active organization. For OAuth/M2M tokens, any supplied organization_id must match the token's organization.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            VolumeOnTheFlyResponse: Successful Response

        Example:
            ```python
            volume = await client.prompt_volumes.volume.on_the_fly(
                keyword="",
                matching_type="exact_match",
                start_date="2024-01-01",
                end_date="2024-01-01",
            )
            ```
        """
        return await self._post(
            "/v2/prompt-volumes/volume/on-the-fly",
            body=await async_maybe_transform(
                {
                    "keyword": keyword,
                    "matching_type": matching_type,
                    "start_date": start_date,
                    "end_date": end_date,
                    "regions": regions,
                    "platforms": platforms,
                    "organization_id": organization_id,
                },
                volume_on_the_fly_params.VolumeOnTheFlyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeOnTheFlyResponse,
        )


class VolumeResourceWithRawResponse:
    def __init__(self, volume: VolumeResource) -> None:
        self._volume = volume

        self.on_the_fly = to_raw_response_wrapper(
            volume.on_the_fly,
        )


class AsyncVolumeResourceWithRawResponse:
    def __init__(self, volume: AsyncVolumeResource) -> None:
        self._volume = volume

        self.on_the_fly = async_to_raw_response_wrapper(
            volume.on_the_fly,
        )


class VolumeResourceWithStreamingResponse:
    def __init__(self, volume: VolumeResource) -> None:
        self._volume = volume

        self.on_the_fly = to_streamed_response_wrapper(
            volume.on_the_fly,
        )


class AsyncVolumeResourceWithStreamingResponse:
    def __init__(self, volume: AsyncVolumeResource) -> None:
        self._volume = volume

        self.on_the_fly = async_to_streamed_response_wrapper(
            volume.on_the_fly,
        )
