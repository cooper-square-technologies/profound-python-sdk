# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Optional, Union
from datetime import datetime
from typing_extensions import Literal

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
from ..._streaming import Stream, AsyncStream
from ...types.prompts.answer_create_v1_prompts_post_response import AnswerCreateV1PromptsPostResponse, AnswersResponseInfo, AnswersRawData, CitationDetail, CitationDetailGroup, SentimentTheme
from ...types.pagination import Pagination
from ...types.region_id_filter import RegionIdFilter
from ...types.region_name_filter import RegionNameFilter
from ...types.model_id_filter import ModelIdFilter
from ...types.tag_id_filter import TagIdFilter
from ...types.analysis_type_filter import AnalysisTypeFilter
from ...types.prompt_type_filter import PromptTypeFilter
from ...types.prompt_filter import PromptFilter
from ...types.persona_id_filter import PersonaIdFilter
from ...types.topic_id_filter import TopicIdFilter
from ...types.asset_id_filter import AssetIdFilter
from ...types.prompts import answer_create_v1_prompts_post_params
from ...types.prompts.answer_query_v2_v2_prompts_post_response import AnswerQueryV2V2PromptsPostResponse
from ...types.prompts import answer_query_v2_v2_prompts_post_params
from ...types.prompts import answer_stream_v2_v2_prompts_stream_post_params

__all__ = ["AnswersResource", "AsyncAnswersResource"]


class AnswersResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AnswersResourceWithRawResponse:
        return AnswersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnswersResourceWithStreamingResponse:
        return AnswersResourceWithStreamingResponse(self)

    def create_v1_prompts_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        pagination: Pagination | Omit = omit,
        filters: Iterable[object] | Omit = omit,
        include: answer_create_v1_prompts_post_params.Include | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnswerCreateV1PromptsPostResponse:
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
            AnswerCreateV1PromptsPostResponse: Successful Response
        
        Example:
            ```python
            answer = client.prompts.answers.create_v1_prompts_post(
                category_id="",
                start_date="",
                end_date="",
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
            answer_create_v1_prompts_post_params.AnswerCreateV1PromptsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AnswerCreateV1PromptsPostResponse,
        )

    def query_v2_v2_prompts_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        include: Optional[Iterable[Literal["run_id", "date", "model", "topic", "topic_id", "persona", "region", "tags", "prompt", "prompt_id", "response", "mentions", "citations", "search_queries", "analysis_types", "sentiment_claims"]]] | Omit = omit,
        filter: Optional[answer_query_v2_v2_prompts_post_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnswerQueryV2V2PromptsPostResponse:
        """
        Query Answers V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            include: Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`, `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`, `citations`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for all of them.
            filter: and/or/not tree over `model`, `topic`, `region`, `persona`, `prompt`, `tag`, `analysis_type` (visibility/sentiment/factcheck); plus top-level `and` leaves `domain` or `page` (`is` one value, or `in` a list). Substring-search the prompt with `{"field": "prompt", "op": "contains", "value": "…"}`.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AnswerQueryV2V2PromptsPostResponse: Successful Response
        
        Example:
            ```python
            answer = client.prompts.answers.query_v2_v2_prompts_post(
                category_id="",
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
            answer_query_v2_v2_prompts_post_params.AnswerQueryV2V2PromptsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AnswerQueryV2V2PromptsPostResponse,
        )

    def stream_v2_v2_prompts_stream_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        include: Optional[Iterable[Literal["run_id", "date", "model", "topic", "topic_id", "persona", "region", "tags", "prompt", "prompt_id", "response", "mentions", "citations", "search_queries", "analysis_types", "sentiment_claims"]]] | Omit = omit,
        filter: Optional[answer_stream_v2_v2_prompts_stream_post_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[str]:
        """
        Stream Answers V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            include: Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`, `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`, `citations`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for all of them.
            filter: and/or/not tree over `model`, `topic`, `region`, `persona`, `prompt`, `tag`, `analysis_type` (visibility/sentiment/factcheck); plus top-level `and` leaves `domain` or `page` (`is` one value, or `in` a list). Substring-search the prompt with `{"field": "prompt", "op": "contains", "value": "…"}`.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            Stream[str]: Successful Response
        
        Example:
            ```python
            stream = client.prompts.answers.stream_v2_v2_prompts_stream_post(
                category_id="",
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
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
            stream=True,
            stream_cls=Stream[str],
        )


class AsyncAnswersResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncAnswersResourceWithRawResponse:
        return AsyncAnswersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnswersResourceWithStreamingResponse:
        return AsyncAnswersResourceWithStreamingResponse(self)

    async def create_v1_prompts_post(
        self,
        *,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        pagination: Pagination | Omit = omit,
        filters: Iterable[object] | Omit = omit,
        include: answer_create_v1_prompts_post_params.Include | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnswerCreateV1PromptsPostResponse:
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
            AnswerCreateV1PromptsPostResponse: Successful Response
        
        Example:
            ```python
            answer = await client.prompts.answers.create_v1_prompts_post(
                category_id="",
                start_date="",
                end_date="",
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
            answer_create_v1_prompts_post_params.AnswerCreateV1PromptsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AnswerCreateV1PromptsPostResponse,
        )

    async def query_v2_v2_prompts_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        include: Optional[Iterable[Literal["run_id", "date", "model", "topic", "topic_id", "persona", "region", "tags", "prompt", "prompt_id", "response", "mentions", "citations", "search_queries", "analysis_types", "sentiment_claims"]]] | Omit = omit,
        filter: Optional[answer_query_v2_v2_prompts_post_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnswerQueryV2V2PromptsPostResponse:
        """
        Query Answers V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            include: Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`, `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`, `citations`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for all of them.
            filter: and/or/not tree over `model`, `topic`, `region`, `persona`, `prompt`, `tag`, `analysis_type` (visibility/sentiment/factcheck); plus top-level `and` leaves `domain` or `page` (`is` one value, or `in` a list). Substring-search the prompt with `{"field": "prompt", "op": "contains", "value": "…"}`.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AnswerQueryV2V2PromptsPostResponse: Successful Response
        
        Example:
            ```python
            answer = await client.prompts.answers.query_v2_v2_prompts_post(
                category_id="",
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
            answer_query_v2_v2_prompts_post_params.AnswerQueryV2V2PromptsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AnswerQueryV2V2PromptsPostResponse,
        )

    async def stream_v2_v2_prompts_stream_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        include: Optional[Iterable[Literal["run_id", "date", "model", "topic", "topic_id", "persona", "region", "tags", "prompt", "prompt_id", "response", "mentions", "citations", "search_queries", "analysis_types", "sentiment_claims"]]] | Omit = omit,
        filter: Optional[answer_stream_v2_v2_prompts_stream_post_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[str]:
        """
        Stream Answers V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            include: Which row fields to return: `run_id`, `date`, `model`, `topic`, `topic_id`, `region`, `persona`, `tags`, `prompt`, `prompt_id`, `response`, `mentions`, `citations`, `search_queries`, `analysis_types`, `sentiment_claims`. Omit for all of them.
            filter: and/or/not tree over `model`, `topic`, `region`, `persona`, `prompt`, `tag`, `analysis_type` (visibility/sentiment/factcheck); plus top-level `and` leaves `domain` or `page` (`is` one value, or `in` a list). Substring-search the prompt with `{"field": "prompt", "op": "contains", "value": "…"}`.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AsyncStream[str]: Successful Response
        
        Example:
            ```python
            stream = await client.prompts.answers.stream_v2_v2_prompts_stream_post(
                category_id="",
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
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[str],
        )


class AnswersResourceWithRawResponse:
    def __init__(self, answers: AnswersResource) -> None:
        self._answers = answers

        self.create_v1_prompts_post = to_raw_response_wrapper(
            answers.create_v1_prompts_post,
        )
        self.query_v2_v2_prompts_post = to_raw_response_wrapper(
            answers.query_v2_v2_prompts_post,
        )
        self.stream_v2_v2_prompts_stream_post = to_raw_response_wrapper(
            answers.stream_v2_v2_prompts_stream_post,
        )


class AsyncAnswersResourceWithRawResponse:
    def __init__(self, answers: AsyncAnswersResource) -> None:
        self._answers = answers

        self.create_v1_prompts_post = async_to_raw_response_wrapper(
            answers.create_v1_prompts_post,
        )
        self.query_v2_v2_prompts_post = async_to_raw_response_wrapper(
            answers.query_v2_v2_prompts_post,
        )
        self.stream_v2_v2_prompts_stream_post = async_to_raw_response_wrapper(
            answers.stream_v2_v2_prompts_stream_post,
        )


class AnswersResourceWithStreamingResponse:
    def __init__(self, answers: AnswersResource) -> None:
        self._answers = answers

        self.create_v1_prompts_post = to_streamed_response_wrapper(
            answers.create_v1_prompts_post,
        )
        self.query_v2_v2_prompts_post = to_streamed_response_wrapper(
            answers.query_v2_v2_prompts_post,
        )
        self.stream_v2_v2_prompts_stream_post = to_streamed_response_wrapper(
            answers.stream_v2_v2_prompts_stream_post,
        )


class AsyncAnswersResourceWithStreamingResponse:
    def __init__(self, answers: AsyncAnswersResource) -> None:
        self._answers = answers

        self.create_v1_prompts_post = async_to_streamed_response_wrapper(
            answers.create_v1_prompts_post,
        )
        self.query_v2_v2_prompts_post = async_to_streamed_response_wrapper(
            answers.query_v2_v2_prompts_post,
        )
        self.stream_v2_v2_prompts_stream_post = async_to_streamed_response_wrapper(
            answers.stream_v2_v2_prompts_stream_post,
        )
