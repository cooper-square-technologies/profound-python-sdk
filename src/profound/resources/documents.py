# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    document_list_params,
    document_create_params,
    document_delete_params,
    document_update_params,
    document_retrieve_params,
    document_replace_content_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.document_list_response import DocumentListResponse
from ..types.document_create_response import DocumentCreateResponse
from ..types.document_update_response import DocumentUpdateResponse
from ..types.document_retrieve_response import DocumentRetrieveResponse
from ..types.document_replace_content_response import DocumentReplaceContentResponse

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

    def retrieve(
        self,
        document_id: str,
        *,
        organization_id: str,
        include_comments: bool | Omit = omit,
        include_tabs: bool | Omit = omit,
        preview: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentRetrieveResponse:
        """
        Read a document: its metadata, its default tab's body, its other tabs, its
        comments, and its version hash.

        You can read any document you have access to in the Profound app, including ones
        created there rather than through this API.

        By default this is a preview: the body is truncated to save your context, and
        the version hash is withheld so a preview alone can never be used to replace a
        document blindly. Pass `preview=false` when you intend to write.

        Args:
          document_id: ID of the document.

          organization_id: ID of the organization that owns the document. Required — Profound API keys are
              user-scoped, so the owning organization must be named explicitly. The caller
              must be a member of this organization.

          include_comments: Include the document's review comments, each mapped to `{content, context}`. On
              by default — a comment is part of the document's review state, not an aside.
              Turn it off to skip the comment-thread walk upstream; off, `comments` is omitted
              from the response rather than returned as an empty list.

          include_tabs: Include the document's other tabs. On by default — a tab body is part of the
              document, not an aside. Off, `additional_tabs` is omitted from the response
              rather than returned as an empty list.

          preview: Bound every body in the response — `content_markdown` and each tab's — and set
              `content_truncated` if any was cut. On by default. Upstream has no partial-read
              of its own — every read is a full round trip through the collaborative editor —
              so this saves your context, not upstream cost. A preview read also omits
              `version_hash`, on purpose: a hash returned next to a body you have not fully
              seen invites replacing content you never read. Pass `preview=false` before you
              intend to write, to get the whole body, `content_truncated: false`, and the
              hash.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            path_template("/v1/documents/{document_id}", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "include_comments": include_comments,
                        "include_tabs": include_tabs,
                        "preview": preview,
                    },
                    document_retrieve_params.DocumentRetrieveParams,
                ),
            ),
            cast_to=DocumentRetrieveResponse,
        )

    def update(
        self,
        document_id: str,
        *,
        organization_id: str,
        name: Optional[str] | Omit = omit,
        visibility: Optional[Literal["invited_only", "organization"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateResponse:
        """
        Rename a document, change who can see it, or both in one call.

        Renaming sets a permanent lock on the title, and changing visibility can
        silently change who has access — see the `name` and `visibility` field
        descriptions for what each one does before you use it.

        Renaming needs edit access; changing visibility is creator-only, and upstream
        enforces it. You can act on a document this API created, or one you created
        yourself in the Profound app — not one merely shared with you.

        Args:
          document_id: ID of the document.

          organization_id: ID of the organization that owns the document. Required — Profound API keys are
              user-scoped, so the owning organization must be named explicitly. The caller
              must be a member of this organization.

          name: New title for the document. Renaming sets a permanent lock: once a document is
              renamed through this route, its title stops following the first heading of its
              content, for the rest of the document's life, and no route can undo the lock.
              Omit to leave the title as it is.

          visibility: New sharing scope: `invited_only` for only the people invited to the document,
              or `organization` for everyone in the owning organization. Only the document's
              creator can change this; omit to leave sharing as it is. Three things worth
              knowing before you set it: `organization` visibility grants view only — there is
              no value here that grants the organization edit access. Setting `invited_only`
              removes the organization's access entirely. And re-asserting `organization` on a
              document whose organization grant is already `edit` silently downgrades the
              whole organization to view — upstream replays the access sync whenever this
              field is sent, and that sync always upserts view, even when the value you sent
              matches the one already stored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._patch(
            path_template("/v1/documents/{document_id}", document_id=document_id),
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "name": name,
                    "visibility": visibility,
                },
                document_update_params.DocumentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateResponse,
        )

    def list(
        self,
        *,
        organization_id: str,
        limit: int | Omit = omit,
        next_cursor: Optional[str] | Omit = omit,
        q: Optional[str] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentListResponse:
        """
        List documents visible to your organization, newest-modified-first.

        Documents are ordered by last-modified time, most recent first, with no other
        sort option. This is a walk over a live, mutable collection: a document created
        or modified while you are paging can shift which page it lands on, so a single
        walk may show it to you twice or, rarely, skip it.

        This response never includes a total count. Upstream counts totals before
        applying your organization's access filter, so a total, or treating a short page
        as the last one, would misreport what you can actually see. Keep following
        `pagination.next_cursor` until it comes back null — that, and not a short or
        even an empty page, is the end of the walk. A page whose rows the access filter
        removed entirely is empty while later pages still hold documents, so the last
        page of a walk may legitimately be an empty one.

        Args:
          organization_id: ID of the organization whose documents to list. Required. The caller must be a
              member of this organization.

          q: Filter to documents whose name contains this text, case-insensitively. Matches
              only the document's name, never its content — a query that finds nothing does
              not mean the topic is unwritten, only that no title mentions it. Blank or
              omitted returns every document. Ignored when sent alongside `next_cursor`, which
              carries the filter the walk started with. Matching is name-only as of this
              release; broader matching may follow if upstream changes how it indexes the name
              column.

          sort: Documents are always ordered newest-modified-first (`updated_at DESC`, then
              `created_at DESC`, then `id DESC`); there is no parameter that changes this.
              `recency` is the only accepted value, and passing it is a no-op that names the
              guarantee rather than altering it — any other value is rejected outright rather
              than silently ignored. Ordering is never re-applied to a returned page either:
              that would only be consistent within the page, not across a paginated walk.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/documents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "limit": limit,
                        "next_cursor": next_cursor,
                        "q": q,
                        "sort": sort,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            cast_to=DocumentListResponse,
        )

    def delete(
        self,
        document_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a document created through this integration.

        Only documents created through this integration can be deleted here. A document
        created in the Profound app can never be deleted through this route, even by the
        person who owns it — creation provenance is stamped once, at creation, and is
        never backfilled onto documents made another way.

        The delete is soft: the row is marked deleted at the storage layer rather than
        destroyed. There is no restore through this API, or any other — treat a delete
        as final even though the data itself is not gone.

        A 404 means the document is not visible to you at all. It covers three cases the
        response does not distinguish, on purpose: the document never existed, it was
        already deleted by an earlier call to this same route, or it exists but your
        credential resolves no role on it. Deleting the same document twice returns 404
        on the second call, not a second 204.

        A 403 means the opposite: the document is visible to you but not deletable here,
        and the message says which rule refused — it was not created through this
        integration, or you are not its creator. Deleting is creator-only, so edit
        access is not enough to remove a document out from under its owner.

        Args:
          document_id: ID of the document.

          organization_id: ID of the organization that owns the document. You must be a member of it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/documents/{document_id}", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"organization_id": organization_id}, document_delete_params.DocumentDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    def replace_content(
        self,
        document_id: str,
        *,
        content_markdown: str,
        organization_id: str,
        skip_title_sync: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentReplaceContentResponse:
        """
        Overwrite a document's entire body with new markdown, replacing what it held
        before.

        This is a whole-body replace, not a patch: send the complete new text every
        time. An empty `content_markdown` is valid and clears the document.

        Two destructive side effects apply on every call, regardless of what you send:

        - The document collapses to its default tab. Every non-default tab is deleted,
          and the comments map is cleared for **all** tabs, including the default one —
          a document with a live comment thread on any tab loses it.
        - `skip_title_sync` defaults to `false`, matching the Profound app: the title
          follows the new content's first heading, so a replace silently renames the
          document unless the heading matches the current title or `skip_title_sync` is
          set.

        There is no compare-and-swap: this call does not accept a precondition, and
        nothing stops two concurrent replaces from silently overwriting each other
        last-writer-wins. Upstream's own `version_hash` documentation says as much — the
        token is "still a change detector rather than a precondition: a caller must not
        treat a matching token as licence to overwrite blindly, because it names the
        room at a moment cortex observed and not the moment its own write lands."
        Sending a `working_version_hash` (or any spelling of it) is rejected with a
        `400` naming this rather than accepted and silently discarded, which is what
        happens on the upstream route this wraps.

        You can replace a document this API created, or one you created yourself
        directly — not merely one shared with you.

        Args:
          document_id: ID of the document.

          content_markdown: New markdown body for the document, replacing everything it held before. An
              empty string is valid and clears the document — nothing else warns you before
              that happens, so treat sending one as deliberate. Whole-body replace only: send
              the complete new text, not just the part that changed. Capped at 1,000,000
              bytes; the upstream router separately caps the entire request at 2 MiB, so a
              body near this cap can still be refused in transit rather than by this field.

          organization_id: ID of the organization that owns the document. Required — Profound API keys are
              user-scoped, so the owning organization must be chosen explicitly. The caller
              must be a member of this organization.

          skip_title_sync: Off by default, matching the Profound app: the document's title follows the new
              content's first heading, so a replace silently renames the document whenever
              that heading differs from the current title. Set true to keep the current title
              regardless of what the new content's first heading says.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._post(
            path_template("/v1/documents/{document_id}/content", document_id=document_id),
            body=maybe_transform(
                {
                    "content_markdown": content_markdown,
                    "organization_id": organization_id,
                    "skip_title_sync": skip_title_sync,
                },
                document_replace_content_params.DocumentReplaceContentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentReplaceContentResponse,
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

    async def retrieve(
        self,
        document_id: str,
        *,
        organization_id: str,
        include_comments: bool | Omit = omit,
        include_tabs: bool | Omit = omit,
        preview: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentRetrieveResponse:
        """
        Read a document: its metadata, its default tab's body, its other tabs, its
        comments, and its version hash.

        You can read any document you have access to in the Profound app, including ones
        created there rather than through this API.

        By default this is a preview: the body is truncated to save your context, and
        the version hash is withheld so a preview alone can never be used to replace a
        document blindly. Pass `preview=false` when you intend to write.

        Args:
          document_id: ID of the document.

          organization_id: ID of the organization that owns the document. Required — Profound API keys are
              user-scoped, so the owning organization must be named explicitly. The caller
              must be a member of this organization.

          include_comments: Include the document's review comments, each mapped to `{content, context}`. On
              by default — a comment is part of the document's review state, not an aside.
              Turn it off to skip the comment-thread walk upstream; off, `comments` is omitted
              from the response rather than returned as an empty list.

          include_tabs: Include the document's other tabs. On by default — a tab body is part of the
              document, not an aside. Off, `additional_tabs` is omitted from the response
              rather than returned as an empty list.

          preview: Bound every body in the response — `content_markdown` and each tab's — and set
              `content_truncated` if any was cut. On by default. Upstream has no partial-read
              of its own — every read is a full round trip through the collaborative editor —
              so this saves your context, not upstream cost. A preview read also omits
              `version_hash`, on purpose: a hash returned next to a body you have not fully
              seen invites replacing content you never read. Pass `preview=false` before you
              intend to write, to get the whole body, `content_truncated: false`, and the
              hash.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            path_template("/v1/documents/{document_id}", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "include_comments": include_comments,
                        "include_tabs": include_tabs,
                        "preview": preview,
                    },
                    document_retrieve_params.DocumentRetrieveParams,
                ),
            ),
            cast_to=DocumentRetrieveResponse,
        )

    async def update(
        self,
        document_id: str,
        *,
        organization_id: str,
        name: Optional[str] | Omit = omit,
        visibility: Optional[Literal["invited_only", "organization"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateResponse:
        """
        Rename a document, change who can see it, or both in one call.

        Renaming sets a permanent lock on the title, and changing visibility can
        silently change who has access — see the `name` and `visibility` field
        descriptions for what each one does before you use it.

        Renaming needs edit access; changing visibility is creator-only, and upstream
        enforces it. You can act on a document this API created, or one you created
        yourself in the Profound app — not one merely shared with you.

        Args:
          document_id: ID of the document.

          organization_id: ID of the organization that owns the document. Required — Profound API keys are
              user-scoped, so the owning organization must be named explicitly. The caller
              must be a member of this organization.

          name: New title for the document. Renaming sets a permanent lock: once a document is
              renamed through this route, its title stops following the first heading of its
              content, for the rest of the document's life, and no route can undo the lock.
              Omit to leave the title as it is.

          visibility: New sharing scope: `invited_only` for only the people invited to the document,
              or `organization` for everyone in the owning organization. Only the document's
              creator can change this; omit to leave sharing as it is. Three things worth
              knowing before you set it: `organization` visibility grants view only — there is
              no value here that grants the organization edit access. Setting `invited_only`
              removes the organization's access entirely. And re-asserting `organization` on a
              document whose organization grant is already `edit` silently downgrades the
              whole organization to view — upstream replays the access sync whenever this
              field is sent, and that sync always upserts view, even when the value you sent
              matches the one already stored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._patch(
            path_template("/v1/documents/{document_id}", document_id=document_id),
            body=await async_maybe_transform(
                {
                    "organization_id": organization_id,
                    "name": name,
                    "visibility": visibility,
                },
                document_update_params.DocumentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateResponse,
        )

    async def list(
        self,
        *,
        organization_id: str,
        limit: int | Omit = omit,
        next_cursor: Optional[str] | Omit = omit,
        q: Optional[str] | Omit = omit,
        sort: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentListResponse:
        """
        List documents visible to your organization, newest-modified-first.

        Documents are ordered by last-modified time, most recent first, with no other
        sort option. This is a walk over a live, mutable collection: a document created
        or modified while you are paging can shift which page it lands on, so a single
        walk may show it to you twice or, rarely, skip it.

        This response never includes a total count. Upstream counts totals before
        applying your organization's access filter, so a total, or treating a short page
        as the last one, would misreport what you can actually see. Keep following
        `pagination.next_cursor` until it comes back null — that, and not a short or
        even an empty page, is the end of the walk. A page whose rows the access filter
        removed entirely is empty while later pages still hold documents, so the last
        page of a walk may legitimately be an empty one.

        Args:
          organization_id: ID of the organization whose documents to list. Required. The caller must be a
              member of this organization.

          q: Filter to documents whose name contains this text, case-insensitively. Matches
              only the document's name, never its content — a query that finds nothing does
              not mean the topic is unwritten, only that no title mentions it. Blank or
              omitted returns every document. Ignored when sent alongside `next_cursor`, which
              carries the filter the walk started with. Matching is name-only as of this
              release; broader matching may follow if upstream changes how it indexes the name
              column.

          sort: Documents are always ordered newest-modified-first (`updated_at DESC`, then
              `created_at DESC`, then `id DESC`); there is no parameter that changes this.
              `recency` is the only accepted value, and passing it is a no-op that names the
              guarantee rather than altering it — any other value is rejected outright rather
              than silently ignored. Ordering is never re-applied to a returned page either:
              that would only be consistent within the page, not across a paginated walk.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/documents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "limit": limit,
                        "next_cursor": next_cursor,
                        "q": q,
                        "sort": sort,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            cast_to=DocumentListResponse,
        )

    async def delete(
        self,
        document_id: str,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a document created through this integration.

        Only documents created through this integration can be deleted here. A document
        created in the Profound app can never be deleted through this route, even by the
        person who owns it — creation provenance is stamped once, at creation, and is
        never backfilled onto documents made another way.

        The delete is soft: the row is marked deleted at the storage layer rather than
        destroyed. There is no restore through this API, or any other — treat a delete
        as final even though the data itself is not gone.

        A 404 means the document is not visible to you at all. It covers three cases the
        response does not distinguish, on purpose: the document never existed, it was
        already deleted by an earlier call to this same route, or it exists but your
        credential resolves no role on it. Deleting the same document twice returns 404
        on the second call, not a second 204.

        A 403 means the opposite: the document is visible to you but not deletable here,
        and the message says which rule refused — it was not created through this
        integration, or you are not its creator. Deleting is creator-only, so edit
        access is not enough to remove a document out from under its owner.

        Args:
          document_id: ID of the document.

          organization_id: ID of the organization that owns the document. You must be a member of it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/documents/{document_id}", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, document_delete_params.DocumentDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def replace_content(
        self,
        document_id: str,
        *,
        content_markdown: str,
        organization_id: str,
        skip_title_sync: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentReplaceContentResponse:
        """
        Overwrite a document's entire body with new markdown, replacing what it held
        before.

        This is a whole-body replace, not a patch: send the complete new text every
        time. An empty `content_markdown` is valid and clears the document.

        Two destructive side effects apply on every call, regardless of what you send:

        - The document collapses to its default tab. Every non-default tab is deleted,
          and the comments map is cleared for **all** tabs, including the default one —
          a document with a live comment thread on any tab loses it.
        - `skip_title_sync` defaults to `false`, matching the Profound app: the title
          follows the new content's first heading, so a replace silently renames the
          document unless the heading matches the current title or `skip_title_sync` is
          set.

        There is no compare-and-swap: this call does not accept a precondition, and
        nothing stops two concurrent replaces from silently overwriting each other
        last-writer-wins. Upstream's own `version_hash` documentation says as much — the
        token is "still a change detector rather than a precondition: a caller must not
        treat a matching token as licence to overwrite blindly, because it names the
        room at a moment cortex observed and not the moment its own write lands."
        Sending a `working_version_hash` (or any spelling of it) is rejected with a
        `400` naming this rather than accepted and silently discarded, which is what
        happens on the upstream route this wraps.

        You can replace a document this API created, or one you created yourself
        directly — not merely one shared with you.

        Args:
          document_id: ID of the document.

          content_markdown: New markdown body for the document, replacing everything it held before. An
              empty string is valid and clears the document — nothing else warns you before
              that happens, so treat sending one as deliberate. Whole-body replace only: send
              the complete new text, not just the part that changed. Capped at 1,000,000
              bytes; the upstream router separately caps the entire request at 2 MiB, so a
              body near this cap can still be refused in transit rather than by this field.

          organization_id: ID of the organization that owns the document. Required — Profound API keys are
              user-scoped, so the owning organization must be chosen explicitly. The caller
              must be a member of this organization.

          skip_title_sync: Off by default, matching the Profound app: the document's title follows the new
              content's first heading, so a replace silently renames the document whenever
              that heading differs from the current title. Set true to keep the current title
              regardless of what the new content's first heading says.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._post(
            path_template("/v1/documents/{document_id}/content", document_id=document_id),
            body=await async_maybe_transform(
                {
                    "content_markdown": content_markdown,
                    "organization_id": organization_id,
                    "skip_title_sync": skip_title_sync,
                },
                document_replace_content_params.DocumentReplaceContentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentReplaceContentResponse,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create = to_raw_response_wrapper(
            documents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            documents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            documents.update,
        )
        self.list = to_raw_response_wrapper(
            documents.list,
        )
        self.delete = to_raw_response_wrapper(
            documents.delete,
        )
        self.replace_content = to_raw_response_wrapper(
            documents.replace_content,
        )


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create = async_to_raw_response_wrapper(
            documents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            documents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            documents.update,
        )
        self.list = async_to_raw_response_wrapper(
            documents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            documents.delete,
        )
        self.replace_content = async_to_raw_response_wrapper(
            documents.replace_content,
        )


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create = to_streamed_response_wrapper(
            documents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            documents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            documents.update,
        )
        self.list = to_streamed_response_wrapper(
            documents.list,
        )
        self.delete = to_streamed_response_wrapper(
            documents.delete,
        )
        self.replace_content = to_streamed_response_wrapper(
            documents.replace_content,
        )


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create = async_to_streamed_response_wrapper(
            documents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            documents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            documents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            documents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            documents.delete,
        )
        self.replace_content = async_to_streamed_response_wrapper(
            documents.replace_content,
        )
