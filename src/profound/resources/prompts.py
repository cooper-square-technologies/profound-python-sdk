# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Union
from datetime import datetime

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.prompt_answers_response import PromptAnswersResponse
from ..types.shared_params.pagination import Pagination
from ..types import prompt_answers_params

__all__ = ["PromptsResource", "AsyncPromptsResource"]


class PromptsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptsResourceWithRawResponse:
        return PromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptsResourceWithStreamingResponse:
        return PromptsResourceWithStreamingResponse(self)

    def answers(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        pagination: Pagination | Omit = omit,
        filters: Iterable[prompt_answers_params.Filter] | Omit = omit,
        include: prompt_answers_params.Include | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptAnswersResponse:
        """
        Get Answers

        Args:
            category_id: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            pagination: Pagination parameters for the results. Default is 10,000 rows with no offset.
            filters: List of filters to apply to the answers report.
            include: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PromptAnswersResponse: Successful Response

        Example:
            ```python
            prompt = client.prompts.answers(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )
            ```
        """
        return self._post(
            "/v1/prompts/answers",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "pagination": pagination,
                    "filters": filters,
                    "include": include,
                },
                prompt_answers_params.PromptAnswersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptAnswersResponse,
        )


class AsyncPromptsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptsResourceWithRawResponse:
        return AsyncPromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptsResourceWithStreamingResponse:
        return AsyncPromptsResourceWithStreamingResponse(self)

    async def answers(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        pagination: Pagination | Omit = omit,
        filters: Iterable[prompt_answers_params.Filter] | Omit = omit,
        include: prompt_answers_params.Include | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptAnswersResponse:
        """
        Get Answers

        Args:
            category_id: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            pagination: Pagination parameters for the results. Default is 10,000 rows with no offset.
            filters: List of filters to apply to the answers report.
            include: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PromptAnswersResponse: Successful Response

        Example:
            ```python
            prompt = await client.prompts.answers(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )
            ```
        """
        return await self._post(
            "/v1/prompts/answers",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "pagination": pagination,
                    "filters": filters,
                    "include": include,
                },
                prompt_answers_params.PromptAnswersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptAnswersResponse,
        )


class PromptsResourceWithRawResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts

        self.answers = to_raw_response_wrapper(
            prompts.answers,
        )


class AsyncPromptsResourceWithRawResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts

        self.answers = async_to_raw_response_wrapper(
            prompts.answers,
        )


class PromptsResourceWithStreamingResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts

        self.answers = to_streamed_response_wrapper(
            prompts.answers,
        )


class AsyncPromptsResourceWithStreamingResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts

        self.answers = async_to_streamed_response_wrapper(
            prompts.answers,
        )
