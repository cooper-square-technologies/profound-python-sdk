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
from ....types.reports.factcheck.claim_query_claims_response import ClaimQueryClaimsResponse
from ....types.shared_params.filter_node import FilterNode
from ....types.reports.factcheck import claim_query_claims_params, claim_stream_claims_params
from ....types.reports.factcheck.claim_stream_claims_response import ClaimStreamClaimsResponse

__all__ = ["ClaimsResource", "AsyncClaimsResource"]


class ClaimsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClaimsResourceWithRawResponse:
        return ClaimsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClaimsResourceWithStreamingResponse:
        return ClaimsResourceWithStreamingResponse(self)

    def query_claims(
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
    ) -> ClaimQueryClaimsResponse:
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
            ClaimQueryClaimsResponse: Successful Response

        Example:
            ```python
            claim = client.reports.factcheck.claims.query_claims(
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
                claim_query_claims_params.ClaimQueryClaimsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClaimQueryClaimsResponse,
        )

    def stream_claims(
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
    ) -> Stream[ClaimStreamClaimsResponse]:
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
            Stream[ClaimStreamClaimsResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = client.reports.factcheck.claims.stream_claims(
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
                claim_stream_claims_params.ClaimStreamClaimsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClaimStreamClaimsResponse,
            stream=True,
            stream_cls=Stream[ClaimStreamClaimsResponse],
        )


class AsyncClaimsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClaimsResourceWithRawResponse:
        return AsyncClaimsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClaimsResourceWithStreamingResponse:
        return AsyncClaimsResourceWithStreamingResponse(self)

    async def query_claims(
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
    ) -> ClaimQueryClaimsResponse:
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
            ClaimQueryClaimsResponse: Successful Response

        Example:
            ```python
            claim = await client.reports.factcheck.claims.query_claims(
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
                claim_query_claims_params.ClaimQueryClaimsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClaimQueryClaimsResponse,
        )

    async def stream_claims(
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
    ) -> AsyncStream[ClaimStreamClaimsResponse]:
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
            AsyncStream[ClaimStreamClaimsResponse]: Server-sent events stream. Emits one `summary` event (the report `info` block) first, then one `result` event per row.

        Example:
            ```python
            stream = await client.reports.factcheck.claims.stream_claims(
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
                claim_stream_claims_params.ClaimStreamClaimsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClaimStreamClaimsResponse,
            stream=True,
            stream_cls=AsyncStream[ClaimStreamClaimsResponse],
        )


class ClaimsResourceWithRawResponse:
    def __init__(self, claims: ClaimsResource) -> None:
        self._claims = claims

        self.query_claims = to_raw_response_wrapper(
            claims.query_claims,
        )
        self.stream_claims = to_raw_response_wrapper(
            claims.stream_claims,
        )


class AsyncClaimsResourceWithRawResponse:
    def __init__(self, claims: AsyncClaimsResource) -> None:
        self._claims = claims

        self.query_claims = async_to_raw_response_wrapper(
            claims.query_claims,
        )
        self.stream_claims = async_to_raw_response_wrapper(
            claims.stream_claims,
        )


class ClaimsResourceWithStreamingResponse:
    def __init__(self, claims: ClaimsResource) -> None:
        self._claims = claims

        self.query_claims = to_streamed_response_wrapper(
            claims.query_claims,
        )
        self.stream_claims = to_streamed_response_wrapper(
            claims.stream_claims,
        )


class AsyncClaimsResourceWithStreamingResponse:
    def __init__(self, claims: AsyncClaimsResource) -> None:
        self._claims = claims

        self.query_claims = async_to_streamed_response_wrapper(
            claims.query_claims,
        )
        self.stream_claims = async_to_streamed_response_wrapper(
            claims.stream_claims,
        )
