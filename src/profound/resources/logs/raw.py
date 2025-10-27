# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Union, Iterable, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

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
from ...types.logs import raw_bots_params, raw_logs_params
from ..._base_client import make_request_options
from ...types.logs.raw_bots_response import RawBotsResponse
from ...types.logs.raw_logs_response import RawLogsResponse
from ...types.shared_params.pagination import Pagination

__all__ = ["RawResource", "AsyncRawResource"]


class RawResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RawResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return RawResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RawResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return RawResourceWithStreamingResponse(self)

    def bots(
        self,
        *,
        domain: str,
        metrics: List[Literal["count"]],
        start_date: Union[str, datetime],
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[
            Literal[
                "method",
                "path",
                "status_code",
                "ip",
                "user_agent",
                "referer",
                "query_params",
                "bot_name",
                "bot_provider",
                "bot_types",
            ]
        ]
        | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[raw_bots_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RawBotsResponse:
        """
        Get identified bot logs with filters

        Args:
          domain: Domain to query logs for.

          start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS,
              or full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          end_date: End date for logs. Accepts same formats as start_date. Defaults to now if
              omitted.

          filters: List of filters to apply to the bots logs query.

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
        return cast(
            RawBotsResponse,
            self._post(
                "/v1/logs/raw/bots",
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
                    raw_bots_params.RawBotsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, RawBotsResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def logs(
        self,
        *,
        domain: str,
        metrics: List[Literal["count"]],
        start_date: Union[str, datetime],
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[
            Literal[
                "timestamp",
                "method",
                "host",
                "path",
                "status_code",
                "ip",
                "user_agent",
                "referer",
                "bytes_sent",
                "duration_ms",
                "query_params",
            ]
        ]
        | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[raw_logs_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RawLogsResponse:
        """
        Get all logs with filters

        Args:
          domain: Domain to query logs for.

          start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS,
              or full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          end_date: End date for logs. Accepts same formats as start_date. Defaults to now if
              omitted.

          filters: Filters to apply to the logs query.

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
        return cast(
            RawLogsResponse,
            self._post(
                "/v1/logs/raw",
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
                    raw_logs_params.RawLogsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, RawLogsResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncRawResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRawResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRawResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRawResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncRawResourceWithStreamingResponse(self)

    async def bots(
        self,
        *,
        domain: str,
        metrics: List[Literal["count"]],
        start_date: Union[str, datetime],
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[
            Literal[
                "method",
                "path",
                "status_code",
                "ip",
                "user_agent",
                "referer",
                "query_params",
                "bot_name",
                "bot_provider",
                "bot_types",
            ]
        ]
        | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[raw_bots_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RawBotsResponse:
        """
        Get identified bot logs with filters

        Args:
          domain: Domain to query logs for.

          start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS,
              or full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          end_date: End date for logs. Accepts same formats as start_date. Defaults to now if
              omitted.

          filters: List of filters to apply to the bots logs query.

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
        return cast(
            RawBotsResponse,
            await self._post(
                "/v1/logs/raw/bots",
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
                    raw_bots_params.RawBotsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, RawBotsResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def logs(
        self,
        *,
        domain: str,
        metrics: List[Literal["count"]],
        start_date: Union[str, datetime],
        date_interval: Literal["day", "week", "month", "year"] | Omit = omit,
        dimensions: List[
            Literal[
                "timestamp",
                "method",
                "host",
                "path",
                "status_code",
                "ip",
                "user_agent",
                "referer",
                "bytes_sent",
                "duration_ms",
                "query_params",
            ]
        ]
        | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        filters: Iterable[raw_logs_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RawLogsResponse:
        """
        Get all logs with filters

        Args:
          domain: Domain to query logs for.

          start_date: Start date for logs. Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS,
              or full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          end_date: End date for logs. Accepts same formats as start_date. Defaults to now if
              omitted.

          filters: Filters to apply to the logs query.

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
        return cast(
            RawLogsResponse,
            await self._post(
                "/v1/logs/raw",
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
                    raw_logs_params.RawLogsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, RawLogsResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class RawResourceWithRawResponse:
    def __init__(self, raw: RawResource) -> None:
        self._raw = raw

        self.bots = to_raw_response_wrapper(
            raw.bots,
        )
        self.logs = to_raw_response_wrapper(
            raw.logs,
        )


class AsyncRawResourceWithRawResponse:
    def __init__(self, raw: AsyncRawResource) -> None:
        self._raw = raw

        self.bots = async_to_raw_response_wrapper(
            raw.bots,
        )
        self.logs = async_to_raw_response_wrapper(
            raw.logs,
        )


class RawResourceWithStreamingResponse:
    def __init__(self, raw: RawResource) -> None:
        self._raw = raw

        self.bots = to_streamed_response_wrapper(
            raw.bots,
        )
        self.logs = to_streamed_response_wrapper(
            raw.logs,
        )


class AsyncRawResourceWithStreamingResponse:
    def __init__(self, raw: AsyncRawResource) -> None:
        self._raw = raw

        self.bots = async_to_streamed_response_wrapper(
            raw.bots,
        )
        self.logs = async_to_streamed_response_wrapper(
            raw.logs,
        )
