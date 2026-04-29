# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import knowledge_base_list_params, knowledge_base_search_params
from .folders import (
    FoldersResource,
    AsyncFoldersResource,
    FoldersResourceWithRawResponse,
    AsyncFoldersResourceWithRawResponse,
    FoldersResourceWithStreamingResponse,
    AsyncFoldersResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .documents import (
    DocumentsResource,
    AsyncDocumentsResource,
    DocumentsResourceWithRawResponse,
    AsyncDocumentsResourceWithRawResponse,
    DocumentsResourceWithStreamingResponse,
    AsyncDocumentsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.knowledge_base_list_response import KnowledgeBaseListResponse
from ...types.knowledge_base_search_response import KnowledgeBaseSearchResponse

__all__ = ["KnowledgeBasesResource", "AsyncKnowledgeBasesResource"]


class KnowledgeBasesResource(SyncAPIResource):
    @cached_property
    def documents(self) -> DocumentsResource:
        return DocumentsResource(self._client)

    @cached_property
    def folders(self) -> FoldersResource:
        return FoldersResource(self._client)

    @cached_property
    def with_raw_response(self) -> KnowledgeBasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return KnowledgeBasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgeBasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return KnowledgeBasesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseListResponse:
        """
        List knowledge bases accessible to the API key.

        Args:
          organization_id: Organization scope for API keys that can access multiple organizations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/knowledge-bases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, knowledge_base_list_params.KnowledgeBaseListParams
                ),
            ),
            cast_to=KnowledgeBaseListResponse,
        )

    def search(
        self,
        knowledge_base_id: str,
        *,
        query: str,
        top_k: int,
        organization_id: Optional[str] | Omit = omit,
        filters: Optional[knowledge_base_search_params.Filters] | Omit = omit,
        return_full_page: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseSearchResponse:
        """
        Search a knowledge base and return matching snippets or pages.

        Args:
          knowledge_base_id: Unique knowledge base ID.

          query: Search query.

          top_k: Maximum number of results to return.

          organization_id: Organization scope for API keys that can access multiple organizations.

          filters: Optional search filters.

          return_full_page: Return full page content instead of snippets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._post(
            path_template("/v1/knowledge-bases/{knowledge_base_id}/search", knowledge_base_id=knowledge_base_id),
            body=maybe_transform(
                {
                    "query": query,
                    "top_k": top_k,
                    "filters": filters,
                    "return_full_page": return_full_page,
                },
                knowledge_base_search_params.KnowledgeBaseSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, knowledge_base_search_params.KnowledgeBaseSearchParams
                ),
            ),
            cast_to=KnowledgeBaseSearchResponse,
        )


class AsyncKnowledgeBasesResource(AsyncAPIResource):
    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        return AsyncDocumentsResource(self._client)

    @cached_property
    def folders(self) -> AsyncFoldersResource:
        return AsyncFoldersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKnowledgeBasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowledgeBasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowledgeBasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncKnowledgeBasesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseListResponse:
        """
        List knowledge bases accessible to the API key.

        Args:
          organization_id: Organization scope for API keys that can access multiple organizations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/knowledge-bases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, knowledge_base_list_params.KnowledgeBaseListParams
                ),
            ),
            cast_to=KnowledgeBaseListResponse,
        )

    async def search(
        self,
        knowledge_base_id: str,
        *,
        query: str,
        top_k: int,
        organization_id: Optional[str] | Omit = omit,
        filters: Optional[knowledge_base_search_params.Filters] | Omit = omit,
        return_full_page: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseSearchResponse:
        """
        Search a knowledge base and return matching snippets or pages.

        Args:
          knowledge_base_id: Unique knowledge base ID.

          query: Search query.

          top_k: Maximum number of results to return.

          organization_id: Organization scope for API keys that can access multiple organizations.

          filters: Optional search filters.

          return_full_page: Return full page content instead of snippets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._post(
            path_template("/v1/knowledge-bases/{knowledge_base_id}/search", knowledge_base_id=knowledge_base_id),
            body=await async_maybe_transform(
                {
                    "query": query,
                    "top_k": top_k,
                    "filters": filters,
                    "return_full_page": return_full_page,
                },
                knowledge_base_search_params.KnowledgeBaseSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, knowledge_base_search_params.KnowledgeBaseSearchParams
                ),
            ),
            cast_to=KnowledgeBaseSearchResponse,
        )


class KnowledgeBasesResourceWithRawResponse:
    def __init__(self, knowledge_bases: KnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.list = to_raw_response_wrapper(
            knowledge_bases.list,
        )
        self.search = to_raw_response_wrapper(
            knowledge_bases.search,
        )

    @cached_property
    def documents(self) -> DocumentsResourceWithRawResponse:
        return DocumentsResourceWithRawResponse(self._knowledge_bases.documents)

    @cached_property
    def folders(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self._knowledge_bases.folders)


class AsyncKnowledgeBasesResourceWithRawResponse:
    def __init__(self, knowledge_bases: AsyncKnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.list = async_to_raw_response_wrapper(
            knowledge_bases.list,
        )
        self.search = async_to_raw_response_wrapper(
            knowledge_bases.search,
        )

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithRawResponse:
        return AsyncDocumentsResourceWithRawResponse(self._knowledge_bases.documents)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self._knowledge_bases.folders)


class KnowledgeBasesResourceWithStreamingResponse:
    def __init__(self, knowledge_bases: KnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.list = to_streamed_response_wrapper(
            knowledge_bases.list,
        )
        self.search = to_streamed_response_wrapper(
            knowledge_bases.search,
        )

    @cached_property
    def documents(self) -> DocumentsResourceWithStreamingResponse:
        return DocumentsResourceWithStreamingResponse(self._knowledge_bases.documents)

    @cached_property
    def folders(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self._knowledge_bases.folders)


class AsyncKnowledgeBasesResourceWithStreamingResponse:
    def __init__(self, knowledge_bases: AsyncKnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.list = async_to_streamed_response_wrapper(
            knowledge_bases.list,
        )
        self.search = async_to_streamed_response_wrapper(
            knowledge_bases.search,
        )

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithStreamingResponse:
        return AsyncDocumentsResourceWithStreamingResponse(self._knowledge_bases.documents)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self._knowledge_bases.folders)
