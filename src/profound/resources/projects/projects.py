# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Optional
from ..._types import SequenceNotStr

from ..._types import Body, Omit, Query, Headers, NotGiven, NoneType, omit, not_given
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
from .generations import (
    GenerationsResource,
    AsyncGenerationsResource,
    GenerationsResourceWithRawResponse,
    AsyncGenerationsResourceWithRawResponse,
    GenerationsResourceWithStreamingResponse,
    AsyncGenerationsResourceWithStreamingResponse,
)
from .tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from ...types.project_list_response import ProjectListResponse
from ...types import (
    project_list_params,
    project_create_params,
    project_retrieve_params,
    project_delete_params,
    project_get_status_params,
    project_archive_params,
    project_unarchive_params,
)
from ...types.project_create_response import ProjectCreateResponse
from ...types.project_retrieve_response import ProjectRetrieveResponse
from ...types.project_get_status_response import ProjectGetStatusResponse
from ...types.project_archive_response import ProjectArchiveResponse
from ...types.project_unarchive_response import ProjectUnarchiveResponse

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
    @cached_property
    def generations(self) -> GenerationsResource:
        return GenerationsResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        category_id: str,
        status: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectListResponse:
        """
        List Projects

        Args:
            category_id: Category that owns the project.
            status: Comma-separated project statuses: suggested, tracked, retired.
            limit: Query parameter.
            offset: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectListResponse: Successful Response

        Example:
            ```python
            project = client.projects.list(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=100,
                offset=0,
            )
            ```
        """
        return self._get(
            "/v1/projects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"category_id": category_id, "status": status, "limit": limit, "offset": offset},
                    project_list_params.ProjectListParams,
                ),
            ),
            cast_to=ProjectListResponse,
        )

    def create(
        self,
        *,
        category_id: str,
        title: Optional[str] | Omit = omit,
        project_name: Optional[str] | Omit = omit,
        focus: Optional[str] | Omit = omit,
        topics: SequenceNotStr[str] | Omit = omit,
        attachments: Iterable[project_create_params.Attachment] | Omit = omit,
        generation_context: Optional[project_create_params.GenerationContext] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectCreateResponse:
        """
        Create Project

        Args:
            category_id: Body parameter.
            title: Body parameter.
            project_name: Body parameter.
            focus: Body parameter.
            topics: Body parameter.
            attachments: Body parameter.
            generation_context: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectCreateResponse: Successful Response

        Example:
            ```python
            project = client.projects.create(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        return self._post(
            "/v1/projects",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "title": title,
                    "project_name": project_name,
                    "focus": focus,
                    "topics": topics,
                    "attachments": attachments,
                    "generation_context": generation_context,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateResponse,
        )

    def retrieve(
        self,
        project_id: str,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectRetrieveResponse:
        """
        Get Project

        Args:
            project_id: Unique project ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectRetrieveResponse: Successful Response

        Example:
            ```python
            project = client.projects.retrieve(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/v1/projects/{project_id}", **{"project_id": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"category_id": category_id}, project_retrieve_params.ProjectRetrieveParams),
            ),
            cast_to=ProjectRetrieveResponse,
        )

    def delete(
        self,
        project_id: str,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Project

        Args:
            project_id: Unique project ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful Response

        Example:
            ```python
            client.projects.delete(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/projects/{project_id}", **{"project_id": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"category_id": category_id}, project_delete_params.ProjectDeleteParams),
            ),
            cast_to=NoneType,
        )

    def get_status(
        self,
        project_id: str,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectGetStatusResponse:
        """
        Get Project Status

        Args:
            project_id: Unique project ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectGetStatusResponse: Successful Response

        Example:
            ```python
            project = client.projects.get_status(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/v1/projects/{project_id}/status", **{"project_id": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"category_id": category_id}, project_get_status_params.ProjectGetStatusParams),
            ),
            cast_to=ProjectGetStatusResponse,
        )

    def archive(
        self,
        project_id: str,
        *,
        reason: Optional[str] | Omit = omit,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectArchiveResponse:
        """
        Archive Project

        Args:
            project_id: Unique project ID.
            reason: Body parameter.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectArchiveResponse: Successful Response

        Example:
            ```python
            project = client.projects.archive(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/v1/projects/{project_id}/archive", **{"project_id": project_id}),
            body=maybe_transform(
                {"reason": reason},
                project_archive_params.ProjectArchiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"category_id": category_id}, project_archive_params.ProjectArchiveParams),
            ),
            cast_to=ProjectArchiveResponse,
        )

    def unarchive(
        self,
        project_id: str,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectUnarchiveResponse:
        """
        Unarchive Project

        Args:
            project_id: Unique project ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectUnarchiveResponse: Successful Response

        Example:
            ```python
            project = client.projects.unarchive(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/v1/projects/{project_id}/unarchive", **{"project_id": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"category_id": category_id}, project_unarchive_params.ProjectUnarchiveParams),
            ),
            cast_to=ProjectUnarchiveResponse,
        )


class AsyncProjectsResource(AsyncAPIResource):
    @cached_property
    def generations(self) -> AsyncGenerationsResource:
        return AsyncGenerationsResource(self._client)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        category_id: str,
        status: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectListResponse:
        """
        List Projects

        Args:
            category_id: Category that owns the project.
            status: Comma-separated project statuses: suggested, tracked, retired.
            limit: Query parameter.
            offset: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectListResponse: Successful Response

        Example:
            ```python
            project = await client.projects.list(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                limit=100,
                offset=0,
            )
            ```
        """
        return await self._get(
            "/v1/projects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id, "status": status, "limit": limit, "offset": offset},
                    project_list_params.ProjectListParams,
                ),
            ),
            cast_to=ProjectListResponse,
        )

    async def create(
        self,
        *,
        category_id: str,
        title: Optional[str] | Omit = omit,
        project_name: Optional[str] | Omit = omit,
        focus: Optional[str] | Omit = omit,
        topics: SequenceNotStr[str] | Omit = omit,
        attachments: Iterable[project_create_params.Attachment] | Omit = omit,
        generation_context: Optional[project_create_params.GenerationContext] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectCreateResponse:
        """
        Create Project

        Args:
            category_id: Body parameter.
            title: Body parameter.
            project_name: Body parameter.
            focus: Body parameter.
            topics: Body parameter.
            attachments: Body parameter.
            generation_context: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectCreateResponse: Successful Response

        Example:
            ```python
            project = await client.projects.create(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        return await self._post(
            "/v1/projects",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "title": title,
                    "project_name": project_name,
                    "focus": focus,
                    "topics": topics,
                    "attachments": attachments,
                    "generation_context": generation_context,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateResponse,
        )

    async def retrieve(
        self,
        project_id: str,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectRetrieveResponse:
        """
        Get Project

        Args:
            project_id: Unique project ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectRetrieveResponse: Successful Response

        Example:
            ```python
            project = await client.projects.retrieve(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/v1/projects/{project_id}", **{"project_id": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id}, project_retrieve_params.ProjectRetrieveParams
                ),
            ),
            cast_to=ProjectRetrieveResponse,
        )

    async def delete(
        self,
        project_id: str,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Project

        Args:
            project_id: Unique project ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Successful Response

        Example:
            ```python
            await client.projects.delete(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/projects/{project_id}", **{"project_id": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id}, project_delete_params.ProjectDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def get_status(
        self,
        project_id: str,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectGetStatusResponse:
        """
        Get Project Status

        Args:
            project_id: Unique project ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectGetStatusResponse: Successful Response

        Example:
            ```python
            project = await client.projects.get_status(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/v1/projects/{project_id}/status", **{"project_id": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id}, project_get_status_params.ProjectGetStatusParams
                ),
            ),
            cast_to=ProjectGetStatusResponse,
        )

    async def archive(
        self,
        project_id: str,
        *,
        reason: Optional[str] | Omit = omit,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectArchiveResponse:
        """
        Archive Project

        Args:
            project_id: Unique project ID.
            reason: Body parameter.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectArchiveResponse: Successful Response

        Example:
            ```python
            project = await client.projects.archive(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/v1/projects/{project_id}/archive", **{"project_id": project_id}),
            body=await async_maybe_transform(
                {"reason": reason},
                project_archive_params.ProjectArchiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id}, project_archive_params.ProjectArchiveParams
                ),
            ),
            cast_to=ProjectArchiveResponse,
        )

    async def unarchive(
        self,
        project_id: str,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectUnarchiveResponse:
        """
        Unarchive Project

        Args:
            project_id: Unique project ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ProjectUnarchiveResponse: Successful Response

        Example:
            ```python
            project = await client.projects.unarchive(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/v1/projects/{project_id}/unarchive", **{"project_id": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id}, project_unarchive_params.ProjectUnarchiveParams
                ),
            ),
            cast_to=ProjectUnarchiveResponse,
        )


class ProjectsResourceWithRawResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.list = to_raw_response_wrapper(
            projects.list,
        )
        self.create = to_raw_response_wrapper(
            projects.create,
        )
        self.retrieve = to_raw_response_wrapper(
            projects.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            projects.delete,
        )
        self.get_status = to_raw_response_wrapper(
            projects.get_status,
        )
        self.archive = to_raw_response_wrapper(
            projects.archive,
        )
        self.unarchive = to_raw_response_wrapper(
            projects.unarchive,
        )

    @cached_property
    def generations(self) -> GenerationsResourceWithRawResponse:
        return GenerationsResourceWithRawResponse(self._projects.generations)

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._projects.tasks)


class AsyncProjectsResourceWithRawResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.list = async_to_raw_response_wrapper(
            projects.list,
        )
        self.create = async_to_raw_response_wrapper(
            projects.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            projects.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            projects.delete,
        )
        self.get_status = async_to_raw_response_wrapper(
            projects.get_status,
        )
        self.archive = async_to_raw_response_wrapper(
            projects.archive,
        )
        self.unarchive = async_to_raw_response_wrapper(
            projects.unarchive,
        )

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithRawResponse:
        return AsyncGenerationsResourceWithRawResponse(self._projects.generations)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._projects.tasks)


class ProjectsResourceWithStreamingResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.list = to_streamed_response_wrapper(
            projects.list,
        )
        self.create = to_streamed_response_wrapper(
            projects.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            projects.delete,
        )
        self.get_status = to_streamed_response_wrapper(
            projects.get_status,
        )
        self.archive = to_streamed_response_wrapper(
            projects.archive,
        )
        self.unarchive = to_streamed_response_wrapper(
            projects.unarchive,
        )

    @cached_property
    def generations(self) -> GenerationsResourceWithStreamingResponse:
        return GenerationsResourceWithStreamingResponse(self._projects.generations)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._projects.tasks)


class AsyncProjectsResourceWithStreamingResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.list = async_to_streamed_response_wrapper(
            projects.list,
        )
        self.create = async_to_streamed_response_wrapper(
            projects.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            projects.delete,
        )
        self.get_status = async_to_streamed_response_wrapper(
            projects.get_status,
        )
        self.archive = async_to_streamed_response_wrapper(
            projects.archive,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            projects.unarchive,
        )

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithStreamingResponse:
        return AsyncGenerationsResourceWithStreamingResponse(self._projects.generations)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._projects.tasks)
