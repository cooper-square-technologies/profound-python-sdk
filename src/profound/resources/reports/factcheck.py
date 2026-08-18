# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional
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
from ..._streaming import Stream, AsyncStream
from ...types.reports.factcheck_query_scores_v2_post_response import FactcheckQueryScoresV2PostResponse
from ...types.shared_params.filter_node import FilterNode
from ...types.reports import (
    factcheck_query_scores_v2_post_params,
    factcheck_stream_scores_v2_stream_post_params,
    factcheck_query_claims_v2_claims_post_params,
    factcheck_stream_claims_v2_claims_stream_post_params,
)
from ...types.reports.factcheck_stream_scores_v2_stream_post_response import FactcheckStreamScoresV2StreamPostResponse
from ...types.reports.factcheck_query_claims_v2_claims_post_response import FactcheckQueryClaimsV2ClaimsPostResponse
from ...types.reports.factcheck_stream_claims_v2_claims_stream_post_response import (
    FactcheckStreamClaimsV2ClaimsStreamPostResponse,
)

__all__ = ["FactcheckResource", "AsyncFactcheckResource"]


class FactcheckResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FactcheckResourceWithRawResponse:
        return FactcheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FactcheckResourceWithStreamingResponse:
        return FactcheckResourceWithStreamingResponse(self)

    def query_scores_v2_post(
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
    ) -> FactcheckQueryScoresV2PostResponse:
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
            FactcheckQueryScoresV2PostResponse: Successful Response

        Example:
            ```python
            factcheck = client.reports.factcheck.query_scores_v2_post(
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
                factcheck_query_scores_v2_post_params.FactcheckQueryScoresV2PostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FactcheckQueryScoresV2PostResponse,
        )

    def stream_scores_v2_stream_post(
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
    ) -> Stream[FactcheckStreamScoresV2StreamPostResponse]:
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
            Stream[FactcheckStreamScoresV2StreamPostResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = client.reports.factcheck.stream_scores_v2_stream_post(
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
                factcheck_stream_scores_v2_stream_post_params.FactcheckStreamScoresV2StreamPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FactcheckStreamScoresV2StreamPostResponse,
            stream=True,
            stream_cls=Stream[FactcheckStreamScoresV2StreamPostResponse],
        )

    def query_claims_v2_claims_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["model", "region", "persona", "prompt", "topic", "tag", "theme"]] | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        include: Optional[List[Literal["theme", "reasoning", "models", "evidence", "citation_sources"]]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FactcheckQueryClaimsV2ClaimsPostResponse:
        """
        Query Claims

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Optional single dim to section the claims (e.g. per model). Empty → one flat claim list.
            filter: Scope which responses count (see Filtering).
            include: Optional per-claim detail fields to add to each claim (see options).
            limit: Claims (or sections) per page; default 25.
            max_results: Stream only: cap entries returned.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FactcheckQueryClaimsV2ClaimsPostResponse: Successful Response

        Example:
            ```python
            factcheck = client.reports.factcheck.query_claims_v2_claims_post(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )
            ```
        """
        return self._post(
            "/v2/reports/factcheck/claims",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "filter": filter,
                    "include": include,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                factcheck_query_claims_v2_claims_post_params.FactcheckQueryClaimsV2ClaimsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FactcheckQueryClaimsV2ClaimsPostResponse,
        )

    def stream_claims_v2_claims_stream_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["model", "region", "persona", "prompt", "topic", "tag", "theme"]] | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        include: Optional[List[Literal["theme", "reasoning", "models", "evidence", "citation_sources"]]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[FactcheckStreamClaimsV2ClaimsStreamPostResponse]:
        """
        Stream Claims

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Optional single dim to section the claims (e.g. per model). Empty → one flat claim list.
            filter: Scope which responses count (see Filtering).
            include: Optional per-claim detail fields to add to each claim (see options).
            limit: Claims (or sections) per page; default 25.
            max_results: Stream only: cap entries returned.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Stream[FactcheckStreamClaimsV2ClaimsStreamPostResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = client.reports.factcheck.stream_claims_v2_claims_stream_post(
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
            "/v2/reports/factcheck/claims/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "filter": filter,
                    "include": include,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                factcheck_stream_claims_v2_claims_stream_post_params.FactcheckStreamClaimsV2ClaimsStreamPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FactcheckStreamClaimsV2ClaimsStreamPostResponse,
            stream=True,
            stream_cls=Stream[FactcheckStreamClaimsV2ClaimsStreamPostResponse],
        )


class AsyncFactcheckResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFactcheckResourceWithRawResponse:
        return AsyncFactcheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFactcheckResourceWithStreamingResponse:
        return AsyncFactcheckResourceWithStreamingResponse(self)

    async def query_scores_v2_post(
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
    ) -> FactcheckQueryScoresV2PostResponse:
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
            FactcheckQueryScoresV2PostResponse: Successful Response

        Example:
            ```python
            factcheck = await client.reports.factcheck.query_scores_v2_post(
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
                factcheck_query_scores_v2_post_params.FactcheckQueryScoresV2PostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FactcheckQueryScoresV2PostResponse,
        )

    async def stream_scores_v2_stream_post(
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
    ) -> AsyncStream[FactcheckStreamScoresV2StreamPostResponse]:
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
            AsyncStream[FactcheckStreamScoresV2StreamPostResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = await client.reports.factcheck.stream_scores_v2_stream_post(
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
                factcheck_stream_scores_v2_stream_post_params.FactcheckStreamScoresV2StreamPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FactcheckStreamScoresV2StreamPostResponse,
            stream=True,
            stream_cls=AsyncStream[FactcheckStreamScoresV2StreamPostResponse],
        )

    async def query_claims_v2_claims_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["model", "region", "persona", "prompt", "topic", "tag", "theme"]] | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        include: Optional[List[Literal["theme", "reasoning", "models", "evidence", "citation_sources"]]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FactcheckQueryClaimsV2ClaimsPostResponse:
        """
        Query Claims

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Optional single dim to section the claims (e.g. per model). Empty → one flat claim list.
            filter: Scope which responses count (see Filtering).
            include: Optional per-claim detail fields to add to each claim (see options).
            limit: Claims (or sections) per page; default 25.
            max_results: Stream only: cap entries returned.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FactcheckQueryClaimsV2ClaimsPostResponse: Successful Response

        Example:
            ```python
            factcheck = await client.reports.factcheck.query_claims_v2_claims_post(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                start_date="",
                end_date="",
            )
            ```
        """
        return await self._post(
            "/v2/reports/factcheck/claims",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "filter": filter,
                    "include": include,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                factcheck_query_claims_v2_claims_post_params.FactcheckQueryClaimsV2ClaimsPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FactcheckQueryClaimsV2ClaimsPostResponse,
        )

    async def stream_claims_v2_claims_stream_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        group_by: List[Literal["model", "region", "persona", "prompt", "topic", "tag", "theme"]] | Omit = omit,
        filter: Optional[FilterNode] | Omit = omit,
        include: Optional[List[Literal["theme", "reasoning", "models", "evidence", "citation_sources"]]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[FactcheckStreamClaimsV2ClaimsStreamPostResponse]:
        """
        Stream Claims

        Args:
            category_id: Body parameter.
            start_date: YYYY-MM-DD, ET, inclusive
            end_date: YYYY-MM-DD, ET, inclusive
            group_by: Optional single dim to section the claims (e.g. per model). Empty → one flat claim list.
            filter: Scope which responses count (see Filtering).
            include: Optional per-claim detail fields to add to each claim (see options).
            limit: Claims (or sections) per page; default 25.
            max_results: Stream only: cap entries returned.
            cursor: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncStream[FactcheckStreamClaimsV2ClaimsStreamPostResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = await client.reports.factcheck.stream_claims_v2_claims_stream_post(
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
            "/v2/reports/factcheck/claims/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "group_by": group_by,
                    "filter": filter,
                    "include": include,
                    "limit": limit,
                    "max_results": max_results,
                    "cursor": cursor,
                },
                factcheck_stream_claims_v2_claims_stream_post_params.FactcheckStreamClaimsV2ClaimsStreamPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FactcheckStreamClaimsV2ClaimsStreamPostResponse,
            stream=True,
            stream_cls=AsyncStream[FactcheckStreamClaimsV2ClaimsStreamPostResponse],
        )


class FactcheckResourceWithRawResponse:
    def __init__(self, factcheck: FactcheckResource) -> None:
        self._factcheck = factcheck

        self.query_scores_v2_post = to_raw_response_wrapper(
            factcheck.query_scores_v2_post,
        )
        self.stream_scores_v2_stream_post = to_raw_response_wrapper(
            factcheck.stream_scores_v2_stream_post,
        )
        self.query_claims_v2_claims_post = to_raw_response_wrapper(
            factcheck.query_claims_v2_claims_post,
        )
        self.stream_claims_v2_claims_stream_post = to_raw_response_wrapper(
            factcheck.stream_claims_v2_claims_stream_post,
        )


class AsyncFactcheckResourceWithRawResponse:
    def __init__(self, factcheck: AsyncFactcheckResource) -> None:
        self._factcheck = factcheck

        self.query_scores_v2_post = async_to_raw_response_wrapper(
            factcheck.query_scores_v2_post,
        )
        self.stream_scores_v2_stream_post = async_to_raw_response_wrapper(
            factcheck.stream_scores_v2_stream_post,
        )
        self.query_claims_v2_claims_post = async_to_raw_response_wrapper(
            factcheck.query_claims_v2_claims_post,
        )
        self.stream_claims_v2_claims_stream_post = async_to_raw_response_wrapper(
            factcheck.stream_claims_v2_claims_stream_post,
        )


class FactcheckResourceWithStreamingResponse:
    def __init__(self, factcheck: FactcheckResource) -> None:
        self._factcheck = factcheck

        self.query_scores_v2_post = to_streamed_response_wrapper(
            factcheck.query_scores_v2_post,
        )
        self.stream_scores_v2_stream_post = to_streamed_response_wrapper(
            factcheck.stream_scores_v2_stream_post,
        )
        self.query_claims_v2_claims_post = to_streamed_response_wrapper(
            factcheck.query_claims_v2_claims_post,
        )
        self.stream_claims_v2_claims_stream_post = to_streamed_response_wrapper(
            factcheck.stream_claims_v2_claims_stream_post,
        )


class AsyncFactcheckResourceWithStreamingResponse:
    def __init__(self, factcheck: AsyncFactcheckResource) -> None:
        self._factcheck = factcheck

        self.query_scores_v2_post = async_to_streamed_response_wrapper(
            factcheck.query_scores_v2_post,
        )
        self.stream_scores_v2_stream_post = async_to_streamed_response_wrapper(
            factcheck.stream_scores_v2_stream_post,
        )
        self.query_claims_v2_claims_post = async_to_streamed_response_wrapper(
            factcheck.query_claims_v2_claims_post,
        )
        self.stream_claims_v2_claims_stream_post = async_to_streamed_response_wrapper(
            factcheck.stream_claims_v2_claims_stream_post,
        )
