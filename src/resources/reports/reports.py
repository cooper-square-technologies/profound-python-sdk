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
from .citations import (
    CitationsResource,
    AsyncCitationsResource,
    CitationsResourceWithRawResponse,
    AsyncCitationsResourceWithRawResponse,
    CitationsResourceWithStreamingResponse,
    AsyncCitationsResourceWithStreamingResponse,
)
from .visibility import (
    VisibilityResource,
    AsyncVisibilityResource,
    VisibilityResourceWithRawResponse,
    AsyncVisibilityResourceWithRawResponse,
    VisibilityResourceWithStreamingResponse,
    AsyncVisibilityResourceWithStreamingResponse,
)
from .sentiment import (
    SentimentResource,
    AsyncSentimentResource,
    SentimentResourceWithRawResponse,
    AsyncSentimentResourceWithRawResponse,
    SentimentResourceWithStreamingResponse,
    AsyncSentimentResourceWithStreamingResponse,
)
from .web_search_results import (
    WebSearchResultsResource,
    AsyncWebSearchResultsResource,
    WebSearchResultsResourceWithRawResponse,
    AsyncWebSearchResultsResourceWithRawResponse,
    WebSearchResultsResourceWithStreamingResponse,
    AsyncWebSearchResultsResourceWithStreamingResponse,
)
from .referrals import (
    ReferralsResource,
    AsyncReferralsResource,
    ReferralsResourceWithRawResponse,
    AsyncReferralsResourceWithRawResponse,
    ReferralsResourceWithStreamingResponse,
    AsyncReferralsResourceWithStreamingResponse,
)
from .bots import (
    BotsResource,
    AsyncBotsResource,
    BotsResourceWithRawResponse,
    AsyncBotsResourceWithRawResponse,
    BotsResourceWithStreamingResponse,
    AsyncBotsResourceWithStreamingResponse,
)
from .query_fanouts import (
    QueryFanoutsResource,
    AsyncQueryFanoutsResource,
    QueryFanoutsResourceWithRawResponse,
    AsyncQueryFanoutsResourceWithRawResponse,
    QueryFanoutsResourceWithStreamingResponse,
    AsyncQueryFanoutsResourceWithStreamingResponse,
)
from .shopping import (
    ShoppingResource,
    AsyncShoppingResource,
    ShoppingResourceWithRawResponse,
    AsyncShoppingResourceWithRawResponse,
    ShoppingResourceWithStreamingResponse,
    AsyncShoppingResourceWithStreamingResponse,
)
from .accuracy import (
    AccuracyResource,
    AsyncAccuracyResource,
    AccuracyResourceWithRawResponse,
    AsyncAccuracyResourceWithRawResponse,
    AccuracyResourceWithStreamingResponse,
    AsyncAccuracyResourceWithStreamingResponse,
)
from ...types.report_query_sentiment_v2_v1_sentiment_v2_post_response import ReportQuerySentimentV2V1SentimentV2PostResponse, SentimentV2ReportInfo, Query, SentimentDataPoint, SentimentPeriodScores, SentimentScores, SentimentGroupMetadata
from ...types.pagination import Pagination
from ...types import report_query_sentiment_v2_v1_sentiment_v2_post_params

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):

    @cached_property
    def citations(self) -> CitationsResource:
        return CitationsResource(self._client)

    @cached_property
    def visibility(self) -> VisibilityResource:
        return VisibilityResource(self._client)

    @cached_property
    def sentiment(self) -> SentimentResource:
        return SentimentResource(self._client)

    @cached_property
    def web_search_results(self) -> WebSearchResultsResource:
        return WebSearchResultsResource(self._client)

    @cached_property
    def referrals(self) -> ReferralsResource:
        return ReferralsResource(self._client)

    @cached_property
    def bots(self) -> BotsResource:
        return BotsResource(self._client)

    @cached_property
    def query_fanouts(self) -> QueryFanoutsResource:
        return QueryFanoutsResource(self._client)

    @cached_property
    def shopping(self) -> ShoppingResource:
        return ShoppingResource(self._client)

    @cached_property
    def accuracy(self) -> AccuracyResource:
        return AccuracyResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        return ReportsResourceWithStreamingResponse(self)

    def query_sentiment_v2_v1_sentiment_v2_post(
        self,
        *,
        category_id: str,
        asset_name: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["date", "topic", "region", "model", "prompt", "persona", "tag", "theme", "claim", "run", "asset_name"]] | Omit = omit,
        metrics: Iterable[Literal["sentiment", "occurrence"]],
        filters: Iterable[object] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportQuerySentimentV2V1SentimentV2PostResponse:
        """
        Query Sentiment V2
        
        Args:
            category_id: Body parameter.
            asset_name: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            comparison_start_date: Start of the previous period for delta computation.
            comparison_end_date: End of the previous period for delta computation.
            date_interval: Date interval for the report. Only used when dimensions includes date.
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            filters: List of filters to apply to the sentiment-v2 report.
            order_by: Custom ordering of report results. Dimension keys must also be present in dimensions. The sentiment metric orders by positive_sentiment.
            pagination: Pagination settings for the report results.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ReportQuerySentimentV2V1SentimentV2PostResponse: Successful Response
        
        Example:
            ```python
            report = client.reports.query_sentiment_v2_v1_sentiment_v2_post(
                category_id="",
                asset_name="",
                start_date="",
                end_date="",
                date_interval="day",
                metrics=[],
            )
            ```
        """
        return self._post(
            "/v1/reports/sentiment-v2",
            body=maybe_transform(
            {
            "category_id": category_id,
            "asset_name": asset_name,
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "date_interval": date_interval,
            "dimensions": dimensions,
            "metrics": metrics,
            "filters": filters,
            "order_by": order_by,
            "pagination": pagination,
        },
            report_query_sentiment_v2_v1_sentiment_v2_post_params.ReportQuerySentimentV2V1SentimentV2PostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReportQuerySentimentV2V1SentimentV2PostResponse,
        )


class AsyncReportsResource(AsyncAPIResource):

    @cached_property
    def citations(self) -> AsyncCitationsResource:
        return AsyncCitationsResource(self._client)

    @cached_property
    def visibility(self) -> AsyncVisibilityResource:
        return AsyncVisibilityResource(self._client)

    @cached_property
    def sentiment(self) -> AsyncSentimentResource:
        return AsyncSentimentResource(self._client)

    @cached_property
    def web_search_results(self) -> AsyncWebSearchResultsResource:
        return AsyncWebSearchResultsResource(self._client)

    @cached_property
    def referrals(self) -> AsyncReferralsResource:
        return AsyncReferralsResource(self._client)

    @cached_property
    def bots(self) -> AsyncBotsResource:
        return AsyncBotsResource(self._client)

    @cached_property
    def query_fanouts(self) -> AsyncQueryFanoutsResource:
        return AsyncQueryFanoutsResource(self._client)

    @cached_property
    def shopping(self) -> AsyncShoppingResource:
        return AsyncShoppingResource(self._client)

    @cached_property
    def accuracy(self) -> AsyncAccuracyResource:
        return AsyncAccuracyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        return AsyncReportsResourceWithStreamingResponse(self)

    async def query_sentiment_v2_v1_sentiment_v2_post(
        self,
        *,
        category_id: str,
        asset_name: str,
        start_date: Union[str, datetime],
        end_date: Union[str, datetime],
        comparison_start_date: Optional[Union[str, datetime]] | Omit = omit,
        comparison_end_date: Optional[Union[str, datetime]] | Omit = omit,
        date_interval: Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"] | Omit = omit,
        dimensions: Iterable[Literal["date", "topic", "region", "model", "prompt", "persona", "tag", "theme", "claim", "run", "asset_name"]] | Omit = omit,
        metrics: Iterable[Literal["sentiment", "occurrence"]],
        filters: Iterable[object] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportQuerySentimentV2V1SentimentV2PostResponse:
        """
        Query Sentiment V2
        
        Args:
            category_id: Body parameter.
            asset_name: Body parameter.
            start_date: Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            end_date: End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp.
            comparison_start_date: Start of the previous period for delta computation.
            comparison_end_date: End of the previous period for delta computation.
            date_interval: Date interval for the report. Only used when dimensions includes date.
            dimensions: Dimensions to group the report by.
            metrics: Body parameter.
            filters: List of filters to apply to the sentiment-v2 report.
            order_by: Custom ordering of report results. Dimension keys must also be present in dimensions. The sentiment metric orders by positive_sentiment.
            pagination: Pagination settings for the report results.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            ReportQuerySentimentV2V1SentimentV2PostResponse: Successful Response
        
        Example:
            ```python
            report = await client.reports.query_sentiment_v2_v1_sentiment_v2_post(
                category_id="",
                asset_name="",
                start_date="",
                end_date="",
                date_interval="day",
                metrics=[],
            )
            ```
        """
        return await self._post(
            "/v1/reports/sentiment-v2",
            body=await async_maybe_transform(
            {
            "category_id": category_id,
            "asset_name": asset_name,
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "date_interval": date_interval,
            "dimensions": dimensions,
            "metrics": metrics,
            "filters": filters,
            "order_by": order_by,
            "pagination": pagination,
        },
            report_query_sentiment_v2_v1_sentiment_v2_post_params.ReportQuerySentimentV2V1SentimentV2PostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReportQuerySentimentV2V1SentimentV2PostResponse,
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.query_sentiment_v2_v1_sentiment_v2_post = to_raw_response_wrapper(
            reports.query_sentiment_v2_v1_sentiment_v2_post,
        )

    @cached_property
    def citations(self) -> CitationsResourceWithRawResponse:
        return CitationsResourceWithRawResponse(self._reports.citations)

    @cached_property
    def visibility(self) -> VisibilityResourceWithRawResponse:
        return VisibilityResourceWithRawResponse(self._reports.visibility)

    @cached_property
    def sentiment(self) -> SentimentResourceWithRawResponse:
        return SentimentResourceWithRawResponse(self._reports.sentiment)

    @cached_property
    def web_search_results(self) -> WebSearchResultsResourceWithRawResponse:
        return WebSearchResultsResourceWithRawResponse(self._reports.web_search_results)

    @cached_property
    def referrals(self) -> ReferralsResourceWithRawResponse:
        return ReferralsResourceWithRawResponse(self._reports.referrals)

    @cached_property
    def bots(self) -> BotsResourceWithRawResponse:
        return BotsResourceWithRawResponse(self._reports.bots)

    @cached_property
    def query_fanouts(self) -> QueryFanoutsResourceWithRawResponse:
        return QueryFanoutsResourceWithRawResponse(self._reports.query_fanouts)

    @cached_property
    def shopping(self) -> ShoppingResourceWithRawResponse:
        return ShoppingResourceWithRawResponse(self._reports.shopping)

    @cached_property
    def accuracy(self) -> AccuracyResourceWithRawResponse:
        return AccuracyResourceWithRawResponse(self._reports.accuracy)


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.query_sentiment_v2_v1_sentiment_v2_post = async_to_raw_response_wrapper(
            reports.query_sentiment_v2_v1_sentiment_v2_post,
        )

    @cached_property
    def citations(self) -> AsyncCitationsResourceWithRawResponse:
        return AsyncCitationsResourceWithRawResponse(self._reports.citations)

    @cached_property
    def visibility(self) -> AsyncVisibilityResourceWithRawResponse:
        return AsyncVisibilityResourceWithRawResponse(self._reports.visibility)

    @cached_property
    def sentiment(self) -> AsyncSentimentResourceWithRawResponse:
        return AsyncSentimentResourceWithRawResponse(self._reports.sentiment)

    @cached_property
    def web_search_results(self) -> AsyncWebSearchResultsResourceWithRawResponse:
        return AsyncWebSearchResultsResourceWithRawResponse(self._reports.web_search_results)

    @cached_property
    def referrals(self) -> AsyncReferralsResourceWithRawResponse:
        return AsyncReferralsResourceWithRawResponse(self._reports.referrals)

    @cached_property
    def bots(self) -> AsyncBotsResourceWithRawResponse:
        return AsyncBotsResourceWithRawResponse(self._reports.bots)

    @cached_property
    def query_fanouts(self) -> AsyncQueryFanoutsResourceWithRawResponse:
        return AsyncQueryFanoutsResourceWithRawResponse(self._reports.query_fanouts)

    @cached_property
    def shopping(self) -> AsyncShoppingResourceWithRawResponse:
        return AsyncShoppingResourceWithRawResponse(self._reports.shopping)

    @cached_property
    def accuracy(self) -> AsyncAccuracyResourceWithRawResponse:
        return AsyncAccuracyResourceWithRawResponse(self._reports.accuracy)


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.query_sentiment_v2_v1_sentiment_v2_post = to_streamed_response_wrapper(
            reports.query_sentiment_v2_v1_sentiment_v2_post,
        )

    @cached_property
    def citations(self) -> CitationsResourceWithStreamingResponse:
        return CitationsResourceWithStreamingResponse(self._reports.citations)

    @cached_property
    def visibility(self) -> VisibilityResourceWithStreamingResponse:
        return VisibilityResourceWithStreamingResponse(self._reports.visibility)

    @cached_property
    def sentiment(self) -> SentimentResourceWithStreamingResponse:
        return SentimentResourceWithStreamingResponse(self._reports.sentiment)

    @cached_property
    def web_search_results(self) -> WebSearchResultsResourceWithStreamingResponse:
        return WebSearchResultsResourceWithStreamingResponse(self._reports.web_search_results)

    @cached_property
    def referrals(self) -> ReferralsResourceWithStreamingResponse:
        return ReferralsResourceWithStreamingResponse(self._reports.referrals)

    @cached_property
    def bots(self) -> BotsResourceWithStreamingResponse:
        return BotsResourceWithStreamingResponse(self._reports.bots)

    @cached_property
    def query_fanouts(self) -> QueryFanoutsResourceWithStreamingResponse:
        return QueryFanoutsResourceWithStreamingResponse(self._reports.query_fanouts)

    @cached_property
    def shopping(self) -> ShoppingResourceWithStreamingResponse:
        return ShoppingResourceWithStreamingResponse(self._reports.shopping)

    @cached_property
    def accuracy(self) -> AccuracyResourceWithStreamingResponse:
        return AccuracyResourceWithStreamingResponse(self._reports.accuracy)


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.query_sentiment_v2_v1_sentiment_v2_post = async_to_streamed_response_wrapper(
            reports.query_sentiment_v2_v1_sentiment_v2_post,
        )

    @cached_property
    def citations(self) -> AsyncCitationsResourceWithStreamingResponse:
        return AsyncCitationsResourceWithStreamingResponse(self._reports.citations)

    @cached_property
    def visibility(self) -> AsyncVisibilityResourceWithStreamingResponse:
        return AsyncVisibilityResourceWithStreamingResponse(self._reports.visibility)

    @cached_property
    def sentiment(self) -> AsyncSentimentResourceWithStreamingResponse:
        return AsyncSentimentResourceWithStreamingResponse(self._reports.sentiment)

    @cached_property
    def web_search_results(self) -> AsyncWebSearchResultsResourceWithStreamingResponse:
        return AsyncWebSearchResultsResourceWithStreamingResponse(self._reports.web_search_results)

    @cached_property
    def referrals(self) -> AsyncReferralsResourceWithStreamingResponse:
        return AsyncReferralsResourceWithStreamingResponse(self._reports.referrals)

    @cached_property
    def bots(self) -> AsyncBotsResourceWithStreamingResponse:
        return AsyncBotsResourceWithStreamingResponse(self._reports.bots)

    @cached_property
    def query_fanouts(self) -> AsyncQueryFanoutsResourceWithStreamingResponse:
        return AsyncQueryFanoutsResourceWithStreamingResponse(self._reports.query_fanouts)

    @cached_property
    def shopping(self) -> AsyncShoppingResourceWithStreamingResponse:
        return AsyncShoppingResourceWithStreamingResponse(self._reports.shopping)

    @cached_property
    def accuracy(self) -> AsyncAccuracyResourceWithStreamingResponse:
        return AsyncAccuracyResourceWithStreamingResponse(self._reports.accuracy)
