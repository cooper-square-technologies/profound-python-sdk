# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.organization_list_category_regions_v1_org_categories_category_regions_get_response import OrganizationListCategoryRegionsV1OrgCategoriesCategoryRegionsGetResponse

__all__ = ["OrganizationResource", "AsyncOrganizationResource"]


class OrganizationResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> OrganizationResourceWithRawResponse:
        return OrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationResourceWithStreamingResponse:
        return OrganizationResourceWithStreamingResponse(self)

    def list_category_regions_v1_org_categories_category_regions_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryRegionsV1OrgCategoriesCategoryRegionsGetResponse:
        """
        Get the regions for a specific category.
        
        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationListCategoryRegionsV1OrgCategoriesCategoryRegionsGetResponse: Successful Response
        
        Example:
            ```python
            organization = client.organization.list_category_regions_v1_org_categories_category_regions_get(
                category_id="categoryId",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/regions", **{"category_id": category_id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationListCategoryRegionsV1OrgCategoriesCategoryRegionsGetResponse,
        )


class AsyncOrganizationResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationResourceWithRawResponse:
        return AsyncOrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationResourceWithStreamingResponse:
        return AsyncOrganizationResourceWithStreamingResponse(self)

    async def list_category_regions_v1_org_categories_category_regions_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryRegionsV1OrgCategoriesCategoryRegionsGetResponse:
        """
        Get the regions for a specific category.
        
        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            OrganizationListCategoryRegionsV1OrgCategoriesCategoryRegionsGetResponse: Successful Response
        
        Example:
            ```python
            organization = await client.organization.list_category_regions_v1_org_categories_category_regions_get(
                category_id="categoryId",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/regions", **{"category_id": category_id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationListCategoryRegionsV1OrgCategoriesCategoryRegionsGetResponse,
        )


class OrganizationResourceWithRawResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

        self.list_category_regions_v1_org_categories_category_regions_get = to_raw_response_wrapper(
            organization.list_category_regions_v1_org_categories_category_regions_get,
        )


class AsyncOrganizationResourceWithRawResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

        self.list_category_regions_v1_org_categories_category_regions_get = async_to_raw_response_wrapper(
            organization.list_category_regions_v1_org_categories_category_regions_get,
        )


class OrganizationResourceWithStreamingResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

        self.list_category_regions_v1_org_categories_category_regions_get = to_streamed_response_wrapper(
            organization.list_category_regions_v1_org_categories_category_regions_get,
        )


class AsyncOrganizationResourceWithStreamingResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

        self.list_category_regions_v1_org_categories_category_regions_get = async_to_streamed_response_wrapper(
            organization.list_category_regions_v1_org_categories_category_regions_get,
        )
