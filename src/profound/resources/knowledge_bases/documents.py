# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast

import httpx

from ..._files import deepcopy_with_paths
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.knowledge_bases import document_create_params, document_delete_params, document_update_params
from ...types.knowledge_bases.document_create_response import DocumentCreateResponse
from ...types.knowledge_bases.document_delete_response import DocumentDeleteResponse
from ...types.knowledge_bases.document_update_response import DocumentUpdateResponse

__all__ = ["DocumentsResource", "AsyncDocumentsResource"]


class DocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return DocumentsResourceWithStreamingResponse(self)

    def create(
        self,
        knowledge_base_id: str,
        *,
        name: str,
        text: str,
        organization_id: Optional[str] | Omit = omit,
        folder: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateResponse:
        """
        Add a document to a knowledge base using JSON text or multipart file upload.

        Args:
          knowledge_base_id: Unique knowledge base ID.

          name: Unique document name.

          text: Text content to add to the document.

          organization_id: Organization scope for API keys that can access multiple organizations.

          folder: Folder path to add the document under.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        body = deepcopy_with_paths(
            {
                "name": name,
                "text": text,
                "folder": folder,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/v1/knowledge-bases/{knowledge_base_id}/documents", knowledge_base_id=knowledge_base_id),
            body=maybe_transform(body, document_create_params.DocumentCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, document_create_params.DocumentCreateParams
                ),
            ),
            cast_to=DocumentCreateResponse,
        )

    def update(
        self,
        knowledge_base_id: str,
        *,
        name: str,
        text: str,
        organization_id: Optional[str] | Omit = omit,
        folder: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateResponse:
        """
        Overwrite a knowledge base document using JSON text or multipart file upload.

        Args:
          knowledge_base_id: Unique knowledge base ID.

          name: Document name or path to update.

          text: Replacement text content for the document.

          organization_id: Organization scope for API keys that can access multiple organizations.

          folder: Folder path containing the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        body = deepcopy_with_paths(
            {
                "name": name,
                "text": text,
                "folder": folder,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            path_template("/v1/knowledge-bases/{knowledge_base_id}/documents", knowledge_base_id=knowledge_base_id),
            body=maybe_transform(body, document_update_params.DocumentUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, document_update_params.DocumentUpdateParams
                ),
            ),
            cast_to=DocumentUpdateResponse,
        )

    def delete(
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
    ) -> DocumentDeleteResponse:
        """
        Delete an existing document from a knowledge base.

        Args:
          knowledge_base_id: Unique knowledge base ID.

          name: Document path to delete.

          organization_id: Organization scope for API keys that can access multiple organizations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._delete(
            path_template("/v1/knowledge-bases/{knowledge_base_id}/documents", knowledge_base_id=knowledge_base_id),
            body=maybe_transform({"name": name}, document_delete_params.DocumentDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, document_delete_params.DocumentDeleteParams
                ),
            ),
            cast_to=DocumentDeleteResponse,
        )


class AsyncDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncDocumentsResourceWithStreamingResponse(self)

    async def create(
        self,
        knowledge_base_id: str,
        *,
        name: str,
        text: str,
        organization_id: Optional[str] | Omit = omit,
        folder: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateResponse:
        """
        Add a document to a knowledge base using JSON text or multipart file upload.

        Args:
          knowledge_base_id: Unique knowledge base ID.

          name: Unique document name.

          text: Text content to add to the document.

          organization_id: Organization scope for API keys that can access multiple organizations.

          folder: Folder path to add the document under.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        body = deepcopy_with_paths(
            {
                "name": name,
                "text": text,
                "folder": folder,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/v1/knowledge-bases/{knowledge_base_id}/documents", knowledge_base_id=knowledge_base_id),
            body=await async_maybe_transform(body, document_create_params.DocumentCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, document_create_params.DocumentCreateParams
                ),
            ),
            cast_to=DocumentCreateResponse,
        )

    async def update(
        self,
        knowledge_base_id: str,
        *,
        name: str,
        text: str,
        organization_id: Optional[str] | Omit = omit,
        folder: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateResponse:
        """
        Overwrite a knowledge base document using JSON text or multipart file upload.

        Args:
          knowledge_base_id: Unique knowledge base ID.

          name: Document name or path to update.

          text: Replacement text content for the document.

          organization_id: Organization scope for API keys that can access multiple organizations.

          folder: Folder path containing the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        body = deepcopy_with_paths(
            {
                "name": name,
                "text": text,
                "folder": folder,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            path_template("/v1/knowledge-bases/{knowledge_base_id}/documents", knowledge_base_id=knowledge_base_id),
            body=await async_maybe_transform(body, document_update_params.DocumentUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, document_update_params.DocumentUpdateParams
                ),
            ),
            cast_to=DocumentUpdateResponse,
        )

    async def delete(
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
    ) -> DocumentDeleteResponse:
        """
        Delete an existing document from a knowledge base.

        Args:
          knowledge_base_id: Unique knowledge base ID.

          name: Document path to delete.

          organization_id: Organization scope for API keys that can access multiple organizations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._delete(
            path_template("/v1/knowledge-bases/{knowledge_base_id}/documents", knowledge_base_id=knowledge_base_id),
            body=await async_maybe_transform({"name": name}, document_delete_params.DocumentDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, document_delete_params.DocumentDeleteParams
                ),
            ),
            cast_to=DocumentDeleteResponse,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create = to_raw_response_wrapper(
            documents.create,
        )
        self.update = to_raw_response_wrapper(
            documents.update,
        )
        self.delete = to_raw_response_wrapper(
            documents.delete,
        )


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create = async_to_raw_response_wrapper(
            documents.create,
        )
        self.update = async_to_raw_response_wrapper(
            documents.update,
        )
        self.delete = async_to_raw_response_wrapper(
            documents.delete,
        )


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create = to_streamed_response_wrapper(
            documents.create,
        )
        self.update = to_streamed_response_wrapper(
            documents.update,
        )
        self.delete = to_streamed_response_wrapper(
            documents.delete,
        )


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create = async_to_streamed_response_wrapper(
            documents.create,
        )
        self.update = async_to_streamed_response_wrapper(
            documents.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            documents.delete,
        )
