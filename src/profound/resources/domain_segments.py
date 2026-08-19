# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.domain_segment_list_v2_get_response import DomainSegmentListV2GetResponse
from ..types import domain_segment_list_v2_get_params

__all__ = ["DomainSegmentsResource", "AsyncDomainSegmentsResource"]


class DomainSegmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainSegmentsResourceWithRawResponse:
        return DomainSegmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainSegmentsResourceWithStreamingResponse:
        return DomainSegmentsResourceWithStreamingResponse(self)

    def list_v2_get(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainSegmentListV2GetResponse:
        """
        List domain segments visible to the caller for a workspace.

        Returns the id and name of every domain segment the caller can access, so a
        customer can discover a `view_id` to pass into agent analytics report queries.

        Args:
            organization_id: Organization UUID to list segments for. Required when the caller belongs to multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DomainSegmentListV2GetResponse: Successful Response

        Example:
            ```python
            domain_segment = client.domain_segments.list_v2_get()
            ```
        """
        return self._get(
            "/v2/domain-segments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, domain_segment_list_v2_get_params.DomainSegmentListV2GetParams
                ),
            ),
            cast_to=DomainSegmentListV2GetResponse,
        )


class AsyncDomainSegmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainSegmentsResourceWithRawResponse:
        return AsyncDomainSegmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainSegmentsResourceWithStreamingResponse:
        return AsyncDomainSegmentsResourceWithStreamingResponse(self)

    async def list_v2_get(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainSegmentListV2GetResponse:
        """
        List domain segments visible to the caller for a workspace.

        Returns the id and name of every domain segment the caller can access, so a
        customer can discover a `view_id` to pass into agent analytics report queries.

        Args:
            organization_id: Organization UUID to list segments for. Required when the caller belongs to multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DomainSegmentListV2GetResponse: Successful Response

        Example:
            ```python
            domain_segment = await client.domain_segments.list_v2_get()
            ```
        """
        return await self._get(
            "/v2/domain-segments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, domain_segment_list_v2_get_params.DomainSegmentListV2GetParams
                ),
            ),
            cast_to=DomainSegmentListV2GetResponse,
        )


class DomainSegmentsResourceWithRawResponse:
    def __init__(self, domain_segments: DomainSegmentsResource) -> None:
        self._domain_segments = domain_segments

        self.list_v2_get = to_raw_response_wrapper(
            domain_segments.list_v2_get,
        )


class AsyncDomainSegmentsResourceWithRawResponse:
    def __init__(self, domain_segments: AsyncDomainSegmentsResource) -> None:
        self._domain_segments = domain_segments

        self.list_v2_get = async_to_raw_response_wrapper(
            domain_segments.list_v2_get,
        )


class DomainSegmentsResourceWithStreamingResponse:
    def __init__(self, domain_segments: DomainSegmentsResource) -> None:
        self._domain_segments = domain_segments

        self.list_v2_get = to_streamed_response_wrapper(
            domain_segments.list_v2_get,
        )


class AsyncDomainSegmentsResourceWithStreamingResponse:
    def __init__(self, domain_segments: AsyncDomainSegmentsResource) -> None:
        self._domain_segments = domain_segments

        self.list_v2_get = async_to_streamed_response_wrapper(
            domain_segments.list_v2_get,
        )
