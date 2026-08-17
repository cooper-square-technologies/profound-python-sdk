# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Optional

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
from .categories import (
    CategoriesResource,
    AsyncCategoriesResource,
    CategoriesResourceWithRawResponse,
    AsyncCategoriesResourceWithRawResponse,
    CategoriesResourceWithStreamingResponse,
    AsyncCategoriesResourceWithStreamingResponse,
)
from ...types.organization_list_response import OrganizationListResponse
from ...types.organization_regions_response import OrganizationRegionsResponse
from ...types import organization_regions_params
from ...types.organization_models_response import OrganizationModelsResponse
from ...types.organization_domains_response import OrganizationDomainsResponse, DomainWithOrganization
from ...types import organization_domains_params
from ...types.organization_list_assets_response import OrganizationListAssetsResponse, CategoryAssetWithCategory
from ...types import organization_list_assets_params
from ...types.organization_get_personas_response import OrganizationGetPersonasResponse, OrganizationPersonasWithCategory
from ...types import organization_get_personas_params

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):

    @cached_property
    def categories(self) -> CategoriesResource:
        return CategoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
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
        """
        Return every organization the caller's API key grants access to. Use this to discover organization IDs before calling endpoints that accept an `organization_id` filter.
        
        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationListResponse: Successful Response
        
        Example:
            ```python
            organization = client.organizations.list()
            ```
        """
        return self._get(
            "/v1/org",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationListResponse,
        )

    def regions(
        self,
        *,
        organization_ids: Optional[Iterable[str]] | Omit = omit,
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
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationRegionsResponse: Successful Response
        
        Example:
            ```python
            organization = client.organizations.regions()
            ```
        """
        return self._get(
            "/v1/org/regions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"organization_ids": organization_ids}, organization_regions_params.OrganizationRegionsParams)),
            cast_to=OrganizationRegionsResponse,
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
        """
        Get the organization models.
        
        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationModelsResponse: Successful Response
        
        Example:
            ```python
            organization = client.organizations.models()
            ```
        """
        return self._get(
            "/v1/org/models",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationModelsResponse,
        )

    def domains(
        self,
        *,
        organization_ids: Optional[Iterable[str]] | Omit = omit,
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
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationDomainsResponse: Successful Response
        
        Example:
            ```python
            organization = client.organizations.domains()
            ```
        """
        return self._get(
            "/v1/org/domains",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"organization_ids": organization_ids}, organization_domains_params.OrganizationDomainsParams)),
            cast_to=OrganizationDomainsResponse,
        )

    def list_assets(
        self,
        *,
        organization_ids: Optional[Iterable[str]] | Omit = omit,
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
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationListAssetsResponse: Successful Response
        
        Example:
            ```python
            organization = client.organizations.list_assets()
            ```
        """
        return self._get(
            "/v1/org/assets",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"organization_ids": organization_ids}, organization_list_assets_params.OrganizationListAssetsParams)),
            cast_to=OrganizationListAssetsResponse,
        )

    def get_personas(
        self,
        *,
        organization_ids: Optional[Iterable[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationGetPersonasResponse:
        """
        Get the organization personas, one row per (persona, organization) pair.
        
        Same (item, org) fan-out as ``get_assets``: a persona's category can be
        owned by multiple orgs, and each owning org gets its own row so no
        association is silently dropped.
        
        Args:
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationGetPersonasResponse: Successful Response
        
        Example:
            ```python
            organization = client.organizations.get_personas()
            ```
        """
        return self._get(
            "/v1/org/personas",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"organization_ids": organization_ids}, organization_get_personas_params.OrganizationGetPersonasParams)),
            cast_to=OrganizationGetPersonasResponse,
        )


class AsyncOrganizationsResource(AsyncAPIResource):

    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        return AsyncCategoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
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
        """
        Return every organization the caller's API key grants access to. Use this to discover organization IDs before calling endpoints that accept an `organization_id` filter.
        
        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationListResponse: Successful Response
        
        Example:
            ```python
            organization = await client.organizations.list()
            ```
        """
        return await self._get(
            "/v1/org",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationListResponse,
        )

    async def regions(
        self,
        *,
        organization_ids: Optional[Iterable[str]] | Omit = omit,
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
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationRegionsResponse: Successful Response
        
        Example:
            ```python
            organization = await client.organizations.regions()
            ```
        """
        return await self._get(
            "/v1/org/regions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"organization_ids": organization_ids}, organization_regions_params.OrganizationRegionsParams)),
            cast_to=OrganizationRegionsResponse,
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
        """
        Get the organization models.
        
        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationModelsResponse: Successful Response
        
        Example:
            ```python
            organization = await client.organizations.models()
            ```
        """
        return await self._get(
            "/v1/org/models",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationModelsResponse,
        )

    async def domains(
        self,
        *,
        organization_ids: Optional[Iterable[str]] | Omit = omit,
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
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationDomainsResponse: Successful Response
        
        Example:
            ```python
            organization = await client.organizations.domains()
            ```
        """
        return await self._get(
            "/v1/org/domains",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"organization_ids": organization_ids}, organization_domains_params.OrganizationDomainsParams)),
            cast_to=OrganizationDomainsResponse,
        )

    async def list_assets(
        self,
        *,
        organization_ids: Optional[Iterable[str]] | Omit = omit,
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
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationListAssetsResponse: Successful Response
        
        Example:
            ```python
            organization = await client.organizations.list_assets()
            ```
        """
        return await self._get(
            "/v1/org/assets",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"organization_ids": organization_ids}, organization_list_assets_params.OrganizationListAssetsParams)),
            cast_to=OrganizationListAssetsResponse,
        )

    async def get_personas(
        self,
        *,
        organization_ids: Optional[Iterable[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationGetPersonasResponse:
        """
        Get the organization personas, one row per (persona, organization) pair.
        
        Same (item, org) fan-out as ``get_assets``: a persona's category can be
        owned by multiple orgs, and each owning org gets its own row so no
        association is silently dropped.
        
        Args:
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationGetPersonasResponse: Successful Response
        
        Example:
            ```python
            organization = await client.organizations.get_personas()
            ```
        """
        return await self._get(
            "/v1/org/personas",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"organization_ids": organization_ids}, organization_get_personas_params.OrganizationGetPersonasParams)),
            cast_to=OrganizationGetPersonasResponse,
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.list = to_raw_response_wrapper(
            organizations.list,
        )
        self.regions = to_raw_response_wrapper(
            organizations.regions,
        )
        self.models = to_raw_response_wrapper(
            organizations.models,
        )
        self.domains = to_raw_response_wrapper(
            organizations.domains,
        )
        self.list_assets = to_raw_response_wrapper(
            organizations.list_assets,
        )
        self.get_personas = to_raw_response_wrapper(
            organizations.get_personas,
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
        self.regions = async_to_raw_response_wrapper(
            organizations.regions,
        )
        self.models = async_to_raw_response_wrapper(
            organizations.models,
        )
        self.domains = async_to_raw_response_wrapper(
            organizations.domains,
        )
        self.list_assets = async_to_raw_response_wrapper(
            organizations.list_assets,
        )
        self.get_personas = async_to_raw_response_wrapper(
            organizations.get_personas,
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
        self.regions = to_streamed_response_wrapper(
            organizations.regions,
        )
        self.models = to_streamed_response_wrapper(
            organizations.models,
        )
        self.domains = to_streamed_response_wrapper(
            organizations.domains,
        )
        self.list_assets = to_streamed_response_wrapper(
            organizations.list_assets,
        )
        self.get_personas = to_streamed_response_wrapper(
            organizations.get_personas,
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
        self.regions = async_to_streamed_response_wrapper(
            organizations.regions,
        )
        self.models = async_to_streamed_response_wrapper(
            organizations.models,
        )
        self.domains = async_to_streamed_response_wrapper(
            organizations.domains,
        )
        self.list_assets = async_to_streamed_response_wrapper(
            organizations.list_assets,
        )
        self.get_personas = async_to_streamed_response_wrapper(
            organizations.get_personas,
        )

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self._organizations.categories)
