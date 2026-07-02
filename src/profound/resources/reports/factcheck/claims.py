# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ....types.reports.factcheck import claim_query_claims_params, claim_stream_claims_params
from ....types.reports.factcheck.claim_query_claims_response import ClaimQueryClaimsResponse

__all__ = ["ClaimsResource", "AsyncClaimsResource"]


class ClaimsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClaimsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ClaimsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClaimsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return ClaimsResourceWithStreamingResponse(self)

    def query_claims(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[claim_query_claims_params.Filter] | Omit = omit,
        group_by: List[Literal["model", "region", "persona", "prompt", "topic", "tag", "theme"]] | Omit = omit,
        include: Optional[List[Literal["theme", "reasoning", "models", "evidence", "citation_sources"]]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
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
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: Optional single dim to section the claims (e.g. per model). Empty → one flat
              claim list.

          include: Claim detail: theme, reasoning, models, evidence, citation_sources.

          limit: Claims (or sections) per page; default 25.

          max_results: Stream only: cap entries returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/reports/factcheck/claims",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "include": include,
                    "limit": limit,
                    "max_results": max_results,
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
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[claim_stream_claims_params.Filter] | Omit = omit,
        group_by: List[Literal["model", "region", "persona", "prompt", "topic", "tag", "theme"]] | Omit = omit,
        include: Optional[List[Literal["theme", "reasoning", "models", "evidence", "citation_sources"]]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stream Claims

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: Optional single dim to section the claims (e.g. per model). Empty → one flat
              claim list.

          include: Claim detail: theme, reasoning, models, evidence, citation_sources.

          limit: Claims (or sections) per page; default 25.

          max_results: Stream only: cap entries returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v2/reports/factcheck/claims/stream",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "include": include,
                    "limit": limit,
                    "max_results": max_results,
                },
                claim_stream_claims_params.ClaimStreamClaimsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncClaimsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClaimsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncClaimsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClaimsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncClaimsResourceWithStreamingResponse(self)

    async def query_claims(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[claim_query_claims_params.Filter] | Omit = omit,
        group_by: List[Literal["model", "region", "persona", "prompt", "topic", "tag", "theme"]] | Omit = omit,
        include: Optional[List[Literal["theme", "reasoning", "models", "evidence", "citation_sources"]]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
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
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: Optional single dim to section the claims (e.g. per model). Empty → one flat
              claim list.

          include: Claim detail: theme, reasoning, models, evidence, citation_sources.

          limit: Claims (or sections) per page; default 25.

          max_results: Stream only: cap entries returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/reports/factcheck/claims",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "include": include,
                    "limit": limit,
                    "max_results": max_results,
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
        end_date: str,
        start_date: str,
        cursor: Optional[str] | Omit = omit,
        filter: Optional[claim_stream_claims_params.Filter] | Omit = omit,
        group_by: List[Literal["model", "region", "persona", "prompt", "topic", "tag", "theme"]] | Omit = omit,
        include: Optional[List[Literal["theme", "reasoning", "models", "evidence", "citation_sources"]]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stream Claims

        Args:
          end_date: YYYY-MM-DD, ET, inclusive

          start_date: YYYY-MM-DD, ET, inclusive

          filter: A leaf (`field`/`op`/`value`) or an `and`/`or`/`not` group.

          group_by: Optional single dim to section the claims (e.g. per model). Empty → one flat
              claim list.

          include: Claim detail: theme, reasoning, models, evidence, citation_sources.

          limit: Claims (or sections) per page; default 25.

          max_results: Stream only: cap entries returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v2/reports/factcheck/claims/stream",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "cursor": cursor,
                    "filter": filter,
                    "group_by": group_by,
                    "include": include,
                    "limit": limit,
                    "max_results": max_results,
                },
                claim_stream_claims_params.ClaimStreamClaimsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
