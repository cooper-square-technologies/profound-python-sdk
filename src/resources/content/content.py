# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from .optimization import (
    OptimizationResource,
    AsyncOptimizationResource,
    OptimizationResourceWithRawResponse,
    AsyncOptimizationResourceWithRawResponse,
    OptimizationResourceWithStreamingResponse,
    AsyncOptimizationResourceWithStreamingResponse,
)

__all__ = ["ContentResource", "AsyncContentResource"]


class ContentResource(SyncAPIResource):

    @cached_property
    def optimization(self) -> OptimizationResource:
        return OptimizationResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContentResourceWithRawResponse:
        return ContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentResourceWithStreamingResponse:
        return ContentResourceWithStreamingResponse(self)


class AsyncContentResource(AsyncAPIResource):

    @cached_property
    def optimization(self) -> AsyncOptimizationResource:
        return AsyncOptimizationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContentResourceWithRawResponse:
        return AsyncContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentResourceWithStreamingResponse:
        return AsyncContentResourceWithStreamingResponse(self)


class ContentResourceWithRawResponse:
    def __init__(self, content: ContentResource) -> None:
        self._content = content


    @cached_property
    def optimization(self) -> OptimizationResourceWithRawResponse:
        return OptimizationResourceWithRawResponse(self._content.optimization)


class AsyncContentResourceWithRawResponse:
    def __init__(self, content: AsyncContentResource) -> None:
        self._content = content


    @cached_property
    def optimization(self) -> AsyncOptimizationResourceWithRawResponse:
        return AsyncOptimizationResourceWithRawResponse(self._content.optimization)


class ContentResourceWithStreamingResponse:
    def __init__(self, content: ContentResource) -> None:
        self._content = content


    @cached_property
    def optimization(self) -> OptimizationResourceWithStreamingResponse:
        return OptimizationResourceWithStreamingResponse(self._content.optimization)


class AsyncContentResourceWithStreamingResponse:
    def __init__(self, content: AsyncContentResource) -> None:
        self._content = content


    @cached_property
    def optimization(self) -> AsyncOptimizationResourceWithStreamingResponse:
        return AsyncOptimizationResourceWithStreamingResponse(self._content.optimization)
