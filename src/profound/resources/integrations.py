# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
from typing_extensions import Literal

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
from ..types.integration_list_v1_get_response import IntegrationListV1GetResponse
from ..types import integration_list_v1_get_params

__all__ = ["IntegrationsResource", "AsyncIntegrationsResource"]


class IntegrationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntegrationsResourceWithRawResponse:
        return IntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsResourceWithStreamingResponse:
        return IntegrationsResourceWithStreamingResponse(self)

    def list_v1_get(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        provider: Optional[str] | Omit = omit,
        status_filter: Optional[Literal["active", "pending", "needs_reauth", "revoking", "revoked"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListV1GetResponse:
        """
        List the organization's connected integrations.

        Returns every connected integration by default, each with its lifecycle
        `status`; pass `status_filter` to narrow to one status (e.g. `needs_reauth`).
        Each row's `integration_id` is the value a hub-backed node needs bound to it.

        Args:
            organization_id: Organization scope for API keys that can access multiple organizations.
            provider: Filter to a single connector/provider id, e.g. `google_drive`.
            status_filter: Filter to one lifecycle status. Omitted returns all statuses.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationListV1GetResponse: Successful Response

        Example:
            ```python
            integration = client.integrations.list_v1_get()
            ```
        """
        return self._get(
            "/v1/integrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id, "provider": provider, "status_filter": status_filter},
                    integration_list_v1_get_params.IntegrationListV1GetParams,
                ),
            ),
            cast_to=IntegrationListV1GetResponse,
        )


class AsyncIntegrationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsResourceWithRawResponse:
        return AsyncIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        return AsyncIntegrationsResourceWithStreamingResponse(self)

    async def list_v1_get(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        provider: Optional[str] | Omit = omit,
        status_filter: Optional[Literal["active", "pending", "needs_reauth", "revoking", "revoked"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListV1GetResponse:
        """
        List the organization's connected integrations.

        Returns every connected integration by default, each with its lifecycle
        `status`; pass `status_filter` to narrow to one status (e.g. `needs_reauth`).
        Each row's `integration_id` is the value a hub-backed node needs bound to it.

        Args:
            organization_id: Organization scope for API keys that can access multiple organizations.
            provider: Filter to a single connector/provider id, e.g. `google_drive`.
            status_filter: Filter to one lifecycle status. Omitted returns all statuses.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            IntegrationListV1GetResponse: Successful Response

        Example:
            ```python
            integration = await client.integrations.list_v1_get()
            ```
        """
        return await self._get(
            "/v1/integrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id, "provider": provider, "status_filter": status_filter},
                    integration_list_v1_get_params.IntegrationListV1GetParams,
                ),
            ),
            cast_to=IntegrationListV1GetResponse,
        )


class IntegrationsResourceWithRawResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.list_v1_get = to_raw_response_wrapper(
            integrations.list_v1_get,
        )


class AsyncIntegrationsResourceWithRawResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.list_v1_get = async_to_raw_response_wrapper(
            integrations.list_v1_get,
        )


class IntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.list_v1_get = to_streamed_response_wrapper(
            integrations.list_v1_get,
        )


class AsyncIntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.list_v1_get = async_to_streamed_response_wrapper(
            integrations.list_v1_get,
        )
