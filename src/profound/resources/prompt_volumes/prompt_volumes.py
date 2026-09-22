# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .volume import (
    VolumeResource,
    AsyncVolumeResource,
    VolumeResourceWithRawResponse,
    AsyncVolumeResourceWithRawResponse,
    VolumeResourceWithStreamingResponse,
    AsyncVolumeResourceWithStreamingResponse,
)
from .intents import (
    IntentsResource,
    AsyncIntentsResource,
    IntentsResourceWithRawResponse,
    AsyncIntentsResourceWithRawResponse,
    IntentsResourceWithStreamingResponse,
    AsyncIntentsResourceWithStreamingResponse,
)

__all__ = ["PromptVolumesResource", "AsyncPromptVolumesResource"]


class PromptVolumesResource(SyncAPIResource):
    @cached_property
    def volume(self) -> VolumeResource:
        return VolumeResource(self._client)

    @cached_property
    def intents(self) -> IntentsResource:
        return IntentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PromptVolumesResourceWithRawResponse:
        return PromptVolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptVolumesResourceWithStreamingResponse:
        return PromptVolumesResourceWithStreamingResponse(self)


class AsyncPromptVolumesResource(AsyncAPIResource):
    @cached_property
    def volume(self) -> AsyncVolumeResource:
        return AsyncVolumeResource(self._client)

    @cached_property
    def intents(self) -> AsyncIntentsResource:
        return AsyncIntentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPromptVolumesResourceWithRawResponse:
        return AsyncPromptVolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptVolumesResourceWithStreamingResponse:
        return AsyncPromptVolumesResourceWithStreamingResponse(self)


class PromptVolumesResourceWithRawResponse:
    def __init__(self, prompt_volumes: PromptVolumesResource) -> None:
        self._prompt_volumes = prompt_volumes

    @cached_property
    def volume(self) -> VolumeResourceWithRawResponse:
        return VolumeResourceWithRawResponse(self._prompt_volumes.volume)

    @cached_property
    def intents(self) -> IntentsResourceWithRawResponse:
        return IntentsResourceWithRawResponse(self._prompt_volumes.intents)


class AsyncPromptVolumesResourceWithRawResponse:
    def __init__(self, prompt_volumes: AsyncPromptVolumesResource) -> None:
        self._prompt_volumes = prompt_volumes

    @cached_property
    def volume(self) -> AsyncVolumeResourceWithRawResponse:
        return AsyncVolumeResourceWithRawResponse(self._prompt_volumes.volume)

    @cached_property
    def intents(self) -> AsyncIntentsResourceWithRawResponse:
        return AsyncIntentsResourceWithRawResponse(self._prompt_volumes.intents)


class PromptVolumesResourceWithStreamingResponse:
    def __init__(self, prompt_volumes: PromptVolumesResource) -> None:
        self._prompt_volumes = prompt_volumes

    @cached_property
    def volume(self) -> VolumeResourceWithStreamingResponse:
        return VolumeResourceWithStreamingResponse(self._prompt_volumes.volume)

    @cached_property
    def intents(self) -> IntentsResourceWithStreamingResponse:
        return IntentsResourceWithStreamingResponse(self._prompt_volumes.intents)


class AsyncPromptVolumesResourceWithStreamingResponse:
    def __init__(self, prompt_volumes: AsyncPromptVolumesResource) -> None:
        self._prompt_volumes = prompt_volumes

    @cached_property
    def volume(self) -> AsyncVolumeResourceWithStreamingResponse:
        return AsyncVolumeResourceWithStreamingResponse(self._prompt_volumes.volume)

    @cached_property
    def intents(self) -> AsyncIntentsResourceWithStreamingResponse:
        return AsyncIntentsResourceWithStreamingResponse(self._prompt_volumes.intents)
