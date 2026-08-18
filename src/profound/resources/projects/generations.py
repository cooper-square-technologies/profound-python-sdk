# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional

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
from ...types.projects.generation_list_v1_get_response import GenerationListV1GetResponse
from ...types.projects import generation_list_v1_get_params, generation_retrieve_status_v1_run_get_params
from ...types.projects.generation_retrieve_status_v1_run_get_response import GenerationRetrieveStatusV1RunGetResponse

__all__ = ["GenerationsResource", "AsyncGenerationsResource"]


class GenerationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerationsResourceWithRawResponse:
        return GenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerationsResourceWithStreamingResponse:
        return GenerationsResourceWithStreamingResponse(self)

    def list_v1_get(
        self,
        *,
        category_id: str,
        status: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationListV1GetResponse:
        """
        List Project Generations

        Args:
            category_id: Category that owns the project.
            status: Comma-separated generation statuses: queued, running, completed, failed.
            limit: Query parameter.
            offset: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            GenerationListV1GetResponse: Successful Response

        Example:
            ```python
            generation = client.projects.generations.list_v1_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=100,
                offset=0,
            )
            ```
        """
        return self._get(
            "/v1/projects/generations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"category_id": category_id, "status": status, "limit": limit, "offset": offset},
                    generation_list_v1_get_params.GenerationListV1GetParams,
                ),
            ),
            cast_to=GenerationListV1GetResponse,
        )

    def retrieve_status_v1_run_get(
        self,
        run_id: str,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationRetrieveStatusV1RunGetResponse:
        """
        Get Project Generation Status

        Args:
            run_id: Unique project generation run ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            GenerationRetrieveStatusV1RunGetResponse: Successful Response

        Example:
            ```python
            generation = client.projects.generations.retrieve_status_v1_run_get(
                run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if run_id is None or (isinstance(run_id, str) and not run_id):
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/v1/projects/generations/{run_id}", **{"run_id": run_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"category_id": category_id},
                    generation_retrieve_status_v1_run_get_params.GenerationRetrieveStatusV1RunGetParams,
                ),
            ),
            cast_to=GenerationRetrieveStatusV1RunGetResponse,
        )


class AsyncGenerationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerationsResourceWithRawResponse:
        return AsyncGenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerationsResourceWithStreamingResponse:
        return AsyncGenerationsResourceWithStreamingResponse(self)

    async def list_v1_get(
        self,
        *,
        category_id: str,
        status: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationListV1GetResponse:
        """
        List Project Generations

        Args:
            category_id: Category that owns the project.
            status: Comma-separated generation statuses: queued, running, completed, failed.
            limit: Query parameter.
            offset: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            GenerationListV1GetResponse: Successful Response

        Example:
            ```python
            generation = await client.projects.generations.list_v1_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=100,
                offset=0,
            )
            ```
        """
        return await self._get(
            "/v1/projects/generations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id, "status": status, "limit": limit, "offset": offset},
                    generation_list_v1_get_params.GenerationListV1GetParams,
                ),
            ),
            cast_to=GenerationListV1GetResponse,
        )

    async def retrieve_status_v1_run_get(
        self,
        run_id: str,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationRetrieveStatusV1RunGetResponse:
        """
        Get Project Generation Status

        Args:
            run_id: Unique project generation run ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            GenerationRetrieveStatusV1RunGetResponse: Successful Response

        Example:
            ```python
            generation = await client.projects.generations.retrieve_status_v1_run_get(
                run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if run_id is None or (isinstance(run_id, str) and not run_id):
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/v1/projects/generations/{run_id}", **{"run_id": run_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id},
                    generation_retrieve_status_v1_run_get_params.GenerationRetrieveStatusV1RunGetParams,
                ),
            ),
            cast_to=GenerationRetrieveStatusV1RunGetResponse,
        )


class GenerationsResourceWithRawResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.list_v1_get = to_raw_response_wrapper(
            generations.list_v1_get,
        )
        self.retrieve_status_v1_run_get = to_raw_response_wrapper(
            generations.retrieve_status_v1_run_get,
        )


class AsyncGenerationsResourceWithRawResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.list_v1_get = async_to_raw_response_wrapper(
            generations.list_v1_get,
        )
        self.retrieve_status_v1_run_get = async_to_raw_response_wrapper(
            generations.retrieve_status_v1_run_get,
        )


class GenerationsResourceWithStreamingResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.list_v1_get = to_streamed_response_wrapper(
            generations.list_v1_get,
        )
        self.retrieve_status_v1_run_get = to_streamed_response_wrapper(
            generations.retrieve_status_v1_run_get,
        )


class AsyncGenerationsResourceWithStreamingResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.list_v1_get = async_to_streamed_response_wrapper(
            generations.list_v1_get,
        )
        self.retrieve_status_v1_run_get = async_to_streamed_response_wrapper(
            generations.retrieve_status_v1_run_get,
        )
