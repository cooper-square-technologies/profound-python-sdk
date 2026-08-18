# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, List, Optional
from typing_extensions import Literal
from .._types import SequenceNotStr

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
from ..types.organization_list_v1_org_get_response import OrganizationListV1OrgGetResponse
from ..types.organization_list_regions_v1_org_regions_get_response import OrganizationListRegionsV1OrgRegionsGetResponse
from ..types import (
    organization_list_regions_v1_org_regions_get_params,
    organization_list_domains_v1_org_domains_get_params,
    organization_list_assets_v1_org_assets_get_params,
    organization_list_personas_v1_org_personas_get_params,
    organization_list_categories_v1_org_categories_get_params,
    organization_list_category_prompts_v1_org_categories_category_prompts_get_params,
    organization_create_category_prompts_v1_org_categories_category_id_prompts_post_params,
    organization_update_category_prompts_v1_org_categories_category_id_prompts_patch_params,
    organization_update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch_params,
)
from ..types.organization_list_models_v1_org_models_get_response import OrganizationListModelsV1OrgModelsGetResponse
from ..types.organization_list_domains_v1_org_domains_get_response import OrganizationListDomainsV1OrgDomainsGetResponse
from ..types.organization_list_assets_v1_org_assets_get_response import OrganizationListAssetsV1OrgAssetsGetResponse
from ..types.organization_list_personas_v1_org_personas_get_response import (
    OrganizationListPersonasV1OrgPersonasGetResponse,
)
from ..types.organization_list_categories_v1_org_categories_get_response import (
    OrganizationListCategoriesV1OrgCategoriesGetResponse,
)
from ..types.organization_list_category_topics_v1_org_categories_category_topics_get_response import (
    OrganizationListCategoryTopicsV1OrgCategoriesCategoryTopicsGetResponse,
)
from ..types.organization_list_category_tags_v1_org_categories_category_tags_get_response import (
    OrganizationListCategoryTagsV1OrgCategoriesCategoryTagsGetResponse,
)
from ..types.organization_list_category_regions_v1_org_categories_category_regions_get_response import (
    OrganizationListCategoryRegionsV1OrgCategoriesCategoryRegionsGetResponse,
)
from ..types.organization_list_category_citation_categories_v1_org_categories_category_citation_categories_get_response import (
    OrganizationListCategoryCitationCategoriesV1OrgCategoriesCategoryCitationCategoriesGetResponse,
)
from ..types.organization_list_category_citation_tags_v1_org_categories_category_citation_tags_get_response import (
    OrganizationListCategoryCitationTagsV1OrgCategoriesCategoryCitationTagsGetResponse,
)
from ..types.organization_list_category_prompts_v1_org_categories_category_prompts_get_response import (
    OrganizationListCategoryPromptsV1OrgCategoriesCategoryPromptsGetResponse,
)
from ..types.organization_create_category_prompts_v1_org_categories_category_id_prompts_post_response import (
    OrganizationCreateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPostResponse,
)
from ..types.organization_update_category_prompts_v1_org_categories_category_id_prompts_patch_response import (
    OrganizationUpdateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPatchResponse,
)
from ..types.organization_update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch_response import (
    OrganizationUpdateCategoryPromptStatusV1OrgCategoriesCategoryIDPromptsStatusPatchResponse,
)
from ..types.organization_list_category_assets_v1_org_categories_category_assets_get_response import (
    OrganizationListCategoryAssetsV1OrgCategoriesCategoryAssetsGetResponse,
)
from ..types.organization_list_category_personas_v1_org_categories_category_personas_get_response import (
    OrganizationListCategoryPersonasV1OrgCategoriesCategoryPersonasGetResponse,
)

__all__ = ["OrganizationResource", "AsyncOrganizationResource"]


class OrganizationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrganizationResourceWithRawResponse:
        return OrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationResourceWithStreamingResponse:
        return OrganizationResourceWithStreamingResponse(self)

    def list_v1_org_get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListV1OrgGetResponse:
        """
        Return every organization the caller's API key grants access to. Use this to discover organization IDs before calling endpoints that accept an `organization_id` filter.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListV1OrgGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_v1_org_get()
            ```
        """
        return self._get(
            "/v1/org",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListV1OrgGetResponse,
        )

    def list_regions_v1_org_regions_get(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListRegionsV1OrgRegionsGetResponse:
        """
        Get the organization regions.

        Args:
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListRegionsV1OrgRegionsGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_regions_v1_org_regions_get()
            ```
        """
        return self._get(
            "/v1/org/regions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_ids": organization_ids},
                    organization_list_regions_v1_org_regions_get_params.OrganizationListRegionsV1OrgRegionsGetParams,
                ),
            ),
            cast_to=OrganizationListRegionsV1OrgRegionsGetResponse,
        )

    def list_models_v1_org_models_get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListModelsV1OrgModelsGetResponse:
        """
        Get the organization models.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListModelsV1OrgModelsGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_models_v1_org_models_get()
            ```
        """
        return self._get(
            "/v1/org/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListModelsV1OrgModelsGetResponse,
        )

    def list_domains_v1_org_domains_get(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListDomainsV1OrgDomainsGetResponse:
        """
        Get the organization domains.

        Args:
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListDomainsV1OrgDomainsGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_domains_v1_org_domains_get()
            ```
        """
        return self._get(
            "/v1/org/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_ids": organization_ids},
                    organization_list_domains_v1_org_domains_get_params.OrganizationListDomainsV1OrgDomainsGetParams,
                ),
            ),
            cast_to=OrganizationListDomainsV1OrgDomainsGetResponse,
        )

    def list_assets_v1_org_assets_get(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListAssetsV1OrgAssetsGetResponse:
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
            OrganizationListAssetsV1OrgAssetsGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_assets_v1_org_assets_get()
            ```
        """
        return self._get(
            "/v1/org/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_ids": organization_ids},
                    organization_list_assets_v1_org_assets_get_params.OrganizationListAssetsV1OrgAssetsGetParams,
                ),
            ),
            cast_to=OrganizationListAssetsV1OrgAssetsGetResponse,
        )

    def list_personas_v1_org_personas_get(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListPersonasV1OrgPersonasGetResponse:
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
            OrganizationListPersonasV1OrgPersonasGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_personas_v1_org_personas_get()
            ```
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
                    organization_list_personas_v1_org_personas_get_params.OrganizationListPersonasV1OrgPersonasGetParams,
                ),
            ),
            cast_to=OrganizationListPersonasV1OrgPersonasGetResponse,
        )

    def list_categories_v1_org_categories_get(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoriesV1OrgCategoriesGetResponse:
        """
        Get the organization categories, one row per (category, organization) pair.

        Args:
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoriesV1OrgCategoriesGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_categories_v1_org_categories_get()
            ```
        """
        return self._get(
            "/v1/org/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_ids": organization_ids},
                    organization_list_categories_v1_org_categories_get_params.OrganizationListCategoriesV1OrgCategoriesGetParams,
                ),
            ),
            cast_to=OrganizationListCategoriesV1OrgCategoriesGetResponse,
        )

    def list_category_topics_v1_org_categories_category_topics_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryTopicsV1OrgCategoriesCategoryTopicsGetResponse:
        """
        Get the topics for a specific category.

        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryTopicsV1OrgCategoriesCategoryTopicsGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_category_topics_v1_org_categories_category_topics_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/topics", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryTopicsV1OrgCategoriesCategoryTopicsGetResponse,
        )

    def list_category_tags_v1_org_categories_category_tags_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryTagsV1OrgCategoriesCategoryTagsGetResponse:
        """
        Get the tags for a specific category.

        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryTagsV1OrgCategoriesCategoryTagsGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_category_tags_v1_org_categories_category_tags_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/tags", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryTagsV1OrgCategoriesCategoryTagsGetResponse,
        )

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
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/regions", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryRegionsV1OrgCategoriesCategoryRegionsGetResponse,
        )

    def list_category_citation_categories_v1_org_categories_category_citation_categories_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryCitationCategoriesV1OrgCategoriesCategoryCitationCategoriesGetResponse:
        """
        Get the citation categories for a category: the built-in buckets plus any custom categories.

        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryCitationCategoriesV1OrgCategoriesCategoryCitationCategoriesGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_category_citation_categories_v1_org_categories_category_citation_categories_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/citation-categories", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryCitationCategoriesV1OrgCategoriesCategoryCitationCategoriesGetResponse,
        )

    def list_category_citation_tags_v1_org_categories_category_citation_tags_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryCitationTagsV1OrgCategoriesCategoryCitationTagsGetResponse:
        """
        Get the custom citation tags defined for a category.

        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryCitationTagsV1OrgCategoriesCategoryCitationTagsGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_category_citation_tags_v1_org_categories_category_citation_tags_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/citation-tags", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryCitationTagsV1OrgCategoriesCategoryCitationTagsGetResponse,
        )

    def list_category_prompts_v1_org_categories_category_prompts_get(
        self,
        category_id: str,
        *,
        limit: int | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        order_by: Literal["created_at", "prompt"] | Omit = omit,
        order_dir: Literal["asc", "desc"] | Omit = omit,
        analysis_type: List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]] | Omit = omit,
        prompt_type: List[Literal["visibility", "sentiment"]] | Omit = omit,
        status: List[Literal["active", "disabled"]] | Omit = omit,
        topic_id: SequenceNotStr[str] | Omit = omit,
        tag_id: SequenceNotStr[str] | Omit = omit,
        region_id: SequenceNotStr[str] | Omit = omit,
        platform_id: SequenceNotStr[str] | Omit = omit,
        persona_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryPromptsV1OrgCategoriesCategoryPromptsGetResponse:
        """
        Retrieve prompts in a category with optional filtering by type, topic, tag, region, platform, or persona. Supports cursor-based pagination.

        Args:
            category_id: Path parameter.
            limit: Maximum number of prompts to return.
            cursor: Pagination cursor from a previous response.
            order_by: Field used to order prompts.
            order_dir: Sort direction for the selected order field.
            analysis_type: Filter by analysis type (visibility, sentiment, accuracy).
            prompt_type: Deprecated. Use analysis_type instead.
            status: Filter by prompt status. Defaults to `active` only.
            topic_id: Filter by topic IDs.
            tag_id: Filter by tag IDs.
            region_id: Filter by region IDs.
            platform_id: Filter by platform IDs.
            persona_id: Filter by persona IDs.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryPromptsV1OrgCategoriesCategoryPromptsGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_category_prompts_v1_org_categories_category_prompts_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=10000,
                status=["active"],
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/prompts", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                        "order_by": order_by,
                        "order_dir": order_dir,
                        "analysis_type": analysis_type,
                        "prompt_type": prompt_type,
                        "status": status,
                        "topic_id": topic_id,
                        "tag_id": tag_id,
                        "region_id": region_id,
                        "platform_id": platform_id,
                        "persona_id": persona_id,
                    },
                    organization_list_category_prompts_v1_org_categories_category_prompts_get_params.OrganizationListCategoryPromptsV1OrgCategoriesCategoryPromptsGetParams,
                ),
            ),
            cast_to=OrganizationListCategoryPromptsV1OrgCategoriesCategoryPromptsGetResponse,
        )

    def create_category_prompts_v1_org_categories_category_id_prompts_post(
        self,
        category_id: str,
        *,
        prompts: Iterable[
            organization_create_category_prompts_v1_org_categories_category_id_prompts_post_params.Prompt
        ],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationCreateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPostResponse:
        """
        Create one or more prompts in a category. Topics and tags are auto-created if referenced by name and not yet existing. Use dry_run to preview without persisting.

        Args:
            category_id: Path parameter.
            prompts: List of prompts to create.
            dry_run: When true, validate and preview changes without persisting them.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationCreateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPostResponse: Successful Response

        Example:
            ```python
            organization = client.organization.create_category_prompts_v1_org_categories_category_id_prompts_post(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                prompts=[],
                dry_run=False,
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._post(
            path_template("/v1/org/categories/{category_id}/prompts", **{"category_id": category_id}),
            body=maybe_transform(
                {
                    "prompts": prompts,
                    "dry_run": dry_run,
                },
                organization_create_category_prompts_v1_org_categories_category_id_prompts_post_params.OrganizationCreateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationCreateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPostResponse,
        )

    def update_category_prompts_v1_org_categories_category_id_prompts_patch(
        self,
        category_id: str,
        *,
        prompts: Iterable[
            organization_update_category_prompts_v1_org_categories_category_id_prompts_patch_params.Prompt
        ],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationUpdateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPatchResponse:
        """
        Update one or more existing prompts. Only provided fields are changed. Dimension fields (regions, platforms, personas, tags) replace the full set when provided. Use dry_run to preview without persisting.

        Args:
            category_id: Path parameter.
            prompts: List of prompt updates. Each entry must include an `id` and at least one field to change.
            dry_run: When true, validate and preview changes without persisting them.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationUpdateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPatchResponse: Successful Response

        Example:
            ```python
            organization = client.organization.update_category_prompts_v1_org_categories_category_id_prompts_patch(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                prompts=[],
                dry_run=False,
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._patch(
            path_template("/v1/org/categories/{category_id}/prompts", **{"category_id": category_id}),
            body=maybe_transform(
                {
                    "prompts": prompts,
                    "dry_run": dry_run,
                },
                organization_update_category_prompts_v1_org_categories_category_id_prompts_patch_params.OrganizationUpdateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationUpdateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPatchResponse,
        )

    def update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch(
        self,
        category_id: str,
        *,
        prompt_ids: SequenceNotStr[str],
        status: Literal["active", "disabled", "deleted"],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationUpdateCategoryPromptStatusV1OrgCategoriesCategoryIDPromptsStatusPatchResponse:
        """
        Bulk-update the status of one or more prompts. Prompts already in the target status are skipped. Use dry_run to preview without persisting.

        Status options:
        - 'active': Prompts will run daily.
        - 'disabled': Prompts will not run moving forward, but historical data is preserved.
        - 'deleted': Prompts are deleted along with historical data

        Args:
            category_id: Path parameter.
            prompt_ids: IDs of the prompts to update.
            status: Target status: 'active', 'disabled', or 'deleted'.
            dry_run: When true, validate and preview changes without persisting them.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationUpdateCategoryPromptStatusV1OrgCategoriesCategoryIDPromptsStatusPatchResponse: Successful Response

        Example:
            ```python
            organization = client.organization.update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                prompt_ids=[],
                status="active",
                dry_run=False,
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._patch(
            path_template("/v1/org/categories/{category_id}/prompts/status", **{"category_id": category_id}),
            body=maybe_transform(
                {
                    "prompt_ids": prompt_ids,
                    "status": status,
                    "dry_run": dry_run,
                },
                organization_update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch_params.OrganizationUpdateCategoryPromptStatusV1OrgCategoriesCategoryIDPromptsStatusPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationUpdateCategoryPromptStatusV1OrgCategoriesCategoryIDPromptsStatusPatchResponse,
        )

    def list_category_assets_v1_org_categories_category_assets_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryAssetsV1OrgCategoriesCategoryAssetsGetResponse:
        """
        Get Category Assets

        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryAssetsV1OrgCategoriesCategoryAssetsGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_category_assets_v1_org_categories_category_assets_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/assets", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryAssetsV1OrgCategoriesCategoryAssetsGetResponse,
        )

    def list_category_personas_v1_org_categories_category_personas_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryPersonasV1OrgCategoriesCategoryPersonasGetResponse:
        """
        Get Category Personas

        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryPersonasV1OrgCategoriesCategoryPersonasGetResponse: Successful Response

        Example:
            ```python
            organization = client.organization.list_category_personas_v1_org_categories_category_personas_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/personas", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryPersonasV1OrgCategoriesCategoryPersonasGetResponse,
        )


class AsyncOrganizationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrganizationResourceWithRawResponse:
        return AsyncOrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationResourceWithStreamingResponse:
        return AsyncOrganizationResourceWithStreamingResponse(self)

    async def list_v1_org_get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListV1OrgGetResponse:
        """
        Return every organization the caller's API key grants access to. Use this to discover organization IDs before calling endpoints that accept an `organization_id` filter.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListV1OrgGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_v1_org_get()
            ```
        """
        return await self._get(
            "/v1/org",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListV1OrgGetResponse,
        )

    async def list_regions_v1_org_regions_get(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListRegionsV1OrgRegionsGetResponse:
        """
        Get the organization regions.

        Args:
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListRegionsV1OrgRegionsGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_regions_v1_org_regions_get()
            ```
        """
        return await self._get(
            "/v1/org/regions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_ids": organization_ids},
                    organization_list_regions_v1_org_regions_get_params.OrganizationListRegionsV1OrgRegionsGetParams,
                ),
            ),
            cast_to=OrganizationListRegionsV1OrgRegionsGetResponse,
        )

    async def list_models_v1_org_models_get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListModelsV1OrgModelsGetResponse:
        """
        Get the organization models.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListModelsV1OrgModelsGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_models_v1_org_models_get()
            ```
        """
        return await self._get(
            "/v1/org/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListModelsV1OrgModelsGetResponse,
        )

    async def list_domains_v1_org_domains_get(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListDomainsV1OrgDomainsGetResponse:
        """
        Get the organization domains.

        Args:
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListDomainsV1OrgDomainsGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_domains_v1_org_domains_get()
            ```
        """
        return await self._get(
            "/v1/org/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_ids": organization_ids},
                    organization_list_domains_v1_org_domains_get_params.OrganizationListDomainsV1OrgDomainsGetParams,
                ),
            ),
            cast_to=OrganizationListDomainsV1OrgDomainsGetResponse,
        )

    async def list_assets_v1_org_assets_get(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListAssetsV1OrgAssetsGetResponse:
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
            OrganizationListAssetsV1OrgAssetsGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_assets_v1_org_assets_get()
            ```
        """
        return await self._get(
            "/v1/org/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_ids": organization_ids},
                    organization_list_assets_v1_org_assets_get_params.OrganizationListAssetsV1OrgAssetsGetParams,
                ),
            ),
            cast_to=OrganizationListAssetsV1OrgAssetsGetResponse,
        )

    async def list_personas_v1_org_personas_get(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListPersonasV1OrgPersonasGetResponse:
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
            OrganizationListPersonasV1OrgPersonasGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_personas_v1_org_personas_get()
            ```
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
                    organization_list_personas_v1_org_personas_get_params.OrganizationListPersonasV1OrgPersonasGetParams,
                ),
            ),
            cast_to=OrganizationListPersonasV1OrgPersonasGetResponse,
        )

    async def list_categories_v1_org_categories_get(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoriesV1OrgCategoriesGetResponse:
        """
        Get the organization categories, one row per (category, organization) pair.

        Args:
            organization_ids: Restrict results to one or more organizations the caller belongs to. Repeat the parameter to target multiple orgs (e.g. `?organization_ids=<id1>&organization_ids=<id2>`). Omit to return data from every organization the caller has access to.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoriesV1OrgCategoriesGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_categories_v1_org_categories_get()
            ```
        """
        return await self._get(
            "/v1/org/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_ids": organization_ids},
                    organization_list_categories_v1_org_categories_get_params.OrganizationListCategoriesV1OrgCategoriesGetParams,
                ),
            ),
            cast_to=OrganizationListCategoriesV1OrgCategoriesGetResponse,
        )

    async def list_category_topics_v1_org_categories_category_topics_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryTopicsV1OrgCategoriesCategoryTopicsGetResponse:
        """
        Get the topics for a specific category.

        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryTopicsV1OrgCategoriesCategoryTopicsGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_category_topics_v1_org_categories_category_topics_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/topics", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryTopicsV1OrgCategoriesCategoryTopicsGetResponse,
        )

    async def list_category_tags_v1_org_categories_category_tags_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryTagsV1OrgCategoriesCategoryTagsGetResponse:
        """
        Get the tags for a specific category.

        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryTagsV1OrgCategoriesCategoryTagsGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_category_tags_v1_org_categories_category_tags_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/tags", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryTagsV1OrgCategoriesCategoryTagsGetResponse,
        )

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
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/regions", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryRegionsV1OrgCategoriesCategoryRegionsGetResponse,
        )

    async def list_category_citation_categories_v1_org_categories_category_citation_categories_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryCitationCategoriesV1OrgCategoriesCategoryCitationCategoriesGetResponse:
        """
        Get the citation categories for a category: the built-in buckets plus any custom categories.

        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryCitationCategoriesV1OrgCategoriesCategoryCitationCategoriesGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_category_citation_categories_v1_org_categories_category_citation_categories_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/citation-categories", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryCitationCategoriesV1OrgCategoriesCategoryCitationCategoriesGetResponse,
        )

    async def list_category_citation_tags_v1_org_categories_category_citation_tags_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryCitationTagsV1OrgCategoriesCategoryCitationTagsGetResponse:
        """
        Get the custom citation tags defined for a category.

        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryCitationTagsV1OrgCategoriesCategoryCitationTagsGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_category_citation_tags_v1_org_categories_category_citation_tags_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/citation-tags", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryCitationTagsV1OrgCategoriesCategoryCitationTagsGetResponse,
        )

    async def list_category_prompts_v1_org_categories_category_prompts_get(
        self,
        category_id: str,
        *,
        limit: int | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        order_by: Literal["created_at", "prompt"] | Omit = omit,
        order_dir: Literal["asc", "desc"] | Omit = omit,
        analysis_type: List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]] | Omit = omit,
        prompt_type: List[Literal["visibility", "sentiment"]] | Omit = omit,
        status: List[Literal["active", "disabled"]] | Omit = omit,
        topic_id: SequenceNotStr[str] | Omit = omit,
        tag_id: SequenceNotStr[str] | Omit = omit,
        region_id: SequenceNotStr[str] | Omit = omit,
        platform_id: SequenceNotStr[str] | Omit = omit,
        persona_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryPromptsV1OrgCategoriesCategoryPromptsGetResponse:
        """
        Retrieve prompts in a category with optional filtering by type, topic, tag, region, platform, or persona. Supports cursor-based pagination.

        Args:
            category_id: Path parameter.
            limit: Maximum number of prompts to return.
            cursor: Pagination cursor from a previous response.
            order_by: Field used to order prompts.
            order_dir: Sort direction for the selected order field.
            analysis_type: Filter by analysis type (visibility, sentiment, accuracy).
            prompt_type: Deprecated. Use analysis_type instead.
            status: Filter by prompt status. Defaults to `active` only.
            topic_id: Filter by topic IDs.
            tag_id: Filter by tag IDs.
            region_id: Filter by region IDs.
            platform_id: Filter by platform IDs.
            persona_id: Filter by persona IDs.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryPromptsV1OrgCategoriesCategoryPromptsGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_category_prompts_v1_org_categories_category_prompts_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=10000,
                status=["active"],
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/prompts", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "cursor": cursor,
                        "order_by": order_by,
                        "order_dir": order_dir,
                        "analysis_type": analysis_type,
                        "prompt_type": prompt_type,
                        "status": status,
                        "topic_id": topic_id,
                        "tag_id": tag_id,
                        "region_id": region_id,
                        "platform_id": platform_id,
                        "persona_id": persona_id,
                    },
                    organization_list_category_prompts_v1_org_categories_category_prompts_get_params.OrganizationListCategoryPromptsV1OrgCategoriesCategoryPromptsGetParams,
                ),
            ),
            cast_to=OrganizationListCategoryPromptsV1OrgCategoriesCategoryPromptsGetResponse,
        )

    async def create_category_prompts_v1_org_categories_category_id_prompts_post(
        self,
        category_id: str,
        *,
        prompts: Iterable[
            organization_create_category_prompts_v1_org_categories_category_id_prompts_post_params.Prompt
        ],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationCreateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPostResponse:
        """
        Create one or more prompts in a category. Topics and tags are auto-created if referenced by name and not yet existing. Use dry_run to preview without persisting.

        Args:
            category_id: Path parameter.
            prompts: List of prompts to create.
            dry_run: When true, validate and preview changes without persisting them.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationCreateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPostResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.create_category_prompts_v1_org_categories_category_id_prompts_post(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                prompts=[],
                dry_run=False,
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._post(
            path_template("/v1/org/categories/{category_id}/prompts", **{"category_id": category_id}),
            body=await async_maybe_transform(
                {
                    "prompts": prompts,
                    "dry_run": dry_run,
                },
                organization_create_category_prompts_v1_org_categories_category_id_prompts_post_params.OrganizationCreateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationCreateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPostResponse,
        )

    async def update_category_prompts_v1_org_categories_category_id_prompts_patch(
        self,
        category_id: str,
        *,
        prompts: Iterable[
            organization_update_category_prompts_v1_org_categories_category_id_prompts_patch_params.Prompt
        ],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationUpdateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPatchResponse:
        """
        Update one or more existing prompts. Only provided fields are changed. Dimension fields (regions, platforms, personas, tags) replace the full set when provided. Use dry_run to preview without persisting.

        Args:
            category_id: Path parameter.
            prompts: List of prompt updates. Each entry must include an `id` and at least one field to change.
            dry_run: When true, validate and preview changes without persisting them.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationUpdateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPatchResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.update_category_prompts_v1_org_categories_category_id_prompts_patch(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                prompts=[],
                dry_run=False,
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._patch(
            path_template("/v1/org/categories/{category_id}/prompts", **{"category_id": category_id}),
            body=await async_maybe_transform(
                {
                    "prompts": prompts,
                    "dry_run": dry_run,
                },
                organization_update_category_prompts_v1_org_categories_category_id_prompts_patch_params.OrganizationUpdateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationUpdateCategoryPromptsV1OrgCategoriesCategoryIDPromptsPatchResponse,
        )

    async def update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch(
        self,
        category_id: str,
        *,
        prompt_ids: SequenceNotStr[str],
        status: Literal["active", "disabled", "deleted"],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationUpdateCategoryPromptStatusV1OrgCategoriesCategoryIDPromptsStatusPatchResponse:
        """
        Bulk-update the status of one or more prompts. Prompts already in the target status are skipped. Use dry_run to preview without persisting.

        Status options:
        - 'active': Prompts will run daily.
        - 'disabled': Prompts will not run moving forward, but historical data is preserved.
        - 'deleted': Prompts are deleted along with historical data

        Args:
            category_id: Path parameter.
            prompt_ids: IDs of the prompts to update.
            status: Target status: 'active', 'disabled', or 'deleted'.
            dry_run: When true, validate and preview changes without persisting them.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationUpdateCategoryPromptStatusV1OrgCategoriesCategoryIDPromptsStatusPatchResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                prompt_ids=[],
                status="active",
                dry_run=False,
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._patch(
            path_template("/v1/org/categories/{category_id}/prompts/status", **{"category_id": category_id}),
            body=await async_maybe_transform(
                {
                    "prompt_ids": prompt_ids,
                    "status": status,
                    "dry_run": dry_run,
                },
                organization_update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch_params.OrganizationUpdateCategoryPromptStatusV1OrgCategoriesCategoryIDPromptsStatusPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationUpdateCategoryPromptStatusV1OrgCategoriesCategoryIDPromptsStatusPatchResponse,
        )

    async def list_category_assets_v1_org_categories_category_assets_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryAssetsV1OrgCategoriesCategoryAssetsGetResponse:
        """
        Get Category Assets

        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryAssetsV1OrgCategoriesCategoryAssetsGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_category_assets_v1_org_categories_category_assets_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/assets", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryAssetsV1OrgCategoriesCategoryAssetsGetResponse,
        )

    async def list_category_personas_v1_org_categories_category_personas_get(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationListCategoryPersonasV1OrgCategoriesCategoryPersonasGetResponse:
        """
        Get Category Personas

        Args:
            category_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationListCategoryPersonasV1OrgCategoriesCategoryPersonasGetResponse: Successful Response

        Example:
            ```python
            organization = await client.organization.list_category_personas_v1_org_categories_category_personas_get(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if category_id is None or (isinstance(category_id, str) and not category_id):
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/personas", **{"category_id": category_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListCategoryPersonasV1OrgCategoriesCategoryPersonasGetResponse,
        )


class OrganizationResourceWithRawResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

        self.list_v1_org_get = to_raw_response_wrapper(
            organization.list_v1_org_get,
        )
        self.list_regions_v1_org_regions_get = to_raw_response_wrapper(
            organization.list_regions_v1_org_regions_get,
        )
        self.list_models_v1_org_models_get = to_raw_response_wrapper(
            organization.list_models_v1_org_models_get,
        )
        self.list_domains_v1_org_domains_get = to_raw_response_wrapper(
            organization.list_domains_v1_org_domains_get,
        )
        self.list_assets_v1_org_assets_get = to_raw_response_wrapper(
            organization.list_assets_v1_org_assets_get,
        )
        self.list_personas_v1_org_personas_get = to_raw_response_wrapper(
            organization.list_personas_v1_org_personas_get,
        )
        self.list_categories_v1_org_categories_get = to_raw_response_wrapper(
            organization.list_categories_v1_org_categories_get,
        )
        self.list_category_topics_v1_org_categories_category_topics_get = to_raw_response_wrapper(
            organization.list_category_topics_v1_org_categories_category_topics_get,
        )
        self.list_category_tags_v1_org_categories_category_tags_get = to_raw_response_wrapper(
            organization.list_category_tags_v1_org_categories_category_tags_get,
        )
        self.list_category_regions_v1_org_categories_category_regions_get = to_raw_response_wrapper(
            organization.list_category_regions_v1_org_categories_category_regions_get,
        )
        self.list_category_citation_categories_v1_org_categories_category_citation_categories_get = (
            to_raw_response_wrapper(
                organization.list_category_citation_categories_v1_org_categories_category_citation_categories_get,
            )
        )
        self.list_category_citation_tags_v1_org_categories_category_citation_tags_get = to_raw_response_wrapper(
            organization.list_category_citation_tags_v1_org_categories_category_citation_tags_get,
        )
        self.list_category_prompts_v1_org_categories_category_prompts_get = to_raw_response_wrapper(
            organization.list_category_prompts_v1_org_categories_category_prompts_get,
        )
        self.create_category_prompts_v1_org_categories_category_id_prompts_post = to_raw_response_wrapper(
            organization.create_category_prompts_v1_org_categories_category_id_prompts_post,
        )
        self.update_category_prompts_v1_org_categories_category_id_prompts_patch = to_raw_response_wrapper(
            organization.update_category_prompts_v1_org_categories_category_id_prompts_patch,
        )
        self.update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch = to_raw_response_wrapper(
            organization.update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch,
        )
        self.list_category_assets_v1_org_categories_category_assets_get = to_raw_response_wrapper(
            organization.list_category_assets_v1_org_categories_category_assets_get,
        )
        self.list_category_personas_v1_org_categories_category_personas_get = to_raw_response_wrapper(
            organization.list_category_personas_v1_org_categories_category_personas_get,
        )


class AsyncOrganizationResourceWithRawResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

        self.list_v1_org_get = async_to_raw_response_wrapper(
            organization.list_v1_org_get,
        )
        self.list_regions_v1_org_regions_get = async_to_raw_response_wrapper(
            organization.list_regions_v1_org_regions_get,
        )
        self.list_models_v1_org_models_get = async_to_raw_response_wrapper(
            organization.list_models_v1_org_models_get,
        )
        self.list_domains_v1_org_domains_get = async_to_raw_response_wrapper(
            organization.list_domains_v1_org_domains_get,
        )
        self.list_assets_v1_org_assets_get = async_to_raw_response_wrapper(
            organization.list_assets_v1_org_assets_get,
        )
        self.list_personas_v1_org_personas_get = async_to_raw_response_wrapper(
            organization.list_personas_v1_org_personas_get,
        )
        self.list_categories_v1_org_categories_get = async_to_raw_response_wrapper(
            organization.list_categories_v1_org_categories_get,
        )
        self.list_category_topics_v1_org_categories_category_topics_get = async_to_raw_response_wrapper(
            organization.list_category_topics_v1_org_categories_category_topics_get,
        )
        self.list_category_tags_v1_org_categories_category_tags_get = async_to_raw_response_wrapper(
            organization.list_category_tags_v1_org_categories_category_tags_get,
        )
        self.list_category_regions_v1_org_categories_category_regions_get = async_to_raw_response_wrapper(
            organization.list_category_regions_v1_org_categories_category_regions_get,
        )
        self.list_category_citation_categories_v1_org_categories_category_citation_categories_get = (
            async_to_raw_response_wrapper(
                organization.list_category_citation_categories_v1_org_categories_category_citation_categories_get,
            )
        )
        self.list_category_citation_tags_v1_org_categories_category_citation_tags_get = async_to_raw_response_wrapper(
            organization.list_category_citation_tags_v1_org_categories_category_citation_tags_get,
        )
        self.list_category_prompts_v1_org_categories_category_prompts_get = async_to_raw_response_wrapper(
            organization.list_category_prompts_v1_org_categories_category_prompts_get,
        )
        self.create_category_prompts_v1_org_categories_category_id_prompts_post = async_to_raw_response_wrapper(
            organization.create_category_prompts_v1_org_categories_category_id_prompts_post,
        )
        self.update_category_prompts_v1_org_categories_category_id_prompts_patch = async_to_raw_response_wrapper(
            organization.update_category_prompts_v1_org_categories_category_id_prompts_patch,
        )
        self.update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch = (
            async_to_raw_response_wrapper(
                organization.update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch,
            )
        )
        self.list_category_assets_v1_org_categories_category_assets_get = async_to_raw_response_wrapper(
            organization.list_category_assets_v1_org_categories_category_assets_get,
        )
        self.list_category_personas_v1_org_categories_category_personas_get = async_to_raw_response_wrapper(
            organization.list_category_personas_v1_org_categories_category_personas_get,
        )


class OrganizationResourceWithStreamingResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

        self.list_v1_org_get = to_streamed_response_wrapper(
            organization.list_v1_org_get,
        )
        self.list_regions_v1_org_regions_get = to_streamed_response_wrapper(
            organization.list_regions_v1_org_regions_get,
        )
        self.list_models_v1_org_models_get = to_streamed_response_wrapper(
            organization.list_models_v1_org_models_get,
        )
        self.list_domains_v1_org_domains_get = to_streamed_response_wrapper(
            organization.list_domains_v1_org_domains_get,
        )
        self.list_assets_v1_org_assets_get = to_streamed_response_wrapper(
            organization.list_assets_v1_org_assets_get,
        )
        self.list_personas_v1_org_personas_get = to_streamed_response_wrapper(
            organization.list_personas_v1_org_personas_get,
        )
        self.list_categories_v1_org_categories_get = to_streamed_response_wrapper(
            organization.list_categories_v1_org_categories_get,
        )
        self.list_category_topics_v1_org_categories_category_topics_get = to_streamed_response_wrapper(
            organization.list_category_topics_v1_org_categories_category_topics_get,
        )
        self.list_category_tags_v1_org_categories_category_tags_get = to_streamed_response_wrapper(
            organization.list_category_tags_v1_org_categories_category_tags_get,
        )
        self.list_category_regions_v1_org_categories_category_regions_get = to_streamed_response_wrapper(
            organization.list_category_regions_v1_org_categories_category_regions_get,
        )
        self.list_category_citation_categories_v1_org_categories_category_citation_categories_get = (
            to_streamed_response_wrapper(
                organization.list_category_citation_categories_v1_org_categories_category_citation_categories_get,
            )
        )
        self.list_category_citation_tags_v1_org_categories_category_citation_tags_get = to_streamed_response_wrapper(
            organization.list_category_citation_tags_v1_org_categories_category_citation_tags_get,
        )
        self.list_category_prompts_v1_org_categories_category_prompts_get = to_streamed_response_wrapper(
            organization.list_category_prompts_v1_org_categories_category_prompts_get,
        )
        self.create_category_prompts_v1_org_categories_category_id_prompts_post = to_streamed_response_wrapper(
            organization.create_category_prompts_v1_org_categories_category_id_prompts_post,
        )
        self.update_category_prompts_v1_org_categories_category_id_prompts_patch = to_streamed_response_wrapper(
            organization.update_category_prompts_v1_org_categories_category_id_prompts_patch,
        )
        self.update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch = (
            to_streamed_response_wrapper(
                organization.update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch,
            )
        )
        self.list_category_assets_v1_org_categories_category_assets_get = to_streamed_response_wrapper(
            organization.list_category_assets_v1_org_categories_category_assets_get,
        )
        self.list_category_personas_v1_org_categories_category_personas_get = to_streamed_response_wrapper(
            organization.list_category_personas_v1_org_categories_category_personas_get,
        )


class AsyncOrganizationResourceWithStreamingResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

        self.list_v1_org_get = async_to_streamed_response_wrapper(
            organization.list_v1_org_get,
        )
        self.list_regions_v1_org_regions_get = async_to_streamed_response_wrapper(
            organization.list_regions_v1_org_regions_get,
        )
        self.list_models_v1_org_models_get = async_to_streamed_response_wrapper(
            organization.list_models_v1_org_models_get,
        )
        self.list_domains_v1_org_domains_get = async_to_streamed_response_wrapper(
            organization.list_domains_v1_org_domains_get,
        )
        self.list_assets_v1_org_assets_get = async_to_streamed_response_wrapper(
            organization.list_assets_v1_org_assets_get,
        )
        self.list_personas_v1_org_personas_get = async_to_streamed_response_wrapper(
            organization.list_personas_v1_org_personas_get,
        )
        self.list_categories_v1_org_categories_get = async_to_streamed_response_wrapper(
            organization.list_categories_v1_org_categories_get,
        )
        self.list_category_topics_v1_org_categories_category_topics_get = async_to_streamed_response_wrapper(
            organization.list_category_topics_v1_org_categories_category_topics_get,
        )
        self.list_category_tags_v1_org_categories_category_tags_get = async_to_streamed_response_wrapper(
            organization.list_category_tags_v1_org_categories_category_tags_get,
        )
        self.list_category_regions_v1_org_categories_category_regions_get = async_to_streamed_response_wrapper(
            organization.list_category_regions_v1_org_categories_category_regions_get,
        )
        self.list_category_citation_categories_v1_org_categories_category_citation_categories_get = (
            async_to_streamed_response_wrapper(
                organization.list_category_citation_categories_v1_org_categories_category_citation_categories_get,
            )
        )
        self.list_category_citation_tags_v1_org_categories_category_citation_tags_get = (
            async_to_streamed_response_wrapper(
                organization.list_category_citation_tags_v1_org_categories_category_citation_tags_get,
            )
        )
        self.list_category_prompts_v1_org_categories_category_prompts_get = async_to_streamed_response_wrapper(
            organization.list_category_prompts_v1_org_categories_category_prompts_get,
        )
        self.create_category_prompts_v1_org_categories_category_id_prompts_post = async_to_streamed_response_wrapper(
            organization.create_category_prompts_v1_org_categories_category_id_prompts_post,
        )
        self.update_category_prompts_v1_org_categories_category_id_prompts_patch = async_to_streamed_response_wrapper(
            organization.update_category_prompts_v1_org_categories_category_id_prompts_patch,
        )
        self.update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch = (
            async_to_streamed_response_wrapper(
                organization.update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch,
            )
        )
        self.list_category_assets_v1_org_categories_category_assets_get = async_to_streamed_response_wrapper(
            organization.list_category_assets_v1_org_categories_category_assets_get,
        )
        self.list_category_personas_v1_org_categories_category_personas_get = async_to_streamed_response_wrapper(
            organization.list_category_personas_v1_org_categories_category_personas_get,
        )
