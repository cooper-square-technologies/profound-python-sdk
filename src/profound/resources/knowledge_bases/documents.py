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
from ...types.shared.document_operation_response import DocumentOperationResponse
from ...types.knowledge_bases import (
    document_create_v1_id_post_params,
    document_update_v1_id_put_params,
    document_delete_v1_id_delete_params,
)

__all__ = ["DocumentsResource", "AsyncDocumentsResource"]


class DocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsResourceWithRawResponse:
        return DocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsResourceWithStreamingResponse:
        return DocumentsResourceWithStreamingResponse(self)

    def create_v1_id_post(
        self,
        knowledge_base_id: str,
        *,
        name: str,
        text: str,
        folder: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentOperationResponse:
        """
        Add a document to a knowledge base using JSON text or multipart file upload.

        Args:
            knowledge_base_id: Unique knowledge base ID.
            name: Unique document name.
            text: Text content to add to the document.
            folder: Folder path to add the document under.
            organization_id: Organization scope for API keys that can access multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DocumentOperationResponse: Successful Response

        Example:
            ```python
            document = client.knowledge_bases.documents.create_v1_id_post(
                knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
                text="x",
            )
            ```
        """
        if knowledge_base_id is None or (isinstance(knowledge_base_id, str) and not knowledge_base_id):
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._post(
            path_template(
                "/v1/knowledge-bases/{knowledge_base_id}/documents", **{"knowledge_base_id": knowledge_base_id}
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "text": text,
                    "folder": folder,
                },
                document_create_v1_id_post_params.DocumentCreateV1IDPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, document_create_v1_id_post_params.DocumentCreateV1IDPostParams
                ),
            ),
            cast_to=DocumentOperationResponse,
        )

    def update_v1_id_put(
        self,
        knowledge_base_id: str,
        *,
        name: str,
        text: str,
        folder: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentOperationResponse:
        """
        Overwrite a knowledge base document using JSON text or multipart file upload.

        Args:
            knowledge_base_id: Unique knowledge base ID.
            name: Document name or path to update.
            text: Replacement text content for the document.
            folder: Folder path containing the document.
            organization_id: Organization scope for API keys that can access multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DocumentOperationResponse: Successful Response

        Example:
            ```python
            document = client.knowledge_bases.documents.update_v1_id_put(
                knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
                text="x",
            )
            ```
        """
        if knowledge_base_id is None or (isinstance(knowledge_base_id, str) and not knowledge_base_id):
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._put(
            path_template(
                "/v1/knowledge-bases/{knowledge_base_id}/documents", **{"knowledge_base_id": knowledge_base_id}
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "text": text,
                    "folder": folder,
                },
                document_update_v1_id_put_params.DocumentUpdateV1IDPutParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, document_update_v1_id_put_params.DocumentUpdateV1IDPutParams
                ),
            ),
            cast_to=DocumentOperationResponse,
        )

    def delete_v1_id_delete(
        self,
        knowledge_base_id: str,
        *,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentOperationResponse:
        """
        Delete an existing document from a knowledge base.

        Args:
            knowledge_base_id: Unique knowledge base ID.
            name: Document path to delete.
            organization_id: Organization scope for API keys that can access multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DocumentOperationResponse: Successful Response

        Example:
            ```python
            document = client.knowledge_bases.documents.delete_v1_id_delete(
                knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
            )
            ```
        """
        if knowledge_base_id is None or (isinstance(knowledge_base_id, str) and not knowledge_base_id):
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._delete(
            path_template(
                "/v1/knowledge-bases/{knowledge_base_id}/documents", **{"knowledge_base_id": knowledge_base_id}
            ),
            body=maybe_transform(
                {"name": name},
                document_delete_v1_id_delete_params.DocumentDeleteV1IDDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id},
                    document_delete_v1_id_delete_params.DocumentDeleteV1IDDeleteParams,
                ),
            ),
            cast_to=DocumentOperationResponse,
        )


class AsyncDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsResourceWithRawResponse:
        return AsyncDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsResourceWithStreamingResponse:
        return AsyncDocumentsResourceWithStreamingResponse(self)

    async def create_v1_id_post(
        self,
        knowledge_base_id: str,
        *,
        name: str,
        text: str,
        folder: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentOperationResponse:
        """
        Add a document to a knowledge base using JSON text or multipart file upload.

        Args:
            knowledge_base_id: Unique knowledge base ID.
            name: Unique document name.
            text: Text content to add to the document.
            folder: Folder path to add the document under.
            organization_id: Organization scope for API keys that can access multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DocumentOperationResponse: Successful Response

        Example:
            ```python
            document = await client.knowledge_bases.documents.create_v1_id_post(
                knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
                text="x",
            )
            ```
        """
        if knowledge_base_id is None or (isinstance(knowledge_base_id, str) and not knowledge_base_id):
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._post(
            path_template(
                "/v1/knowledge-bases/{knowledge_base_id}/documents", **{"knowledge_base_id": knowledge_base_id}
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "text": text,
                    "folder": folder,
                },
                document_create_v1_id_post_params.DocumentCreateV1IDPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, document_create_v1_id_post_params.DocumentCreateV1IDPostParams
                ),
            ),
            cast_to=DocumentOperationResponse,
        )

    async def update_v1_id_put(
        self,
        knowledge_base_id: str,
        *,
        name: str,
        text: str,
        folder: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentOperationResponse:
        """
        Overwrite a knowledge base document using JSON text or multipart file upload.

        Args:
            knowledge_base_id: Unique knowledge base ID.
            name: Document name or path to update.
            text: Replacement text content for the document.
            folder: Folder path containing the document.
            organization_id: Organization scope for API keys that can access multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DocumentOperationResponse: Successful Response

        Example:
            ```python
            document = await client.knowledge_bases.documents.update_v1_id_put(
                knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
                text="x",
            )
            ```
        """
        if knowledge_base_id is None or (isinstance(knowledge_base_id, str) and not knowledge_base_id):
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._put(
            path_template(
                "/v1/knowledge-bases/{knowledge_base_id}/documents", **{"knowledge_base_id": knowledge_base_id}
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "text": text,
                    "folder": folder,
                },
                document_update_v1_id_put_params.DocumentUpdateV1IDPutParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, document_update_v1_id_put_params.DocumentUpdateV1IDPutParams
                ),
            ),
            cast_to=DocumentOperationResponse,
        )

    async def delete_v1_id_delete(
        self,
        knowledge_base_id: str,
        *,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentOperationResponse:
        """
        Delete an existing document from a knowledge base.

        Args:
            knowledge_base_id: Unique knowledge base ID.
            name: Document path to delete.
            organization_id: Organization scope for API keys that can access multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DocumentOperationResponse: Successful Response

        Example:
            ```python
            document = await client.knowledge_bases.documents.delete_v1_id_delete(
                knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="x",
            )
            ```
        """
        if knowledge_base_id is None or (isinstance(knowledge_base_id, str) and not knowledge_base_id):
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._delete(
            path_template(
                "/v1/knowledge-bases/{knowledge_base_id}/documents", **{"knowledge_base_id": knowledge_base_id}
            ),
            body=await async_maybe_transform(
                {"name": name},
                document_delete_v1_id_delete_params.DocumentDeleteV1IDDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id},
                    document_delete_v1_id_delete_params.DocumentDeleteV1IDDeleteParams,
                ),
            ),
            cast_to=DocumentOperationResponse,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create_v1_id_post = to_raw_response_wrapper(
            documents.create_v1_id_post,
        )
        self.update_v1_id_put = to_raw_response_wrapper(
            documents.update_v1_id_put,
        )
        self.delete_v1_id_delete = to_raw_response_wrapper(
            documents.delete_v1_id_delete,
        )


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create_v1_id_post = async_to_raw_response_wrapper(
            documents.create_v1_id_post,
        )
        self.update_v1_id_put = async_to_raw_response_wrapper(
            documents.update_v1_id_put,
        )
        self.delete_v1_id_delete = async_to_raw_response_wrapper(
            documents.delete_v1_id_delete,
        )


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create_v1_id_post = to_streamed_response_wrapper(
            documents.create_v1_id_post,
        )
        self.update_v1_id_put = to_streamed_response_wrapper(
            documents.update_v1_id_put,
        )
        self.delete_v1_id_delete = to_streamed_response_wrapper(
            documents.delete_v1_id_delete,
        )


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create_v1_id_post = async_to_streamed_response_wrapper(
            documents.create_v1_id_post,
        )
        self.update_v1_id_put = async_to_streamed_response_wrapper(
            documents.update_v1_id_put,
        )
        self.delete_v1_id_delete = async_to_streamed_response_wrapper(
            documents.delete_v1_id_delete,
        )
