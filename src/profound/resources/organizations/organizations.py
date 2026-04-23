# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import (
    organization_domains_params,
    organization_regions_params,
    organization_list_assets_params,
    organization_get_personas_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .categories import (
    CategoriesResource,
    AsyncCategoriesResource,
    CategoriesResourceWithRawResponse,
    AsyncCategoriesResourceWithRawResponse,
    CategoriesResourceWithStreamingResponse,
    AsyncCategoriesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.organization_list_response import OrganizationListResponse
from ...types.organization_models_response import OrganizationModelsResponse
from ...types.organization_domains_response import OrganizationDomainsResponse
from ...types.organization_regions_response import OrganizationRegionsResponse
from ...types.organization_list_assets_response import OrganizationListAssetsResponse
from ...types.organization_get_personas_response import OrganizationGetPersonasResponse

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def categories(self) -> CategoriesResource:
        return CategoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListResponse:
        """Return every organization the caller's API key grants access to.

        Use this to
        discover organization IDs before calling endpoints that accept an
        `organization_id` filter.
        """
        return self._get(
            "/v1/org",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListResponse,
        )

    def domains(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationDomainsResponse:
        """
        Get the organization domains.

        Args:
          organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the
              parameter to target multiple orgs (e.g.
              `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from
              every organization the caller has access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/org/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_ids": organization_ids}, organization_domains_params.OrganizationDomainsParams
                ),
            ),
            cast_to=OrganizationDomainsResponse,
        )

    def get_personas(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationGetPersonasResponse:
        """
        Get the organization personas, one row per (persona, organization) pair.

        Same (item, org) fan-out as `get_assets`: a persona's category can be owned by
        multiple orgs, and each owning org gets its own row so no association is
        silently dropped.

        Args:
          organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the
              parameter to target multiple orgs (e.g.
              `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from
              every organization the caller has access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/org/personas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_ids": organization_ids},
                    organization_get_personas_params.OrganizationGetPersonasParams,
                ),
            ),
            cast_to=OrganizationGetPersonasResponse,
        )

    def list_assets(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListAssetsResponse:
        """
        Get the organization assets, one row per (asset, organization) pair.

        An asset's category can belong to multiple organizations; one asset row is
        emitted per owning org so no association is silently dropped.

        Args:
          organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the
              parameter to target multiple orgs (e.g.
              `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from
              every organization the caller has access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/org/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_ids": organization_ids}, organization_list_assets_params.OrganizationListAssetsParams
                ),
            ),
            cast_to=OrganizationListAssetsResponse,
        )

    def models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationModelsResponse:
        """Get the organization models."""
        return self._get(
            "/v1/org/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationModelsResponse,
        )

    def regions(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationRegionsResponse:
        """
        Get the organization regions.

        Args:
          organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the
              parameter to target multiple orgs (e.g.
              `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from
              every organization the caller has access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/org/regions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_ids": organization_ids}, organization_regions_params.OrganizationRegionsParams
                ),
            ),
            cast_to=OrganizationRegionsResponse,
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        return AsyncCategoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListResponse:
        """Return every organization the caller's API key grants access to.

        Use this to
        discover organization IDs before calling endpoints that accept an
        `organization_id` filter.
        """
        return await self._get(
            "/v1/org",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListResponse,
        )

    async def domains(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationDomainsResponse:
        """
        Get the organization domains.

        Args:
          organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the
              parameter to target multiple orgs (e.g.
              `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from
              every organization the caller has access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/org/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_ids": organization_ids}, organization_domains_params.OrganizationDomainsParams
                ),
            ),
            cast_to=OrganizationDomainsResponse,
        )

    async def get_personas(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationGetPersonasResponse:
        """
        Get the organization personas, one row per (persona, organization) pair.

        Same (item, org) fan-out as `get_assets`: a persona's category can be owned by
        multiple orgs, and each owning org gets its own row so no association is
        silently dropped.

        Args:
          organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the
              parameter to target multiple orgs (e.g.
              `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from
              every organization the caller has access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/org/personas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_ids": organization_ids},
                    organization_get_personas_params.OrganizationGetPersonasParams,
                ),
            ),
            cast_to=OrganizationGetPersonasResponse,
        )

    async def list_assets(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListAssetsResponse:
        """
        Get the organization assets, one row per (asset, organization) pair.

        An asset's category can belong to multiple organizations; one asset row is
        emitted per owning org so no association is silently dropped.

        Args:
          organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the
              parameter to target multiple orgs (e.g.
              `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from
              every organization the caller has access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/org/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_ids": organization_ids}, organization_list_assets_params.OrganizationListAssetsParams
                ),
            ),
            cast_to=OrganizationListAssetsResponse,
        )

    async def models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationModelsResponse:
        """Get the organization models."""
        return await self._get(
            "/v1/org/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationModelsResponse,
        )

    async def regions(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationRegionsResponse:
        """
        Get the organization regions.

        Args:
          organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the
              parameter to target multiple orgs (e.g.
              `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from
              every organization the caller has access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/org/regions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_ids": organization_ids}, organization_regions_params.OrganizationRegionsParams
                ),
            ),
            cast_to=OrganizationRegionsResponse,
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.list = to_raw_response_wrapper(
            organizations.list,
        )
        self.domains = to_raw_response_wrapper(
            organizations.domains,
        )
        self.get_personas = to_raw_response_wrapper(
            organizations.get_personas,
        )
        self.list_assets = to_raw_response_wrapper(
            organizations.list_assets,
        )
        self.models = to_raw_response_wrapper(
            organizations.models,
        )
        self.regions = to_raw_response_wrapper(
            organizations.regions,
        )

    @cached_property
    def categories(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self._organizations.categories)


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.list = async_to_raw_response_wrapper(
            organizations.list,
        )
        self.domains = async_to_raw_response_wrapper(
            organizations.domains,
        )
        self.get_personas = async_to_raw_response_wrapper(
            organizations.get_personas,
        )
        self.list_assets = async_to_raw_response_wrapper(
            organizations.list_assets,
        )
        self.models = async_to_raw_response_wrapper(
            organizations.models,
        )
        self.regions = async_to_raw_response_wrapper(
            organizations.regions,
        )

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self._organizations.categories)


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.list = to_streamed_response_wrapper(
            organizations.list,
        )
        self.domains = to_streamed_response_wrapper(
            organizations.domains,
        )
        self.get_personas = to_streamed_response_wrapper(
            organizations.get_personas,
        )
        self.list_assets = to_streamed_response_wrapper(
            organizations.list_assets,
        )
        self.models = to_streamed_response_wrapper(
            organizations.models,
        )
        self.regions = to_streamed_response_wrapper(
            organizations.regions,
        )

    @cached_property
    def categories(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self._organizations.categories)


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.list = async_to_streamed_response_wrapper(
            organizations.list,
        )
        self.domains = async_to_streamed_response_wrapper(
            organizations.domains,
        )
        self.get_personas = async_to_streamed_response_wrapper(
            organizations.get_personas,
        )
        self.list_assets = async_to_streamed_response_wrapper(
            organizations.list_assets,
        )
        self.models = async_to_streamed_response_wrapper(
            organizations.models,
        )
        self.regions = async_to_streamed_response_wrapper(
            organizations.regions,
        )

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self._organizations.categories)
