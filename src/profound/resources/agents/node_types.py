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
from ...types.agents.node_type_list_response import NodeTypeListResponse
from ...types.agents.node_type_retrieve_schema_response import NodeTypeRetrieveSchemaResponse

__all__ = ["NodeTypesResource", "AsyncNodeTypesResource"]


class NodeTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NodeTypesResourceWithRawResponse:
        return NodeTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NodeTypesResourceWithStreamingResponse:
        return NodeTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NodeTypeListResponse:
        """
        List the node types available for building agents.

        The set is deterministic and does not depend on the caller, so the response
        is safe to cache across sessions. Integration-dependent and dynamic-schema
        node types are intentionally excluded in v1.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            NodeTypeListResponse: Successful Response

        Example:
            ```python
            node_type = client.agents.node_types.list()
            ```
        """
        return self._get(
            "/v1/agents/node-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeTypeListResponse,
        )

    def retrieve_schema(
        self,
        node_type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NodeTypeRetrieveSchemaResponse:
        """
        Retrieve the JSON schema for a single node type.

        The `schema` field is an opaque JSON Schema for the node's configuration.
        Use `schema_version` as a cache key — it bumps whenever the schema changes.

        Args:
            node_type: The node type to fetch the schema for, e.g. `llm`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            NodeTypeRetrieveSchemaResponse: Successful Response

        Example:
            ```python
            node_type = client.agents.node_types.retrieve_schema(
                node_type="nodeType",
            )
            ```
        """
        if node_type is None or (isinstance(node_type, str) and not node_type):
            raise ValueError(f"Expected a non-empty value for `node_type` but received {node_type!r}")
        return self._get(
            path_template("/v1/agents/node-types/{node_type}/schema", **{"node_type": node_type}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeTypeRetrieveSchemaResponse,
        )


class AsyncNodeTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNodeTypesResourceWithRawResponse:
        return AsyncNodeTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNodeTypesResourceWithStreamingResponse:
        return AsyncNodeTypesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NodeTypeListResponse:
        """
        List the node types available for building agents.

        The set is deterministic and does not depend on the caller, so the response
        is safe to cache across sessions. Integration-dependent and dynamic-schema
        node types are intentionally excluded in v1.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            NodeTypeListResponse: Successful Response

        Example:
            ```python
            node_type = await client.agents.node_types.list()
            ```
        """
        return await self._get(
            "/v1/agents/node-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeTypeListResponse,
        )

    async def retrieve_schema(
        self,
        node_type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NodeTypeRetrieveSchemaResponse:
        """
        Retrieve the JSON schema for a single node type.

        The `schema` field is an opaque JSON Schema for the node's configuration.
        Use `schema_version` as a cache key — it bumps whenever the schema changes.

        Args:
            node_type: The node type to fetch the schema for, e.g. `llm`.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            NodeTypeRetrieveSchemaResponse: Successful Response

        Example:
            ```python
            node_type = await client.agents.node_types.retrieve_schema(
                node_type="nodeType",
            )
            ```
        """
        if node_type is None or (isinstance(node_type, str) and not node_type):
            raise ValueError(f"Expected a non-empty value for `node_type` but received {node_type!r}")
        return await self._get(
            path_template("/v1/agents/node-types/{node_type}/schema", **{"node_type": node_type}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NodeTypeRetrieveSchemaResponse,
        )


class NodeTypesResourceWithRawResponse:
    def __init__(self, node_types: NodeTypesResource) -> None:
        self._node_types = node_types

        self.list = to_raw_response_wrapper(
            node_types.list,
        )
        self.retrieve_schema = to_raw_response_wrapper(
            node_types.retrieve_schema,
        )


class AsyncNodeTypesResourceWithRawResponse:
    def __init__(self, node_types: AsyncNodeTypesResource) -> None:
        self._node_types = node_types

        self.list = async_to_raw_response_wrapper(
            node_types.list,
        )
        self.retrieve_schema = async_to_raw_response_wrapper(
            node_types.retrieve_schema,
        )


class NodeTypesResourceWithStreamingResponse:
    def __init__(self, node_types: NodeTypesResource) -> None:
        self._node_types = node_types

        self.list = to_streamed_response_wrapper(
            node_types.list,
        )
        self.retrieve_schema = to_streamed_response_wrapper(
            node_types.retrieve_schema,
        )


class AsyncNodeTypesResourceWithStreamingResponse:
    def __init__(self, node_types: AsyncNodeTypesResource) -> None:
        self._node_types = node_types

        self.list = async_to_streamed_response_wrapper(
            node_types.list,
        )
        self.retrieve_schema = async_to_streamed_response_wrapper(
            node_types.retrieve_schema,
        )
