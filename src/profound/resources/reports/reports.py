# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, Iterable, List, Optional, Union
from datetime import datetime
from typing_extensions import Literal
from ..._types import SequenceNotStr

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from .web_search_results import (
    WebSearchResultsResource,
    AsyncWebSearchResultsResource,
    WebSearchResultsResourceWithRawResponse,
    AsyncWebSearchResultsResourceWithRawResponse,
    WebSearchResultsResourceWithStreamingResponse,
    AsyncWebSearchResultsResourceWithStreamingResponse,
)
from .shopping import (
    ShoppingResource,
    AsyncShoppingResource,
    ShoppingResourceWithRawResponse,
    AsyncShoppingResourceWithRawResponse,
    ShoppingResourceWithStreamingResponse,
    AsyncShoppingResourceWithStreamingResponse,
)
from ...types.report_citations_response import ReportCitationsResponse
from ...types.shared_params.pagination import Pagination
from ...types import (
    report_citations_params,
    report_visibility_params,
    report_sentiment_params,
    report_get_referrals_report_params,
    report_get_bots_report_params,
    report_get_referrals_report_v2_params,
    report_get_bots_report_v2_params,
    report_query_fanouts_params,
    report_stream_citations_params,
    report_stream_visibility_params,
    report_stream_sentiment_params,
)
from ...types.report_response import ReportResponse
from ...types.report_stream_citations_response import ReportStreamCitationsResponse
from ...types.report_stream_visibility_response import ReportStreamVisibilityResponse
from ...types.report_stream_sentiment_response import ReportStreamSentimentResponse

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    @cached_property
    def web_search_results(self) -> WebSearchResultsResource:
        return WebSearchResultsResource(self._client)

    @cached_property
    def shopping(self) -> ShoppingResource:
        return ShoppingResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        return ReportsResourceWithStreamingResponse(self)

    def citations(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "hostname",
                "path",
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "tag",
                "prompt",
                "prompt_id",
                "url",
                "root_domain",
                "persona",
                "citation_category",
            ]
        ]
        | Omit = omit,
        metrics: List[Literal["count", "citation_share", "share_of_voice", "first_cited_at"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_citations_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCitationsResponse:
        """
        Get citations for a given category.

        The ``mentioned`` filter supports ``is true`` and ``is false``. It uses the
        latest page analysis available at or before ``end_date``; pages without an
        analysis by then are excluded from both values. ``citation_share`` keeps all
        otherwise eligible citations in its denominator when this filter is used.

        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Metrics to include. `share_of_voice` is deprecated, use `citation_share` instead.
            order_by: Custom ordering of the report results.
            pagination: Pagination settings for the report results.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the citations report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ReportCitationsResponse: Successful Response

        Example:
            ```python
            report = client.reports.citations(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )
            ```
        """
        return self._post(
            "/v1/reports/citations",
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
                report_citations_params.ReportCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportCitationsResponse,
        )

    def visibility(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "asset_id",
                "asset_name",
                "prompt",
                "prompt_id",
                "tag",
                "persona",
            ]
        ]
        | Omit = omit,
        metrics: List[
            Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]
        ],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_visibility_params.Filter] | Omit = omit,
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
            report = client.reports.visibility(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
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
                report_visibility_params.ReportVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def sentiment(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "theme",
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "asset_id",
                "asset_name",
                "tag",
                "prompt",
                "prompt_id",
                "sentiment_type",
                "persona",
            ]
        ]
        | Omit = omit,
        metrics: List[Literal["positive", "negative", "occurrences"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_sentiment_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get citations for a given category.

        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering of the report results.
            pagination: Pagination settings for the report results.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the sentiment report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ReportResponse: Successful Response

        Example:
            ```python
            report = client.reports.sentiment(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )
            ```
        """
        return self._post(
            "/v1/reports/sentiment",
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
                report_sentiment_params.ReportSentimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def get_referrals_report(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "host", "path", "referral_source"]] | Omit = omit,
        metrics: List[Literal["visits", "last_visit"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        domain: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        metric_filters: Iterable[report_get_referrals_report_params.MetricFilter] | Omit = omit,
        filters: Iterable[report_get_referrals_report_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get referral traffic report from the daily aggregated materialized view.

        This endpoint queries pre-aggregated daily referral data, making it efficient
        for large date ranges and high-traffic sites.

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
            filters: Filters for referrals report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ReportResponse: Successful Response

        Example:
            ```python
            report = client.reports.get_referrals_report(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                domain="",
                start_date="2024-01-01T00:00:00.000Z",
            )
            ```
        """
        return self._post(
            "/v1/reports/referrals",
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
                report_get_referrals_report_params.ReportGetReferralsReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def get_bots_report(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "host", "path", "bot_name", "bot_provider"]] | Omit = omit,
        metrics: List[Literal["count", "citations", "indexing", "training", "last_visit"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        domain: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        metric_filters: Iterable[report_get_bots_report_params.MetricFilter] | Omit = omit,
        filters: Iterable[report_get_bots_report_params.Filter] | Omit = omit,
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
            report = client.reports.get_bots_report(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                domain="",
                start_date="2024-01-01T00:00:00.000Z",
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
                report_get_bots_report_params.ReportGetBotsReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def get_referrals_report_v2(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "hour", "host", "path", "referral_source", "referral_type"]] | Omit = omit,
        metrics: List[Literal["visits", "last_visit"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        domain: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        timezone: str | Omit = omit,
        metric_filters: Iterable[report_get_referrals_report_v2_params.MetricFilter] | Omit = omit,
        filters: Iterable[report_get_referrals_report_v2_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get referral traffic report from the hourly aggregated materialized view (UTC-based).

        Supports date_interval="hour", calendar intervals through "year", "quarter", and "relative_week".

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
            timezone: IANA timezone name for date bucketing and filter boundaries.
            metric_filters: Numeric filters applied after report metrics are calculated.
            filters: Filters for referrals report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ReportResponse: Successful Response

        Example:
            ```python
            report = client.reports.get_referrals_report_v2(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                domain="",
                start_date="2024-01-01T00:00:00.000Z",
                timezone="UTC",
            )
            ```
        """
        return self._post(
            "/v2/reports/referrals",
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
                    "timezone": timezone,
                    "metric_filters": metric_filters,
                    "filters": filters,
                },
                report_get_referrals_report_v2_params.ReportGetReferralsReportV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def get_bots_report_v2(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "hour", "host", "path", "bot_name", "bot_provider", "bot_type"]] | Omit = omit,
        metrics: List[Literal["count", "citations", "indexing", "training", "last_visit", "agents"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        domain: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        timezone: str | Omit = omit,
        metric_filters: Iterable[report_get_bots_report_v2_params.MetricFilter] | Omit = omit,
        filters: Iterable[report_get_bots_report_v2_params.Filter] | Omit = omit,
        domain_id: Optional[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
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
            timezone: IANA timezone name for date bucketing and filter boundaries.
            metric_filters: Numeric filters applied after report metrics are calculated.
            filters: Filters for bots report.
            domain_id: Domain UUID used for tag lookups.
            tags: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ReportResponse: Successful Response

        Example:
            ```python
            report = client.reports.get_bots_report_v2(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                domain="",
                start_date="2024-01-01T00:00:00.000Z",
                timezone="UTC",
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
                    "timezone": timezone,
                    "metric_filters": metric_filters,
                    "filters": filters,
                    "domain_id": domain_id,
                    "tags": tags,
                },
                report_get_bots_report_v2_params.ReportGetBotsReportV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def query_fanouts(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["prompt", "query", "model", "region", "date"]] | Omit = omit,
        metrics: List[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_query_fanouts_params.Filter] | Omit = omit,
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
            metrics: Metrics to return for each row.
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
            report = client.reports.query_fanouts(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
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
                report_query_fanouts_params.ReportQueryFanoutsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def stream_citations(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "hostname",
                "path",
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "tag",
                "prompt",
                "prompt_id",
                "url",
                "root_domain",
                "persona",
                "citation_category",
            ]
        ]
        | Omit = omit,
        metrics: List[Literal["count", "citation_share", "share_of_voice", "first_cited_at"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_stream_citations_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ReportStreamCitationsResponse]:
        """
        Stream citations with the same filter semantics as the non-streaming route.

        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Metrics to include. `share_of_voice` is deprecated, use `citation_share` instead.
            order_by: Custom ordering of the report results.
            pagination: Body parameter.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the citations report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Stream[ReportStreamCitationsResponse]: Server-sent events stream. Emits a `summary` event first, then one `row` event per streamed row.

        Example:
            ```python
            stream = client.reports.stream_citations(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )

            for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v1/reports/citations/stream",
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
                report_stream_citations_params.ReportStreamCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportStreamCitationsResponse,
            stream=True,
            stream_cls=Stream[ReportStreamCitationsResponse],
        )

    def stream_visibility(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "asset_id",
                "asset_name",
                "prompt",
                "prompt_id",
                "tag",
                "persona",
            ]
        ]
        | Omit = omit,
        metrics: List[
            Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]
        ],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_stream_visibility_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ReportStreamVisibilityResponse]:
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
            Stream[ReportStreamVisibilityResponse]: Server-sent events stream. Emits a `summary` event first, then one `row` event per streamed row.

        Example:
            ```python
            stream = client.reports.stream_visibility(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )

            for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v1/reports/visibility/stream",
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
                report_stream_visibility_params.ReportStreamVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportStreamVisibilityResponse,
            stream=True,
            stream_cls=Stream[ReportStreamVisibilityResponse],
        )

    def stream_sentiment(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "theme",
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "asset_id",
                "asset_name",
                "tag",
                "prompt",
                "prompt_id",
                "sentiment_type",
                "persona",
            ]
        ]
        | Omit = omit,
        metrics: List[Literal["positive", "negative", "occurrences"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_stream_sentiment_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ReportStreamSentimentResponse]:
        """
        Stream Sentiment

        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering of the report results.
            pagination: Body parameter.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the sentiment report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Stream[ReportStreamSentimentResponse]: Server-sent events stream. Emits a `summary` event first, then one `row` event per streamed row.

        Example:
            ```python
            stream = client.reports.stream_sentiment(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )

            for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v1/reports/sentiment/stream",
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
                report_stream_sentiment_params.ReportStreamSentimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportStreamSentimentResponse,
            stream=True,
            stream_cls=Stream[ReportStreamSentimentResponse],
        )


class AsyncReportsResource(AsyncAPIResource):
    @cached_property
    def web_search_results(self) -> AsyncWebSearchResultsResource:
        return AsyncWebSearchResultsResource(self._client)

    @cached_property
    def shopping(self) -> AsyncShoppingResource:
        return AsyncShoppingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        return AsyncReportsResourceWithStreamingResponse(self)

    async def citations(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "hostname",
                "path",
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "tag",
                "prompt",
                "prompt_id",
                "url",
                "root_domain",
                "persona",
                "citation_category",
            ]
        ]
        | Omit = omit,
        metrics: List[Literal["count", "citation_share", "share_of_voice", "first_cited_at"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_citations_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCitationsResponse:
        """
        Get citations for a given category.

        The ``mentioned`` filter supports ``is true`` and ``is false``. It uses the
        latest page analysis available at or before ``end_date``; pages without an
        analysis by then are excluded from both values. ``citation_share`` keeps all
        otherwise eligible citations in its denominator when this filter is used.

        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Metrics to include. `share_of_voice` is deprecated, use `citation_share` instead.
            order_by: Custom ordering of the report results.
            pagination: Pagination settings for the report results.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the citations report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ReportCitationsResponse: Successful Response

        Example:
            ```python
            report = await client.reports.citations(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )
            ```
        """
        return await self._post(
            "/v1/reports/citations",
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
                report_citations_params.ReportCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportCitationsResponse,
        )

    async def visibility(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "asset_id",
                "asset_name",
                "prompt",
                "prompt_id",
                "tag",
                "persona",
            ]
        ]
        | Omit = omit,
        metrics: List[
            Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]
        ],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_visibility_params.Filter] | Omit = omit,
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
            report = await client.reports.visibility(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
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
                report_visibility_params.ReportVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def sentiment(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "theme",
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "asset_id",
                "asset_name",
                "tag",
                "prompt",
                "prompt_id",
                "sentiment_type",
                "persona",
            ]
        ]
        | Omit = omit,
        metrics: List[Literal["positive", "negative", "occurrences"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_sentiment_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get citations for a given category.

        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering of the report results.
            pagination: Pagination settings for the report results.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the sentiment report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ReportResponse: Successful Response

        Example:
            ```python
            report = await client.reports.sentiment(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )
            ```
        """
        return await self._post(
            "/v1/reports/sentiment",
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
                report_sentiment_params.ReportSentimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def get_referrals_report(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "host", "path", "referral_source"]] | Omit = omit,
        metrics: List[Literal["visits", "last_visit"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        domain: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        metric_filters: Iterable[report_get_referrals_report_params.MetricFilter] | Omit = omit,
        filters: Iterable[report_get_referrals_report_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get referral traffic report from the daily aggregated materialized view.

        This endpoint queries pre-aggregated daily referral data, making it efficient
        for large date ranges and high-traffic sites.

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
            filters: Filters for referrals report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ReportResponse: Successful Response

        Example:
            ```python
            report = await client.reports.get_referrals_report(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                domain="",
                start_date="2024-01-01T00:00:00.000Z",
            )
            ```
        """
        return await self._post(
            "/v1/reports/referrals",
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
                report_get_referrals_report_params.ReportGetReferralsReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def get_bots_report(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "host", "path", "bot_name", "bot_provider"]] | Omit = omit,
        metrics: List[Literal["count", "citations", "indexing", "training", "last_visit"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        domain: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        metric_filters: Iterable[report_get_bots_report_params.MetricFilter] | Omit = omit,
        filters: Iterable[report_get_bots_report_params.Filter] | Omit = omit,
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
            report = await client.reports.get_bots_report(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                domain="",
                start_date="2024-01-01T00:00:00.000Z",
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
                report_get_bots_report_params.ReportGetBotsReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def get_referrals_report_v2(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "hour", "host", "path", "referral_source", "referral_type"]] | Omit = omit,
        metrics: List[Literal["visits", "last_visit"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        domain: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        timezone: str | Omit = omit,
        metric_filters: Iterable[report_get_referrals_report_v2_params.MetricFilter] | Omit = omit,
        filters: Iterable[report_get_referrals_report_v2_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get referral traffic report from the hourly aggregated materialized view (UTC-based).

        Supports date_interval="hour", calendar intervals through "year", "quarter", and "relative_week".

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
            timezone: IANA timezone name for date bucketing and filter boundaries.
            metric_filters: Numeric filters applied after report metrics are calculated.
            filters: Filters for referrals report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ReportResponse: Successful Response

        Example:
            ```python
            report = await client.reports.get_referrals_report_v2(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                domain="",
                start_date="2024-01-01T00:00:00.000Z",
                timezone="UTC",
            )
            ```
        """
        return await self._post(
            "/v2/reports/referrals",
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
                    "timezone": timezone,
                    "metric_filters": metric_filters,
                    "filters": filters,
                },
                report_get_referrals_report_v2_params.ReportGetReferralsReportV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def get_bots_report_v2(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "hour", "host", "path", "bot_name", "bot_provider", "bot_type"]] | Omit = omit,
        metrics: List[Literal["count", "citations", "indexing", "training", "last_visit", "agents"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        domain: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        timezone: str | Omit = omit,
        metric_filters: Iterable[report_get_bots_report_v2_params.MetricFilter] | Omit = omit,
        filters: Iterable[report_get_bots_report_v2_params.Filter] | Omit = omit,
        domain_id: Optional[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
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
            timezone: IANA timezone name for date bucketing and filter boundaries.
            metric_filters: Numeric filters applied after report metrics are calculated.
            filters: Filters for bots report.
            domain_id: Domain UUID used for tag lookups.
            tags: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ReportResponse: Successful Response

        Example:
            ```python
            report = await client.reports.get_bots_report_v2(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                domain="",
                start_date="2024-01-01T00:00:00.000Z",
                timezone="UTC",
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
                    "timezone": timezone,
                    "metric_filters": metric_filters,
                    "filters": filters,
                    "domain_id": domain_id,
                    "tags": tags,
                },
                report_get_bots_report_v2_params.ReportGetBotsReportV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def query_fanouts(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["prompt", "query", "model", "region", "date"]] | Omit = omit,
        metrics: List[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_query_fanouts_params.Filter] | Omit = omit,
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
            metrics: Metrics to return for each row.
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
            report = await client.reports.query_fanouts(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
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
                report_query_fanouts_params.ReportQueryFanoutsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def stream_citations(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "hostname",
                "path",
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "tag",
                "prompt",
                "prompt_id",
                "url",
                "root_domain",
                "persona",
                "citation_category",
            ]
        ]
        | Omit = omit,
        metrics: List[Literal["count", "citation_share", "share_of_voice", "first_cited_at"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_stream_citations_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ReportStreamCitationsResponse]:
        """
        Stream citations with the same filter semantics as the non-streaming route.

        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Metrics to include. `share_of_voice` is deprecated, use `citation_share` instead.
            order_by: Custom ordering of the report results.
            pagination: Body parameter.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the citations report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncStream[ReportStreamCitationsResponse]: Server-sent events stream. Emits a `summary` event first, then one `row` event per streamed row.

        Example:
            ```python
            stream = await client.reports.stream_citations(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )

            async for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v1/reports/citations/stream",
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
                report_stream_citations_params.ReportStreamCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportStreamCitationsResponse,
            stream=True,
            stream_cls=AsyncStream[ReportStreamCitationsResponse],
        )

    async def stream_visibility(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "asset_id",
                "asset_name",
                "prompt",
                "prompt_id",
                "tag",
                "persona",
            ]
        ]
        | Omit = omit,
        metrics: List[
            Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]
        ],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_stream_visibility_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ReportStreamVisibilityResponse]:
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
            AsyncStream[ReportStreamVisibilityResponse]: Server-sent events stream. Emits a `summary` event first, then one `row` event per streamed row.

        Example:
            ```python
            stream = await client.reports.stream_visibility(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )

            async for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v1/reports/visibility/stream",
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
                report_stream_visibility_params.ReportStreamVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportStreamVisibilityResponse,
            stream=True,
            stream_cls=AsyncStream[ReportStreamVisibilityResponse],
        )

    async def stream_sentiment(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "theme",
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "asset_id",
                "asset_name",
                "tag",
                "prompt",
                "prompt_id",
                "sentiment_type",
                "persona",
            ]
        ]
        | Omit = omit,
        metrics: List[Literal["positive", "negative", "occurrences"]],
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        category_id: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        filters: Iterable[report_stream_sentiment_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ReportStreamSentimentResponse]:
        """
        Stream Sentiment

        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            order_by: Custom ordering of the report results.
            pagination: Body parameter.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the sentiment report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncStream[ReportStreamSentimentResponse]: Server-sent events stream. Emits a `summary` event first, then one `row` event per streamed row.

        Example:
            ```python
            stream = await client.reports.stream_sentiment(
                date_interval="day",
                dimensions=[],
                metrics=[],
                order_by={},
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="2024-01-01T00:00:00.000Z",
                end_date="2024-01-01T00:00:00.000Z",
            )

            async for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v1/reports/sentiment/stream",
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
                report_stream_sentiment_params.ReportStreamSentimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportStreamSentimentResponse,
            stream=True,
            stream_cls=AsyncStream[ReportStreamSentimentResponse],
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.citations = to_raw_response_wrapper(
            reports.citations,
        )
        self.visibility = to_raw_response_wrapper(
            reports.visibility,
        )
        self.sentiment = to_raw_response_wrapper(
            reports.sentiment,
        )
        self.get_referrals_report = to_raw_response_wrapper(
            reports.get_referrals_report,
        )
        self.get_bots_report = to_raw_response_wrapper(
            reports.get_bots_report,
        )
        self.get_referrals_report_v2 = to_raw_response_wrapper(
            reports.get_referrals_report_v2,
        )
        self.get_bots_report_v2 = to_raw_response_wrapper(
            reports.get_bots_report_v2,
        )
        self.query_fanouts = to_raw_response_wrapper(
            reports.query_fanouts,
        )
        self.stream_citations = to_raw_response_wrapper(
            reports.stream_citations,
        )
        self.stream_visibility = to_raw_response_wrapper(
            reports.stream_visibility,
        )
        self.stream_sentiment = to_raw_response_wrapper(
            reports.stream_sentiment,
        )

    @cached_property
    def web_search_results(self) -> WebSearchResultsResourceWithRawResponse:
        return WebSearchResultsResourceWithRawResponse(self._reports.web_search_results)

    @cached_property
    def shopping(self) -> ShoppingResourceWithRawResponse:
        return ShoppingResourceWithRawResponse(self._reports.shopping)


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.citations = async_to_raw_response_wrapper(
            reports.citations,
        )
        self.visibility = async_to_raw_response_wrapper(
            reports.visibility,
        )
        self.sentiment = async_to_raw_response_wrapper(
            reports.sentiment,
        )
        self.get_referrals_report = async_to_raw_response_wrapper(
            reports.get_referrals_report,
        )
        self.get_bots_report = async_to_raw_response_wrapper(
            reports.get_bots_report,
        )
        self.get_referrals_report_v2 = async_to_raw_response_wrapper(
            reports.get_referrals_report_v2,
        )
        self.get_bots_report_v2 = async_to_raw_response_wrapper(
            reports.get_bots_report_v2,
        )
        self.query_fanouts = async_to_raw_response_wrapper(
            reports.query_fanouts,
        )
        self.stream_citations = async_to_raw_response_wrapper(
            reports.stream_citations,
        )
        self.stream_visibility = async_to_raw_response_wrapper(
            reports.stream_visibility,
        )
        self.stream_sentiment = async_to_raw_response_wrapper(
            reports.stream_sentiment,
        )

    @cached_property
    def web_search_results(self) -> AsyncWebSearchResultsResourceWithRawResponse:
        return AsyncWebSearchResultsResourceWithRawResponse(self._reports.web_search_results)

    @cached_property
    def shopping(self) -> AsyncShoppingResourceWithRawResponse:
        return AsyncShoppingResourceWithRawResponse(self._reports.shopping)


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.citations = to_streamed_response_wrapper(
            reports.citations,
        )
        self.visibility = to_streamed_response_wrapper(
            reports.visibility,
        )
        self.sentiment = to_streamed_response_wrapper(
            reports.sentiment,
        )
        self.get_referrals_report = to_streamed_response_wrapper(
            reports.get_referrals_report,
        )
        self.get_bots_report = to_streamed_response_wrapper(
            reports.get_bots_report,
        )
        self.get_referrals_report_v2 = to_streamed_response_wrapper(
            reports.get_referrals_report_v2,
        )
        self.get_bots_report_v2 = to_streamed_response_wrapper(
            reports.get_bots_report_v2,
        )
        self.query_fanouts = to_streamed_response_wrapper(
            reports.query_fanouts,
        )
        self.stream_citations = to_streamed_response_wrapper(
            reports.stream_citations,
        )
        self.stream_visibility = to_streamed_response_wrapper(
            reports.stream_visibility,
        )
        self.stream_sentiment = to_streamed_response_wrapper(
            reports.stream_sentiment,
        )

    @cached_property
    def web_search_results(self) -> WebSearchResultsResourceWithStreamingResponse:
        return WebSearchResultsResourceWithStreamingResponse(self._reports.web_search_results)

    @cached_property
    def shopping(self) -> ShoppingResourceWithStreamingResponse:
        return ShoppingResourceWithStreamingResponse(self._reports.shopping)


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.citations = async_to_streamed_response_wrapper(
            reports.citations,
        )
        self.visibility = async_to_streamed_response_wrapper(
            reports.visibility,
        )
        self.sentiment = async_to_streamed_response_wrapper(
            reports.sentiment,
        )
        self.get_referrals_report = async_to_streamed_response_wrapper(
            reports.get_referrals_report,
        )
        self.get_bots_report = async_to_streamed_response_wrapper(
            reports.get_bots_report,
        )
        self.get_referrals_report_v2 = async_to_streamed_response_wrapper(
            reports.get_referrals_report_v2,
        )
        self.get_bots_report_v2 = async_to_streamed_response_wrapper(
            reports.get_bots_report_v2,
        )
        self.query_fanouts = async_to_streamed_response_wrapper(
            reports.query_fanouts,
        )
        self.stream_citations = async_to_streamed_response_wrapper(
            reports.stream_citations,
        )
        self.stream_visibility = async_to_streamed_response_wrapper(
            reports.stream_visibility,
        )
        self.stream_sentiment = async_to_streamed_response_wrapper(
            reports.stream_sentiment,
        )

    @cached_property
    def web_search_results(self) -> AsyncWebSearchResultsResourceWithStreamingResponse:
        return AsyncWebSearchResultsResourceWithStreamingResponse(self._reports.web_search_results)

    @cached_property
    def shopping(self) -> AsyncShoppingResourceWithStreamingResponse:
        return AsyncShoppingResourceWithStreamingResponse(self._reports.shopping)
