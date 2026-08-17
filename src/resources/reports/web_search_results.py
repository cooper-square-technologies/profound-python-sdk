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
from ...types.reports.web_search_result_query_response import WebSearchResultQueryResponse, WebSearchResultsResult
from ...types.pagination import Pagination
from ...types.hostname_filter import HostnameFilter
from ...types.path_filter import PathFilter
from ...types.region_id_filter import RegionIdFilter
from ...types.topic_id_filter import TopicIdFilter
from ...types.model_id_filter import ModelIdFilter
from ...types.tag_id_filter import TagIdFilter
from ...types.url_filter import UrlFilter
from ...types.root_domain_filter import RootDomainFilter
from ...types.persona_id_filter import PersonaIdFilter
from ...types.prompt_filter import PromptFilter
from ...types.prompt_id_filter import PromptIdFilter
from ...types.reports import web_search_result_query_params
from ...types.reports.web_search_result_stream_response import WebSearchResultStreamResponse, Query, WebSearchResultStreamResponse2
from ...types.pagination import Pagination
from ...types.hostname_filter import HostnameFilter
from ...types.path_filter import PathFilter
from ...types.region_id_filter import RegionIdFilter
from ...types.topic_id_filter import TopicIdFilter
from ...types.model_id_filter import ModelIdFilter
from ...types.tag_id_filter import TagIdFilter
from ...types.url_filter import UrlFilter
from ...types.root_domain_filter import RootDomainFilter
from ...types.persona_id_filter import PersonaIdFilter
from ...types.prompt_filter import PromptFilter
from ...types.prompt_id_filter import PromptIdFilter
from ...types.reports import web_search_result_stream_params

__all__ = ["WebSearchResultsResource", "AsyncWebSearchResultsResource"]


class WebSearchResultsResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> WebSearchResultsResourceWithRawResponse:
        return WebSearchResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebSearchResultsResourceWithStreamingResponse:
        return WebSearchResultsResourceWithStreamingResponse(self)

    def query(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["hostname", "path", "url", "root_domain", "date", "region", "topic", "topic_id", "model", "tag", "prompt", "prompt_id", "persona", "search_query"]] | Omit = omit,
        metrics: Iterable[Literal["count", "search_share"]],
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
    ) -> WebSearchResultQueryResponse:
        """
        Get web search results for a given category.
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Metrics to include. `search_share` is the per-prompt occurrence rate.
            order_by: Custom ordering of the report results.
            pagination: Pagination settings for the report results.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the web search results report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WebSearchResultQueryResponse: Successful Response
        
        Example:
            ```python
            web_search_result = client.reports.web_search_results.query(
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
            "/v1/reports/web-search-results",
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
            web_search_result_query_params.WebSearchResultQueryParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WebSearchResultQueryResponse,
        )

    def stream(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["hostname", "path", "url", "root_domain", "date", "region", "topic", "topic_id", "model", "tag", "prompt", "prompt_id", "persona", "search_query"]] | Omit = omit,
        metrics: Iterable[Literal["count", "search_share"]],
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
    ) -> Stream[WebSearchResultStreamResponse]:
        """
        Stream Web Search Results
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Metrics to include. `search_share` is the per-prompt occurrence rate.
            order_by: Custom ordering of the report results.
            pagination: Body parameter.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the web search results report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            Stream[WebSearchResultStreamResponse]: Server-sent events stream. Emits a `summary` event first, then one `row` event per streamed row.
        
        Example:
            ```python
            stream = client.reports.web_search_results.stream(
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
            "/v1/reports/web-search-results/stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WebSearchResultStreamResponse,
            stream=True,
            stream_cls=Stream[WebSearchResultStreamResponse],
        )


class AsyncWebSearchResultsResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncWebSearchResultsResourceWithRawResponse:
        return AsyncWebSearchResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebSearchResultsResourceWithStreamingResponse:
        return AsyncWebSearchResultsResourceWithStreamingResponse(self)

    async def query(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["hostname", "path", "url", "root_domain", "date", "region", "topic", "topic_id", "model", "tag", "prompt", "prompt_id", "persona", "search_query"]] | Omit = omit,
        metrics: Iterable[Literal["count", "search_share"]],
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
    ) -> WebSearchResultQueryResponse:
        """
        Get web search results for a given category.
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Metrics to include. `search_share` is the per-prompt occurrence rate.
            order_by: Custom ordering of the report results.
            pagination: Pagination settings for the report results.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the web search results report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WebSearchResultQueryResponse: Successful Response
        
        Example:
            ```python
            web_search_result = await client.reports.web_search_results.query(
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
            "/v1/reports/web-search-results",
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
            web_search_result_query_params.WebSearchResultQueryParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WebSearchResultQueryResponse,
        )

    async def stream(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["hostname", "path", "url", "root_domain", "date", "region", "topic", "topic_id", "model", "tag", "prompt", "prompt_id", "persona", "search_query"]] | Omit = omit,
        metrics: Iterable[Literal["count", "search_share"]],
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
    ) -> AsyncStream[WebSearchResultStreamResponse]:
        """
        Stream Web Search Results
        
        Args:
            date_interval: Date interval for the report. (only used with date dimension)
            dimensions: Dimensions to group the report by.
            metrics: Metrics to include. `search_share` is the per-prompt occurrence rate.
            order_by: Custom ordering of the report results.
            pagination: Body parameter.
            category_id: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            filters: List of filters to apply to the web search results report.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AsyncStream[WebSearchResultStreamResponse]: Server-sent events stream. Emits a `summary` event first, then one `row` event per streamed row.
        
        Example:
            ```python
            stream = await client.reports.web_search_results.stream(
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
            "/v1/reports/web-search-results/stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WebSearchResultStreamResponse,
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
