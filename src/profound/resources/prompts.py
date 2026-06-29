# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import prompt_answers_params, prompt_answers_v2_params, prompt_stream_answers_v2_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.prompt_answers_v2_response import PromptAnswersV2Response

__all__ = ["PromptsResource", "AsyncPromptsResource"]


class PromptsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return PromptsResourceWithStreamingResponse(self)

    def answers(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        filters: Iterable[prompt_answers_params.Filter] | Omit = omit,
        include: prompt_answers_params.Include | Omit = omit,
        pagination: Pagination | Omit = omit,
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
          filters: List of filters to apply to the answers report.

          pagination: Pagination parameters for the results. Default is 10,000 rows with no offset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/prompts/answers",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "filters": filters,
                    "include": include,
                    "pagination": pagination,
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
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[prompt_answers_v2_params.Filter] | Omit = omit,
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
                    "search_queries",
                    "analysis_types",
                    "sentiment_claims",
                ]
            ]
        ]
        | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
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
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          include: Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`,
              `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`,
              `citations`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for
              all of them.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/prompts/answers",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "include": include,
                    "limit": limit,
                    "max_results": max_results,
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
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[prompt_stream_answers_v2_params.Filter] | Omit = omit,
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
                    "search_queries",
                    "analysis_types",
                    "sentiment_claims",
                ]
            ]
        ]
        | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stream Answers V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          include: Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`,
              `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`,
              `citations`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for
              all of them.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v2/prompts/answers/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "include": include,
                    "limit": limit,
                    "max_results": max_results,
                },
                prompt_stream_answers_v2_params.PromptStreamAnswersV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPromptsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncPromptsResourceWithStreamingResponse(self)

    async def answers(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        filters: Iterable[prompt_answers_params.Filter] | Omit = omit,
        include: prompt_answers_params.Include | Omit = omit,
        pagination: Pagination | Omit = omit,
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
          filters: List of filters to apply to the answers report.

          pagination: Pagination parameters for the results. Default is 10,000 rows with no offset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/prompts/answers",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "filters": filters,
                    "include": include,
                    "pagination": pagination,
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
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[prompt_answers_v2_params.Filter] | Omit = omit,
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
                    "search_queries",
                    "analysis_types",
                    "sentiment_claims",
                ]
            ]
        ]
        | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
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
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          include: Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`,
              `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`,
              `citations`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for
              all of them.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/prompts/answers",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "include": include,
                    "limit": limit,
                    "max_results": max_results,
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
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[prompt_stream_answers_v2_params.Filter] | Omit = omit,
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
                    "search_queries",
                    "analysis_types",
                    "sentiment_claims",
                ]
            ]
        ]
        | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stream Answers V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          include: Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`,
              `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`,
              `citations`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for
              all of them.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v2/prompts/answers/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "include": include,
                    "limit": limit,
                    "max_results": max_results,
                },
                prompt_stream_answers_v2_params.PromptStreamAnswersV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
