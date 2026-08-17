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
from ...types.report_response import ReportResponse
from ...types.pagination import Pagination
from ...types.path_filter import PathFilter
from ...types.bot_name_filter import BotNameFilter
from ...types.bot_provider_filter import BotProviderFilter
from ...types.reports import bot_create_report_v1_v1_reports_post_params
from ...types.report_response import ReportResponse
from ...types.pagination import Pagination
from ...types.path_filter import PathFilter
from ...types.bot_name_filter import BotNameFilter
from ...types.bot_provider_filter import BotProviderFilter
from ...types.reports import bot_create_report_v2_v2_reports_post_params

__all__ = ["BotsResource", "AsyncBotsResource"]


class BotsResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> BotsResourceWithRawResponse:
        return BotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BotsResourceWithStreamingResponse:
        return BotsResourceWithStreamingResponse(self)

    def create_report_v1_v1_reports_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["date", "path", "bot_name", "bot_provider"]] | Omit = omit,
        metrics: Iterable[Literal["count", "citations", "indexing", "training", "last_visit"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        domain: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        metric_filters: Iterable[bot_create_report_v1_v1_reports_post_params.MetricFilter] | Omit = omit,
        filters: Iterable[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get bot traffic report from the daily aggregated materialized view.
        
        This endpoint queries pre-aggregated daily bot data, making it efficient
        for large date ranges and high-traffic sites.
        
        Metrics:
        - count: unique bot visits
        - citations: unique citation events
        - indexing: unique indexing events
        - training: unique training events
        - last_visit: most recent visit timestamp
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering of the report results.
            pagination: Pagination settings for the report results.
            domain: Domain to query logs for.
            start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS, or full ISO timestamp.
            end_date: End date for logs. Accepts same formats as start_date. Defaults to now if omitted.
            organization_id: Body parameter.
            metric_filters: Numeric filters applied after report metrics are calculated.
            filters: Filters for bots report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ReportResponse: Successful Response
        
        Example:
            ```python
            bot = client.reports.bots.create_report_v1_v1_reports_post(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                domain="",
                start_date="",
            )
            ```
        """
        return self._post(
            "/v1/reports/bots",
            body=maybe_transform(
            {
            "date_interval": date_interval,
            "dimensions": dimensions,
            "metrics": metrics,
            "order_by": order_by,
            "pagination": pagination,
            "domain": domain,
            "start_date": start_date,
            "end_date": end_date,
            "organization_id": organization_id,
            "metric_filters": metric_filters,
            "filters": filters,
        },
            bot_create_report_v1_v1_reports_post_params.BotCreateReportV1V1ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReportResponse,
        )

    def create_report_v2_v2_reports_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["date", "hour", "path", "bot_name", "bot_provider", "bot_type"]] | Omit = omit,
        metrics: Iterable[Literal["count", "citations", "indexing", "training", "last_visit"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        domain: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        metric_filters: Iterable[bot_create_report_v2_v2_reports_post_params.MetricFilter] | Omit = omit,
        filters: Iterable[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get bot traffic report from the hourly aggregated materialized view (UTC-based).
        
        Supports date_interval="hour", calendar intervals through "year", "quarter", and "relative_week".
        
        Metrics:
        - count: unique bot visits
        - citations: unique citation events (ai_assistant bot type)
        - indexing: unique indexing events (index bot type)
        - training: unique training events (ai_training bot type)
        - last_visit: most recent visit timestamp
        
        Dimensions:
        - date, path, bot_name, bot_provider, bot_type
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering of the report results.
            pagination: Pagination settings for the report results.
            domain: Domain to query logs for.
            start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS, or full ISO timestamp.
            end_date: End date in UTC. Accepts same formats as start_date. Defaults to now UTC if omitted.
            organization_id: Body parameter.
            metric_filters: Numeric filters applied after report metrics are calculated.
            filters: Filters for bots report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ReportResponse: Successful Response
        
        Example:
            ```python
            bot = client.reports.bots.create_report_v2_v2_reports_post(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                domain="",
                start_date="",
            )
            ```
        """
        return self._post(
            "/v2/reports/bots",
            body=maybe_transform(
            {
            "date_interval": date_interval,
            "dimensions": dimensions,
            "metrics": metrics,
            "order_by": order_by,
            "pagination": pagination,
            "domain": domain,
            "start_date": start_date,
            "end_date": end_date,
            "organization_id": organization_id,
            "metric_filters": metric_filters,
            "filters": filters,
        },
            bot_create_report_v2_v2_reports_post_params.BotCreateReportV2V2ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReportResponse,
        )


class AsyncBotsResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncBotsResourceWithRawResponse:
        return AsyncBotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBotsResourceWithStreamingResponse:
        return AsyncBotsResourceWithStreamingResponse(self)

    async def create_report_v1_v1_reports_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["date", "path", "bot_name", "bot_provider"]] | Omit = omit,
        metrics: Iterable[Literal["count", "citations", "indexing", "training", "last_visit"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        domain: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        metric_filters: Iterable[bot_create_report_v1_v1_reports_post_params.MetricFilter] | Omit = omit,
        filters: Iterable[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get bot traffic report from the daily aggregated materialized view.
        
        This endpoint queries pre-aggregated daily bot data, making it efficient
        for large date ranges and high-traffic sites.
        
        Metrics:
        - count: unique bot visits
        - citations: unique citation events
        - indexing: unique indexing events
        - training: unique training events
        - last_visit: most recent visit timestamp
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering of the report results.
            pagination: Pagination settings for the report results.
            domain: Domain to query logs for.
            start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS, or full ISO timestamp.
            end_date: End date for logs. Accepts same formats as start_date. Defaults to now if omitted.
            organization_id: Body parameter.
            metric_filters: Numeric filters applied after report metrics are calculated.
            filters: Filters for bots report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ReportResponse: Successful Response
        
        Example:
            ```python
            bot = await client.reports.bots.create_report_v1_v1_reports_post(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                domain="",
                start_date="",
            )
            ```
        """
        return await self._post(
            "/v1/reports/bots",
            body=await async_maybe_transform(
            {
            "date_interval": date_interval,
            "dimensions": dimensions,
            "metrics": metrics,
            "order_by": order_by,
            "pagination": pagination,
            "domain": domain,
            "start_date": start_date,
            "end_date": end_date,
            "organization_id": organization_id,
            "metric_filters": metric_filters,
            "filters": filters,
        },
            bot_create_report_v1_v1_reports_post_params.BotCreateReportV1V1ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReportResponse,
        )

    async def create_report_v2_v2_reports_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["date", "hour", "path", "bot_name", "bot_provider", "bot_type"]] | Omit = omit,
        metrics: Iterable[Literal["count", "citations", "indexing", "training", "last_visit"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        domain: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        metric_filters: Iterable[bot_create_report_v2_v2_reports_post_params.MetricFilter] | Omit = omit,
        filters: Iterable[object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get bot traffic report from the hourly aggregated materialized view (UTC-based).
        
        Supports date_interval="hour", calendar intervals through "year", "quarter", and "relative_week".
        
        Metrics:
        - count: unique bot visits
        - citations: unique citation events (ai_assistant bot type)
        - indexing: unique indexing events (index bot type)
        - training: unique training events (ai_training bot type)
        - last_visit: most recent visit timestamp
        
        Dimensions:
        - date, path, bot_name, bot_provider, bot_type
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering of the report results.
            pagination: Pagination settings for the report results.
            domain: Domain to query logs for.
            start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS, or full ISO timestamp.
            end_date: End date in UTC. Accepts same formats as start_date. Defaults to now UTC if omitted.
            organization_id: Body parameter.
            metric_filters: Numeric filters applied after report metrics are calculated.
            filters: Filters for bots report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ReportResponse: Successful Response
        
        Example:
            ```python
            bot = await client.reports.bots.create_report_v2_v2_reports_post(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                domain="",
                start_date="",
            )
            ```
        """
        return await self._post(
            "/v2/reports/bots",
            body=await async_maybe_transform(
            {
            "date_interval": date_interval,
            "dimensions": dimensions,
            "metrics": metrics,
            "order_by": order_by,
            "pagination": pagination,
            "domain": domain,
            "start_date": start_date,
            "end_date": end_date,
            "organization_id": organization_id,
            "metric_filters": metric_filters,
            "filters": filters,
        },
            bot_create_report_v2_v2_reports_post_params.BotCreateReportV2V2ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReportResponse,
        )


class BotsResourceWithRawResponse:
    def __init__(self, bots: BotsResource) -> None:
        self._bots = bots

        self.create_report_v1_v1_reports_post = to_raw_response_wrapper(
            bots.create_report_v1_v1_reports_post,
        )
        self.create_report_v2_v2_reports_post = to_raw_response_wrapper(
            bots.create_report_v2_v2_reports_post,
        )


class AsyncBotsResourceWithRawResponse:
    def __init__(self, bots: AsyncBotsResource) -> None:
        self._bots = bots

        self.create_report_v1_v1_reports_post = async_to_raw_response_wrapper(
            bots.create_report_v1_v1_reports_post,
        )
        self.create_report_v2_v2_reports_post = async_to_raw_response_wrapper(
            bots.create_report_v2_v2_reports_post,
        )


class BotsResourceWithStreamingResponse:
    def __init__(self, bots: BotsResource) -> None:
        self._bots = bots

        self.create_report_v1_v1_reports_post = to_streamed_response_wrapper(
            bots.create_report_v1_v1_reports_post,
        )
        self.create_report_v2_v2_reports_post = to_streamed_response_wrapper(
            bots.create_report_v2_v2_reports_post,
        )


class AsyncBotsResourceWithStreamingResponse:
    def __init__(self, bots: AsyncBotsResource) -> None:
        self._bots = bots

        self.create_report_v1_v1_reports_post = async_to_streamed_response_wrapper(
            bots.create_report_v1_v1_reports_post,
        )
        self.create_report_v2_v2_reports_post = async_to_streamed_response_wrapper(
            bots.create_report_v2_v2_reports_post,
        )
