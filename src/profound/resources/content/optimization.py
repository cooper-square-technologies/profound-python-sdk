# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...types.content import optimization_list_params
from ...types.content.optimization_list_response import OptimizationListResponse
from ...types.content.optimization_retrieve_response import OptimizationRetrieveResponse

__all__ = ["OptimizationResource", "AsyncOptimizationResource"]


class OptimizationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptimizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OptimizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptimizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return OptimizationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        content_id: str,
        *,
        asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptimizationRetrieveResponse:
        """
        Optimization Analysis

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if not content_id:
            raise ValueError(f"Expected a non-empty value for `content_id` but received {content_id!r}")
        return self._get(
            f"/v1/content/{asset_id}/optimization/{content_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptimizationRetrieveResponse,
        )

    def list(
        self,
        asset_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptimizationListResponse:
        """
        Optimization List

        Args:
          limit: Maximum number of results to return

          offset: Offset for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get(
            f"/v1/content/{asset_id}/optimization",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    optimization_list_params.OptimizationListParams,
                ),
            ),
            cast_to=OptimizationListResponse,
        )


class AsyncOptimizationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptimizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOptimizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptimizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncOptimizationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        content_id: str,
        *,
        asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptimizationRetrieveResponse:
        """
        Optimization Analysis

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if not content_id:
            raise ValueError(f"Expected a non-empty value for `content_id` but received {content_id!r}")
        return await self._get(
            f"/v1/content/{asset_id}/optimization/{content_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptimizationRetrieveResponse,
        )

    async def list(
        self,
        asset_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptimizationListResponse:
        """
        Optimization List

        Args:
          limit: Maximum number of results to return

          offset: Offset for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._get(
            f"/v1/content/{asset_id}/optimization",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    optimization_list_params.OptimizationListParams,
                ),
            ),
            cast_to=OptimizationListResponse,
        )


class OptimizationResourceWithRawResponse:
    def __init__(self, optimization: OptimizationResource) -> None:
        self._optimization = optimization

        self.retrieve = to_raw_response_wrapper(
            optimization.retrieve,
        )
        self.list = to_raw_response_wrapper(
            optimization.list,
        )


class AsyncOptimizationResourceWithRawResponse:
    def __init__(self, optimization: AsyncOptimizationResource) -> None:
        self._optimization = optimization

        self.retrieve = async_to_raw_response_wrapper(
            optimization.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            optimization.list,
        )


class OptimizationResourceWithStreamingResponse:
    def __init__(self, optimization: OptimizationResource) -> None:
        self._optimization = optimization

        self.retrieve = to_streamed_response_wrapper(
            optimization.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            optimization.list,
        )


class AsyncOptimizationResourceWithStreamingResponse:
    def __init__(self, optimization: AsyncOptimizationResource) -> None:
        self._optimization = optimization

        self.retrieve = async_to_streamed_response_wrapper(
            optimization.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            optimization.list,
        )
