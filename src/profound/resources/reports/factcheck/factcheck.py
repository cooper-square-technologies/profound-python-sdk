# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional
from typing_extensions import Literal

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ...._streaming import Stream, AsyncStream
from .claims import (
    ClaimsResource,
    AsyncClaimsResource,
    ClaimsResourceWithRawResponse,
    AsyncClaimsResourceWithRawResponse,
    ClaimsResourceWithStreamingResponse,
    AsyncClaimsResourceWithStreamingResponse,
)
from ....types.reports.factcheck_query_scores_response import FactcheckQueryScoresResponse
from ....types.shared_params.filter_node import FilterNode
from ....types.reports import factcheck_query_scores_params, factcheck_stream_scores_params
from ....types.reports.factcheck_stream_scores_response import FactcheckStreamScoresResponse

__all__ = ["FactcheckResource", "AsyncFactcheckResource"]


class FactcheckResource(SyncAPIResource):
    @cached_property
    def claims(self) -> ClaimsResource:
        return ClaimsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FactcheckResourceWithRawResponse:
        return FactcheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FactcheckResourceWithStreamingResponse:
        return FactcheckResourceWithStreamingResponse(self)

    def query_scores(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "model", "region", "persona", "prompt", "topic", "tag", "citation", "theme"]]
        | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FactcheckQueryScoresResponse:
        """
        Query Scores

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Up to two dimensions to slice by; empty returns the headline score. `citation` must be alone.
            filter: Scope which responses count (see Filtering).
            limit: Rows per page; default 100.
            max_results: Stream only: cap rows returned.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FactcheckQueryScoresResponse: Successful Response

        Example:
            ```python
            factcheck = client.reports.factcheck.query_scores(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )
            ```
        """
        return self._post(
            "/v2/reports/factcheck",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                factcheck_query_scores_params.FactcheckQueryScoresParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FactcheckQueryScoresResponse,
        )

    def stream_scores(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "model", "region", "persona", "prompt", "topic", "tag", "citation", "theme"]]
        | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[FactcheckStreamScoresResponse]:
        """
        Stream Scores

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Up to two dimensions to slice by; empty returns the headline score. `citation` must be alone.
            filter: Scope which responses count (see Filtering).
            limit: Rows per page; default 100.
            max_results: Stream only: cap rows returned.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Stream[FactcheckStreamScoresResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = client.reports.factcheck.stream_scores(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )

            for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/factcheck/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                factcheck_stream_scores_params.FactcheckStreamScoresParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FactcheckStreamScoresResponse,
            stream=True,
            stream_cls=Stream[FactcheckStreamScoresResponse],
        )


class AsyncFactcheckResource(AsyncAPIResource):
    @cached_property
    def claims(self) -> AsyncClaimsResource:
        return AsyncClaimsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFactcheckResourceWithRawResponse:
        return AsyncFactcheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFactcheckResourceWithStreamingResponse:
        return AsyncFactcheckResourceWithStreamingResponse(self)

    async def query_scores(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "model", "region", "persona", "prompt", "topic", "tag", "citation", "theme"]]
        | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FactcheckQueryScoresResponse:
        """
        Query Scores

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Up to two dimensions to slice by; empty returns the headline score. `citation` must be alone.
            filter: Scope which responses count (see Filtering).
            limit: Rows per page; default 100.
            max_results: Stream only: cap rows returned.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FactcheckQueryScoresResponse: Successful Response

        Example:
            ```python
            factcheck = await client.reports.factcheck.query_scores(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )
            ```
        """
        return await self._post(
            "/v2/reports/factcheck",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                factcheck_query_scores_params.FactcheckQueryScoresParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FactcheckQueryScoresResponse,
        )

    async def stream_scores(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["date", "model", "region", "persona", "prompt", "topic", "tag", "citation", "theme"]]
        | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[FactcheckStreamScoresResponse]:
        """
        Stream Scores

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Up to two dimensions to slice by; empty returns the headline score. `citation` must be alone.
            filter: Scope which responses count (see Filtering).
            limit: Rows per page; default 100.
            max_results: Stream only: cap rows returned.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncStream[FactcheckStreamScoresResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = await client.reports.factcheck.stream_scores(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )

            async for event in stream:
                print(event)
            ```
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/factcheck/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "filter": filter,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                factcheck_stream_scores_params.FactcheckStreamScoresParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FactcheckStreamScoresResponse,
            stream=True,
            stream_cls=AsyncStream[FactcheckStreamScoresResponse],
        )


class FactcheckResourceWithRawResponse:
    def __init__(self, factcheck: FactcheckResource) -> None:
        self._factcheck = factcheck

        self.query_scores = to_raw_response_wrapper(
            factcheck.query_scores,
        )
        self.stream_scores = to_raw_response_wrapper(
            factcheck.stream_scores,
        )

    @cached_property
    def claims(self) -> ClaimsResourceWithRawResponse:
        return ClaimsResourceWithRawResponse(self._factcheck.claims)


class AsyncFactcheckResourceWithRawResponse:
    def __init__(self, factcheck: AsyncFactcheckResource) -> None:
        self._factcheck = factcheck

        self.query_scores = async_to_raw_response_wrapper(
            factcheck.query_scores,
        )
        self.stream_scores = async_to_raw_response_wrapper(
            factcheck.stream_scores,
        )

    @cached_property
    def claims(self) -> AsyncClaimsResourceWithRawResponse:
        return AsyncClaimsResourceWithRawResponse(self._factcheck.claims)


class FactcheckResourceWithStreamingResponse:
    def __init__(self, factcheck: FactcheckResource) -> None:
        self._factcheck = factcheck

        self.query_scores = to_streamed_response_wrapper(
            factcheck.query_scores,
        )
        self.stream_scores = to_streamed_response_wrapper(
            factcheck.stream_scores,
        )

    @cached_property
    def claims(self) -> ClaimsResourceWithStreamingResponse:
        return ClaimsResourceWithStreamingResponse(self._factcheck.claims)


class AsyncFactcheckResourceWithStreamingResponse:
    def __init__(self, factcheck: AsyncFactcheckResource) -> None:
        self._factcheck = factcheck

        self.query_scores = async_to_streamed_response_wrapper(
            factcheck.query_scores,
        )
        self.stream_scores = async_to_streamed_response_wrapper(
            factcheck.stream_scores,
        )

    @cached_property
    def claims(self) -> AsyncClaimsResourceWithStreamingResponse:
        return AsyncClaimsResourceWithStreamingResponse(self._factcheck.claims)
