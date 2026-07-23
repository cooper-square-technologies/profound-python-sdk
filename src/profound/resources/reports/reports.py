# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    report_citations_params,
    report_sentiment_params,
    report_visibility_params,
    report_sentiment_v2_params,
    report_query_fanouts_params,
    report_get_bots_report_params,
    report_query_citations_params,
    report_query_sentiment_params,
    report_query_visibility_params,
    report_stream_citations_params,
    report_stream_sentiment_params,
    report_stream_visibility_params,
    report_get_bots_report_v2_params,
    report_query_query_fanouts_params,
    report_stream_citations_v2_params,
    report_stream_sentiment_v2_params,
    report_get_referrals_report_params,
    report_stream_query_fanouts_params,
    report_stream_visibility_v2_params,
    report_get_referrals_report_v2_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .accuracy import (
    AccuracyResource,
    AsyncAccuracyResource,
    AccuracyResourceWithRawResponse,
    AsyncAccuracyResourceWithRawResponse,
    AccuracyResourceWithStreamingResponse,
    AsyncAccuracyResourceWithStreamingResponse,
)
from .shopping import (
    ShoppingResource,
    AsyncShoppingResource,
    ShoppingResourceWithRawResponse,
    AsyncShoppingResourceWithRawResponse,
    ShoppingResourceWithStreamingResponse,
    AsyncShoppingResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from .web_search_results import (
    WebSearchResultsResource,
    AsyncWebSearchResultsResource,
    WebSearchResultsResourceWithRawResponse,
    AsyncWebSearchResultsResourceWithRawResponse,
    WebSearchResultsResourceWithStreamingResponse,
    AsyncWebSearchResultsResourceWithStreamingResponse,
)
from .factcheck.factcheck import (
    FactcheckResource,
    AsyncFactcheckResource,
    FactcheckResourceWithRawResponse,
    AsyncFactcheckResourceWithRawResponse,
    FactcheckResourceWithStreamingResponse,
    AsyncFactcheckResourceWithStreamingResponse,
)
from ...types.report_response import ReportResponse
from ...types.shared_params.pagination import Pagination
from ...types.report_citations_response import ReportCitationsResponse
from ...types.report_sentiment_v2_response import ReportSentimentV2Response
from ...types.report_query_citations_response import ReportQueryCitationsResponse
from ...types.report_query_sentiment_response import ReportQuerySentimentResponse
from ...types.report_query_visibility_response import ReportQueryVisibilityResponse
from ...types.report_stream_citations_response import ReportStreamCitationsResponse
from ...types.report_stream_sentiment_response import ReportStreamSentimentResponse
from ...types.report_stream_visibility_response import ReportStreamVisibilityResponse
from ...types.report_query_query_fanouts_response import ReportQueryQueryFanoutsResponse
from ...types.report_stream_citations_v2_response import ReportStreamCitationsV2Response
from ...types.report_stream_sentiment_v2_response import ReportStreamSentimentV2Response
from ...types.report_stream_query_fanouts_response import ReportStreamQueryFanoutsResponse
from ...types.report_stream_visibility_v2_response import ReportStreamVisibilityV2Response

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    @cached_property
    def web_search_results(self) -> WebSearchResultsResource:
        return WebSearchResultsResource(self._client)

    @cached_property
    def shopping(self) -> ShoppingResource:
        return ShoppingResource(self._client)

    @cached_property
    def accuracy(self) -> AccuracyResource:
        return AccuracyResource(self._client)

    @cached_property
    def factcheck(self) -> FactcheckResource:
        return FactcheckResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return ReportsResourceWithStreamingResponse(self)

    def citations(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["count", "citation_share", "share_of_voice", "first_cited_at"]],
        start_date: Union[str, datetime],
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
        filters: Iterable[report_citations_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCitationsResponse:
        """
        Get citations for a given category.

        The `mentioned` filter supports `is true` and `is false`. It uses the latest
        page analysis available at or before `end_date`; pages without an analysis by
        then are excluded from both values. `citation_share` keeps all otherwise
        eligible citations in its denominator when this filter is used.

        Args:
          end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          metrics: Metrics to include. `share_of_voice` is deprecated, use `citation_share`
              instead.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the citations report.

          order_by: Custom ordering of the report results.

                  The order is a record of key-value pairs where:
                  - `key` is the field to order by, which can be a metric or dimension
                  - `value` is the direction of the order, either `asc` for ascending or `desc` for descending.

                  When not specified, the default order is the first metric in the query descending.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/citations",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_citations_params.ReportCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportCitationsResponse,
        )

    def get_bots_report(
        self,
        *,
        domain: str,
        metrics: List[Literal["count", "citations", "indexing", "training", "last_visit"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "path", "bot_name", "bot_provider"]] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[report_get_bots_report_params.Filter] | Omit = omit,
        metric_filters: Iterable[report_get_bots_report_params.MetricFilter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get bot traffic report from the daily aggregated materialized view.

        This endpoint queries pre-aggregated daily bot data, making it efficient for
        large date ranges and high-traffic sites.

        Metrics:

        - count: unique bot visits
        - citations: unique citation events
        - indexing: unique indexing events
        - training: unique training events
        - last_visit: most recent visit timestamp

        Args:
          domain: Domain to query logs for.

          start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS,
              or full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          end_date: End date for logs. Accepts same formats as start_date. Defaults to now if
              omitted.

          filters: Filters for bots report.

          metric_filters: Numeric filters applied after report metrics are calculated.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/bots",
            body=maybe_transform(
                {
                    "domain": domain,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "end_date": end_date,
                    "filters": filters,
                    "metric_filters": metric_filters,
                    "order_by": order_by,
                    "organization_id": organization_id,
                    "pagination": pagination,
                },
                report_get_bots_report_params.ReportGetBotsReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def get_bots_report_v2(
        self,
        *,
        domain: str,
        metrics: List[Literal["count", "citations", "indexing", "training", "last_visit", "agents"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "hour", "path", "bot_name", "bot_provider", "bot_type"]] | Omit = omit,
        domain_id: Optional[str] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[report_get_bots_report_v2_params.Filter] | Omit = omit,
        metric_filters: Iterable[report_get_bots_report_v2_params.MetricFilter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        pagination: Pagination | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get bot traffic report from the hourly aggregated materialized view (UTC-based).

        Supports date_interval="hour", calendar intervals through "year", "quarter", and
        "relative_week".

        Metrics:

        - count: unique bot visits
        - citations: unique citation events (ai_assistant bot type)
        - indexing: unique indexing events (index bot type)
        - training: unique training events (ai_training bot type)
        - last_visit: most recent visit timestamp

        Dimensions:

        - date, path, bot_name, bot_provider, bot_type

        Args:
          domain: Domain to query logs for.

          start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS,
              or full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          domain_id: Domain UUID used for tag lookups.

          end_date: End date in UTC. Accepts same formats as start_date. Defaults to now UTC if
              omitted.

          filters: Filters for bots report.

          metric_filters: Numeric filters applied after report metrics are calculated.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Pagination settings for the report results.

          timezone: IANA timezone name for date bucketing and filter boundaries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/bots",
            body=maybe_transform(
                {
                    "domain": domain,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "domain_id": domain_id,
                    "end_date": end_date,
                    "filters": filters,
                    "metric_filters": metric_filters,
                    "order_by": order_by,
                    "organization_id": organization_id,
                    "pagination": pagination,
                    "tags": tags,
                    "timezone": timezone,
                },
                report_get_bots_report_v2_params.ReportGetBotsReportV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def get_referrals_report(
        self,
        *,
        domain: str,
        metrics: List[Literal["visits", "last_visit"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "path", "referral_source"]] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[report_get_referrals_report_params.Filter] | Omit = omit,
        metric_filters: Iterable[report_get_referrals_report_params.MetricFilter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        pagination: Pagination | Omit = omit,
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
          domain: Domain to query logs for.

          start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS,
              or full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          end_date: End date for logs. Accepts same formats as start_date. Defaults to now if
              omitted.

          filters: Filters for referrals report.

          metric_filters: Numeric filters applied after report metrics are calculated.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/referrals",
            body=maybe_transform(
                {
                    "domain": domain,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "end_date": end_date,
                    "filters": filters,
                    "metric_filters": metric_filters,
                    "order_by": order_by,
                    "organization_id": organization_id,
                    "pagination": pagination,
                },
                report_get_referrals_report_params.ReportGetReferralsReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def get_referrals_report_v2(
        self,
        *,
        domain: str,
        metrics: List[Literal["visits", "last_visit"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "hour", "path", "referral_source", "referral_type"]] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[report_get_referrals_report_v2_params.Filter] | Omit = omit,
        metric_filters: Iterable[report_get_referrals_report_v2_params.MetricFilter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        pagination: Pagination | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get referral traffic report from the hourly aggregated materialized view
        (UTC-based).

        Supports date_interval="hour", calendar intervals through "year", "quarter", and
        "relative_week".

        Args:
          domain: Domain to query logs for.

          start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS,
              or full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          end_date: End date in UTC. Accepts same formats as start_date. Defaults to now UTC if
              omitted.

          filters: Filters for referrals report.

          metric_filters: Numeric filters applied after report metrics are calculated.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Pagination settings for the report results.

          timezone: IANA timezone name for date bucketing and filter boundaries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/referrals",
            body=maybe_transform(
                {
                    "domain": domain,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "end_date": end_date,
                    "filters": filters,
                    "metric_filters": metric_filters,
                    "order_by": order_by,
                    "organization_id": organization_id,
                    "pagination": pagination,
                    "timezone": timezone,
                },
                report_get_referrals_report_v2_params.ReportGetReferralsReportV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def query_citations(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        entity: Literal["domain", "page", "citation_category"] | Omit = omit,
        filter: Optional[report_query_citations_params.Filter] | Omit = omit,
        group_by: List[Literal["page", "date", "model", "topic", "region", "persona", "prompt"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["count", "citation_share", "rank", "first_cited_at"]]] | Omit = omit,
        scope: Literal["all", "owned"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportQueryCitationsResponse:
        """
        Query Citations V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          entity: What each row represents: `domain` (default), `page`, or `citation_category`.
              Legacy: `group_by: ["page"]` (with `entity` omitted) is still accepted and is
              equivalent to `entity: "page"`. `citation_category` uses the dashboard split
              view: a citation counts under both its page-level and domain-level category, so
              category shares can sum to more than 100%.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          scope: `all` (every cited domain) or `owned` (only your owned domains). Applies to
              `entity=domain`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/citations",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "entity": entity,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "scope": scope,
                },
                report_query_citations_params.ReportQueryCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportQueryCitationsResponse,
        )

    def query_fanouts(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["prompt", "query", "model", "region", "date"]] | Omit = omit,
        filters: Iterable[report_query_fanouts_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """Query Fanouts

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: Filters to apply to the query fanout report.

          order_by: Custom ordering. Keys must be a requested metric or the `date` dimension. Values
              are `asc` or `desc`. Defaults to first metric descending.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/query-fanouts",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_query_fanouts_params.ReportQueryFanoutsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def query_query_fanouts(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[report_query_query_fanouts_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "model", "region", "prompt", "query"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]]
        | Omit = omit,
        sort: Optional[report_query_query_fanouts_params.Sort] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportQueryQueryFanoutsResponse:
        """
        Query Fanouts V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/query-fanouts",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "sort": sort,
                },
                report_query_query_fanouts_params.ReportQueryQueryFanoutsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportQueryQueryFanoutsResponse,
        )

    def query_sentiment(
        self,
        *,
        asset: str,
        category_id: str,
        end_date: str,
        start_date: str,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[report_query_sentiment_params.Filter] | Omit = omit,
        group_by: List[
            Literal[
                "date", "model", "topic", "region", "prompt", "persona", "tag", "theme", "claim", "run", "competitor"
            ]
        ]
        | Omit = omit,
        include_cited_websites: bool | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["positive_sentiment", "negative_sentiment", "occurrence"]]] | Omit = omit,
        sort: report_query_sentiment_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportQuerySentimentResponse:
        """
        Query Sentiment V2

        Args:
          asset: The brand name to analyze (sentiment is extracted on name, not id).

          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          comparison_end_date: YYYY-MM-DD, ET, inclusive (with start).

          comparison_start_date: YYYY-MM-DD, ET, inclusive (with end).

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          include_cited_websites: Return cited websites per row (only when grouping by `theme`/`claim`).

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/sentiment",
            body=maybe_transform(
                {
                    "asset": asset,
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "include_cited_websites": include_cited_websites,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "sort": sort,
                },
                report_query_sentiment_params.ReportQuerySentimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportQuerySentimentResponse,
        )

    def query_visibility(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        assets: Optional[report_query_visibility_params.Assets] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[report_query_visibility_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "model", "topic", "region", "prompt", "persona"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["visibility_score", "share_of_voice", "average_position"]]] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        sort: report_query_visibility_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportQueryVisibilityResponse:
        """
        Query Visibility V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          assets: A name (`is`), a list (`in`), or {op,value} with op `is`/`in`/`not_in`.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/visibility",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "assets": assets,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "scope": scope,
                    "sort": sort,
                },
                report_query_visibility_params.ReportQueryVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportQueryVisibilityResponse,
        )

    def sentiment(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["positive", "negative", "occurrences"]],
        start_date: Union[str, datetime],
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
        filters: Iterable[report_sentiment_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """Get citations for a given category.

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the sentiment report.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/sentiment",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_sentiment_params.ReportSentimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def sentiment_v2(
        self,
        *,
        asset_name: str,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["sentiment", "occurrence"]],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_bucket: Literal["day", "week", "month"] | Omit = omit,
        dimensions: List[
            Literal[
                "date", "topic", "region", "model", "prompt", "persona", "tag", "theme", "claim", "run", "asset_name"
            ]
        ]
        | Omit = omit,
        filters: Iterable[report_sentiment_v2_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportSentimentV2Response:
        """Query Sentiment V2

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          comparison_end_date: End of the previous period for delta computation.

          comparison_start_date: Start of the previous period for delta computation.

          date_bucket: Date bucket for the report. Only used when dimensions includes date.

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the sentiment-v2 report.

          order_by: Custom ordering of report results. Dimension keys must also be present in
              dimensions. The sentiment metric orders by positive_sentiment.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/sentiment-v2",
            body=maybe_transform(
                {
                    "asset_name": asset_name,
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_bucket": date_bucket,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_sentiment_v2_params.ReportSentimentV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportSentimentV2Response,
        )

    def stream_citations(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["count", "citation_share", "share_of_voice", "first_cited_at"]],
        start_date: Union[str, datetime],
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
        filters: Iterable[report_stream_citations_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
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
          end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          metrics: Metrics to include. `share_of_voice` is deprecated, use `citation_share`
              instead.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the citations report.

          order_by: Custom ordering of the report results.

                  The order is a record of key-value pairs where:
                  - `key` is the field to order by, which can be a metric or dimension
                  - `value` is the direction of the order, either `asc` for ascending or `desc` for descending.

                  When not specified, the default order is the first metric in the query descending.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v1/reports/citations/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_stream_citations_params.ReportStreamCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamCitationsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[ReportStreamCitationsResponse],
        )

    def stream_citations_v2(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        entity: Literal["domain", "page", "citation_category"] | Omit = omit,
        filter: Optional[report_stream_citations_v2_params.Filter] | Omit = omit,
        group_by: List[Literal["page", "date", "model", "topic", "region", "persona", "prompt"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["count", "citation_share", "rank", "first_cited_at"]]] | Omit = omit,
        scope: Literal["all", "owned"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ReportStreamCitationsV2Response]:
        """
        Stream Citations V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          entity: What each row represents: `domain` (default), `page`, or `citation_category`.
              Legacy: `group_by: ["page"]` (with `entity` omitted) is still accepted and is
              equivalent to `entity: "page"`. `citation_category` uses the dashboard split
              view: a citation counts under both its page-level and domain-level category, so
              category shares can sum to more than 100%.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          scope: `all` (every cited domain) or `owned` (only your owned domains). Applies to
              `entity=domain`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/citations/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "entity": entity,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "scope": scope,
                },
                report_stream_citations_v2_params.ReportStreamCitationsV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamCitationsV2Response
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[ReportStreamCitationsV2Response],
        )

    def stream_query_fanouts(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[report_stream_query_fanouts_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "model", "region", "prompt", "query"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]]
        | Omit = omit,
        sort: Optional[report_stream_query_fanouts_params.Sort] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ReportStreamQueryFanoutsResponse]:
        """
        Stream Query Fanouts V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/query-fanouts/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "sort": sort,
                },
                report_stream_query_fanouts_params.ReportStreamQueryFanoutsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamQueryFanoutsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[ReportStreamQueryFanoutsResponse],
        )

    def stream_sentiment(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["positive", "negative", "occurrences"]],
        start_date: Union[str, datetime],
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
        filters: Iterable[report_stream_sentiment_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ReportStreamSentimentResponse]:
        """Stream Sentiment

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the sentiment report.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v1/reports/sentiment/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_stream_sentiment_params.ReportStreamSentimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamSentimentResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[ReportStreamSentimentResponse],
        )

    def stream_sentiment_v2(
        self,
        *,
        asset: str,
        category_id: str,
        end_date: str,
        start_date: str,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[report_stream_sentiment_v2_params.Filter] | Omit = omit,
        group_by: List[
            Literal[
                "date", "model", "topic", "region", "prompt", "persona", "tag", "theme", "claim", "run", "competitor"
            ]
        ]
        | Omit = omit,
        include_cited_websites: bool | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["positive_sentiment", "negative_sentiment", "occurrence"]]] | Omit = omit,
        sort: report_stream_sentiment_v2_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ReportStreamSentimentV2Response]:
        """
        Stream Sentiment V2

        Args:
          asset: The brand name to analyze (sentiment is extracted on name, not id).

          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          comparison_end_date: YYYY-MM-DD, ET, inclusive (with start).

          comparison_start_date: YYYY-MM-DD, ET, inclusive (with end).

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          include_cited_websites: Return cited websites per row (only when grouping by `theme`/`claim`).

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/sentiment/stream",
            body=maybe_transform(
                {
                    "asset": asset,
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "include_cited_websites": include_cited_websites,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "sort": sort,
                },
                report_stream_sentiment_v2_params.ReportStreamSentimentV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamSentimentV2Response
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[ReportStreamSentimentV2Response],
        )

    def stream_visibility(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[
            Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]
        ],
        start_date: Union[str, datetime],
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
        filters: Iterable[report_stream_visibility_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ReportStreamVisibilityResponse]:
        """Stream Visibility

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the visibility report.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v1/reports/visibility/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_stream_visibility_params.ReportStreamVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamVisibilityResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[ReportStreamVisibilityResponse],
        )

    def stream_visibility_v2(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        assets: Optional[report_stream_visibility_v2_params.Assets] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[report_stream_visibility_v2_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "model", "topic", "region", "prompt", "persona"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["visibility_score", "share_of_voice", "average_position"]]] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        sort: report_stream_visibility_v2_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ReportStreamVisibilityV2Response]:
        """
        Stream Visibility V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          assets: A name (`is`), a list (`in`), or {op,value} with op `is`/`in`/`not_in`.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/visibility/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "assets": assets,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "scope": scope,
                    "sort": sort,
                },
                report_stream_visibility_v2_params.ReportStreamVisibilityV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamVisibilityV2Response
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[ReportStreamVisibilityV2Response],
        )

    def visibility(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[
            Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]
        ],
        start_date: Union[str, datetime],
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
        filters: Iterable[report_visibility_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """Query visibility report.

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the visibility report.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/visibility",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_visibility_params.ReportVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )


class AsyncReportsResource(AsyncAPIResource):
    @cached_property
    def web_search_results(self) -> AsyncWebSearchResultsResource:
        return AsyncWebSearchResultsResource(self._client)

    @cached_property
    def shopping(self) -> AsyncShoppingResource:
        return AsyncShoppingResource(self._client)

    @cached_property
    def accuracy(self) -> AsyncAccuracyResource:
        return AsyncAccuracyResource(self._client)

    @cached_property
    def factcheck(self) -> AsyncFactcheckResource:
        return AsyncFactcheckResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncReportsResourceWithStreamingResponse(self)

    async def citations(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["count", "citation_share", "share_of_voice", "first_cited_at"]],
        start_date: Union[str, datetime],
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
        filters: Iterable[report_citations_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCitationsResponse:
        """
        Get citations for a given category.

        The `mentioned` filter supports `is true` and `is false`. It uses the latest
        page analysis available at or before `end_date`; pages without an analysis by
        then are excluded from both values. `citation_share` keeps all otherwise
        eligible citations in its denominator when this filter is used.

        Args:
          end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          metrics: Metrics to include. `share_of_voice` is deprecated, use `citation_share`
              instead.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the citations report.

          order_by: Custom ordering of the report results.

                  The order is a record of key-value pairs where:
                  - `key` is the field to order by, which can be a metric or dimension
                  - `value` is the direction of the order, either `asc` for ascending or `desc` for descending.

                  When not specified, the default order is the first metric in the query descending.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/citations",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_citations_params.ReportCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportCitationsResponse,
        )

    async def get_bots_report(
        self,
        *,
        domain: str,
        metrics: List[Literal["count", "citations", "indexing", "training", "last_visit"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "path", "bot_name", "bot_provider"]] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[report_get_bots_report_params.Filter] | Omit = omit,
        metric_filters: Iterable[report_get_bots_report_params.MetricFilter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get bot traffic report from the daily aggregated materialized view.

        This endpoint queries pre-aggregated daily bot data, making it efficient for
        large date ranges and high-traffic sites.

        Metrics:

        - count: unique bot visits
        - citations: unique citation events
        - indexing: unique indexing events
        - training: unique training events
        - last_visit: most recent visit timestamp

        Args:
          domain: Domain to query logs for.

          start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS,
              or full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          end_date: End date for logs. Accepts same formats as start_date. Defaults to now if
              omitted.

          filters: Filters for bots report.

          metric_filters: Numeric filters applied after report metrics are calculated.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/bots",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "end_date": end_date,
                    "filters": filters,
                    "metric_filters": metric_filters,
                    "order_by": order_by,
                    "organization_id": organization_id,
                    "pagination": pagination,
                },
                report_get_bots_report_params.ReportGetBotsReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def get_bots_report_v2(
        self,
        *,
        domain: str,
        metrics: List[Literal["count", "citations", "indexing", "training", "last_visit", "agents"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "hour", "path", "bot_name", "bot_provider", "bot_type"]] | Omit = omit,
        domain_id: Optional[str] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[report_get_bots_report_v2_params.Filter] | Omit = omit,
        metric_filters: Iterable[report_get_bots_report_v2_params.MetricFilter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        pagination: Pagination | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get bot traffic report from the hourly aggregated materialized view (UTC-based).

        Supports date_interval="hour", calendar intervals through "year", "quarter", and
        "relative_week".

        Metrics:

        - count: unique bot visits
        - citations: unique citation events (ai_assistant bot type)
        - indexing: unique indexing events (index bot type)
        - training: unique training events (ai_training bot type)
        - last_visit: most recent visit timestamp

        Dimensions:

        - date, path, bot_name, bot_provider, bot_type

        Args:
          domain: Domain to query logs for.

          start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS,
              or full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          domain_id: Domain UUID used for tag lookups.

          end_date: End date in UTC. Accepts same formats as start_date. Defaults to now UTC if
              omitted.

          filters: Filters for bots report.

          metric_filters: Numeric filters applied after report metrics are calculated.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Pagination settings for the report results.

          timezone: IANA timezone name for date bucketing and filter boundaries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/bots",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "domain_id": domain_id,
                    "end_date": end_date,
                    "filters": filters,
                    "metric_filters": metric_filters,
                    "order_by": order_by,
                    "organization_id": organization_id,
                    "pagination": pagination,
                    "tags": tags,
                    "timezone": timezone,
                },
                report_get_bots_report_v2_params.ReportGetBotsReportV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def get_referrals_report(
        self,
        *,
        domain: str,
        metrics: List[Literal["visits", "last_visit"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "path", "referral_source"]] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[report_get_referrals_report_params.Filter] | Omit = omit,
        metric_filters: Iterable[report_get_referrals_report_params.MetricFilter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        pagination: Pagination | Omit = omit,
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
          domain: Domain to query logs for.

          start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS,
              or full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          end_date: End date for logs. Accepts same formats as start_date. Defaults to now if
              omitted.

          filters: Filters for referrals report.

          metric_filters: Numeric filters applied after report metrics are calculated.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/referrals",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "end_date": end_date,
                    "filters": filters,
                    "metric_filters": metric_filters,
                    "order_by": order_by,
                    "organization_id": organization_id,
                    "pagination": pagination,
                },
                report_get_referrals_report_params.ReportGetReferralsReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def get_referrals_report_v2(
        self,
        *,
        domain: str,
        metrics: List[Literal["visits", "last_visit"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["date", "hour", "path", "referral_source", "referral_type"]] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[report_get_referrals_report_v2_params.Filter] | Omit = omit,
        metric_filters: Iterable[report_get_referrals_report_v2_params.MetricFilter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        pagination: Pagination | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """
        Get referral traffic report from the hourly aggregated materialized view
        (UTC-based).

        Supports date_interval="hour", calendar intervals through "year", "quarter", and
        "relative_week".

        Args:
          domain: Domain to query logs for.

          start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS,
              or full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          end_date: End date in UTC. Accepts same formats as start_date. Defaults to now UTC if
              omitted.

          filters: Filters for referrals report.

          metric_filters: Numeric filters applied after report metrics are calculated.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Pagination settings for the report results.

          timezone: IANA timezone name for date bucketing and filter boundaries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/referrals",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "end_date": end_date,
                    "filters": filters,
                    "metric_filters": metric_filters,
                    "order_by": order_by,
                    "organization_id": organization_id,
                    "pagination": pagination,
                    "timezone": timezone,
                },
                report_get_referrals_report_v2_params.ReportGetReferralsReportV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def query_citations(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        entity: Literal["domain", "page", "citation_category"] | Omit = omit,
        filter: Optional[report_query_citations_params.Filter] | Omit = omit,
        group_by: List[Literal["page", "date", "model", "topic", "region", "persona", "prompt"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["count", "citation_share", "rank", "first_cited_at"]]] | Omit = omit,
        scope: Literal["all", "owned"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportQueryCitationsResponse:
        """
        Query Citations V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          entity: What each row represents: `domain` (default), `page`, or `citation_category`.
              Legacy: `group_by: ["page"]` (with `entity` omitted) is still accepted and is
              equivalent to `entity: "page"`. `citation_category` uses the dashboard split
              view: a citation counts under both its page-level and domain-level category, so
              category shares can sum to more than 100%.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          scope: `all` (every cited domain) or `owned` (only your owned domains). Applies to
              `entity=domain`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/citations",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "entity": entity,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "scope": scope,
                },
                report_query_citations_params.ReportQueryCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportQueryCitationsResponse,
        )

    async def query_fanouts(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["prompt", "query", "model", "region", "date"]] | Omit = omit,
        filters: Iterable[report_query_fanouts_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """Query Fanouts

        Args:
          end_date: End date.

        Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          start_date: Start date. Accepts YYYY-MM-DD, YYYY-MM-DD HH:MM, or ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: Filters to apply to the query fanout report.

          order_by: Custom ordering. Keys must be a requested metric or the `date` dimension. Values
              are `asc` or `desc`. Defaults to first metric descending.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/query-fanouts",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_query_fanouts_params.ReportQueryFanoutsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def query_query_fanouts(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[report_query_query_fanouts_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "model", "region", "prompt", "query"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]]
        | Omit = omit,
        sort: Optional[report_query_query_fanouts_params.Sort] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportQueryQueryFanoutsResponse:
        """
        Query Fanouts V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/query-fanouts",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "sort": sort,
                },
                report_query_query_fanouts_params.ReportQueryQueryFanoutsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportQueryQueryFanoutsResponse,
        )

    async def query_sentiment(
        self,
        *,
        asset: str,
        category_id: str,
        end_date: str,
        start_date: str,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[report_query_sentiment_params.Filter] | Omit = omit,
        group_by: List[
            Literal[
                "date", "model", "topic", "region", "prompt", "persona", "tag", "theme", "claim", "run", "competitor"
            ]
        ]
        | Omit = omit,
        include_cited_websites: bool | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["positive_sentiment", "negative_sentiment", "occurrence"]]] | Omit = omit,
        sort: report_query_sentiment_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportQuerySentimentResponse:
        """
        Query Sentiment V2

        Args:
          asset: The brand name to analyze (sentiment is extracted on name, not id).

          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          comparison_end_date: YYYY-MM-DD, ET, inclusive (with start).

          comparison_start_date: YYYY-MM-DD, ET, inclusive (with end).

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          include_cited_websites: Return cited websites per row (only when grouping by `theme`/`claim`).

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/sentiment",
            body=await async_maybe_transform(
                {
                    "asset": asset,
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "include_cited_websites": include_cited_websites,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "sort": sort,
                },
                report_query_sentiment_params.ReportQuerySentimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportQuerySentimentResponse,
        )

    async def query_visibility(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        assets: Optional[report_query_visibility_params.Assets] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[report_query_visibility_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "model", "topic", "region", "prompt", "persona"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["visibility_score", "share_of_voice", "average_position"]]] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        sort: report_query_visibility_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportQueryVisibilityResponse:
        """
        Query Visibility V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          assets: A name (`is`), a list (`in`), or {op,value} with op `is`/`in`/`not_in`.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/visibility",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "assets": assets,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "scope": scope,
                    "sort": sort,
                },
                report_query_visibility_params.ReportQueryVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportQueryVisibilityResponse,
        )

    async def sentiment(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["positive", "negative", "occurrences"]],
        start_date: Union[str, datetime],
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
        filters: Iterable[report_sentiment_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """Get citations for a given category.

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the sentiment report.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/sentiment",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_sentiment_params.ReportSentimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def sentiment_v2(
        self,
        *,
        asset_name: str,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["sentiment", "occurrence"]],
        start_date: Union[str, datetime],
        comparison_end_date: Union[str, datetime, None] | Omit = omit,
        comparison_start_date: Union[str, datetime, None] | Omit = omit,
        date_bucket: Literal["day", "week", "month"] | Omit = omit,
        dimensions: List[
            Literal[
                "date", "topic", "region", "model", "prompt", "persona", "tag", "theme", "claim", "run", "asset_name"
            ]
        ]
        | Omit = omit,
        filters: Iterable[report_sentiment_v2_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportSentimentV2Response:
        """Query Sentiment V2

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          comparison_end_date: End of the previous period for delta computation.

          comparison_start_date: Start of the previous period for delta computation.

          date_bucket: Date bucket for the report. Only used when dimensions includes date.

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the sentiment-v2 report.

          order_by: Custom ordering of report results. Dimension keys must also be present in
              dimensions. The sentiment metric orders by positive_sentiment.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/sentiment-v2",
            body=await async_maybe_transform(
                {
                    "asset_name": asset_name,
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_bucket": date_bucket,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_sentiment_v2_params.ReportSentimentV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportSentimentV2Response,
        )

    async def stream_citations(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["count", "citation_share", "share_of_voice", "first_cited_at"]],
        start_date: Union[str, datetime],
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
        filters: Iterable[report_stream_citations_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
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
          end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          metrics: Metrics to include. `share_of_voice` is deprecated, use `citation_share`
              instead.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the citations report.

          order_by: Custom ordering of the report results.

                  The order is a record of key-value pairs where:
                  - `key` is the field to order by, which can be a metric or dimension
                  - `value` is the direction of the order, either `asc` for ascending or `desc` for descending.

                  When not specified, the default order is the first metric in the query descending.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v1/reports/citations/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_stream_citations_params.ReportStreamCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamCitationsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[ReportStreamCitationsResponse],
        )

    async def stream_citations_v2(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        entity: Literal["domain", "page", "citation_category"] | Omit = omit,
        filter: Optional[report_stream_citations_v2_params.Filter] | Omit = omit,
        group_by: List[Literal["page", "date", "model", "topic", "region", "persona", "prompt"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["count", "citation_share", "rank", "first_cited_at"]]] | Omit = omit,
        scope: Literal["all", "owned"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ReportStreamCitationsV2Response]:
        """
        Stream Citations V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          entity: What each row represents: `domain` (default), `page`, or `citation_category`.
              Legacy: `group_by: ["page"]` (with `entity` omitted) is still accepted and is
              equivalent to `entity: "page"`. `citation_category` uses the dashboard split
              view: a citation counts under both its page-level and domain-level category, so
              category shares can sum to more than 100%.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          scope: `all` (every cited domain) or `owned` (only your owned domains). Applies to
              `entity=domain`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/citations/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "entity": entity,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "scope": scope,
                },
                report_stream_citations_v2_params.ReportStreamCitationsV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamCitationsV2Response
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[ReportStreamCitationsV2Response],
        )

    async def stream_query_fanouts(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[report_stream_query_fanouts_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "model", "region", "prompt", "query"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["fanouts_per_execution", "total_fanouts", "share", "query_variations"]]]
        | Omit = omit,
        sort: Optional[report_stream_query_fanouts_params.Sort] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ReportStreamQueryFanoutsResponse]:
        """
        Stream Query Fanouts V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/query-fanouts/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "sort": sort,
                },
                report_stream_query_fanouts_params.ReportStreamQueryFanoutsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamQueryFanoutsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[ReportStreamQueryFanoutsResponse],
        )

    async def stream_sentiment(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["positive", "negative", "occurrences"]],
        start_date: Union[str, datetime],
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
        filters: Iterable[report_stream_sentiment_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ReportStreamSentimentResponse]:
        """Stream Sentiment

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the sentiment report.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v1/reports/sentiment/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_stream_sentiment_params.ReportStreamSentimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamSentimentResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[ReportStreamSentimentResponse],
        )

    async def stream_sentiment_v2(
        self,
        *,
        asset: str,
        category_id: str,
        end_date: str,
        start_date: str,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[report_stream_sentiment_v2_params.Filter] | Omit = omit,
        group_by: List[
            Literal[
                "date", "model", "topic", "region", "prompt", "persona", "tag", "theme", "claim", "run", "competitor"
            ]
        ]
        | Omit = omit,
        include_cited_websites: bool | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["positive_sentiment", "negative_sentiment", "occurrence"]]] | Omit = omit,
        sort: report_stream_sentiment_v2_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ReportStreamSentimentV2Response]:
        """
        Stream Sentiment V2

        Args:
          asset: The brand name to analyze (sentiment is extracted on name, not id).

          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          comparison_end_date: YYYY-MM-DD, ET, inclusive (with start).

          comparison_start_date: YYYY-MM-DD, ET, inclusive (with end).

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          include_cited_websites: Return cited websites per row (only when grouping by `theme`/`claim`).

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/sentiment/stream",
            body=await async_maybe_transform(
                {
                    "asset": asset,
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "include_cited_websites": include_cited_websites,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "sort": sort,
                },
                report_stream_sentiment_v2_params.ReportStreamSentimentV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamSentimentV2Response
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[ReportStreamSentimentV2Response],
        )

    async def stream_visibility(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[
            Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]
        ],
        start_date: Union[str, datetime],
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
        filters: Iterable[report_stream_visibility_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ReportStreamVisibilityResponse]:
        """Stream Visibility

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the visibility report.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Offset-based pagination parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v1/reports/visibility/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_stream_visibility_params.ReportStreamVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamVisibilityResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[ReportStreamVisibilityResponse],
        )

    async def stream_visibility_v2(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        assets: Optional[report_stream_visibility_v2_params.Assets] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[report_stream_visibility_v2_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "model", "topic", "region", "prompt", "persona"]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        metrics: Optional[List[Literal["visibility_score", "share_of_voice", "average_position"]]] | Omit = omit,
        scope: Literal["owned", "all"] | Omit = omit,
        sort: report_stream_visibility_v2_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ReportStreamVisibilityV2Response]:
        """
        Stream Visibility V2

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          assets: A name (`is`), a list (`in`), or {op,value} with op `is`/`in`/`not_in`.

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          limit: Page size; default 10, max 50.

          max_results: Stream endpoint only: cap the number of streamed rows (default: all).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/visibility/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "assets": assets,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "interval": interval,
                    "limit": limit,
                    "max_results": max_results,
                    "metrics": metrics,
                    "scope": scope,
                    "sort": sort,
                },
                report_stream_visibility_v2_params.ReportStreamVisibilityV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, ReportStreamVisibilityV2Response
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[ReportStreamVisibilityV2Response],
        )

    async def visibility(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[
            Literal["share_of_voice", "mentions_count", "visibility_score", "executions", "average_position"]
        ],
        start_date: Union[str, datetime],
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
        filters: Iterable[report_visibility_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportResponse:
        """Query visibility report.

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the visibility report.

          order_by: Custom ordering of the report results.

              The order is a record of key-value pairs where:

              - key is the field to order by, which can be a metric or dimension
              - value is the direction of the order, either 'asc' for ascending or 'desc' for
                descending.

              When not specified, the default order is the first metric in the query
              descending.

          pagination: Pagination settings for the report results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/visibility",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_visibility_params.ReportVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.citations = to_raw_response_wrapper(
            reports.citations,
        )
        self.get_bots_report = to_raw_response_wrapper(
            reports.get_bots_report,
        )
        self.get_bots_report_v2 = to_raw_response_wrapper(
            reports.get_bots_report_v2,
        )
        self.get_referrals_report = to_raw_response_wrapper(
            reports.get_referrals_report,
        )
        self.get_referrals_report_v2 = to_raw_response_wrapper(
            reports.get_referrals_report_v2,
        )
        self.query_citations = to_raw_response_wrapper(
            reports.query_citations,
        )
        self.query_fanouts = to_raw_response_wrapper(
            reports.query_fanouts,
        )
        self.query_query_fanouts = to_raw_response_wrapper(
            reports.query_query_fanouts,
        )
        self.query_sentiment = to_raw_response_wrapper(
            reports.query_sentiment,
        )
        self.query_visibility = to_raw_response_wrapper(
            reports.query_visibility,
        )
        self.sentiment = to_raw_response_wrapper(
            reports.sentiment,
        )
        self.sentiment_v2 = to_raw_response_wrapper(
            reports.sentiment_v2,
        )
        self.stream_citations = to_raw_response_wrapper(
            reports.stream_citations,
        )
        self.stream_citations_v2 = to_raw_response_wrapper(
            reports.stream_citations_v2,
        )
        self.stream_query_fanouts = to_raw_response_wrapper(
            reports.stream_query_fanouts,
        )
        self.stream_sentiment = to_raw_response_wrapper(
            reports.stream_sentiment,
        )
        self.stream_sentiment_v2 = to_raw_response_wrapper(
            reports.stream_sentiment_v2,
        )
        self.stream_visibility = to_raw_response_wrapper(
            reports.stream_visibility,
        )
        self.stream_visibility_v2 = to_raw_response_wrapper(
            reports.stream_visibility_v2,
        )
        self.visibility = to_raw_response_wrapper(
            reports.visibility,
        )

    @cached_property
    def web_search_results(self) -> WebSearchResultsResourceWithRawResponse:
        return WebSearchResultsResourceWithRawResponse(self._reports.web_search_results)

    @cached_property
    def shopping(self) -> ShoppingResourceWithRawResponse:
        return ShoppingResourceWithRawResponse(self._reports.shopping)

    @cached_property
    def accuracy(self) -> AccuracyResourceWithRawResponse:
        return AccuracyResourceWithRawResponse(self._reports.accuracy)

    @cached_property
    def factcheck(self) -> FactcheckResourceWithRawResponse:
        return FactcheckResourceWithRawResponse(self._reports.factcheck)


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.citations = async_to_raw_response_wrapper(
            reports.citations,
        )
        self.get_bots_report = async_to_raw_response_wrapper(
            reports.get_bots_report,
        )
        self.get_bots_report_v2 = async_to_raw_response_wrapper(
            reports.get_bots_report_v2,
        )
        self.get_referrals_report = async_to_raw_response_wrapper(
            reports.get_referrals_report,
        )
        self.get_referrals_report_v2 = async_to_raw_response_wrapper(
            reports.get_referrals_report_v2,
        )
        self.query_citations = async_to_raw_response_wrapper(
            reports.query_citations,
        )
        self.query_fanouts = async_to_raw_response_wrapper(
            reports.query_fanouts,
        )
        self.query_query_fanouts = async_to_raw_response_wrapper(
            reports.query_query_fanouts,
        )
        self.query_sentiment = async_to_raw_response_wrapper(
            reports.query_sentiment,
        )
        self.query_visibility = async_to_raw_response_wrapper(
            reports.query_visibility,
        )
        self.sentiment = async_to_raw_response_wrapper(
            reports.sentiment,
        )
        self.sentiment_v2 = async_to_raw_response_wrapper(
            reports.sentiment_v2,
        )
        self.stream_citations = async_to_raw_response_wrapper(
            reports.stream_citations,
        )
        self.stream_citations_v2 = async_to_raw_response_wrapper(
            reports.stream_citations_v2,
        )
        self.stream_query_fanouts = async_to_raw_response_wrapper(
            reports.stream_query_fanouts,
        )
        self.stream_sentiment = async_to_raw_response_wrapper(
            reports.stream_sentiment,
        )
        self.stream_sentiment_v2 = async_to_raw_response_wrapper(
            reports.stream_sentiment_v2,
        )
        self.stream_visibility = async_to_raw_response_wrapper(
            reports.stream_visibility,
        )
        self.stream_visibility_v2 = async_to_raw_response_wrapper(
            reports.stream_visibility_v2,
        )
        self.visibility = async_to_raw_response_wrapper(
            reports.visibility,
        )

    @cached_property
    def web_search_results(self) -> AsyncWebSearchResultsResourceWithRawResponse:
        return AsyncWebSearchResultsResourceWithRawResponse(self._reports.web_search_results)

    @cached_property
    def shopping(self) -> AsyncShoppingResourceWithRawResponse:
        return AsyncShoppingResourceWithRawResponse(self._reports.shopping)

    @cached_property
    def accuracy(self) -> AsyncAccuracyResourceWithRawResponse:
        return AsyncAccuracyResourceWithRawResponse(self._reports.accuracy)

    @cached_property
    def factcheck(self) -> AsyncFactcheckResourceWithRawResponse:
        return AsyncFactcheckResourceWithRawResponse(self._reports.factcheck)


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.citations = to_streamed_response_wrapper(
            reports.citations,
        )
        self.get_bots_report = to_streamed_response_wrapper(
            reports.get_bots_report,
        )
        self.get_bots_report_v2 = to_streamed_response_wrapper(
            reports.get_bots_report_v2,
        )
        self.get_referrals_report = to_streamed_response_wrapper(
            reports.get_referrals_report,
        )
        self.get_referrals_report_v2 = to_streamed_response_wrapper(
            reports.get_referrals_report_v2,
        )
        self.query_citations = to_streamed_response_wrapper(
            reports.query_citations,
        )
        self.query_fanouts = to_streamed_response_wrapper(
            reports.query_fanouts,
        )
        self.query_query_fanouts = to_streamed_response_wrapper(
            reports.query_query_fanouts,
        )
        self.query_sentiment = to_streamed_response_wrapper(
            reports.query_sentiment,
        )
        self.query_visibility = to_streamed_response_wrapper(
            reports.query_visibility,
        )
        self.sentiment = to_streamed_response_wrapper(
            reports.sentiment,
        )
        self.sentiment_v2 = to_streamed_response_wrapper(
            reports.sentiment_v2,
        )
        self.stream_citations = to_streamed_response_wrapper(
            reports.stream_citations,
        )
        self.stream_citations_v2 = to_streamed_response_wrapper(
            reports.stream_citations_v2,
        )
        self.stream_query_fanouts = to_streamed_response_wrapper(
            reports.stream_query_fanouts,
        )
        self.stream_sentiment = to_streamed_response_wrapper(
            reports.stream_sentiment,
        )
        self.stream_sentiment_v2 = to_streamed_response_wrapper(
            reports.stream_sentiment_v2,
        )
        self.stream_visibility = to_streamed_response_wrapper(
            reports.stream_visibility,
        )
        self.stream_visibility_v2 = to_streamed_response_wrapper(
            reports.stream_visibility_v2,
        )
        self.visibility = to_streamed_response_wrapper(
            reports.visibility,
        )

    @cached_property
    def web_search_results(self) -> WebSearchResultsResourceWithStreamingResponse:
        return WebSearchResultsResourceWithStreamingResponse(self._reports.web_search_results)

    @cached_property
    def shopping(self) -> ShoppingResourceWithStreamingResponse:
        return ShoppingResourceWithStreamingResponse(self._reports.shopping)

    @cached_property
    def accuracy(self) -> AccuracyResourceWithStreamingResponse:
        return AccuracyResourceWithStreamingResponse(self._reports.accuracy)

    @cached_property
    def factcheck(self) -> FactcheckResourceWithStreamingResponse:
        return FactcheckResourceWithStreamingResponse(self._reports.factcheck)


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.citations = async_to_streamed_response_wrapper(
            reports.citations,
        )
        self.get_bots_report = async_to_streamed_response_wrapper(
            reports.get_bots_report,
        )
        self.get_bots_report_v2 = async_to_streamed_response_wrapper(
            reports.get_bots_report_v2,
        )
        self.get_referrals_report = async_to_streamed_response_wrapper(
            reports.get_referrals_report,
        )
        self.get_referrals_report_v2 = async_to_streamed_response_wrapper(
            reports.get_referrals_report_v2,
        )
        self.query_citations = async_to_streamed_response_wrapper(
            reports.query_citations,
        )
        self.query_fanouts = async_to_streamed_response_wrapper(
            reports.query_fanouts,
        )
        self.query_query_fanouts = async_to_streamed_response_wrapper(
            reports.query_query_fanouts,
        )
        self.query_sentiment = async_to_streamed_response_wrapper(
            reports.query_sentiment,
        )
        self.query_visibility = async_to_streamed_response_wrapper(
            reports.query_visibility,
        )
        self.sentiment = async_to_streamed_response_wrapper(
            reports.sentiment,
        )
        self.sentiment_v2 = async_to_streamed_response_wrapper(
            reports.sentiment_v2,
        )
        self.stream_citations = async_to_streamed_response_wrapper(
            reports.stream_citations,
        )
        self.stream_citations_v2 = async_to_streamed_response_wrapper(
            reports.stream_citations_v2,
        )
        self.stream_query_fanouts = async_to_streamed_response_wrapper(
            reports.stream_query_fanouts,
        )
        self.stream_sentiment = async_to_streamed_response_wrapper(
            reports.stream_sentiment,
        )
        self.stream_sentiment_v2 = async_to_streamed_response_wrapper(
            reports.stream_sentiment_v2,
        )
        self.stream_visibility = async_to_streamed_response_wrapper(
            reports.stream_visibility,
        )
        self.stream_visibility_v2 = async_to_streamed_response_wrapper(
            reports.stream_visibility_v2,
        )
        self.visibility = async_to_streamed_response_wrapper(
            reports.visibility,
        )

    @cached_property
    def web_search_results(self) -> AsyncWebSearchResultsResourceWithStreamingResponse:
        return AsyncWebSearchResultsResourceWithStreamingResponse(self._reports.web_search_results)

    @cached_property
    def shopping(self) -> AsyncShoppingResourceWithStreamingResponse:
        return AsyncShoppingResourceWithStreamingResponse(self._reports.shopping)

    @cached_property
    def accuracy(self) -> AsyncAccuracyResourceWithStreamingResponse:
        return AsyncAccuracyResourceWithStreamingResponse(self._reports.accuracy)

    @cached_property
    def factcheck(self) -> AsyncFactcheckResourceWithStreamingResponse:
        return AsyncFactcheckResourceWithStreamingResponse(self._reports.factcheck)
