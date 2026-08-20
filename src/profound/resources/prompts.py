# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, List, Optional, Union
from datetime import datetime
from typing_extensions import Literal

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
from .._streaming import Stream, AsyncStream
from ..types.prompt_answers_response import PromptAnswersResponse
from ..types.shared_params.pagination import Pagination
from ..types import prompt_answers_params, prompt_answers_v2_params, prompt_stream_answers_v2_params
from ..types.prompt_answers_v2_response import PromptAnswersV2Response
from ..types.shared_params.filter_node import FilterNode
from ..types.prompt_stream_answers_v2_response import PromptStreamAnswersV2Response

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

    def answers_v2(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        include: Optional[
            List[
                Literal[
                    "run_id",
                    "date",
                    "model",
                    "topic",
                    "topic_id",
                    "persona",
                    "region",
                    "tags",
                    "prompt",
                    "prompt_id",
                    "response",
                    "mentions",
                    "citations",
                    "citation_details",
                    "search_queries",
                    "analysis_types",
                    "sentiment_claims",
                ]
            ]
        ]
        | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptAnswersV2Response:
        """
        Query Answers V2

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            include: Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`, `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`, `citations`, `citation_details`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for all fields except `citation_details`, which must be requested explicitly because it is expensive.
            filter: and/or/not tree over `model`, `topic`, `region`, `persona`, `prompt`, `tag`, `analysis_type` (visibility/sentiment/factcheck); plus top-level `and` leaves `domain` or `page` (`is` one value, or `in` a list). Substring-search the prompt with `{"field": "prompt", "op": "contains", "value": "…"}`.
            limit: Page size; default 10, max 200.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PromptAnswersV2Response: Successful Response

        Example:
            ```python
            prompt = client.prompts.answers_v2(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )
            ```
        """
        return self._post(
            "/v2/prompts/answers",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "include": include,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                prompt_answers_v2_params.PromptAnswersV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptAnswersV2Response,
        )

    def stream_answers_v2(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        include: Optional[
            List[
                Literal[
                    "run_id",
                    "date",
                    "model",
                    "topic",
                    "topic_id",
                    "persona",
                    "region",
                    "tags",
                    "prompt",
                    "prompt_id",
                    "response",
                    "mentions",
                    "citations",
                    "citation_details",
                    "search_queries",
                    "analysis_types",
                    "sentiment_claims",
                ]
            ]
        ]
        | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[PromptStreamAnswersV2Response]:
        """
        Stream Answers V2

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            include: Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`, `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`, `citations`, `citation_details`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for all fields except `citation_details`, which must be requested explicitly because it is expensive.
            filter: and/or/not tree over `model`, `topic`, `region`, `persona`, `prompt`, `tag`, `analysis_type` (visibility/sentiment/factcheck); plus top-level `and` leaves `domain` or `page` (`is` one value, or `in` a list). Substring-search the prompt with `{"field": "prompt", "op": "contains", "value": "…"}`.
            limit: Page size; default 10, max 200.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Stream[PromptStreamAnswersV2Response]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = client.prompts.stream_answers_v2(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )

            for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/prompts/answers/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "include": include,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                prompt_stream_answers_v2_params.PromptStreamAnswersV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptStreamAnswersV2Response,
            stream=True,
            stream_cls=Stream[PromptStreamAnswersV2Response],
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

    async def answers_v2(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        include: Optional[
            List[
                Literal[
                    "run_id",
                    "date",
                    "model",
                    "topic",
                    "topic_id",
                    "persona",
                    "region",
                    "tags",
                    "prompt",
                    "prompt_id",
                    "response",
                    "mentions",
                    "citations",
                    "citation_details",
                    "search_queries",
                    "analysis_types",
                    "sentiment_claims",
                ]
            ]
        ]
        | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptAnswersV2Response:
        """
        Query Answers V2

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            include: Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`, `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`, `citations`, `citation_details`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for all fields except `citation_details`, which must be requested explicitly because it is expensive.
            filter: and/or/not tree over `model`, `topic`, `region`, `persona`, `prompt`, `tag`, `analysis_type` (visibility/sentiment/factcheck); plus top-level `and` leaves `domain` or `page` (`is` one value, or `in` a list). Substring-search the prompt with `{"field": "prompt", "op": "contains", "value": "…"}`.
            limit: Page size; default 10, max 200.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PromptAnswersV2Response: Successful Response

        Example:
            ```python
            prompt = await client.prompts.answers_v2(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )
            ```
        """
        return await self._post(
            "/v2/prompts/answers",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "include": include,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                prompt_answers_v2_params.PromptAnswersV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptAnswersV2Response,
        )

    async def stream_answers_v2(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        include: Optional[
            List[
                Literal[
                    "run_id",
                    "date",
                    "model",
                    "topic",
                    "topic_id",
                    "persona",
                    "region",
                    "tags",
                    "prompt",
                    "prompt_id",
                    "response",
                    "mentions",
                    "citations",
                    "citation_details",
                    "search_queries",
                    "analysis_types",
                    "sentiment_claims",
                ]
            ]
        ]
        | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[PromptStreamAnswersV2Response]:
        """
        Stream Answers V2

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            include: Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`, `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`, `citations`, `citation_details`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for all fields except `citation_details`, which must be requested explicitly because it is expensive.
            filter: and/or/not tree over `model`, `topic`, `region`, `persona`, `prompt`, `tag`, `analysis_type` (visibility/sentiment/factcheck); plus top-level `and` leaves `domain` or `page` (`is` one value, or `in` a list). Substring-search the prompt with `{"field": "prompt", "op": "contains", "value": "…"}`.
            limit: Page size; default 10, max 200.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncStream[PromptStreamAnswersV2Response]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = await client.prompts.stream_answers_v2(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )

            async for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/prompts/answers/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "include": include,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                prompt_stream_answers_v2_params.PromptStreamAnswersV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptStreamAnswersV2Response,
            stream=True,
            stream_cls=AsyncStream[PromptStreamAnswersV2Response],
        )


class PromptsResourceWithRawResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts

        self.answers = to_raw_response_wrapper(
            prompts.answers,
        )
        self.answers_v2 = to_raw_response_wrapper(
            prompts.answers_v2,
        )
        self.stream_answers_v2 = to_raw_response_wrapper(
            prompts.stream_answers_v2,
        )


class AsyncPromptsResourceWithRawResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts

        self.answers = async_to_raw_response_wrapper(
            prompts.answers,
        )
        self.answers_v2 = async_to_raw_response_wrapper(
            prompts.answers_v2,
        )
        self.stream_answers_v2 = async_to_raw_response_wrapper(
            prompts.stream_answers_v2,
        )


class PromptsResourceWithStreamingResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts

        self.answers = to_streamed_response_wrapper(
            prompts.answers,
        )
        self.answers_v2 = to_streamed_response_wrapper(
            prompts.answers_v2,
        )
        self.stream_answers_v2 = to_streamed_response_wrapper(
            prompts.stream_answers_v2,
        )


class AsyncPromptsResourceWithStreamingResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts

        self.answers = async_to_streamed_response_wrapper(
            prompts.answers,
        )
        self.answers_v2 = async_to_streamed_response_wrapper(
            prompts.answers_v2,
        )
        self.stream_answers_v2 = async_to_streamed_response_wrapper(
            prompts.stream_answers_v2,
        )
