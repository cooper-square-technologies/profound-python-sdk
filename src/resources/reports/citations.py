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
from ...types.reports.citation_query_v1_reports_post_response import CitationQueryV1ReportsPostResponse, CitationsResult
from ...types.pagination import Pagination
from ...types.hostname_filter import HostnameFilter
from ...types.path_filter import PathFilter
from ...types.region_id_filter import RegionIdFilter
from ...types.region_name_filter import RegionNameFilter
from ...types.topic_id_filter import TopicIdFilter
from ...types.topic_name_filter import TopicNameFilter
from ...types.model_id_filter import ModelIdFilter
from ...types.tag_id_filter import TagIdFilter
from ...types.tag_name_filter import TagNameFilter
from ...types.url_filter import UrlFilter
from ...types.root_domain_filter import RootDomainFilter
from ...types.analysis_type_filter import AnalysisTypeFilter
from ...types.prompt_type_filter import PromptTypeFilter
from ...types.persona_id_filter import PersonaIdFilter
from ...types.prompt_filter import PromptFilter
from ...types.prompt_id_filter import PromptIdFilter
from ...types.reports import citation_query_v1_reports_post_params
from ...types.reports.citation_stream_v1_reports_stream_post_response import CitationStreamV1ReportsStreamPostResponse, Query, CitationStreamV1ReportsStreamPostResponse2
from ...types.pagination import Pagination
from ...types.hostname_filter import HostnameFilter
from ...types.path_filter import PathFilter
from ...types.region_id_filter import RegionIdFilter
from ...types.region_name_filter import RegionNameFilter
from ...types.topic_id_filter import TopicIdFilter
from ...types.topic_name_filter import TopicNameFilter
from ...types.model_id_filter import ModelIdFilter
from ...types.tag_id_filter import TagIdFilter
from ...types.tag_name_filter import TagNameFilter
from ...types.url_filter import UrlFilter
from ...types.root_domain_filter import RootDomainFilter
from ...types.analysis_type_filter import AnalysisTypeFilter
from ...types.prompt_type_filter import PromptTypeFilter
from ...types.persona_id_filter import PersonaIdFilter
from ...types.prompt_filter import PromptFilter
from ...types.prompt_id_filter import PromptIdFilter
from ...types.reports import citation_stream_v1_reports_stream_post_params
from ...types.reports.citation_query_v2_v2_reports_post_response import CitationQueryV2V2ReportsPostResponse
from ...types.reports import citation_query_v2_v2_reports_post_params
from ...types.reports import citation_stream_v2_v2_reports_stream_post_params

__all__ = ["CitationsResource", "AsyncCitationsResource"]


class CitationsResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> CitationsResourceWithRawResponse:
        return CitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CitationsResourceWithStreamingResponse:
        return CitationsResourceWithStreamingResponse(self)

    def query_v1_reports_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["hostname", "path", "date", "region", "topic", "topic_id", "model", "tag", "prompt", "prompt_id", "url", "root_domain", "persona", "citation_category"]] | Omit = omit,
        metrics: Iterable[Literal["count", "citation_share", "share_of_voice", "first_cited_at"]],
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
    ) -> CitationQueryV1ReportsPostResponse:
        """
        Get citations for a given category.
        
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
            CitationQueryV1ReportsPostResponse: Successful Response
        
        Example:
            ```python
            citation = client.reports.citations.query_v1_reports_post(
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
            citation_query_v1_reports_post_params.CitationQueryV1ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CitationQueryV1ReportsPostResponse,
        )

    def stream_v1_reports_stream_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["hostname", "path", "date", "region", "topic", "topic_id", "model", "tag", "prompt", "prompt_id", "url", "root_domain", "persona", "citation_category"]] | Omit = omit,
        metrics: Iterable[Literal["count", "citation_share", "share_of_voice", "first_cited_at"]],
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
    ) -> Stream[CitationStreamV1ReportsStreamPostResponse]:
        """
        Stream Citations
        
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
            Stream[CitationStreamV1ReportsStreamPostResponse]: Server-sent events stream. Emits a `summary` event first, then one `row` event per streamed row.
        
        Example:
            ```python
            stream = client.reports.citations.stream_v1_reports_stream_post(
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
            "/v1/reports/citations/stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CitationStreamV1ReportsStreamPostResponse,
            stream=True,
            stream_cls=Stream[CitationStreamV1ReportsStreamPostResponse],
        )

    def query_v2_v2_reports_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: Iterable[Literal["page", "date", "model", "topic", "region", "persona", "prompt"]] | Omit = omit,
        metrics: Optional[Iterable[Literal["count", "citation_share", "rank", "first_cited_at"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        scope: Literal["all", "owned"] | Omit = omit,
        filter: Optional[citation_query_v2_v2_reports_post_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CitationQueryV2V2ReportsPostResponse:
        """
        Query Citations V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            scope: `all` (every cited domain) or `owned` (only your owned domains, for easy client-side totals).
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            CitationQueryV2V2ReportsPostResponse: Successful Response
        
        Example:
            ```python
            citation = client.reports.citations.query_v2_v2_reports_post(
                category_id="",
                start_date="",
                end_date="",
                interval="day",
                scope="all",
            )
            ```
        """
        return self._post(
            "/v2/reports/citations",
            body=maybe_transform(
            {
            "category_id": category_id,
            "start_date": start_date,
            "end_date": end_date,
            "group_by": group_by,
            "metrics": metrics,
            "interval": interval,
            "scope": scope,
            "filter": filter,
            "limit": limit,
            "max_results": max_results,
            "cursor": cursor,
        },
            citation_query_v2_v2_reports_post_params.CitationQueryV2V2ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CitationQueryV2V2ReportsPostResponse,
        )

    def stream_v2_v2_reports_stream_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: Iterable[Literal["page", "date", "model", "topic", "region", "persona", "prompt"]] | Omit = omit,
        metrics: Optional[Iterable[Literal["count", "citation_share", "rank", "first_cited_at"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        scope: Literal["all", "owned"] | Omit = omit,
        filter: Optional[citation_stream_v2_v2_reports_stream_post_params.Filter] | Omit = omit,
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
        Stream Citations V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            scope: `all` (every cited domain) or `owned` (only your owned domains, for easy client-side totals).
            filter: Body parameter.
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
            stream = client.reports.citations.stream_v2_v2_reports_stream_post(
                category_id="",
                start_date="",
                end_date="",
                interval="day",
                scope="all",
            )
            for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/citations/stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
            stream=True,
            stream_cls=Stream[str],
        )


class AsyncCitationsResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncCitationsResourceWithRawResponse:
        return AsyncCitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCitationsResourceWithStreamingResponse:
        return AsyncCitationsResourceWithStreamingResponse(self)

    async def query_v1_reports_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["hostname", "path", "date", "region", "topic", "topic_id", "model", "tag", "prompt", "prompt_id", "url", "root_domain", "persona", "citation_category"]] | Omit = omit,
        metrics: Iterable[Literal["count", "citation_share", "share_of_voice", "first_cited_at"]],
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
    ) -> CitationQueryV1ReportsPostResponse:
        """
        Get citations for a given category.
        
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
            CitationQueryV1ReportsPostResponse: Successful Response
        
        Example:
            ```python
            citation = await client.reports.citations.query_v1_reports_post(
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
            citation_query_v1_reports_post_params.CitationQueryV1ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CitationQueryV1ReportsPostResponse,
        )

    async def stream_v1_reports_stream_post(
        self,
        *,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["hostname", "path", "date", "region", "topic", "topic_id", "model", "tag", "prompt", "prompt_id", "url", "root_domain", "persona", "citation_category"]] | Omit = omit,
        metrics: Iterable[Literal["count", "citation_share", "share_of_voice", "first_cited_at"]],
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
    ) -> AsyncStream[CitationStreamV1ReportsStreamPostResponse]:
        """
        Stream Citations
        
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
            AsyncStream[CitationStreamV1ReportsStreamPostResponse]: Server-sent events stream. Emits a `summary` event first, then one `row` event per streamed row.
        
        Example:
            ```python
            stream = await client.reports.citations.stream_v1_reports_stream_post(
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
            "/v1/reports/citations/stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CitationStreamV1ReportsStreamPostResponse,
            stream=True,
            stream_cls=AsyncStream[CitationStreamV1ReportsStreamPostResponse],
        )

    async def query_v2_v2_reports_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: Iterable[Literal["page", "date", "model", "topic", "region", "persona", "prompt"]] | Omit = omit,
        metrics: Optional[Iterable[Literal["count", "citation_share", "rank", "first_cited_at"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        scope: Literal["all", "owned"] | Omit = omit,
        filter: Optional[citation_query_v2_v2_reports_post_params.Filter] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CitationQueryV2V2ReportsPostResponse:
        """
        Query Citations V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            scope: `all` (every cited domain) or `owned` (only your owned domains, for easy client-side totals).
            filter: Body parameter.
            limit: Page size; default 10, max 50.
            max_results: Stream endpoint only: cap the number of streamed rows (default: all).
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            CitationQueryV2V2ReportsPostResponse: Successful Response
        
        Example:
            ```python
            citation = await client.reports.citations.query_v2_v2_reports_post(
                category_id="",
                start_date="",
                end_date="",
                interval="day",
                scope="all",
            )
            ```
        """
        return await self._post(
            "/v2/reports/citations",
            body=await async_maybe_transform(
            {
            "category_id": category_id,
            "start_date": start_date,
            "end_date": end_date,
            "group_by": group_by,
            "metrics": metrics,
            "interval": interval,
            "scope": scope,
            "filter": filter,
            "limit": limit,
            "max_results": max_results,
            "cursor": cursor,
        },
            citation_query_v2_v2_reports_post_params.CitationQueryV2V2ReportsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CitationQueryV2V2ReportsPostResponse,
        )

    async def stream_v2_v2_reports_stream_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: Iterable[Literal["page", "date", "model", "topic", "region", "persona", "prompt"]] | Omit = omit,
        metrics: Optional[Iterable[Literal["count", "citation_share", "rank", "first_cited_at"]]] | Omit = omit,
        interval: Literal["day", "week", "month"] | Omit = omit,
        scope: Literal["all", "owned"] | Omit = omit,
        filter: Optional[citation_stream_v2_v2_reports_stream_post_params.Filter] | Omit = omit,
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
        Stream Citations V2
        
        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Body parameter.
            metrics: Body parameter.
            interval: Body parameter.
            scope: `all` (every cited domain) or `owned` (only your owned domains, for easy client-side totals).
            filter: Body parameter.
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
            stream = await client.reports.citations.stream_v2_v2_reports_stream_post(
                category_id="",
                start_date="",
                end_date="",
                interval="day",
                scope="all",
            )
            async for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/citations/stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[str],
        )


class CitationsResourceWithRawResponse:
    def __init__(self, citations: CitationsResource) -> None:
        self._citations = citations

        self.query_v1_reports_post = to_raw_response_wrapper(
            citations.query_v1_reports_post,
        )
        self.stream_v1_reports_stream_post = to_raw_response_wrapper(
            citations.stream_v1_reports_stream_post,
        )
        self.query_v2_v2_reports_post = to_raw_response_wrapper(
            citations.query_v2_v2_reports_post,
        )
        self.stream_v2_v2_reports_stream_post = to_raw_response_wrapper(
            citations.stream_v2_v2_reports_stream_post,
        )


class AsyncCitationsResourceWithRawResponse:
    def __init__(self, citations: AsyncCitationsResource) -> None:
        self._citations = citations

        self.query_v1_reports_post = async_to_raw_response_wrapper(
            citations.query_v1_reports_post,
        )
        self.stream_v1_reports_stream_post = async_to_raw_response_wrapper(
            citations.stream_v1_reports_stream_post,
        )
        self.query_v2_v2_reports_post = async_to_raw_response_wrapper(
            citations.query_v2_v2_reports_post,
        )
        self.stream_v2_v2_reports_stream_post = async_to_raw_response_wrapper(
            citations.stream_v2_v2_reports_stream_post,
        )


class CitationsResourceWithStreamingResponse:
    def __init__(self, citations: CitationsResource) -> None:
        self._citations = citations

        self.query_v1_reports_post = to_streamed_response_wrapper(
            citations.query_v1_reports_post,
        )
        self.stream_v1_reports_stream_post = to_streamed_response_wrapper(
            citations.stream_v1_reports_stream_post,
        )
        self.query_v2_v2_reports_post = to_streamed_response_wrapper(
            citations.query_v2_v2_reports_post,
        )
        self.stream_v2_v2_reports_stream_post = to_streamed_response_wrapper(
            citations.stream_v2_v2_reports_stream_post,
        )


class AsyncCitationsResourceWithStreamingResponse:
    def __init__(self, citations: AsyncCitationsResource) -> None:
        self._citations = citations

        self.query_v1_reports_post = async_to_streamed_response_wrapper(
            citations.query_v1_reports_post,
        )
        self.stream_v1_reports_stream_post = async_to_streamed_response_wrapper(
            citations.stream_v1_reports_stream_post,
        )
        self.query_v2_v2_reports_post = async_to_streamed_response_wrapper(
            citations.query_v2_v2_reports_post,
        )
        self.stream_v2_v2_reports_stream_post = async_to_streamed_response_wrapper(
            citations.stream_v2_v2_reports_stream_post,
        )
