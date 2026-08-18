# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict

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
from ...types.agents.run_v1_id_post_response import RunV1IDPostResponse
from ...types.agents import run_v1_id_post_params, run_retrieve_v1_get_params
from ...types.agents.run_retrieve_v1_get_response import RunRetrieveV1GetResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self)

    def v1_id_post(
        self,
        agent_id: str,
        *,
        inputs: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunV1IDPostResponse:
        """
        Start a new run for an agent.

        Runs always execute the agent's live published version, so the agent must be
        published first with `POST /v1/agents/{agent_id}/publish`. Unpublished drafts
        cannot be run.

        Args:
            agent_id: The ID of the agent to run.
            inputs: Input values for the run. Keys should match the property names defined in `schema.input`. Omit the request body when the agent does not require inputs.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RunV1IDPostResponse: Successful Response

        Example:
            ```python
            run = client.agents.runs.v1_id_post(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            path_template("/v1/agents/{agent_id}/runs", **{"agent_id": agent_id}),
            body=maybe_transform(
                {"inputs": inputs},
                run_v1_id_post_params.RunV1IDPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunV1IDPostResponse,
        )

    def retrieve_v1_get(
        self,
        run_id: str,
        *,
        agent_id: str,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunRetrieveV1GetResponse:
        """
        Retrieve the current status and result details for an agent run.

        Args:
            run_id: The ID of the run to retrieve.
            agent_id: The ID of the agent that owns the run.
            verbose: Include each step's raw `outputs` payload in the execution trace.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RunRetrieveV1GetResponse: Successful Response

        Example:
            ```python
            run = client.agents.runs.retrieve_v1_get(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                verbose=False,
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if run_id is None or (isinstance(run_id, str) and not run_id):
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/v1/agents/{agent_id}/runs/{run_id}", **{"agent_id": agent_id, "run_id": run_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"verbose": verbose}, run_retrieve_v1_get_params.RunRetrieveV1GetParams),
            ),
            cast_to=RunRetrieveV1GetResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self)

    async def v1_id_post(
        self,
        agent_id: str,
        *,
        inputs: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunV1IDPostResponse:
        """
        Start a new run for an agent.

        Runs always execute the agent's live published version, so the agent must be
        published first with `POST /v1/agents/{agent_id}/publish`. Unpublished drafts
        cannot be run.

        Args:
            agent_id: The ID of the agent to run.
            inputs: Input values for the run. Keys should match the property names defined in `schema.input`. Omit the request body when the agent does not require inputs.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RunV1IDPostResponse: Successful Response

        Example:
            ```python
            run = await client.agents.runs.v1_id_post(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            path_template("/v1/agents/{agent_id}/runs", **{"agent_id": agent_id}),
            body=await async_maybe_transform(
                {"inputs": inputs},
                run_v1_id_post_params.RunV1IDPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunV1IDPostResponse,
        )

    async def retrieve_v1_get(
        self,
        run_id: str,
        *,
        agent_id: str,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunRetrieveV1GetResponse:
        """
        Retrieve the current status and result details for an agent run.

        Args:
            run_id: The ID of the run to retrieve.
            agent_id: The ID of the agent that owns the run.
            verbose: Include each step's raw `outputs` payload in the execution trace.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RunRetrieveV1GetResponse: Successful Response

        Example:
            ```python
            run = await client.agents.runs.retrieve_v1_get(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                verbose=False,
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if run_id is None or (isinstance(run_id, str) and not run_id):
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/v1/agents/{agent_id}/runs/{run_id}", **{"agent_id": agent_id, "run_id": run_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"verbose": verbose}, run_retrieve_v1_get_params.RunRetrieveV1GetParams
                ),
            ),
            cast_to=RunRetrieveV1GetResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.v1_id_post = to_raw_response_wrapper(
            runs.v1_id_post,
        )
        self.retrieve_v1_get = to_raw_response_wrapper(
            runs.retrieve_v1_get,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.v1_id_post = async_to_raw_response_wrapper(
            runs.v1_id_post,
        )
        self.retrieve_v1_get = async_to_raw_response_wrapper(
            runs.retrieve_v1_get,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.v1_id_post = to_streamed_response_wrapper(
            runs.v1_id_post,
        )
        self.retrieve_v1_get = to_streamed_response_wrapper(
            runs.retrieve_v1_get,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.v1_id_post = async_to_streamed_response_wrapper(
            runs.v1_id_post,
        )
        self.retrieve_v1_get = async_to_streamed_response_wrapper(
            runs.retrieve_v1_get,
        )
