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
from ...types.projects.task_list_response import TaskListResponse
from ...types.projects import (
    task_list_params,
    task_create_params,
    task_retrieve_params,
    task_update_params,
    task_delete_params,
    task_update_status_params,
)
from ...types.projects.task_create_response import TaskCreateResponse
from ...types.projects.task_retrieve_response import TaskRetrieveResponse
from ...types.projects.task_update_response import TaskUpdateResponse
from ...types.projects.task_update_status_response import TaskUpdateStatusResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self)

    def list(
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
    ) -> TaskListResponse:
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
            TaskListResponse: Successful Response

        Example:
            ```python
            task = client.projects.tasks.list(
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
                query=maybe_transform({"category_id": category_id}, task_list_params.TaskListParams),
            ),
            cast_to=TaskListResponse,
        )

    def create(
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
    ) -> TaskCreateResponse:
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
            TaskCreateResponse: Successful Response

        Example:
            ```python
            task = client.projects.tasks.create(
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
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"category_id": category_id}, task_create_params.TaskCreateParams),
            ),
            cast_to=TaskCreateResponse,
        )

    def retrieve(
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
    ) -> TaskRetrieveResponse:
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
            TaskRetrieveResponse: Successful Response

        Example:
            ```python
            task = client.projects.tasks.retrieve(
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
                query=maybe_transform({"category_id": category_id}, task_retrieve_params.TaskRetrieveParams),
            ),
            cast_to=TaskRetrieveResponse,
        )

    def update(
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
    ) -> TaskUpdateResponse:
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
            TaskUpdateResponse: Successful Response

        Example:
            ```python
            task = client.projects.tasks.update(
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
                task_update_params.TaskUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"category_id": category_id}, task_update_params.TaskUpdateParams),
            ),
            cast_to=TaskUpdateResponse,
        )

    def delete(
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
            client.projects.tasks.delete(
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
                query=maybe_transform({"category_id": category_id}, task_delete_params.TaskDeleteParams),
            ),
            cast_to=NoneType,
        )

    def update_status(
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
    ) -> TaskUpdateStatusResponse:
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
            TaskUpdateStatusResponse: Successful Response

        Example:
            ```python
            task = client.projects.tasks.update_status(
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
                task_update_status_params.TaskUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"category_id": category_id}, task_update_status_params.TaskUpdateStatusParams),
            ),
            cast_to=TaskUpdateStatusResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self)

    async def list(
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
    ) -> TaskListResponse:
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
            TaskListResponse: Successful Response

        Example:
            ```python
            task = await client.projects.tasks.list(
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
                query=await async_maybe_transform({"category_id": category_id}, task_list_params.TaskListParams),
            ),
            cast_to=TaskListResponse,
        )

    async def create(
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
    ) -> TaskCreateResponse:
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
            TaskCreateResponse: Successful Response

        Example:
            ```python
            task = await client.projects.tasks.create(
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
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"category_id": category_id}, task_create_params.TaskCreateParams),
            ),
            cast_to=TaskCreateResponse,
        )

    async def retrieve(
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
    ) -> TaskRetrieveResponse:
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
            TaskRetrieveResponse: Successful Response

        Example:
            ```python
            task = await client.projects.tasks.retrieve(
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
                    {"category_id": category_id}, task_retrieve_params.TaskRetrieveParams
                ),
            ),
            cast_to=TaskRetrieveResponse,
        )

    async def update(
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
    ) -> TaskUpdateResponse:
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
            TaskUpdateResponse: Successful Response

        Example:
            ```python
            task = await client.projects.tasks.update(
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
                task_update_params.TaskUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"category_id": category_id}, task_update_params.TaskUpdateParams),
            ),
            cast_to=TaskUpdateResponse,
        )

    async def delete(
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
            await client.projects.tasks.delete(
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
                query=await async_maybe_transform({"category_id": category_id}, task_delete_params.TaskDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def update_status(
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
    ) -> TaskUpdateStatusResponse:
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
            TaskUpdateStatusResponse: Successful Response

        Example:
            ```python
            task = await client.projects.tasks.update_status(
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
                task_update_status_params.TaskUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"category_id": category_id}, task_update_status_params.TaskUpdateStatusParams
                ),
            ),
            cast_to=TaskUpdateStatusResponse,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.list = to_raw_response_wrapper(
            tasks.list,
        )
        self.create = to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tasks.update,
        )
        self.delete = to_raw_response_wrapper(
            tasks.delete,
        )
        self.update_status = to_raw_response_wrapper(
            tasks.update_status,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.list = async_to_raw_response_wrapper(
            tasks.list,
        )
        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tasks.update,
        )
        self.delete = async_to_raw_response_wrapper(
            tasks.delete,
        )
        self.update_status = async_to_raw_response_wrapper(
            tasks.update_status,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.list = to_streamed_response_wrapper(
            tasks.list,
        )
        self.create = to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tasks.update,
        )
        self.delete = to_streamed_response_wrapper(
            tasks.delete,
        )
        self.update_status = to_streamed_response_wrapper(
            tasks.update_status,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tasks.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            tasks.delete,
        )
        self.update_status = async_to_streamed_response_wrapper(
            tasks.update_status,
        )
