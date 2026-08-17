# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional

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
from .documents import (
    DocumentsResource,
    AsyncDocumentsResource,
    DocumentsResourceWithRawResponse,
    AsyncDocumentsResourceWithRawResponse,
    DocumentsResourceWithStreamingResponse,
    AsyncDocumentsResourceWithStreamingResponse,
)
from .folders import (
    FoldersResource,
    AsyncFoldersResource,
    FoldersResourceWithRawResponse,
    AsyncFoldersResourceWithRawResponse,
    FoldersResourceWithStreamingResponse,
    AsyncFoldersResourceWithStreamingResponse,
)
from ...types.knowledge_base_list_response import KnowledgeBaseListResponse, KnowledgeBaseItem
from ...types import knowledge_base_list_params
from ...types.knowledge_base_search_response import KnowledgeBaseSearchResponse, KnowledgeBaseSearchResult, Metadata
from ...types import knowledge_base_search_params

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
        return KnowledgeBasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgeBasesResourceWithStreamingResponse:
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
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            KnowledgeBaseListResponse: Successful Response
        
        Example:
            ```python
            knowledge_base = client.knowledge_bases.list()
            ```
        """
        return self._get(
            "/v1/knowledge-bases",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"organization_id": organization_id}, knowledge_base_list_params.KnowledgeBaseListParams)),
            cast_to=KnowledgeBaseListResponse,
        )

    def search(
        self,
        knowledge_base_id: str,
        *,
        query: str,
        top_k: int,
        return_full_page: bool | Omit = omit,
        filters: Optional[knowledge_base_search_params.Filters] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
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
            return_full_page: Return full page content instead of snippets.
            filters: Optional search filters.
            organization_id: Organization scope for API keys that can access multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            KnowledgeBaseSearchResponse: Successful Response
        
        Example:
            ```python
            knowledge_base = client.knowledge_bases.search(
                knowledge_base_id="knowledgeBaseId",
                query="",
                top_k=0,
                return_full_page=False,
            )
            ```
        """
        if knowledge_base_id is None or (isinstance(knowledge_base_id, str) and not knowledge_base_id):
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._post(
            path_template("/v1/knowledge-bases/{knowledge_base_id}/search", **{"knowledge_base_id": knowledge_base_id}),
            body=maybe_transform(
            {
            "query": query,
            "top_k": top_k,
            "return_full_page": return_full_page,
            "filters": filters,
        },
            knowledge_base_search_params.KnowledgeBaseSearchParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"organization_id": organization_id}, knowledge_base_search_params.KnowledgeBaseSearchParams)),
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
        return AsyncKnowledgeBasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowledgeBasesResourceWithStreamingResponse:
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
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            KnowledgeBaseListResponse: Successful Response
        
        Example:
            ```python
            knowledge_base = await client.knowledge_bases.list()
            ```
        """
        return await self._get(
            "/v1/knowledge-bases",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"organization_id": organization_id}, knowledge_base_list_params.KnowledgeBaseListParams)),
            cast_to=KnowledgeBaseListResponse,
        )

    async def search(
        self,
        knowledge_base_id: str,
        *,
        query: str,
        top_k: int,
        return_full_page: bool | Omit = omit,
        filters: Optional[knowledge_base_search_params.Filters] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
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
            return_full_page: Return full page content instead of snippets.
            filters: Optional search filters.
            organization_id: Organization scope for API keys that can access multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            KnowledgeBaseSearchResponse: Successful Response
        
        Example:
            ```python
            knowledge_base = await client.knowledge_bases.search(
                knowledge_base_id="knowledgeBaseId",
                query="",
                top_k=0,
                return_full_page=False,
            )
            ```
        """
        if knowledge_base_id is None or (isinstance(knowledge_base_id, str) and not knowledge_base_id):
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._post(
            path_template("/v1/knowledge-bases/{knowledge_base_id}/search", **{"knowledge_base_id": knowledge_base_id}),
            body=await async_maybe_transform(
            {
            "query": query,
            "top_k": top_k,
            "return_full_page": return_full_page,
            "filters": filters,
        },
            knowledge_base_search_params.KnowledgeBaseSearchParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"organization_id": organization_id}, knowledge_base_search_params.KnowledgeBaseSearchParams)),
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
