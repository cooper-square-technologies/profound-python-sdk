# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
from typing_extensions import Literal

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
from ...types.projects.task_list_v1_id_get_response import TaskListV1IDGetResponse
from ...types.projects import (
    task_list_v1_id_get_params,
    task_create_v1_id_post_params,
    task_retrieve_v1_get_params,
    task_update_v1_id_id_patch_params,
    task_delete_v1_id_id_delete_params,
    task_update_status_v1_id_id_status_post_params,
)
from ...types.projects.task_create_v1_id_post_response import TaskCreateV1IDPostResponse
from ...types.projects.task_retrieve_v1_get_response import TaskRetrieveV1GetResponse
from ...types.projects.task_update_v1_id_id_patch_response import TaskUpdateV1IDIDPatchResponse
from ...types.projects.task_update_status_v1_id_id_status_post_response import TaskUpdateStatusV1IDIDStatusPostResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self)

    def list_v1_id_get(
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
    ) -> TaskListV1IDGetResponse:
        """
        List Project Tasks

        Args:
            project_id: Unique project ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TaskListV1IDGetResponse: Successful Response

        Example:
            ```python
            task = client.projects.tasks.list_v1_id_get(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/v1/projects/{project_id}/tasks", **{"project_id": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"category_id": category_id}, task_list_v1_id_get_params.TaskListV1IDGetParams),
            ),
            cast_to=TaskListV1IDGetResponse,
        )

    def create_v1_id_post(
        self,
        project_id: str,
        *,
        title: str,
        summary: Optional[str] | Omit = omit,
        brief: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
        topic: Optional[str] | Omit = omit,
        impact: Optional[int] | Omit = omit,
        reference_url: Optional[str] | Omit = omit,
        reference_label: Optional[str] | Omit = omit,
        position: Optional[int] | Omit = omit,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskCreateV1IDPostResponse:
        """
        Create Project Task

        Args:
            project_id: Unique project ID.
            title: Body parameter.
            summary: Body parameter.
            brief: Body parameter.
            type: Body parameter.
            topic: Body parameter.
            impact: Body parameter.
            reference_url: Body parameter.
            reference_label: Body parameter.
            position: Body parameter.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TaskCreateV1IDPostResponse: Successful Response

        Example:
            ```python
            task = client.projects.tasks.create_v1_id_post(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                title="x",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/v1/projects/{project_id}/tasks", **{"project_id": project_id}),
            body=maybe_transform(
                {
                    "title": title,
                    "summary": summary,
                    "brief": brief,
                    "type": type,
                    "topic": topic,
                    "impact": impact,
                    "reference_url": reference_url,
                    "reference_label": reference_label,
                    "position": position,
                },
                task_create_v1_id_post_params.TaskCreateV1IDPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"category_id": category_id}, task_create_v1_id_post_params.TaskCreateV1IDPostParams
                ),
            ),
            cast_to=TaskCreateV1IDPostResponse,
        )

    def retrieve_v1_get(
        self,
        task_id: str,
        *,
        project_id: str,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRetrieveV1GetResponse:
        """
        Get Project Task

        Args:
            task_id: Unique project task ID.
            project_id: Unique project ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TaskRetrieveV1GetResponse: Successful Response

        Example:
            ```python
            task = client.projects.tasks.retrieve_v1_get(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if task_id is None or (isinstance(task_id, str) and not task_id):
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template(
                "/v1/projects/{project_id}/tasks/{task_id}", **{"project_id": project_id, "task_id": task_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"category_id": category_id}, task_retrieve_v1_get_params.TaskRetrieveV1GetParams
                ),
            ),
            cast_to=TaskRetrieveV1GetResponse,
        )

    def update_v1_id_id_patch(
        self,
        task_id: str,
        *,
        project_id: str,
        title: Optional[str] | Omit = omit,
        summary: Optional[str] | Omit = omit,
        brief: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
        topic: Optional[str] | Omit = omit,
        impact: Optional[int] | Omit = omit,
        reference_url: Optional[str] | Omit = omit,
        reference_label: Optional[str] | Omit = omit,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskUpdateV1IDIDPatchResponse:
        """
        Update Project Task

        Args:
            task_id: Unique project task ID.
            project_id: Unique project ID.
            title: Body parameter.
            summary: Body parameter.
            brief: Body parameter.
            type: Body parameter.
            topic: Body parameter.
            impact: Body parameter.
            reference_url: Body parameter.
            reference_label: Body parameter.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TaskUpdateV1IDIDPatchResponse: Successful Response

        Example:
            ```python
            task = client.projects.tasks.update_v1_id_id_patch(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if task_id is None or (isinstance(task_id, str) and not task_id):
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._patch(
            path_template(
                "/v1/projects/{project_id}/tasks/{task_id}", **{"project_id": project_id, "task_id": task_id}
            ),
            body=maybe_transform(
                {
                    "title": title,
                    "summary": summary,
                    "brief": brief,
                    "type": type,
                    "topic": topic,
                    "impact": impact,
                    "reference_url": reference_url,
                    "reference_label": reference_label,
                },
                task_update_v1_id_id_patch_params.TaskUpdateV1IDIDPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"category_id": category_id}, task_update_v1_id_id_patch_params.TaskUpdateV1IDIDPatchParams
                ),
            ),
            cast_to=TaskUpdateV1IDIDPatchResponse,
        )

    def delete_v1_id_id_delete(
        self,
        task_id: str,
        *,
        project_id: str,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Project Task

        Args:
            task_id: Unique project task ID.
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
            client.projects.tasks.delete_v1_id_id_delete(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if task_id is None or (isinstance(task_id, str) and not task_id):
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v1/projects/{project_id}/tasks/{task_id}", **{"project_id": project_id, "task_id": task_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"category_id": category_id}, task_delete_v1_id_id_delete_params.TaskDeleteV1IDIDDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    def update_status_v1_id_id_status_post(
        self,
        task_id: str,
        *,
        project_id: str,
        status: Literal["not_started", "in_progress", "done", "abandoned"],
        note: Optional[str] | Omit = omit,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskUpdateStatusV1IDIDStatusPostResponse:
        """
        Update Project Task Status

        Args:
            task_id: Unique project task ID.
            project_id: Unique project ID.
            status: Body parameter.
            note: Body parameter.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TaskUpdateStatusV1IDIDStatusPostResponse: Successful Response

        Example:
            ```python
            task = client.projects.tasks.update_status_v1_id_id_status_post(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                status="not_started",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if task_id is None or (isinstance(task_id, str) and not task_id):
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._post(
            path_template(
                "/v1/projects/{project_id}/tasks/{task_id}/status", **{"project_id": project_id, "task_id": task_id}
            ),
            body=maybe_transform(
                {
                    "status": status,
                    "note": note,
                },
                task_update_status_v1_id_id_status_post_params.TaskUpdateStatusV1IDIDStatusPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"category_id": category_id},
                    task_update_status_v1_id_id_status_post_params.TaskUpdateStatusV1IDIDStatusPostParams,
                ),
            ),
            cast_to=TaskUpdateStatusV1IDIDStatusPostResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self)

    async def list_v1_id_get(
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
    ) -> TaskListV1IDGetResponse:
        """
        List Project Tasks

        Args:
            project_id: Unique project ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TaskListV1IDGetResponse: Successful Response

        Example:
            ```python
            task = await client.projects.tasks.list_v1_id_get(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/v1/projects/{project_id}/tasks", **{"project_id": project_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id}, task_list_v1_id_get_params.TaskListV1IDGetParams
                ),
            ),
            cast_to=TaskListV1IDGetResponse,
        )

    async def create_v1_id_post(
        self,
        project_id: str,
        *,
        title: str,
        summary: Optional[str] | Omit = omit,
        brief: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
        topic: Optional[str] | Omit = omit,
        impact: Optional[int] | Omit = omit,
        reference_url: Optional[str] | Omit = omit,
        reference_label: Optional[str] | Omit = omit,
        position: Optional[int] | Omit = omit,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskCreateV1IDPostResponse:
        """
        Create Project Task

        Args:
            project_id: Unique project ID.
            title: Body parameter.
            summary: Body parameter.
            brief: Body parameter.
            type: Body parameter.
            topic: Body parameter.
            impact: Body parameter.
            reference_url: Body parameter.
            reference_label: Body parameter.
            position: Body parameter.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TaskCreateV1IDPostResponse: Successful Response

        Example:
            ```python
            task = await client.projects.tasks.create_v1_id_post(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                title="x",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/v1/projects/{project_id}/tasks", **{"project_id": project_id}),
            body=await async_maybe_transform(
                {
                    "title": title,
                    "summary": summary,
                    "brief": brief,
                    "type": type,
                    "topic": topic,
                    "impact": impact,
                    "reference_url": reference_url,
                    "reference_label": reference_label,
                    "position": position,
                },
                task_create_v1_id_post_params.TaskCreateV1IDPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id}, task_create_v1_id_post_params.TaskCreateV1IDPostParams
                ),
            ),
            cast_to=TaskCreateV1IDPostResponse,
        )

    async def retrieve_v1_get(
        self,
        task_id: str,
        *,
        project_id: str,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRetrieveV1GetResponse:
        """
        Get Project Task

        Args:
            task_id: Unique project task ID.
            project_id: Unique project ID.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TaskRetrieveV1GetResponse: Successful Response

        Example:
            ```python
            task = await client.projects.tasks.retrieve_v1_get(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if task_id is None or (isinstance(task_id, str) and not task_id):
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template(
                "/v1/projects/{project_id}/tasks/{task_id}", **{"project_id": project_id, "task_id": task_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id}, task_retrieve_v1_get_params.TaskRetrieveV1GetParams
                ),
            ),
            cast_to=TaskRetrieveV1GetResponse,
        )

    async def update_v1_id_id_patch(
        self,
        task_id: str,
        *,
        project_id: str,
        title: Optional[str] | Omit = omit,
        summary: Optional[str] | Omit = omit,
        brief: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
        topic: Optional[str] | Omit = omit,
        impact: Optional[int] | Omit = omit,
        reference_url: Optional[str] | Omit = omit,
        reference_label: Optional[str] | Omit = omit,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskUpdateV1IDIDPatchResponse:
        """
        Update Project Task

        Args:
            task_id: Unique project task ID.
            project_id: Unique project ID.
            title: Body parameter.
            summary: Body parameter.
            brief: Body parameter.
            type: Body parameter.
            topic: Body parameter.
            impact: Body parameter.
            reference_url: Body parameter.
            reference_label: Body parameter.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TaskUpdateV1IDIDPatchResponse: Successful Response

        Example:
            ```python
            task = await client.projects.tasks.update_v1_id_id_patch(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if task_id is None or (isinstance(task_id, str) and not task_id):
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._patch(
            path_template(
                "/v1/projects/{project_id}/tasks/{task_id}", **{"project_id": project_id, "task_id": task_id}
            ),
            body=await async_maybe_transform(
                {
                    "title": title,
                    "summary": summary,
                    "brief": brief,
                    "type": type,
                    "topic": topic,
                    "impact": impact,
                    "reference_url": reference_url,
                    "reference_label": reference_label,
                },
                task_update_v1_id_id_patch_params.TaskUpdateV1IDIDPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id}, task_update_v1_id_id_patch_params.TaskUpdateV1IDIDPatchParams
                ),
            ),
            cast_to=TaskUpdateV1IDIDPatchResponse,
        )

    async def delete_v1_id_id_delete(
        self,
        task_id: str,
        *,
        project_id: str,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Project Task

        Args:
            task_id: Unique project task ID.
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
            await client.projects.tasks.delete_v1_id_id_delete(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if task_id is None or (isinstance(task_id, str) and not task_id):
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v1/projects/{project_id}/tasks/{task_id}", **{"project_id": project_id, "task_id": task_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id}, task_delete_v1_id_id_delete_params.TaskDeleteV1IDIDDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def update_status_v1_id_id_status_post(
        self,
        task_id: str,
        *,
        project_id: str,
        status: Literal["not_started", "in_progress", "done", "abandoned"],
        note: Optional[str] | Omit = omit,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskUpdateStatusV1IDIDStatusPostResponse:
        """
        Update Project Task Status

        Args:
            task_id: Unique project task ID.
            project_id: Unique project ID.
            status: Body parameter.
            note: Body parameter.
            category_id: Category that owns the project.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            TaskUpdateStatusV1IDIDStatusPostResponse: Successful Response

        Example:
            ```python
            task = await client.projects.tasks.update_status_v1_id_id_status_post(
                project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                status="not_started",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if project_id is None or (isinstance(project_id, str) and not project_id):
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if task_id is None or (isinstance(task_id, str) and not task_id):
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._post(
            path_template(
                "/v1/projects/{project_id}/tasks/{task_id}/status", **{"project_id": project_id, "task_id": task_id}
            ),
            body=await async_maybe_transform(
                {
                    "status": status,
                    "note": note,
                },
                task_update_status_v1_id_id_status_post_params.TaskUpdateStatusV1IDIDStatusPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id},
                    task_update_status_v1_id_id_status_post_params.TaskUpdateStatusV1IDIDStatusPostParams,
                ),
            ),
            cast_to=TaskUpdateStatusV1IDIDStatusPostResponse,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.list_v1_id_get = to_raw_response_wrapper(
            tasks.list_v1_id_get,
        )
        self.create_v1_id_post = to_raw_response_wrapper(
            tasks.create_v1_id_post,
        )
        self.retrieve_v1_get = to_raw_response_wrapper(
            tasks.retrieve_v1_get,
        )
        self.update_v1_id_id_patch = to_raw_response_wrapper(
            tasks.update_v1_id_id_patch,
        )
        self.delete_v1_id_id_delete = to_raw_response_wrapper(
            tasks.delete_v1_id_id_delete,
        )
        self.update_status_v1_id_id_status_post = to_raw_response_wrapper(
            tasks.update_status_v1_id_id_status_post,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.list_v1_id_get = async_to_raw_response_wrapper(
            tasks.list_v1_id_get,
        )
        self.create_v1_id_post = async_to_raw_response_wrapper(
            tasks.create_v1_id_post,
        )
        self.retrieve_v1_get = async_to_raw_response_wrapper(
            tasks.retrieve_v1_get,
        )
        self.update_v1_id_id_patch = async_to_raw_response_wrapper(
            tasks.update_v1_id_id_patch,
        )
        self.delete_v1_id_id_delete = async_to_raw_response_wrapper(
            tasks.delete_v1_id_id_delete,
        )
        self.update_status_v1_id_id_status_post = async_to_raw_response_wrapper(
            tasks.update_status_v1_id_id_status_post,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.list_v1_id_get = to_streamed_response_wrapper(
            tasks.list_v1_id_get,
        )
        self.create_v1_id_post = to_streamed_response_wrapper(
            tasks.create_v1_id_post,
        )
        self.retrieve_v1_get = to_streamed_response_wrapper(
            tasks.retrieve_v1_get,
        )
        self.update_v1_id_id_patch = to_streamed_response_wrapper(
            tasks.update_v1_id_id_patch,
        )
        self.delete_v1_id_id_delete = to_streamed_response_wrapper(
            tasks.delete_v1_id_id_delete,
        )
        self.update_status_v1_id_id_status_post = to_streamed_response_wrapper(
            tasks.update_status_v1_id_id_status_post,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.list_v1_id_get = async_to_streamed_response_wrapper(
            tasks.list_v1_id_get,
        )
        self.create_v1_id_post = async_to_streamed_response_wrapper(
            tasks.create_v1_id_post,
        )
        self.retrieve_v1_get = async_to_streamed_response_wrapper(
            tasks.retrieve_v1_get,
        )
        self.update_v1_id_id_patch = async_to_streamed_response_wrapper(
            tasks.update_v1_id_id_patch,
        )
        self.delete_v1_id_id_delete = async_to_streamed_response_wrapper(
            tasks.delete_v1_id_id_delete,
        )
        self.update_status_v1_id_id_status_post = async_to_streamed_response_wrapper(
            tasks.update_status_v1_id_id_status_post,
        )
