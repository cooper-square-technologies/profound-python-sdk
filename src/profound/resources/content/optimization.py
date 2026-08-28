# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.content.optimization_list_response import OptimizationListResponse
from ...types.content import optimization_list_params
from ...types.content.optimization_retrieve_response import OptimizationRetrieveResponse

__all__ = ["OptimizationResource", "AsyncOptimizationResource"]


class OptimizationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptimizationResourceWithRawResponse:
        return OptimizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptimizationResourceWithStreamingResponse:
        return OptimizationResourceWithStreamingResponse(self)

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
            asset_id: Path parameter.
            limit: Maximum number of results to return
            offset: Offset for pagination
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OptimizationListResponse: Successful Response

        Example:
            ```python
            optimization = client.content.optimization.list(
                asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=10000,
                offset=0,
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get(
            path_template("/v1/content/{asset_id}/optimization", **{"asset_id": asset_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "offset": offset}, optimization_list_params.OptimizationListParams
                ),
            ),
            cast_to=OptimizationListResponse,
        )

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
            content_id: Path parameter.
            asset_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OptimizationRetrieveResponse: Successful Response

        Example:
            ```python
            optimization = client.content.optimization.retrieve(
                asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                content_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if content_id is None or (isinstance(content_id, str) and not content_id):
            raise ValueError(f"Expected a non-empty value for `content_id` but received {content_id!r}")
        return self._get(
            path_template(
                "/v1/content/{asset_id}/optimization/{content_id}", **{"asset_id": asset_id, "content_id": content_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptimizationRetrieveResponse,
        )


class AsyncOptimizationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptimizationResourceWithRawResponse:
        return AsyncOptimizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptimizationResourceWithStreamingResponse:
        return AsyncOptimizationResourceWithStreamingResponse(self)

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
            asset_id: Path parameter.
            limit: Maximum number of results to return
            offset: Offset for pagination
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OptimizationListResponse: Successful Response

        Example:
            ```python
            optimization = await client.content.optimization.list(
                asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=10000,
                offset=0,
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._get(
            path_template("/v1/content/{asset_id}/optimization", **{"asset_id": asset_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "offset": offset}, optimization_list_params.OptimizationListParams
                ),
            ),
            cast_to=OptimizationListResponse,
        )

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
            content_id: Path parameter.
            asset_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OptimizationRetrieveResponse: Successful Response

        Example:
            ```python
            optimization = await client.content.optimization.retrieve(
                asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                content_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if asset_id is None or (isinstance(asset_id, str) and not asset_id):
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if content_id is None or (isinstance(content_id, str) and not content_id):
            raise ValueError(f"Expected a non-empty value for `content_id` but received {content_id!r}")
        return await self._get(
            path_template(
                "/v1/content/{asset_id}/optimization/{content_id}", **{"asset_id": asset_id, "content_id": content_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OptimizationRetrieveResponse,
        )


class OptimizationResourceWithRawResponse:
    def __init__(self, optimization: OptimizationResource) -> None:
        self._optimization = optimization

        self.list = to_raw_response_wrapper(
            optimization.list,
        )
        self.retrieve = to_raw_response_wrapper(
            optimization.retrieve,
        )


class AsyncOptimizationResourceWithRawResponse:
    def __init__(self, optimization: AsyncOptimizationResource) -> None:
        self._optimization = optimization

        self.list = async_to_raw_response_wrapper(
            optimization.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            optimization.retrieve,
        )


class OptimizationResourceWithStreamingResponse:
    def __init__(self, optimization: OptimizationResource) -> None:
        self._optimization = optimization

        self.list = to_streamed_response_wrapper(
            optimization.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            optimization.retrieve,
        )


class AsyncOptimizationResourceWithStreamingResponse:
    def __init__(self, optimization: AsyncOptimizationResource) -> None:
        self._optimization = optimization

        self.list = async_to_streamed_response_wrapper(
            optimization.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            optimization.retrieve,
        )
