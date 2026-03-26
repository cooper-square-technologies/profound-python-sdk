# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import prompt_volume_create_volume_params, prompt_volume_list_citation_prompts_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared_params.pagination import Pagination

__all__ = ["PromptVolumesResource", "AsyncPromptVolumesResource"]


class PromptVolumesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptVolumesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PromptVolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptVolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return PromptVolumesResourceWithStreamingResponse(self)

    def create_volume(
        self,
        *,
        end_date: Union[str, datetime],
        metrics: List[Literal["volume", "change"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["keyword", "date", "platform", "country_code", "matching_type", "frequency"]]
        | Omit = omit,
        filters: Iterable[prompt_volume_create_volume_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Get Volume

        Args:
          end_date: End date for the query.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the query. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: Filters to apply to the query

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
        return self._post(
            "/v1/prompt-volumes/volume",
            body=maybe_transform(
                {
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                prompt_volume_create_volume_params.PromptVolumeCreateVolumeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list_citation_prompts(
        self,
        *,
        input_domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Get Citation Prompts

        Args:
          input_domain: Domain to look up (e.g.

        ramp.com)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/prompt-volumes/citation-prompts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"input_domain": input_domain},
                    prompt_volume_list_citation_prompts_params.PromptVolumeListCitationPromptsParams,
                ),
            ),
            cast_to=object,
        )


class AsyncPromptVolumesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptVolumesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptVolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptVolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncPromptVolumesResourceWithStreamingResponse(self)

    async def create_volume(
        self,
        *,
        end_date: Union[str, datetime],
        metrics: List[Literal["volume", "change"]],
        start_date: Union[str, datetime],
        date_interval: Literal["hour", "day", "week", "month", "year", "relative_week"] | Omit = omit,
        dimensions: List[Literal["keyword", "date", "platform", "country_code", "matching_type", "frequency"]]
        | Omit = omit,
        filters: Iterable[prompt_volume_create_volume_params.Filter] | Omit = omit,
        order_by: Dict[str, Literal["asc", "desc"]] | Omit = omit,
        pagination: Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Get Volume

        Args:
          end_date: End date for the query.

        Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          start_date: Start date for the query. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full
              ISO timestamp.

          date_interval: Date interval for the report. (only used with date dimension)

          dimensions: Dimensions to group the report by.

          filters: Filters to apply to the query

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
        return await self._post(
            "/v1/prompt-volumes/volume",
            body=await async_maybe_transform(
                {
                    "end_date": end_date,
                    "metrics": metrics,
                    "start_date": start_date,
                    "date_interval": date_interval,
                    "dimensions": dimensions,
                    "filters": filters,
                    "order_by": order_by,
                    "pagination": pagination,
                },
                prompt_volume_create_volume_params.PromptVolumeCreateVolumeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def list_citation_prompts(
        self,
        *,
        input_domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Get Citation Prompts

        Args:
          input_domain: Domain to look up (e.g.

        ramp.com)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/prompt-volumes/citation-prompts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"input_domain": input_domain},
                    prompt_volume_list_citation_prompts_params.PromptVolumeListCitationPromptsParams,
                ),
            ),
            cast_to=object,
        )


class PromptVolumesResourceWithRawResponse:
    def __init__(self, prompt_volumes: PromptVolumesResource) -> None:
        self._prompt_volumes = prompt_volumes

        self.create_volume = to_raw_response_wrapper(
            prompt_volumes.create_volume,
        )
        self.list_citation_prompts = to_raw_response_wrapper(
            prompt_volumes.list_citation_prompts,
        )


class AsyncPromptVolumesResourceWithRawResponse:
    def __init__(self, prompt_volumes: AsyncPromptVolumesResource) -> None:
        self._prompt_volumes = prompt_volumes

        self.create_volume = async_to_raw_response_wrapper(
            prompt_volumes.create_volume,
        )
        self.list_citation_prompts = async_to_raw_response_wrapper(
            prompt_volumes.list_citation_prompts,
        )


class PromptVolumesResourceWithStreamingResponse:
    def __init__(self, prompt_volumes: PromptVolumesResource) -> None:
        self._prompt_volumes = prompt_volumes

        self.create_volume = to_streamed_response_wrapper(
            prompt_volumes.create_volume,
        )
        self.list_citation_prompts = to_streamed_response_wrapper(
            prompt_volumes.list_citation_prompts,
        )


class AsyncPromptVolumesResourceWithStreamingResponse:
    def __init__(self, prompt_volumes: AsyncPromptVolumesResource) -> None:
        self._prompt_volumes = prompt_volumes

        self.create_volume = async_to_streamed_response_wrapper(
            prompt_volumes.create_volume,
        )
        self.list_citation_prompts = async_to_streamed_response_wrapper(
            prompt_volumes.list_citation_prompts,
        )
