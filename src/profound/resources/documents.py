# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import document_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.document_create_response import DocumentCreateResponse

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
        *,
        id: str,
        content_markdown: str,
        name: str,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateResponse:
        """
        Create a Profound document with markdown content.

        `organization_id` is required and you must be a member of it. You choose the
        document's `id`, and creation is idempotent on it: repeating the request returns
        the existing document rather than creating a second one.

        New documents are visible only to their creator; share them from the Profound
        app, or open one with the `url` in the response.

        A `201` response does not confirm that a new document was created: it is also
        returned when `id` already existed, in which case the existing document comes
        back unchanged. Upstream gives no signal to tell the two apart, so this endpoint
        does not claim to either — it is safe to retry with the same `id` either way.

        Args:
          id:
              ID for the new document, chosen by you. Creation is idempotent on this ID:
              repeating a request with the same ID returns the existing document instead of
              creating a second one, so a retry after a network error is safe.

          content_markdown: Initial document body as markdown. Must be non-empty. Rendered into the
              collaborative editor, so the result is real editable content, not a stored blob.

          name: Title for the document. Must be non-empty.

          organization_id: ID of the organization that will own the document. Required — Profound API keys
              are user-scoped, so the owning organization must be chosen explicitly. The
              caller must be a member of this organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/documents",
            body=maybe_transform(
                {
                    "id": id,
                    "content_markdown": content_markdown,
                    "name": name,
                    "organization_id": organization_id,
                },
                document_create_params.DocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCreateResponse,
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
        *,
        id: str,
        content_markdown: str,
        name: str,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateResponse:
        """
        Create a Profound document with markdown content.

        `organization_id` is required and you must be a member of it. You choose the
        document's `id`, and creation is idempotent on it: repeating the request returns
        the existing document rather than creating a second one.

        New documents are visible only to their creator; share them from the Profound
        app, or open one with the `url` in the response.

        A `201` response does not confirm that a new document was created: it is also
        returned when `id` already existed, in which case the existing document comes
        back unchanged. Upstream gives no signal to tell the two apart, so this endpoint
        does not claim to either — it is safe to retry with the same `id` either way.

        Args:
          id:
              ID for the new document, chosen by you. Creation is idempotent on this ID:
              repeating a request with the same ID returns the existing document instead of
              creating a second one, so a retry after a network error is safe.

          content_markdown: Initial document body as markdown. Must be non-empty. Rendered into the
              collaborative editor, so the result is real editable content, not a stored blob.

          name: Title for the document. Must be non-empty.

          organization_id: ID of the organization that will own the document. Required — Profound API keys
              are user-scoped, so the owning organization must be chosen explicitly. The
              caller must be a member of this organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/documents",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "content_markdown": content_markdown,
                    "name": name,
                    "organization_id": organization_id,
                },
                document_create_params.DocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCreateResponse,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create = to_raw_response_wrapper(
            documents.create,
        )


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create = async_to_raw_response_wrapper(
            documents.create,
        )


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create = to_streamed_response_wrapper(
            documents.create,
        )


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create = async_to_streamed_response_wrapper(
            documents.create,
        )
