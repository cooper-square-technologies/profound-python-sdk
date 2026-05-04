# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.organizations import (
    category_list_params,
    category_prompts_params,
    category_create_prompts_params,
    category_update_prompts_params,
    category_update_prompt_status_params,
)
from ...types.organizations.category_list_response import CategoryListResponse
from ...types.organizations.category_tags_response import CategoryTagsResponse
from ...types.organizations.category_assets_response import CategoryAssetsResponse
from ...types.organizations.category_topics_response import CategoryTopicsResponse
from ...types.organizations.category_prompts_response import CategoryPromptsResponse
from ...types.organizations.category_create_prompts_response import CategoryCreatePromptsResponse
from ...types.organizations.category_update_prompts_response import CategoryUpdatePromptsResponse
from ...types.organizations.category_update_prompt_status_response import CategoryUpdatePromptStatusResponse
from ...types.organizations.category_get_category_personas_response import CategoryGetCategoryPersonasResponse

__all__ = ["CategoriesResource", "AsyncCategoriesResource"]


class CategoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return CategoriesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryListResponse:
        """
        Get the organization categories, one row per (category, organization) pair.

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
            "/v1/org/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"organization_ids": organization_ids}, category_list_params.CategoryListParams),
            ),
            cast_to=CategoryListResponse,
        )

    def assets(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryAssetsResponse:
        """
        Get Category Assets

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/assets", category_id=category_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryAssetsResponse,
        )

    def create_prompts(
        self,
        category_id: str,
        *,
        prompts: Iterable[category_create_prompts_params.Prompt],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryCreatePromptsResponse:
        """Create one or more prompts in a category.

        Topics and tags are auto-created if
        referenced by name and not yet existing. Use dry_run to preview without
        persisting.

        Args:
          prompts: List of prompts to create.

          dry_run: When true, validate and preview changes without persisting them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._post(
            path_template("/v1/org/categories/{category_id}/prompts", category_id=category_id),
            body=maybe_transform(
                {
                    "prompts": prompts,
                    "dry_run": dry_run,
                },
                category_create_prompts_params.CategoryCreatePromptsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryCreatePromptsResponse,
        )

    def get_category_personas(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryGetCategoryPersonasResponse:
        """
        Get Category Personas

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/personas", category_id=category_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryGetCategoryPersonasResponse,
        )

    def prompts(
        self,
        category_id: str,
        *,
        analysis_type: List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        order_dir: Literal["asc", "desc"] | Omit = omit,
        persona_id: SequenceNotStr[str] | Omit = omit,
        platform_id: SequenceNotStr[str] | Omit = omit,
        prompt_type: List[Literal["visibility", "sentiment"]] | Omit = omit,
        region_id: SequenceNotStr[str] | Omit = omit,
        status: List[Literal["active", "disabled"]] | Omit = omit,
        tag_id: SequenceNotStr[str] | Omit = omit,
        topic_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryPromptsResponse:
        """
        Retrieve prompts in a category with optional filtering by type, topic, tag,
        region, platform, or persona. Supports cursor-based pagination.

        Args:
          analysis_type: Filter by analysis type (visibility, sentiment, accuracy).

          cursor: Pagination cursor from a previous response.

          limit: Maximum number of prompts to return.

          order_dir: Sort direction by creation date.

          persona_id: Filter by persona IDs.

          platform_id: Filter by platform IDs.

          prompt_type: Deprecated. Use analysis_type instead.

          region_id: Filter by region IDs.

          status: Filter by prompt status. Defaults to `active` only.

          tag_id: Filter by tag IDs.

          topic_id: Filter by topic IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/prompts", category_id=category_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "analysis_type": analysis_type,
                        "cursor": cursor,
                        "limit": limit,
                        "order_dir": order_dir,
                        "persona_id": persona_id,
                        "platform_id": platform_id,
                        "prompt_type": prompt_type,
                        "region_id": region_id,
                        "status": status,
                        "tag_id": tag_id,
                        "topic_id": topic_id,
                    },
                    category_prompts_params.CategoryPromptsParams,
                ),
            ),
            cast_to=CategoryPromptsResponse,
        )

    def tags(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryTagsResponse:
        """
        Get the tags for a specific category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/tags", category_id=category_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryTagsResponse,
        )

    def topics(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryTopicsResponse:
        """
        Get the topics for a specific category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._get(
            path_template("/v1/org/categories/{category_id}/topics", category_id=category_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryTopicsResponse,
        )

    def update_prompt_status(
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
    ) -> CategoryUpdatePromptStatusResponse:
        """Bulk-update the status of one or more prompts.

        Prompts already in the target
        status are skipped. Use dry_run to preview without persisting.

        Status options:

        - 'active': Prompts will run daily.
        - 'disabled': Prompts will not run moving forward, but historical data is
          preserved.
        - 'deleted': Prompts are deleted along with historical data

        Args:
          prompt_ids: IDs of the prompts to update.

          status: Target status: 'active', 'disabled', or 'deleted'.

          dry_run: When true, validate and preview changes without persisting them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._patch(
            path_template("/v1/org/categories/{category_id}/prompts/status", category_id=category_id),
            body=maybe_transform(
                {
                    "prompt_ids": prompt_ids,
                    "status": status,
                    "dry_run": dry_run,
                },
                category_update_prompt_status_params.CategoryUpdatePromptStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryUpdatePromptStatusResponse,
        )

    def update_prompts(
        self,
        category_id: str,
        *,
        prompts: Iterable[category_update_prompts_params.Prompt],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryUpdatePromptsResponse:
        """Update one or more existing prompts.

        Only provided fields are changed. Dimension
        fields (regions, platforms, personas, tags) replace the full set when provided.
        Use dry_run to preview without persisting.

        Args:
          prompts: List of prompt updates. Each entry must include an `id` and at least one field
              to change.

          dry_run: When true, validate and preview changes without persisting them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return self._patch(
            path_template("/v1/org/categories/{category_id}/prompts", category_id=category_id),
            body=maybe_transform(
                {
                    "prompts": prompts,
                    "dry_run": dry_run,
                },
                category_update_prompts_params.CategoryUpdatePromptsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryUpdatePromptsResponse,
        )


class AsyncCategoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCategoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCategoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCategoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncCategoriesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryListResponse:
        """
        Get the organization categories, one row per (category, organization) pair.

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
            "/v1/org/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_ids": organization_ids}, category_list_params.CategoryListParams
                ),
            ),
            cast_to=CategoryListResponse,
        )

    async def assets(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryAssetsResponse:
        """
        Get Category Assets

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/assets", category_id=category_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryAssetsResponse,
        )

    async def create_prompts(
        self,
        category_id: str,
        *,
        prompts: Iterable[category_create_prompts_params.Prompt],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryCreatePromptsResponse:
        """Create one or more prompts in a category.

        Topics and tags are auto-created if
        referenced by name and not yet existing. Use dry_run to preview without
        persisting.

        Args:
          prompts: List of prompts to create.

          dry_run: When true, validate and preview changes without persisting them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._post(
            path_template("/v1/org/categories/{category_id}/prompts", category_id=category_id),
            body=await async_maybe_transform(
                {
                    "prompts": prompts,
                    "dry_run": dry_run,
                },
                category_create_prompts_params.CategoryCreatePromptsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryCreatePromptsResponse,
        )

    async def get_category_personas(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryGetCategoryPersonasResponse:
        """
        Get Category Personas

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/personas", category_id=category_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryGetCategoryPersonasResponse,
        )

    async def prompts(
        self,
        category_id: str,
        *,
        analysis_type: List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        order_dir: Literal["asc", "desc"] | Omit = omit,
        persona_id: SequenceNotStr[str] | Omit = omit,
        platform_id: SequenceNotStr[str] | Omit = omit,
        prompt_type: List[Literal["visibility", "sentiment"]] | Omit = omit,
        region_id: SequenceNotStr[str] | Omit = omit,
        status: List[Literal["active", "disabled"]] | Omit = omit,
        tag_id: SequenceNotStr[str] | Omit = omit,
        topic_id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryPromptsResponse:
        """
        Retrieve prompts in a category with optional filtering by type, topic, tag,
        region, platform, or persona. Supports cursor-based pagination.

        Args:
          analysis_type: Filter by analysis type (visibility, sentiment, accuracy).

          cursor: Pagination cursor from a previous response.

          limit: Maximum number of prompts to return.

          order_dir: Sort direction by creation date.

          persona_id: Filter by persona IDs.

          platform_id: Filter by platform IDs.

          prompt_type: Deprecated. Use analysis_type instead.

          region_id: Filter by region IDs.

          status: Filter by prompt status. Defaults to `active` only.

          tag_id: Filter by tag IDs.

          topic_id: Filter by topic IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/prompts", category_id=category_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "analysis_type": analysis_type,
                        "cursor": cursor,
                        "limit": limit,
                        "order_dir": order_dir,
                        "persona_id": persona_id,
                        "platform_id": platform_id,
                        "prompt_type": prompt_type,
                        "region_id": region_id,
                        "status": status,
                        "tag_id": tag_id,
                        "topic_id": topic_id,
                    },
                    category_prompts_params.CategoryPromptsParams,
                ),
            ),
            cast_to=CategoryPromptsResponse,
        )

    async def tags(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryTagsResponse:
        """
        Get the tags for a specific category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/tags", category_id=category_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryTagsResponse,
        )

    async def topics(
        self,
        category_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryTopicsResponse:
        """
        Get the topics for a specific category.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._get(
            path_template("/v1/org/categories/{category_id}/topics", category_id=category_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryTopicsResponse,
        )

    async def update_prompt_status(
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
    ) -> CategoryUpdatePromptStatusResponse:
        """Bulk-update the status of one or more prompts.

        Prompts already in the target
        status are skipped. Use dry_run to preview without persisting.

        Status options:

        - 'active': Prompts will run daily.
        - 'disabled': Prompts will not run moving forward, but historical data is
          preserved.
        - 'deleted': Prompts are deleted along with historical data

        Args:
          prompt_ids: IDs of the prompts to update.

          status: Target status: 'active', 'disabled', or 'deleted'.

          dry_run: When true, validate and preview changes without persisting them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._patch(
            path_template("/v1/org/categories/{category_id}/prompts/status", category_id=category_id),
            body=await async_maybe_transform(
                {
                    "prompt_ids": prompt_ids,
                    "status": status,
                    "dry_run": dry_run,
                },
                category_update_prompt_status_params.CategoryUpdatePromptStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryUpdatePromptStatusResponse,
        )

    async def update_prompts(
        self,
        category_id: str,
        *,
        prompts: Iterable[category_update_prompts_params.Prompt],
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CategoryUpdatePromptsResponse:
        """Update one or more existing prompts.

        Only provided fields are changed. Dimension
        fields (regions, platforms, personas, tags) replace the full set when provided.
        Use dry_run to preview without persisting.

        Args:
          prompts: List of prompt updates. Each entry must include an `id` and at least one field
              to change.

          dry_run: When true, validate and preview changes without persisting them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not category_id:
            raise ValueError(f"Expected a non-empty value for `category_id` but received {category_id!r}")
        return await self._patch(
            path_template("/v1/org/categories/{category_id}/prompts", category_id=category_id),
            body=await async_maybe_transform(
                {
                    "prompts": prompts,
                    "dry_run": dry_run,
                },
                category_update_prompts_params.CategoryUpdatePromptsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CategoryUpdatePromptsResponse,
        )


class CategoriesResourceWithRawResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.list = to_raw_response_wrapper(
            categories.list,
        )
        self.assets = to_raw_response_wrapper(
            categories.assets,
        )
        self.create_prompts = to_raw_response_wrapper(
            categories.create_prompts,
        )
        self.get_category_personas = to_raw_response_wrapper(
            categories.get_category_personas,
        )
        self.prompts = to_raw_response_wrapper(
            categories.prompts,
        )
        self.tags = to_raw_response_wrapper(
            categories.tags,
        )
        self.topics = to_raw_response_wrapper(
            categories.topics,
        )
        self.update_prompt_status = to_raw_response_wrapper(
            categories.update_prompt_status,
        )
        self.update_prompts = to_raw_response_wrapper(
            categories.update_prompts,
        )


class AsyncCategoriesResourceWithRawResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.list = async_to_raw_response_wrapper(
            categories.list,
        )
        self.assets = async_to_raw_response_wrapper(
            categories.assets,
        )
        self.create_prompts = async_to_raw_response_wrapper(
            categories.create_prompts,
        )
        self.get_category_personas = async_to_raw_response_wrapper(
            categories.get_category_personas,
        )
        self.prompts = async_to_raw_response_wrapper(
            categories.prompts,
        )
        self.tags = async_to_raw_response_wrapper(
            categories.tags,
        )
        self.topics = async_to_raw_response_wrapper(
            categories.topics,
        )
        self.update_prompt_status = async_to_raw_response_wrapper(
            categories.update_prompt_status,
        )
        self.update_prompts = async_to_raw_response_wrapper(
            categories.update_prompts,
        )


class CategoriesResourceWithStreamingResponse:
    def __init__(self, categories: CategoriesResource) -> None:
        self._categories = categories

        self.list = to_streamed_response_wrapper(
            categories.list,
        )
        self.assets = to_streamed_response_wrapper(
            categories.assets,
        )
        self.create_prompts = to_streamed_response_wrapper(
            categories.create_prompts,
        )
        self.get_category_personas = to_streamed_response_wrapper(
            categories.get_category_personas,
        )
        self.prompts = to_streamed_response_wrapper(
            categories.prompts,
        )
        self.tags = to_streamed_response_wrapper(
            categories.tags,
        )
        self.topics = to_streamed_response_wrapper(
            categories.topics,
        )
        self.update_prompt_status = to_streamed_response_wrapper(
            categories.update_prompt_status,
        )
        self.update_prompts = to_streamed_response_wrapper(
            categories.update_prompts,
        )


class AsyncCategoriesResourceWithStreamingResponse:
    def __init__(self, categories: AsyncCategoriesResource) -> None:
        self._categories = categories

        self.list = async_to_streamed_response_wrapper(
            categories.list,
        )
        self.assets = async_to_streamed_response_wrapper(
            categories.assets,
        )
        self.create_prompts = async_to_streamed_response_wrapper(
            categories.create_prompts,
        )
        self.get_category_personas = async_to_streamed_response_wrapper(
            categories.get_category_personas,
        )
        self.prompts = async_to_streamed_response_wrapper(
            categories.prompts,
        )
        self.tags = async_to_streamed_response_wrapper(
            categories.tags,
        )
        self.topics = async_to_streamed_response_wrapper(
            categories.topics,
        )
        self.update_prompt_status = async_to_streamed_response_wrapper(
            categories.update_prompt_status,
        )
        self.update_prompts = async_to_streamed_response_wrapper(
            categories.update_prompts,
        )
