# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, Iterable, Optional, Union
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
from ...types.report_response import ReportResponse
from ...types.pagination import Pagination
from ...types.region_id_filter import RegionIdFilter
from ...types.region_name_filter import RegionNameFilter
from ...types.model_id_filter import ModelIdFilter
from ...types.topic_id_filter import TopicIdFilter
from ...types.tag_id_filter import TagIdFilter
from ...types.prompt_id_filter import PromptIdFilter
from ...types.persona_id_filter import PersonaIdFilter
from ...types.analysis_type_filter import AnalysisTypeFilter
from ...types.prompt_type_filter import PromptTypeFilter
from ...types.reports import query_fanout_v1_reports_post_params
from ...types.reports.query_fanout_v2_v2_reports_post_response import QueryFanoutV2V2ReportsPostResponse
from ...types.reports import query_fanout_v2_v2_reports_post_params
from ...types.reports import query_fanout_stream_v2_v2_reports_stream_post_params

__all__ = ["QueryFanoutsResource", "AsyncQueryFanoutsResource"]


class QueryFanoutsResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> QueryFanoutsResourceWithRawResponse:
        return QueryFanoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryFanoutsResourceWithStreamingResponse:
        return QueryFanoutsResourceWithStreamingResponse(self)

    def v1_reports_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["prompt", "query", "model", "region", "date"]] | Omit = omit,
        metrics: Iterable[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Query Fanouts
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering. Keys must be a requested metric or the ``date`` dimension. Values are ``asc`` or ``desc``. Defaults to first metric descending.
            pagination: Pagination settings for the report results.
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            filters: Filters to apply to the query fanout report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ReportResponse: Successful Response
        
        Example:
            ```python
            query_fanout = client.reports.query_fanouts.v1_reports_post(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="",
                start_date="",
                end_date="",
            )
            ```
        """
        return self._post(
            "/v1/reports/query-fanouts",
            body=maybe_transform(
            {
            "date_interval": date_interval,
            "dimensions": dimensions,
            "metrics": metrics,
            "order_by": order_by,
            "pagination": pagination,
            "category_id": category_id,
            "start_date": start_date,
            "end_date": end_date,
            "filters": filters,
        },
            query_fanout_v1_reports_post_params.QueryFanoutV1ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReportResponse,
        )

    def v2_v2_reports_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: Iterable[Literal["date", "model", "region", "prompt", "query"]] | Omit = omit,
        metrics: Optional[Iterable[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[query_fanout_v2_v2_reports_post_params.Filter] | Omit = omit,
        sort: Optional[query_fanout_v2_v2_reports_post_params.Sort] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryFanoutV2V2ReportsPostResponse:
        """
        Query Fanouts V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            filter: Body parameter.
            sort: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            QueryFanoutV2V2ReportsPostResponse: Successful Response
        
        Example:
            ```python
            query_fanout = client.reports.query_fanouts.v2_v2_reports_post(
                category_id="",
                start_date="",
                end_date="",
                interval="day",
            )
            ```
        """
        return self._post(
            "/v2/reports/query-fanouts",
            body=maybe_transform(
            {
            "category_id": category_id,
            "start_date": start_date,
            "end_date": end_date,
            "group_by": group_by,
            "metrics": metrics,
            "interval": interval,
            "filter": filter,
            "sort": sort,
            "limit": limit,
            "max_results": max_results,
            "cursor": cursor,
        },
            query_fanout_v2_v2_reports_post_params.QueryFanoutV2V2ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=QueryFanoutV2V2ReportsPostResponse,
        )

    def stream_v2_v2_reports_stream_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: Iterable[Literal["date", "model", "region", "prompt", "query"]] | Omit = omit,
        metrics: Optional[Iterable[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[query_fanout_stream_v2_v2_reports_stream_post_params.Filter] | Omit = omit,
        sort: Optional[query_fanout_stream_v2_v2_reports_stream_post_params.Sort] | Omit = omit,
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
        Stream Query Fanouts V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            filter: Body parameter.
            sort: Body parameter.
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
            stream = client.reports.query_fanouts.stream_v2_v2_reports_stream_post(
                category_id="",
                start_date="",
                end_date="",
                interval="day",
            )
            for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/query-fanouts/stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
            stream=True,
            stream_cls=Stream[str],
        )


class AsyncQueryFanoutsResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncQueryFanoutsResourceWithRawResponse:
        return AsyncQueryFanoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryFanoutsResourceWithStreamingResponse:
        return AsyncQueryFanoutsResourceWithStreamingResponse(self)

    async def v1_reports_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["prompt", "query", "model", "region", "date"]] | Omit = omit,
        metrics: Iterable[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Query Fanouts
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering. Keys must be a requested metric or the ``date`` dimension. Values are ``asc`` or ``desc``. Defaults to first metric descending.
            pagination: Pagination settings for the report results.
            category_id: Body parameter.
            start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            end_date: End date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.
            filters: Filters to apply to the query fanout report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ReportResponse: Successful Response
        
        Example:
            ```python
            query_fanout = await client.reports.query_fanouts.v1_reports_post(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="",
                start_date="",
                end_date="",
            )
            ```
        """
        return await self._post(
            "/v1/reports/query-fanouts",
            body=await async_maybe_transform(
            {
            "date_interval": date_interval,
            "dimensions": dimensions,
            "metrics": metrics,
            "order_by": order_by,
            "pagination": pagination,
            "category_id": category_id,
            "start_date": start_date,
            "end_date": end_date,
            "filters": filters,
        },
            query_fanout_v1_reports_post_params.QueryFanoutV1ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReportResponse,
        )

    async def v2_v2_reports_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: Iterable[Literal["date", "model", "region", "prompt", "query"]] | Omit = omit,
        metrics: Optional[Iterable[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[query_fanout_v2_v2_reports_post_params.Filter] | Omit = omit,
        sort: Optional[query_fanout_v2_v2_reports_post_params.Sort] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryFanoutV2V2ReportsPostResponse:
        """
        Query Fanouts V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            filter: Body parameter.
            sort: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            QueryFanoutV2V2ReportsPostResponse: Successful Response
        
        Example:
            ```python
            query_fanout = await client.reports.query_fanouts.v2_v2_reports_post(
                category_id="",
                start_date="",
                end_date="",
                interval="day",
            )
            ```
        """
        return await self._post(
            "/v2/reports/query-fanouts",
            body=await async_maybe_transform(
            {
            "category_id": category_id,
            "start_date": start_date,
            "end_date": end_date,
            "group_by": group_by,
            "metrics": metrics,
            "interval": interval,
            "filter": filter,
            "sort": sort,
            "limit": limit,
            "max_results": max_results,
            "cursor": cursor,
        },
            query_fanout_v2_v2_reports_post_params.QueryFanoutV2V2ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=QueryFanoutV2V2ReportsPostResponse,
        )

    async def stream_v2_v2_reports_stream_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: Iterable[Literal["date", "model", "region", "prompt", "query"]] | Omit = omit,
        metrics: Optional[Iterable[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        filter: Optional[query_fanout_stream_v2_v2_reports_stream_post_params.Filter] | Omit = omit,
        sort: Optional[query_fanout_stream_v2_v2_reports_stream_post_params.Sort] | Omit = omit,
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
        Stream Query Fanouts V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            filter: Body parameter.
            sort: Body parameter.
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
            stream = await client.reports.query_fanouts.stream_v2_v2_reports_stream_post(
                category_id="",
                start_date="",
                end_date="",
                interval="day",
            )
            async for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/query-fanouts/stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[str],
        )


class QueryFanoutsResourceWithRawResponse:
    def __init__(self, query_fanouts: QueryFanoutsResource) -> None:
        self._query_fanouts = query_fanouts

        self.v1_reports_post = to_raw_response_wrapper(
            query_fanouts.v1_reports_post,
        )
        self.v2_v2_reports_post = to_raw_response_wrapper(
            query_fanouts.v2_v2_reports_post,
        )
        self.stream_v2_v2_reports_stream_post = to_raw_response_wrapper(
            query_fanouts.stream_v2_v2_reports_stream_post,
        )


class AsyncQueryFanoutsResourceWithRawResponse:
    def __init__(self, query_fanouts: AsyncQueryFanoutsResource) -> None:
        self._query_fanouts = query_fanouts

        self.v1_reports_post = async_to_raw_response_wrapper(
            query_fanouts.v1_reports_post,
        )
        self.v2_v2_reports_post = async_to_raw_response_wrapper(
            query_fanouts.v2_v2_reports_post,
        )
        self.stream_v2_v2_reports_stream_post = async_to_raw_response_wrapper(
            query_fanouts.stream_v2_v2_reports_stream_post,
        )


class QueryFanoutsResourceWithStreamingResponse:
    def __init__(self, query_fanouts: QueryFanoutsResource) -> None:
        self._query_fanouts = query_fanouts

        self.v1_reports_post = to_streamed_response_wrapper(
            query_fanouts.v1_reports_post,
        )
        self.v2_v2_reports_post = to_streamed_response_wrapper(
            query_fanouts.v2_v2_reports_post,
        )
        self.stream_v2_v2_reports_stream_post = to_streamed_response_wrapper(
            query_fanouts.stream_v2_v2_reports_stream_post,
        )


class AsyncQueryFanoutsResourceWithStreamingResponse:
    def __init__(self, query_fanouts: AsyncQueryFanoutsResource) -> None:
        self._query_fanouts = query_fanouts

        self.v1_reports_post = async_to_streamed_response_wrapper(
            query_fanouts.v1_reports_post,
        )
        self.v2_v2_reports_post = async_to_streamed_response_wrapper(
            query_fanouts.v2_v2_reports_post,
        )
        self.stream_v2_v2_reports_stream_post = async_to_streamed_response_wrapper(
            query_fanouts.stream_v2_v2_reports_stream_post,
        )
