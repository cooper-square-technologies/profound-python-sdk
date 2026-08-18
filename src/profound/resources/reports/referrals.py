# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, Iterable, List, Optional, Union
from datetime import datetime
from typing_extensions import Literal

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
from ...types.shared.response import Response
from ...types.shared_params.pagination import Pagination
from ...types.shared_params.numeric_metric_filter import NumericMetricFilter
from ...types.reports import referral_create_v1_v1_post_params, referral_create_v2_v2_post_params

__all__ = ["ReferralsResource", "AsyncReferralsResource"]


class ReferralsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReferralsResourceWithRawResponse:
        return ReferralsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferralsResourceWithStreamingResponse:
        return ReferralsResourceWithStreamingResponse(self)

    def create_v1_v1_post(
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
        metric_filters: Iterable[NumericMetricFilter] | Omit = omit,
        filters: Iterable[referral_create_v1_v1_post_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Response:
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
            Response: Successful Response

        Example:
            ```python
            referral = client.reports.referrals.create_v1_v1_post(
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
                referral_create_v1_v1_post_params.ReferralCreateV1V1PostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Response,
        )

    def create_v2_v2_post(
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
        metric_filters: Iterable[NumericMetricFilter] | Omit = omit,
        filters: Iterable[referral_create_v2_v2_post_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Response:
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
            Response: Successful Response

        Example:
            ```python
            referral = client.reports.referrals.create_v2_v2_post(
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
                referral_create_v2_v2_post_params.ReferralCreateV2V2PostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Response,
        )


class AsyncReferralsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReferralsResourceWithRawResponse:
        return AsyncReferralsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferralsResourceWithStreamingResponse:
        return AsyncReferralsResourceWithStreamingResponse(self)

    async def create_v1_v1_post(
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
        metric_filters: Iterable[NumericMetricFilter] | Omit = omit,
        filters: Iterable[referral_create_v1_v1_post_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Response:
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
            Response: Successful Response

        Example:
            ```python
            referral = await client.reports.referrals.create_v1_v1_post(
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
                referral_create_v1_v1_post_params.ReferralCreateV1V1PostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Response,
        )

    async def create_v2_v2_post(
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
        metric_filters: Iterable[NumericMetricFilter] | Omit = omit,
        filters: Iterable[referral_create_v2_v2_post_params.Filter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Response:
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
            Response: Successful Response

        Example:
            ```python
            referral = await client.reports.referrals.create_v2_v2_post(
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
                referral_create_v2_v2_post_params.ReferralCreateV2V2PostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Response,
        )


class ReferralsResourceWithRawResponse:
    def __init__(self, referrals: ReferralsResource) -> None:
        self._referrals = referrals

        self.create_v1_v1_post = to_raw_response_wrapper(
            referrals.create_v1_v1_post,
        )
        self.create_v2_v2_post = to_raw_response_wrapper(
            referrals.create_v2_v2_post,
        )


class AsyncReferralsResourceWithRawResponse:
    def __init__(self, referrals: AsyncReferralsResource) -> None:
        self._referrals = referrals

        self.create_v1_v1_post = async_to_raw_response_wrapper(
            referrals.create_v1_v1_post,
        )
        self.create_v2_v2_post = async_to_raw_response_wrapper(
            referrals.create_v2_v2_post,
        )


class ReferralsResourceWithStreamingResponse:
    def __init__(self, referrals: ReferralsResource) -> None:
        self._referrals = referrals

        self.create_v1_v1_post = to_streamed_response_wrapper(
            referrals.create_v1_v1_post,
        )
        self.create_v2_v2_post = to_streamed_response_wrapper(
            referrals.create_v2_v2_post,
        )


class AsyncReferralsResourceWithStreamingResponse:
    def __init__(self, referrals: AsyncReferralsResource) -> None:
        self._referrals = referrals

        self.create_v1_v1_post = async_to_streamed_response_wrapper(
            referrals.create_v1_v1_post,
        )
        self.create_v2_v2_post = async_to_streamed_response_wrapper(
            referrals.create_v2_v2_post,
        )
