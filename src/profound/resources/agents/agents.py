# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, List, Optional
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
from .node_types import (
    NodeTypesResource,
    AsyncNodeTypesResource,
    NodeTypesResourceWithRawResponse,
    AsyncNodeTypesResourceWithRawResponse,
    NodeTypesResourceWithStreamingResponse,
    AsyncNodeTypesResourceWithStreamingResponse,
)
from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ...types.agent_list_v1_get_response import AgentListV1GetResponse
from ...types import (
    agent_list_v1_get_params,
    agent_create_v1_post_params,
    agent_retrieve_v1_get_params,
    agent_update_v1_id_patch_params,
    agent_list_graph_v1_graph_get_params,
)
from ...types.shared.agent import Agent
from ...types.agent_retrieve_v1_get_response import AgentRetrieveV1GetResponse
from ...types.shared.agent_version import AgentVersion
from ...types.agent_update_v1_id_patch_response import AgentUpdateV1IDPatchResponse
from ...types.agent_list_graph_v1_graph_get_response import AgentListGraphV1GraphGetResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def node_types(self) -> NodeTypesResource:
        return NodeTypesResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        return AgentsResourceWithStreamingResponse(self)

    def list_v1_get(
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
    ) -> AgentListV1GetResponse:
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
            AgentListV1GetResponse: Successful Response

        Example:
            ```python
            agent = client.agents.list_v1_get(
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
                    agent_list_v1_get_params.AgentListV1GetParams,
                ),
            ),
            cast_to=AgentListV1GetResponse,
        )

    def create_v1_post(
        self,
        *,
        organization_id: str,
        name: str,
        description: Optional[str] | Omit = omit,
        graph: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Create a new draft agent owned by the given organization.

        `organization_id` is required and you must be a member of it. The agent is created
        as a `draft`; publish it with `POST /v1/agents/{agent_id}/publish` once its graph
        is ready.

        Args:
            organization_id: ID of the organization that will own the agent. Required — Profound API keys are user-scoped, so the owning organization must be chosen explicitly. The caller must be a member of this organization.
            name: Display name for the agent. Must be non-empty.
            description: Short description of the agent.
            graph: Initial workflow graph for the agent's draft version. Optional — an agent can be created empty and have its graph filled in later.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Agent: Successful Response

        Example:
            ```python
            agent = client.agents.create_v1_post(
                organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
            )
            ```
        """
        return self._post(
            "/v1/agents",
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "name": name,
                    "description": description,
                    "graph": graph,
                },
                agent_create_v1_post_params.AgentCreateV1PostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def publish_v1_id_publish_post(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Publish an agent's latest draft as its live published version.

        You must be a member of the agent's organization. Publishing promotes the current
        draft graph to a new published version. A draft that cannot produce its declared
        input/output contract is rejected with `422` and is not published.

        Args:
            agent_id: The ID of the agent to publish.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Agent: Successful Response

        Example:
            ```python
            agent = client.agents.publish_v1_id_publish_post(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            path_template("/v1/agents/{agent_id}/publish", **{"agent_id": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def retrieve_v1_get(
        self,
        agent_id: str,
        *,
        version: AgentVersion | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveV1GetResponse:
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
            AgentRetrieveV1GetResponse: Successful Response

        Example:
            ```python
            agent = client.agents.retrieve_v1_get(
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
                query=maybe_transform({"version": version}, agent_retrieve_v1_get_params.AgentRetrieveV1GetParams),
            ),
            cast_to=AgentRetrieveV1GetResponse,
        )

    def update_v1_id_patch(
        self,
        agent_id: str,
        *,
        graph: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdateV1IDPatchResponse:
        """
        Update an agent's draft graph in place.

        You must be a member of the agent's organization. The agent's draft is replaced with the
        supplied graph and re-validated, so you can iterate one draft — create, then update per
        fix — instead of creating a new agent on every change. The response carries the updated
        `validation`; publish with `POST /v1/agents/{agent_id}/publish` once `validation.valid`.

        Args:
            agent_id: The ID of the agent to update.
            graph: New workflow graph for the agent's draft version. Replaces the current draft graph; the agent is iterated in place rather than re-created, so its ID is stable. Required — a null graph is rejected as a 422 here rather than as a relayed upstream error.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentUpdateV1IDPatchResponse: Successful Response

        Example:
            ```python
            agent = client.agents.update_v1_id_patch(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                graph={},
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            path_template("/v1/agents/{agent_id}", **{"agent_id": agent_id}),
            body=maybe_transform(
                {"graph": graph},
                agent_update_v1_id_patch_params.AgentUpdateV1IDPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateV1IDPatchResponse,
        )

    def list_graph_v1_graph_get(
        self,
        agent_id: str,
        *,
        version: AgentVersion | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListGraphV1GraphGetResponse:
        """
        Retrieve an agent's full workflow graph (`{nodes, edges}`).

        The graph is returned verbatim in the canonical dialect — the same shape `POST /v1/agents`
        and `PATCH /v1/agents/{agent_id}` accept — so a known-good agent can be read back, copied,
        and edited. Tool-backed nodes appear in their lowered `tool` form rather than the friendly
        v1 node types. A `draft` is visible only to its creator; the `published` version is visible
        across its organization.

        Args:
            agent_id: The ID of the agent whose graph to retrieve.
            version: Version of the agent whose graph to retrieve. Use `published` for the live version, or `draft` for the latest unpublished changes. Defaults to `published`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentListGraphV1GraphGetResponse: Successful Response

        Example:
            ```python
            agent = client.agents.list_graph_v1_graph_get(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            path_template("/v1/agents/{agent_id}/graph", **{"agent_id": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"version": version}, agent_list_graph_v1_graph_get_params.AgentListGraphV1GraphGetParams
                ),
            ),
            cast_to=AgentListGraphV1GraphGetResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def node_types(self) -> AsyncNodeTypesResource:
        return AsyncNodeTypesResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def list_v1_get(
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
    ) -> AgentListV1GetResponse:
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
            AgentListV1GetResponse: Successful Response

        Example:
            ```python
            agent = await client.agents.list_v1_get(
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
                    agent_list_v1_get_params.AgentListV1GetParams,
                ),
            ),
            cast_to=AgentListV1GetResponse,
        )

    async def create_v1_post(
        self,
        *,
        organization_id: str,
        name: str,
        description: Optional[str] | Omit = omit,
        graph: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Create a new draft agent owned by the given organization.

        `organization_id` is required and you must be a member of it. The agent is created
        as a `draft`; publish it with `POST /v1/agents/{agent_id}/publish` once its graph
        is ready.

        Args:
            organization_id: ID of the organization that will own the agent. Required — Profound API keys are user-scoped, so the owning organization must be chosen explicitly. The caller must be a member of this organization.
            name: Display name for the agent. Must be non-empty.
            description: Short description of the agent.
            graph: Initial workflow graph for the agent's draft version. Optional — an agent can be created empty and have its graph filled in later.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Agent: Successful Response

        Example:
            ```python
            agent = await client.agents.create_v1_post(
                organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
            )
            ```
        """
        return await self._post(
            "/v1/agents",
            body=await async_maybe_transform(
                {
                    "organization_id": organization_id,
                    "name": name,
                    "description": description,
                    "graph": graph,
                },
                agent_create_v1_post_params.AgentCreateV1PostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def publish_v1_id_publish_post(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Publish an agent's latest draft as its live published version.

        You must be a member of the agent's organization. Publishing promotes the current
        draft graph to a new published version. A draft that cannot produce its declared
        input/output contract is rejected with `422` and is not published.

        Args:
            agent_id: The ID of the agent to publish.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Agent: Successful Response

        Example:
            ```python
            agent = await client.agents.publish_v1_id_publish_post(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            path_template("/v1/agents/{agent_id}/publish", **{"agent_id": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def retrieve_v1_get(
        self,
        agent_id: str,
        *,
        version: AgentVersion | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveV1GetResponse:
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
            AgentRetrieveV1GetResponse: Successful Response

        Example:
            ```python
            agent = await client.agents.retrieve_v1_get(
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
                query=await async_maybe_transform(
                    {"version": version}, agent_retrieve_v1_get_params.AgentRetrieveV1GetParams
                ),
            ),
            cast_to=AgentRetrieveV1GetResponse,
        )

    async def update_v1_id_patch(
        self,
        agent_id: str,
        *,
        graph: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdateV1IDPatchResponse:
        """
        Update an agent's draft graph in place.

        You must be a member of the agent's organization. The agent's draft is replaced with the
        supplied graph and re-validated, so you can iterate one draft — create, then update per
        fix — instead of creating a new agent on every change. The response carries the updated
        `validation`; publish with `POST /v1/agents/{agent_id}/publish` once `validation.valid`.

        Args:
            agent_id: The ID of the agent to update.
            graph: New workflow graph for the agent's draft version. Replaces the current draft graph; the agent is iterated in place rather than re-created, so its ID is stable. Required — a null graph is rejected as a 422 here rather than as a relayed upstream error.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentUpdateV1IDPatchResponse: Successful Response

        Example:
            ```python
            agent = await client.agents.update_v1_id_patch(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                graph={},
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            path_template("/v1/agents/{agent_id}", **{"agent_id": agent_id}),
            body=await async_maybe_transform(
                {"graph": graph},
                agent_update_v1_id_patch_params.AgentUpdateV1IDPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdateV1IDPatchResponse,
        )

    async def list_graph_v1_graph_get(
        self,
        agent_id: str,
        *,
        version: AgentVersion | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListGraphV1GraphGetResponse:
        """
        Retrieve an agent's full workflow graph (`{nodes, edges}`).

        The graph is returned verbatim in the canonical dialect — the same shape `POST /v1/agents`
        and `PATCH /v1/agents/{agent_id}` accept — so a known-good agent can be read back, copied,
        and edited. Tool-backed nodes appear in their lowered `tool` form rather than the friendly
        v1 node types. A `draft` is visible only to its creator; the `published` version is visible
        across its organization.

        Args:
            agent_id: The ID of the agent whose graph to retrieve.
            version: Version of the agent whose graph to retrieve. Use `published` for the live version, or `draft` for the latest unpublished changes. Defaults to `published`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AgentListGraphV1GraphGetResponse: Successful Response

        Example:
            ```python
            agent = await client.agents.list_graph_v1_graph_get(
                agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if agent_id is None or (isinstance(agent_id, str) and not agent_id):
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            path_template("/v1/agents/{agent_id}/graph", **{"agent_id": agent_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"version": version}, agent_list_graph_v1_graph_get_params.AgentListGraphV1GraphGetParams
                ),
            ),
            cast_to=AgentListGraphV1GraphGetResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.list_v1_get = to_raw_response_wrapper(
            agents.list_v1_get,
        )
        self.create_v1_post = to_raw_response_wrapper(
            agents.create_v1_post,
        )
        self.publish_v1_id_publish_post = to_raw_response_wrapper(
            agents.publish_v1_id_publish_post,
        )
        self.retrieve_v1_get = to_raw_response_wrapper(
            agents.retrieve_v1_get,
        )
        self.update_v1_id_patch = to_raw_response_wrapper(
            agents.update_v1_id_patch,
        )
        self.list_graph_v1_graph_get = to_raw_response_wrapper(
            agents.list_graph_v1_graph_get,
        )

    @cached_property
    def node_types(self) -> NodeTypesResourceWithRawResponse:
        return NodeTypesResourceWithRawResponse(self._agents.node_types)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._agents.runs)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.list_v1_get = async_to_raw_response_wrapper(
            agents.list_v1_get,
        )
        self.create_v1_post = async_to_raw_response_wrapper(
            agents.create_v1_post,
        )
        self.publish_v1_id_publish_post = async_to_raw_response_wrapper(
            agents.publish_v1_id_publish_post,
        )
        self.retrieve_v1_get = async_to_raw_response_wrapper(
            agents.retrieve_v1_get,
        )
        self.update_v1_id_patch = async_to_raw_response_wrapper(
            agents.update_v1_id_patch,
        )
        self.list_graph_v1_graph_get = async_to_raw_response_wrapper(
            agents.list_graph_v1_graph_get,
        )

    @cached_property
    def node_types(self) -> AsyncNodeTypesResourceWithRawResponse:
        return AsyncNodeTypesResourceWithRawResponse(self._agents.node_types)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._agents.runs)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.list_v1_get = to_streamed_response_wrapper(
            agents.list_v1_get,
        )
        self.create_v1_post = to_streamed_response_wrapper(
            agents.create_v1_post,
        )
        self.publish_v1_id_publish_post = to_streamed_response_wrapper(
            agents.publish_v1_id_publish_post,
        )
        self.retrieve_v1_get = to_streamed_response_wrapper(
            agents.retrieve_v1_get,
        )
        self.update_v1_id_patch = to_streamed_response_wrapper(
            agents.update_v1_id_patch,
        )
        self.list_graph_v1_graph_get = to_streamed_response_wrapper(
            agents.list_graph_v1_graph_get,
        )

    @cached_property
    def node_types(self) -> NodeTypesResourceWithStreamingResponse:
        return NodeTypesResourceWithStreamingResponse(self._agents.node_types)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._agents.runs)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.list_v1_get = async_to_streamed_response_wrapper(
            agents.list_v1_get,
        )
        self.create_v1_post = async_to_streamed_response_wrapper(
            agents.create_v1_post,
        )
        self.publish_v1_id_publish_post = async_to_streamed_response_wrapper(
            agents.publish_v1_id_publish_post,
        )
        self.retrieve_v1_get = async_to_streamed_response_wrapper(
            agents.retrieve_v1_get,
        )
        self.update_v1_id_patch = async_to_streamed_response_wrapper(
            agents.update_v1_id_patch,
        )
        self.list_graph_v1_graph_get = async_to_streamed_response_wrapper(
            agents.list_graph_v1_graph_get,
        )

    @cached_property
    def node_types(self) -> AsyncNodeTypesResourceWithStreamingResponse:
        return AsyncNodeTypesResourceWithStreamingResponse(self._agents.node_types)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._agents.runs)
