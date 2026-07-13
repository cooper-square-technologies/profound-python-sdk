# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.projects import (
    task_list_params,
    task_create_params,
    task_delete_params,
    task_update_params,
    task_retrieve_params,
    task_update_status_params,
)
from ...types.projects.task_list_response import TaskListResponse
from ...types.projects.task_create_response import TaskCreateResponse
from ...types.projects.task_update_response import TaskUpdateResponse
from ...types.projects.task_retrieve_response import TaskRetrieveResponse
from ...types.projects.task_update_status_response import TaskUpdateStatusResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: str,
        *,
        category_id: str,
        title: str,
        brief: Optional[str] | Omit = omit,
        impact: Optional[int] | Omit = omit,
        position: Optional[int] | Omit = omit,
        reference_label: Optional[str] | Omit = omit,
        reference_url: Optional[str] | Omit = omit,
        summary: Optional[str] | Omit = omit,
        topic: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
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

          category_id: Category that owns the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/v1/projects/{project_id}/tasks", project_id=project_id),
            body=maybe_transform(
                {
                    "title": title,
                    "brief": brief,
                    "impact": impact,
                    "position": position,
                    "reference_label": reference_label,
                    "reference_url": reference_url,
                    "summary": summary,
                    "topic": topic,
                    "type": type,
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
          project_id: Unique project ID.

          task_id: Unique project task ID.

          category_id: Category that owns the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template("/v1/projects/{project_id}/tasks/{task_id}", project_id=project_id, task_id=task_id),
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
        category_id: str,
        brief: Optional[str] | Omit = omit,
        impact: Optional[int] | Omit = omit,
        reference_label: Optional[str] | Omit = omit,
        reference_url: Optional[str] | Omit = omit,
        summary: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        topic: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
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
          project_id: Unique project ID.

          task_id: Unique project task ID.

          category_id: Category that owns the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._patch(
            path_template("/v1/projects/{project_id}/tasks/{task_id}", project_id=project_id, task_id=task_id),
            body=maybe_transform(
                {
                    "brief": brief,
                    "impact": impact,
                    "reference_label": reference_label,
                    "reference_url": reference_url,
                    "summary": summary,
                    "title": title,
                    "topic": topic,
                    "type": type,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/v1/projects/{project_id}/tasks", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"category_id": category_id}, task_list_params.TaskListParams),
            ),
            cast_to=TaskListResponse,
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
          project_id: Unique project ID.

          task_id: Unique project task ID.

          category_id: Category that owns the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/projects/{project_id}/tasks/{task_id}", project_id=project_id, task_id=task_id),
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
        category_id: str,
        status: Literal["not_started", "in_progress", "done", "abandoned"],
        note: Optional[str] | Omit = omit,
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
          project_id: Unique project ID.

          task_id: Unique project task ID.

          category_id: Category that owns the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._post(
            path_template("/v1/projects/{project_id}/tasks/{task_id}/status", project_id=project_id, task_id=task_id),
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: str,
        *,
        category_id: str,
        title: str,
        brief: Optional[str] | Omit = omit,
        impact: Optional[int] | Omit = omit,
        position: Optional[int] | Omit = omit,
        reference_label: Optional[str] | Omit = omit,
        reference_url: Optional[str] | Omit = omit,
        summary: Optional[str] | Omit = omit,
        topic: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
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

          category_id: Category that owns the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/v1/projects/{project_id}/tasks", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "title": title,
                    "brief": brief,
                    "impact": impact,
                    "position": position,
                    "reference_label": reference_label,
                    "reference_url": reference_url,
                    "summary": summary,
                    "topic": topic,
                    "type": type,
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
          project_id: Unique project ID.

          task_id: Unique project task ID.

          category_id: Category that owns the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template("/v1/projects/{project_id}/tasks/{task_id}", project_id=project_id, task_id=task_id),
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
        category_id: str,
        brief: Optional[str] | Omit = omit,
        impact: Optional[int] | Omit = omit,
        reference_label: Optional[str] | Omit = omit,
        reference_url: Optional[str] | Omit = omit,
        summary: Optional[str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        topic: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
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
          project_id: Unique project ID.

          task_id: Unique project task ID.

          category_id: Category that owns the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._patch(
            path_template("/v1/projects/{project_id}/tasks/{task_id}", project_id=project_id, task_id=task_id),
            body=await async_maybe_transform(
                {
                    "brief": brief,
                    "impact": impact,
                    "reference_label": reference_label,
                    "reference_url": reference_url,
                    "summary": summary,
                    "title": title,
                    "topic": topic,
                    "type": type,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/v1/projects/{project_id}/tasks", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"category_id": category_id}, task_list_params.TaskListParams),
            ),
            cast_to=TaskListResponse,
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
          project_id: Unique project ID.

          task_id: Unique project task ID.

          category_id: Category that owns the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/projects/{project_id}/tasks/{task_id}", project_id=project_id, task_id=task_id),
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
        category_id: str,
        status: Literal["not_started", "in_progress", "done", "abandoned"],
        note: Optional[str] | Omit = omit,
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
          project_id: Unique project ID.

          task_id: Unique project task ID.

          category_id: Category that owns the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._post(
            path_template("/v1/projects/{project_id}/tasks/{task_id}/status", project_id=project_id, task_id=task_id),
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

        self.create = to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tasks.update,
        )
        self.list = to_raw_response_wrapper(
            tasks.list,
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

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tasks.update,
        )
        self.list = async_to_raw_response_wrapper(
            tasks.list,
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

        self.create = to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = to_streamed_response_wrapper(
            tasks.list,
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

        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tasks.delete,
        )
        self.update_status = async_to_streamed_response_wrapper(
            tasks.update_status,
        )
