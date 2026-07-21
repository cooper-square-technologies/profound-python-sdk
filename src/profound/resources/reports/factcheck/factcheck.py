# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Optional, cast
from typing_extensions import Literal

import httpx

from .claims import (
    ClaimsResource,
    AsyncClaimsResource,
    ClaimsResourceWithRawResponse,
    AsyncClaimsResourceWithRawResponse,
    ClaimsResourceWithStreamingResponse,
    AsyncClaimsResourceWithStreamingResponse,
)
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
from ...._streaming import Stream, AsyncStream
from ...._base_client import make_request_options
from ....types.reports import factcheck_query_scores_params, factcheck_stream_scores_params
from ....types.reports.factcheck_query_scores_response import FactcheckQueryScoresResponse
from ....types.reports.factcheck_stream_scores_response import FactcheckStreamScoresResponse

__all__ = ["FactcheckResource", "AsyncFactcheckResource"]


class FactcheckResource(SyncAPIResource):
    @cached_property
    def claims(self) -> ClaimsResource:
        return ClaimsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FactcheckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return FactcheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FactcheckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return FactcheckResourceWithStreamingResponse(self)

    def query_scores(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[factcheck_query_scores_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "model", "region", "persona", "prompt", "topic", "tag", "citation", "theme"]]
        | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
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
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: Up to two dimensions to slice by; empty returns the headline score. `citation`
              must be alone.

          limit: Rows per page; default 100.

          max_results: Stream only: cap rows returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/factcheck",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "limit": limit,
                    "max_results": max_results,
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
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[factcheck_stream_scores_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "model", "region", "persona", "prompt", "topic", "tag", "citation", "theme"]]
        | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
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
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: Up to two dimensions to slice by; empty returns the headline score. `citation`
              must be alone.

          limit: Rows per page; default 100.

          max_results: Stream only: cap rows returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v2/reports/factcheck/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "limit": limit,
                    "max_results": max_results,
                },
                factcheck_stream_scores_params.FactcheckStreamScoresParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, FactcheckStreamScoresResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[FactcheckStreamScoresResponse],
        )


class AsyncFactcheckResource(AsyncAPIResource):
    @cached_property
    def claims(self) -> AsyncClaimsResource:
        return AsyncClaimsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFactcheckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFactcheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFactcheckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncFactcheckResourceWithStreamingResponse(self)

    async def query_scores(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[factcheck_query_scores_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "model", "region", "persona", "prompt", "topic", "tag", "citation", "theme"]]
        | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
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
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: Up to two dimensions to slice by; empty returns the headline score. `citation`
              must be alone.

          limit: Rows per page; default 100.

          max_results: Stream only: cap rows returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/factcheck",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "limit": limit,
                    "max_results": max_results,
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
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[factcheck_stream_scores_params.Filter] | Omit = omit,
        group_by: List[Literal["date", "model", "region", "persona", "prompt", "topic", "tag", "citation", "theme"]]
        | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
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
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: Up to two dimensions to slice by; empty returns the headline score. `citation`
              must be alone.

          limit: Rows per page; default 100.

          max_results: Stream only: cap rows returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/factcheck/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "limit": limit,
                    "max_results": max_results,
                },
                factcheck_stream_scores_params.FactcheckStreamScoresParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, FactcheckStreamScoresResponse
            ),  # Union types cannot be passed in as arguments in the type system
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
