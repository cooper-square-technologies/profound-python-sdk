# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return ContentResourceWithStreamingResponse(self)


class AsyncContentResource(AsyncAPIResource):
    @cached_property
    def optimization(self) -> AsyncOptimizationResource:
        return AsyncOptimizationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
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
