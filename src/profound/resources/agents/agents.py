# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional
from typing_extensions import Literal

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
from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ...types.agent_list_response import AgentListResponse
from ...types import agent_list_params, agent_retrieve_params
from ...types.agent_retrieve_response import AgentRetrieveResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        return AgentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        statuses: Optional[List[Literal["published", "draft"]]] | Omit = omit,
        limit: int | Omit = omit,
        next_cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        List agents available to your organization.

        Agent status reflects whether an agent has ever been published. `published`
        agents have a live published version. `draft` agents have not been
        published yet.

        Args:
            statuses: Optional status filter. Use `published` to list agents that have a live published version, or `draft` to list agents that have not been published yet. Defaults to `published`.
            limit: Query parameter.
            next_cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentListResponse: Successful Response

        Example:
            ```python
            agent = client.agents.list(
                limit=100,
            )
            ```
        """
        return self._get(
            "/v1/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"statuses": statuses, "limit": limit, "next_cursor": next_cursor},
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    def retrieve(
        self,
        agent_id: str,
        *,
        version: Literal["published", "draft"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveResponse:
        """
        Retrieve an agent and its schema details.

        Agents can have both a live published version and a draft version with newer
        unpublished changes. Use the `version` parameter to choose which state to return.

        Args:
            agent_id: The ID of the agent to retrieve.
            version: Version of the agent to retrieve. Use `published` for the live version, or `draft` for the latest unpublished changes for the same agent. Defaults to `published`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentRetrieveResponse: Successful Response

        Example:
            ```python
            agent = client.agents.retrieve(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/v1/agents/{agent_id}", **{"agent_id": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"version": version}, agent_retrieve_params.AgentRetrieveParams),
            ),
            cast_to=AgentRetrieveResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        statuses: Optional[List[Literal["published", "draft"]]] | Omit = omit,
        limit: int | Omit = omit,
        next_cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        List agents available to your organization.

        Agent status reflects whether an agent has ever been published. `published`
        agents have a live published version. `draft` agents have not been
        published yet.

        Args:
            statuses: Optional status filter. Use `published` to list agents that have a live published version, or `draft` to list agents that have not been published yet. Defaults to `published`.
            limit: Query parameter.
            next_cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentListResponse: Successful Response

        Example:
            ```python
            agent = await client.agents.list(
                limit=100,
            )
            ```
        """
        return await self._get(
            "/v1/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"statuses": statuses, "limit": limit, "next_cursor": next_cursor},
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    async def retrieve(
        self,
        agent_id: str,
        *,
        version: Literal["published", "draft"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveResponse:
        """
        Retrieve an agent and its schema details.

        Agents can have both a live published version and a draft version with newer
        unpublished changes. Use the `version` parameter to choose which state to return.

        Args:
            agent_id: The ID of the agent to retrieve.
            version: Version of the agent to retrieve. Use `published` for the live version, or `draft` for the latest unpublished changes for the same agent. Defaults to `published`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentRetrieveResponse: Successful Response

        Example:
            ```python
            agent = await client.agents.retrieve(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/v1/agents/{agent_id}", **{"agent_id": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"version": version}, agent_retrieve_params.AgentRetrieveParams),
            ),
            cast_to=AgentRetrieveResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._agents.runs)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._agents.runs)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._agents.runs)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._agents.runs)
