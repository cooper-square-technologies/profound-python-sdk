# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, Iterable, Optional, Union
from datetime import datetime
from typing_extensions import Literal
from ..._types import SequenceNotStr

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
from ...types.topic_name_filter import TopicNameFilter
from ...types.tag_id_filter import TagIdFilter
from ...types.tag_name_filter import TagNameFilter
from ...types.prompt_id_filter import PromptIdFilter
from ...types.prompt_filter import PromptFilter
from ...types.persona_id_filter import PersonaIdFilter
from ...types.reports import visibility_query_v1_reports_post_params
from ...types.reports.visibility_stream_v1_reports_stream_post_response import VisibilityStreamV1ReportsStreamPostResponse, Query, VisibilityStreamV1ReportsStreamPostResponse2
from ...types.pagination import Pagination
from ...types.region_id_filter import RegionIdFilter
from ...types.region_name_filter import RegionNameFilter
from ...types.model_id_filter import ModelIdFilter
from ...types.topic_id_filter import TopicIdFilter
from ...types.topic_name_filter import TopicNameFilter
from ...types.tag_id_filter import TagIdFilter
from ...types.tag_name_filter import TagNameFilter
from ...types.prompt_id_filter import PromptIdFilter
from ...types.prompt_filter import PromptFilter
from ...types.persona_id_filter import PersonaIdFilter
from ...types.reports import visibility_stream_v1_reports_stream_post_params
from ...types.reports.visibility_query_v2_v2_reports_post_response import VisibilityQueryV2V2ReportsPostResponse
from ...types.reports import visibility_query_v2_v2_reports_post_params
from ...types.reports import visibility_stream_v2_v2_reports_stream_post_params

__all__ = ["VisibilityResource", "AsyncVisibilityResource"]


class VisibilityResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> VisibilityResourceWithRawResponse:
        return VisibilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VisibilityResourceWithStreamingResponse:
        return VisibilityResourceWithStreamingResponse(self)

    def query_v1_reports_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["date", "region", "topic", "topic_id", "model", "asset_id", "asset_name", "prompt", "prompt_id", "tag", "persona"]] | Omit = omit,
        metrics: Iterable[Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]],
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
        Query visibility report.
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering of the report results.
            pagination: Pagination settings for the report results.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the visibility report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ReportResponse: Successful Response
        
        Example:
            ```python
            visibility = client.reports.visibility.query_v1_reports_post(
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
            "/v1/reports/visibility",
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
            visibility_query_v1_reports_post_params.VisibilityQueryV1ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReportResponse,
        )

    def stream_v1_reports_stream_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["date", "region", "topic", "topic_id", "model", "asset_id", "asset_name", "prompt", "prompt_id", "tag", "persona"]] | Omit = omit,
        metrics: Iterable[Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
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
    ) -> Stream[VisibilityStreamV1ReportsStreamPostResponse]:
        """
        Stream Visibility
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering of the report results.
            pagination: Body parameter.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the visibility report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            Stream[VisibilityStreamV1ReportsStreamPostResponse]: Server-sent events stream. Emits a `summary` event first, then one `row` event per streamed row.
        
        Example:
            ```python
            stream = client.reports.visibility.stream_v1_reports_stream_post(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
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
            "/v1/reports/visibility/stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=VisibilityStreamV1ReportsStreamPostResponse,
            stream=True,
            stream_cls=Stream[VisibilityStreamV1ReportsStreamPostResponse],
        )

    def query_v2_v2_reports_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: Iterable[Literal["date", "model", "topic", "region", "prompt", "persona"]] | Omit = omit,
        metrics: Optional[Iterable[Literal["visibility_score", "share_of_voice", "average_position"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        assets: Optional[Union[str, SequenceNotStr[str], object]] | Omit = omit,
        filter: Optional[visibility_query_v2_v2_reports_post_params.Filter] | Omit = omit,
        sort: visibility_query_v2_v2_reports_post_params.Sort | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VisibilityQueryV2V2ReportsPostResponse:
        """
        Query Visibility V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            scope: Body parameter.
            assets: A name (`is`), a list (`in`), or {op,value} with op `is`/`in`/`not_in`.
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
            VisibilityQueryV2V2ReportsPostResponse: Successful Response
        
        Example:
            ```python
            visibility = client.reports.visibility.query_v2_v2_reports_post(
                category_id="",
                start_date="",
                end_date="",
                interval="day",
                scope="owned",
            )
            ```
        """
        return self._post(
            "/v2/reports/visibility",
            body=maybe_transform(
            {
            "category_id": category_id,
            "start_date": start_date,
            "end_date": end_date,
            "group_by": group_by,
            "metrics": metrics,
            "interval": interval,
            "scope": scope,
            "assets": assets,
            "filter": filter,
            "sort": sort,
            "limit": limit,
            "max_results": max_results,
            "cursor": cursor,
        },
            visibility_query_v2_v2_reports_post_params.VisibilityQueryV2V2ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=VisibilityQueryV2V2ReportsPostResponse,
        )

    def stream_v2_v2_reports_stream_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: Iterable[Literal["date", "model", "topic", "region", "prompt", "persona"]] | Omit = omit,
        metrics: Optional[Iterable[Literal["visibility_score", "share_of_voice", "average_position"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        assets: Optional[Union[str, SequenceNotStr[str], object]] | Omit = omit,
        filter: Optional[visibility_stream_v2_v2_reports_stream_post_params.Filter] | Omit = omit,
        sort: visibility_stream_v2_v2_reports_stream_post_params.Sort | Omit = omit,
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
        Stream Visibility V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            scope: Body parameter.
            assets: A name (`is`), a list (`in`), or {op,value} with op `is`/`in`/`not_in`.
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
            stream = client.reports.visibility.stream_v2_v2_reports_stream_post(
                category_id="",
                start_date="",
                end_date="",
                interval="day",
                scope="owned",
            )
            for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/visibility/stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
            stream=True,
            stream_cls=Stream[str],
        )


class AsyncVisibilityResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncVisibilityResourceWithRawResponse:
        return AsyncVisibilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVisibilityResourceWithStreamingResponse:
        return AsyncVisibilityResourceWithStreamingResponse(self)

    async def query_v1_reports_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["date", "region", "topic", "topic_id", "model", "asset_id", "asset_name", "prompt", "prompt_id", "tag", "persona"]] | Omit = omit,
        metrics: Iterable[Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]],
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
        Query visibility report.
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering of the report results.
            pagination: Pagination settings for the report results.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the visibility report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ReportResponse: Successful Response
        
        Example:
            ```python
            visibility = await client.reports.visibility.query_v1_reports_post(
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
            "/v1/reports/visibility",
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
            visibility_query_v1_reports_post_params.VisibilityQueryV1ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReportResponse,
        )

    async def stream_v1_reports_stream_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["date", "region", "topic", "topic_id", "model", "asset_id", "asset_name", "prompt", "prompt_id", "tag", "persona"]] | Omit = omit,
        metrics: Iterable[Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
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
    ) -> AsyncStream[VisibilityStreamV1ReportsStreamPostResponse]:
        """
        Stream Visibility
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering of the report results.
            pagination: Body parameter.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the visibility report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AsyncStream[VisibilityStreamV1ReportsStreamPostResponse]: Server-sent events stream. Emits a `summary` event first, then one `row` event per streamed row.
        
        Example:
            ```python
            stream = await client.reports.visibility.stream_v1_reports_stream_post(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
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
            "/v1/reports/visibility/stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=VisibilityStreamV1ReportsStreamPostResponse,
            stream=True,
            stream_cls=AsyncStream[VisibilityStreamV1ReportsStreamPostResponse],
        )

    async def query_v2_v2_reports_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: Iterable[Literal["date", "model", "topic", "region", "prompt", "persona"]] | Omit = omit,
        metrics: Optional[Iterable[Literal["visibility_score", "share_of_voice", "average_position"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        assets: Optional[Union[str, SequenceNotStr[str], object]] | Omit = omit,
        filter: Optional[visibility_query_v2_v2_reports_post_params.Filter] | Omit = omit,
        sort: visibility_query_v2_v2_reports_post_params.Sort | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VisibilityQueryV2V2ReportsPostResponse:
        """
        Query Visibility V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            scope: Body parameter.
            assets: A name (`is`), a list (`in`), or {op,value} with op `is`/`in`/`not_in`.
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
            VisibilityQueryV2V2ReportsPostResponse: Successful Response
        
        Example:
            ```python
            visibility = await client.reports.visibility.query_v2_v2_reports_post(
                category_id="",
                start_date="",
                end_date="",
                interval="day",
                scope="owned",
            )
            ```
        """
        return await self._post(
            "/v2/reports/visibility",
            body=await async_maybe_transform(
            {
            "category_id": category_id,
            "start_date": start_date,
            "end_date": end_date,
            "group_by": group_by,
            "metrics": metrics,
            "interval": interval,
            "scope": scope,
            "assets": assets,
            "filter": filter,
            "sort": sort,
            "limit": limit,
            "max_results": max_results,
            "cursor": cursor,
        },
            visibility_query_v2_v2_reports_post_params.VisibilityQueryV2V2ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=VisibilityQueryV2V2ReportsPostResponse,
        )

    async def stream_v2_v2_reports_stream_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: Iterable[Literal["date", "model", "topic", "region", "prompt", "persona"]] | Omit = omit,
        metrics: Optional[Iterable[Literal["visibility_score", "share_of_voice", "average_position"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        assets: Optional[Union[str, SequenceNotStr[str], object]] | Omit = omit,
        filter: Optional[visibility_stream_v2_v2_reports_stream_post_params.Filter] | Omit = omit,
        sort: visibility_stream_v2_v2_reports_stream_post_params.Sort | Omit = omit,
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
        Stream Visibility V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            scope: Body parameter.
            assets: A name (`is`), a list (`in`), or {op,value} with op `is`/`in`/`not_in`.
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
            stream = await client.reports.visibility.stream_v2_v2_reports_stream_post(
                category_id="",
                start_date="",
                end_date="",
                interval="day",
                scope="owned",
            )
            async for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/visibility/stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[str],
        )


class VisibilityResourceWithRawResponse:
    def __init__(self, visibility: VisibilityResource) -> None:
        self._visibility = visibility

        self.query_v1_reports_post = to_raw_response_wrapper(
            visibility.query_v1_reports_post,
        )
        self.stream_v1_reports_stream_post = to_raw_response_wrapper(
            visibility.stream_v1_reports_stream_post,
        )
        self.query_v2_v2_reports_post = to_raw_response_wrapper(
            visibility.query_v2_v2_reports_post,
        )
        self.stream_v2_v2_reports_stream_post = to_raw_response_wrapper(
            visibility.stream_v2_v2_reports_stream_post,
        )


class AsyncVisibilityResourceWithRawResponse:
    def __init__(self, visibility: AsyncVisibilityResource) -> None:
        self._visibility = visibility

        self.query_v1_reports_post = async_to_raw_response_wrapper(
            visibility.query_v1_reports_post,
        )
        self.stream_v1_reports_stream_post = async_to_raw_response_wrapper(
            visibility.stream_v1_reports_stream_post,
        )
        self.query_v2_v2_reports_post = async_to_raw_response_wrapper(
            visibility.query_v2_v2_reports_post,
        )
        self.stream_v2_v2_reports_stream_post = async_to_raw_response_wrapper(
            visibility.stream_v2_v2_reports_stream_post,
        )


class VisibilityResourceWithStreamingResponse:
    def __init__(self, visibility: VisibilityResource) -> None:
        self._visibility = visibility

        self.query_v1_reports_post = to_streamed_response_wrapper(
            visibility.query_v1_reports_post,
        )
        self.stream_v1_reports_stream_post = to_streamed_response_wrapper(
            visibility.stream_v1_reports_stream_post,
        )
        self.query_v2_v2_reports_post = to_streamed_response_wrapper(
            visibility.query_v2_v2_reports_post,
        )
        self.stream_v2_v2_reports_stream_post = to_streamed_response_wrapper(
            visibility.stream_v2_v2_reports_stream_post,
        )


class AsyncVisibilityResourceWithStreamingResponse:
    def __init__(self, visibility: AsyncVisibilityResource) -> None:
        self._visibility = visibility

        self.query_v1_reports_post = async_to_streamed_response_wrapper(
            visibility.query_v1_reports_post,
        )
        self.stream_v1_reports_stream_post = async_to_streamed_response_wrapper(
            visibility.stream_v1_reports_stream_post,
        )
        self.query_v2_v2_reports_post = async_to_streamed_response_wrapper(
            visibility.query_v2_v2_reports_post,
        )
        self.stream_v2_v2_reports_stream_post = async_to_streamed_response_wrapper(
            visibility.stream_v2_v2_reports_stream_post,
        )
