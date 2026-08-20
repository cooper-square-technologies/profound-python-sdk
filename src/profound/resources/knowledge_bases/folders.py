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
from ...types.knowledge_bases.folder_create_response import FolderCreateResponse
from ...types.knowledge_bases import folder_create_params, folder_delete_params
from ...types.knowledge_bases.folder_delete_response import FolderDeleteResponse

__all__ = ["FoldersResource", "AsyncFoldersResource"]


class FoldersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self)

    def create(
        self,
        knowledge_base_id: str,
        *,
        path: str,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """
        Create an empty folder at the requested knowledge base path.

        Args:
            knowledge_base_id: Unique knowledge base ID.
            path: Folder path to create.
            organization_id: Organization scope for API keys that can access multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderCreateResponse: Successful Response

        Example:
            ```python
            folder = client.knowledge_bases.folders.create(
                knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                path="x",
            )
            ```
        """
        if knowledge_base_id is None or (isinstance(knowledge_base_id, str) and not knowledge_base_id):
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._post(
            path_template(
                "/v1/knowledge-bases/{knowledge_base_id}/folders", **{"knowledge_base_id": knowledge_base_id}
            ),
            body=maybe_transform(
                {"path": path},
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"organization_id": organization_id}, folder_create_params.FolderCreateParams),
            ),
            cast_to=FolderCreateResponse,
        )

    def delete(
        self,
        knowledge_base_id: str,
        *,
        path: str,
        recursive: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteResponse:
        """
        Delete a folder. With recursive=false, non-empty folders return 409 and no contents are deleted.

        Args:
            knowledge_base_id: Unique knowledge base ID.
            path: Folder path to delete.
            recursive: When false, only empty folders are deleted and non-empty folders return a conflict. When true, the folder and all contents are deleted.
            organization_id: Organization scope for API keys that can access multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderDeleteResponse: Successful Response

        Example:
            ```python
            folder = client.knowledge_bases.folders.delete(
                knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                path="x",
                recursive=False,
            )
            ```
        """
        if knowledge_base_id is None or (isinstance(knowledge_base_id, str) and not knowledge_base_id):
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._delete(
            path_template(
                "/v1/knowledge-bases/{knowledge_base_id}/folders", **{"knowledge_base_id": knowledge_base_id}
            ),
            body=maybe_transform(
                {
                    "path": path,
                    "recursive": recursive,
                },
                folder_delete_params.FolderDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"organization_id": organization_id}, folder_delete_params.FolderDeleteParams),
            ),
            cast_to=FolderDeleteResponse,
        )


class AsyncFoldersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self)

    async def create(
        self,
        knowledge_base_id: str,
        *,
        path: str,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """
        Create an empty folder at the requested knowledge base path.

        Args:
            knowledge_base_id: Unique knowledge base ID.
            path: Folder path to create.
            organization_id: Organization scope for API keys that can access multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderCreateResponse: Successful Response

        Example:
            ```python
            folder = await client.knowledge_bases.folders.create(
                knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                path="x",
            )
            ```
        """
        if knowledge_base_id is None or (isinstance(knowledge_base_id, str) and not knowledge_base_id):
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._post(
            path_template(
                "/v1/knowledge-bases/{knowledge_base_id}/folders", **{"knowledge_base_id": knowledge_base_id}
            ),
            body=await async_maybe_transform(
                {"path": path},
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, folder_create_params.FolderCreateParams
                ),
            ),
            cast_to=FolderCreateResponse,
        )

    async def delete(
        self,
        knowledge_base_id: str,
        *,
        path: str,
        recursive: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteResponse:
        """
        Delete a folder. With recursive=false, non-empty folders return 409 and no contents are deleted.

        Args:
            knowledge_base_id: Unique knowledge base ID.
            path: Folder path to delete.
            recursive: When false, only empty folders are deleted and non-empty folders return a conflict. When true, the folder and all contents are deleted.
            organization_id: Organization scope for API keys that can access multiple organizations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FolderDeleteResponse: Successful Response

        Example:
            ```python
            folder = await client.knowledge_bases.folders.delete(
                knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                path="x",
                recursive=False,
            )
            ```
        """
        if knowledge_base_id is None or (isinstance(knowledge_base_id, str) and not knowledge_base_id):
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._delete(
            path_template(
                "/v1/knowledge-bases/{knowledge_base_id}/folders", **{"knowledge_base_id": knowledge_base_id}
            ),
            body=await async_maybe_transform(
                {
                    "path": path,
                    "recursive": recursive,
                },
                folder_delete_params.FolderDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, folder_delete_params.FolderDeleteParams
                ),
            ),
            cast_to=FolderDeleteResponse,
        )


class FoldersResourceWithRawResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_raw_response_wrapper(
            folders.create,
        )
        self.delete = to_raw_response_wrapper(
            folders.delete,
        )


class AsyncFoldersResourceWithRawResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_raw_response_wrapper(
            folders.create,
        )
        self.delete = async_to_raw_response_wrapper(
            folders.delete,
        )


class FoldersResourceWithStreamingResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_streamed_response_wrapper(
            folders.create,
        )
        self.delete = to_streamed_response_wrapper(
            folders.delete,
        )


class AsyncFoldersResourceWithStreamingResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_streamed_response_wrapper(
            folders.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            folders.delete,
        )
