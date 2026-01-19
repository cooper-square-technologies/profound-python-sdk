# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    report_citations_params,
    report_sentiment_params,
    report_visibility_params,
    report_get_bots_report_params,
    report_get_referrals_report_params,
)
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
from ..types.report_response import ReportResponse
from ..types.shared_params.pagination import Pagination
from ..types.report_citations_response import ReportCitationsResponse

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
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
        metrics: List[Literal["count", "share_of_voice"]],
        start_date: Union[str, datetime],
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[
            Literal[
                "hostname",
                "path",
                "date",
                "region",
                "topic",
                "model",
                "tag",
                "prompt",
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
        """Get citations for a given category.

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the citations report.

          order_by: Custom ordering of the report results.

                  The order is a record of key-value pairs where:
                  - `key` is the field to order by, which can be a metric and/or `date`, `hostname`, `path` dimensions
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
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[Literal["date", "path", "bot_name", "bot_provider"]] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[report_get_bots_report_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
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
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_get_bots_report_params.ReportGetBotsReportParams,
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
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[Literal["date", "path", "referral_source"]] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[report_get_referrals_report_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
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
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_get_referrals_report_params.ReportGetReferralsReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    def sentiment(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["positive", "negative", "occurrences"]],
        start_date: Union[str, datetime],
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[
            Literal[
                "theme",
                "date",
                "region",
                "topic",
                "model",
                "asset_id",
                "asset_name",
                "tag",
                "prompt",
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

    def visibility(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["share_of_voice", "mentions_count", "visibility_score", "executions"]],
        start_date: Union[str, datetime],
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[
            Literal["date", "region", "topic", "model", "asset_id", "asset_name", "prompt", "tag", "persona"]
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
        metrics: List[Literal["count", "share_of_voice"]],
        start_date: Union[str, datetime],
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[
            Literal[
                "hostname",
                "path",
                "date",
                "region",
                "topic",
                "model",
                "tag",
                "prompt",
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
        """Get citations for a given category.

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the citations report.

          order_by: Custom ordering of the report results.

                  The order is a record of key-value pairs where:
                  - `key` is the field to order by, which can be a metric and/or `date`, `hostname`, `path` dimensions
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
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[Literal["date", "path", "bot_name", "bot_provider"]] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[report_get_bots_report_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
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
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_get_bots_report_params.ReportGetBotsReportParams,
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
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[Literal["date", "path", "referral_source"]] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[report_get_referrals_report_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
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
                    "order_by": order_by,
                    "pagination": pagination,
                },
                report_get_referrals_report_params.ReportGetReferralsReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportResponse,
        )

    async def sentiment(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["positive", "negative", "occurrences"]],
        start_date: Union[str, datetime],
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[
            Literal[
                "theme",
                "date",
                "region",
                "topic",
                "model",
                "asset_id",
                "asset_name",
                "tag",
                "prompt",
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

    async def visibility(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["share_of_voice", "mentions_count", "visibility_score", "executions"]],
        start_date: Union[str, datetime],
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[
            Literal["date", "region", "topic", "model", "asset_id", "asset_name", "prompt", "tag", "persona"]
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
        self.get_referrals_report = to_raw_response_wrapper(
            reports.get_referrals_report,
        )
        self.sentiment = to_raw_response_wrapper(
            reports.sentiment,
        )
        self.visibility = to_raw_response_wrapper(
            reports.visibility,
        )


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.citations = async_to_raw_response_wrapper(
            reports.citations,
        )
        self.get_bots_report = async_to_raw_response_wrapper(
            reports.get_bots_report,
        )
        self.get_referrals_report = async_to_raw_response_wrapper(
            reports.get_referrals_report,
        )
        self.sentiment = async_to_raw_response_wrapper(
            reports.sentiment,
        )
        self.visibility = async_to_raw_response_wrapper(
            reports.visibility,
        )


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.citations = to_streamed_response_wrapper(
            reports.citations,
        )
        self.get_bots_report = to_streamed_response_wrapper(
            reports.get_bots_report,
        )
        self.get_referrals_report = to_streamed_response_wrapper(
            reports.get_referrals_report,
        )
        self.sentiment = to_streamed_response_wrapper(
            reports.sentiment,
        )
        self.visibility = to_streamed_response_wrapper(
            reports.visibility,
        )


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.citations = async_to_streamed_response_wrapper(
            reports.citations,
        )
        self.get_bots_report = async_to_streamed_response_wrapper(
            reports.get_bots_report,
        )
        self.get_referrals_report = async_to_streamed_response_wrapper(
            reports.get_referrals_report,
        )
        self.sentiment = async_to_streamed_response_wrapper(
            reports.sentiment,
        )
        self.visibility = async_to_streamed_response_wrapper(
            reports.visibility,
        )
