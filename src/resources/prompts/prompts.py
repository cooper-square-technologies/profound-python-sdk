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
from .answers import (
    AnswersResource,
    AsyncAnswersResource,
    AnswersResourceWithRawResponse,
    AsyncAnswersResourceWithRawResponse,
    AnswersResourceWithStreamingResponse,
    AsyncAnswersResourceWithStreamingResponse,
)

__all__ = ["PromptsResource", "AsyncPromptsResource"]


class PromptsResource(SyncAPIResource):

    @cached_property
    def answers(self) -> AnswersResource:
        return AnswersResource(self._client)

    @cached_property
    def with_raw_response(self) -> PromptsResourceWithRawResponse:
        return PromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptsResourceWithStreamingResponse:
        return PromptsResourceWithStreamingResponse(self)


class AsyncPromptsResource(AsyncAPIResource):

    @cached_property
    def answers(self) -> AsyncAnswersResource:
        return AsyncAnswersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPromptsResourceWithRawResponse:
        return AsyncPromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptsResourceWithStreamingResponse:
        return AsyncPromptsResourceWithStreamingResponse(self)


class PromptsResourceWithRawResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts


    @cached_property
    def answers(self) -> AnswersResourceWithRawResponse:
        return AnswersResourceWithRawResponse(self._prompts.answers)


class AsyncPromptsResourceWithRawResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts


    @cached_property
    def answers(self) -> AsyncAnswersResourceWithRawResponse:
        return AsyncAnswersResourceWithRawResponse(self._prompts.answers)


class PromptsResourceWithStreamingResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts


    @cached_property
    def answers(self) -> AnswersResourceWithStreamingResponse:
        return AnswersResourceWithStreamingResponse(self._prompts.answers)


class AsyncPromptsResourceWithStreamingResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts


    @cached_property
    def answers(self) -> AsyncAnswersResourceWithStreamingResponse:
        return AsyncAnswersResourceWithStreamingResponse(self._prompts.answers)
