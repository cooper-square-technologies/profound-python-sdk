# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.projects.generation_list_response import GenerationListResponse
from ...types.projects.generation_retrieve_response import GenerationRetrieveResponse

__all__ = ["GenerationsResource", "AsyncGenerationsResource"]


class GenerationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerationsResourceWithRawResponse:
        return GenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerationsResourceWithStreamingResponse:
        return GenerationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationListResponse:
        """
        List Project Generations

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            GenerationListResponse: Successful Response

        Example:
            ```python
            generation = client.projects.generations.list()
            ```

        Deprecated: this method is deprecated.
        """
        return self._get(
            "/v1/projects/generations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationListResponse,
        )

    def retrieve(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationRetrieveResponse:
        """
        Get Project Generation Status

        Args:
            run_id: Unique project generation run ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            GenerationRetrieveResponse: Successful Response

        Example:
            ```python
            generation = client.projects.generations.retrieve(
                run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if run_id is None or (isinstance(run_id, str) and not run_id):
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/v1/projects/generations/{run_id}", **{"run_id": run_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationRetrieveResponse,
        )


class AsyncGenerationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerationsResourceWithRawResponse:
        return AsyncGenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerationsResourceWithStreamingResponse:
        return AsyncGenerationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationListResponse:
        """
        List Project Generations

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            GenerationListResponse: Successful Response

        Example:
            ```python
            generation = await client.projects.generations.list()
            ```

        Deprecated: this method is deprecated.
        """
        return await self._get(
            "/v1/projects/generations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationListResponse,
        )

    async def retrieve(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationRetrieveResponse:
        """
        Get Project Generation Status

        Args:
            run_id: Unique project generation run ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            GenerationRetrieveResponse: Successful Response

        Example:
            ```python
            generation = await client.projects.generations.retrieve(
                run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```

        Deprecated: this method is deprecated.
        """
        if run_id is None or (isinstance(run_id, str) and not run_id):
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/v1/projects/generations/{run_id}", **{"run_id": run_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationRetrieveResponse,
        )


class GenerationsResourceWithRawResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.list = to_raw_response_wrapper(
            generations.list,
        )
        self.retrieve = to_raw_response_wrapper(
            generations.retrieve,
        )


class AsyncGenerationsResourceWithRawResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.list = async_to_raw_response_wrapper(
            generations.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            generations.retrieve,
        )


class GenerationsResourceWithStreamingResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.list = to_streamed_response_wrapper(
            generations.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            generations.retrieve,
        )


class AsyncGenerationsResourceWithStreamingResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.list = async_to_streamed_response_wrapper(
            generations.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            generations.retrieve,
        )
