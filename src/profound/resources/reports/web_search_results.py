# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Union, Iterable, Optional, cast
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
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.reports import web_search_result_query_params, web_search_result_stream_params
from ...types.shared_params.pagination import Pagination
from ...types.reports.web_search_result_query_response import WebSearchResultQueryResponse
from ...types.reports.web_search_result_stream_response import WebSearchResultStreamResponse

__all__ = ["WebSearchResultsResource", "AsyncWebSearchResultsResource"]


class WebSearchResultsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebSearchResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WebSearchResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebSearchResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return WebSearchResultsResourceWithStreamingResponse(self)

    def query(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["count", "search_share"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "hostname",
                "path",
                "url",
                "root_domain",
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "tag",
                "prompt",
                "prompt_id",
                "persona",
                "search_query",
            ]
        ]
        | Omit = omit,
        filters: Iterable[web_search_result_query_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebSearchResultQueryResponse:
        """
        Get web search results for a given category.

        Args:
          end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          metrics: Metrics to include. `search_share` is the per-prompt occurrence rate.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the web search results report.

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
            "/v1/reports/web-search-results",
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
                web_search_result_query_params.WebSearchResultQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebSearchResultQueryResponse,
        )

    def stream(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["count", "search_share"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "hostname",
                "path",
                "url",
                "root_domain",
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "tag",
                "prompt",
                "prompt_id",
                "persona",
                "search_query",
            ]
        ]
        | Omit = omit,
        filters: Iterable[web_search_result_stream_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[WebSearchResultStreamResponse]:
        """Stream Web Search Results

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          metrics: Metrics to include. `search_share` is the per-prompt occurrence rate.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the web search results report.

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
            "/v1/reports/web-search-results/stream",
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
                web_search_result_stream_params.WebSearchResultStreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, WebSearchResultStreamResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[WebSearchResultStreamResponse],
        )


class AsyncWebSearchResultsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebSearchResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWebSearchResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebSearchResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncWebSearchResultsResourceWithStreamingResponse(self)

    async def query(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["count", "search_share"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "hostname",
                "path",
                "url",
                "root_domain",
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "tag",
                "prompt",
                "prompt_id",
                "persona",
                "search_query",
            ]
        ]
        | Omit = omit,
        filters: Iterable[web_search_result_query_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebSearchResultQueryResponse:
        """
        Get web search results for a given category.

        Args:
          end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          metrics: Metrics to include. `search_share` is the per-prompt occurrence rate.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the web search results report.

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
            "/v1/reports/web-search-results",
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
                web_search_result_query_params.WebSearchResultQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebSearchResultQueryResponse,
        )

    async def stream(
        self,
        *,
        category_id: str,
        end_date: Union[str, datetime],
        metrics: List[Literal["count", "search_share"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: List[
            Literal[
                "hostname",
                "path",
                "url",
                "root_domain",
                "date",
                "region",
                "topic",
                "topic_id",
                "model",
                "tag",
                "prompt",
                "prompt_id",
                "persona",
                "search_query",
            ]
        ]
        | Omit = omit,
        filters: Iterable[web_search_result_stream_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Optional[Pagination] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[WebSearchResultStreamResponse]:
        """Stream Web Search Results

        Args:
          end_date: End date for the report.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          metrics: Metrics to include. `search_share` is the per-prompt occurrence rate.

          start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or
              full ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: List of filters to apply to the web search results report.

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
            "/v1/reports/web-search-results/stream",
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
                web_search_result_stream_params.WebSearchResultStreamParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, WebSearchResultStreamResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[WebSearchResultStreamResponse],
        )


class WebSearchResultsResourceWithRawResponse:
    def __init__(self, web_search_results: WebSearchResultsResource) -> None:
        self._web_search_results = web_search_results

        self.query = to_raw_response_wrapper(
            web_search_results.query,
        )
        self.stream = to_raw_response_wrapper(
            web_search_results.stream,
        )


class AsyncWebSearchResultsResourceWithRawResponse:
    def __init__(self, web_search_results: AsyncWebSearchResultsResource) -> None:
        self._web_search_results = web_search_results

        self.query = async_to_raw_response_wrapper(
            web_search_results.query,
        )
        self.stream = async_to_raw_response_wrapper(
            web_search_results.stream,
        )


class WebSearchResultsResourceWithStreamingResponse:
    def __init__(self, web_search_results: WebSearchResultsResource) -> None:
        self._web_search_results = web_search_results

        self.query = to_streamed_response_wrapper(
            web_search_results.query,
        )
        self.stream = to_streamed_response_wrapper(
            web_search_results.stream,
        )


class AsyncWebSearchResultsResourceWithStreamingResponse:
    def __init__(self, web_search_results: AsyncWebSearchResultsResource) -> None:
        self._web_search_results = web_search_results

        self.query = async_to_streamed_response_wrapper(
            web_search_results.query,
        )
        self.stream = async_to_streamed_response_wrapper(
            web_search_results.stream,
        )
