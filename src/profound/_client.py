# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import os
import threading
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, is_mapping_t, get_async_library
from ._compat import cached_property
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._version import __version__

if TYPE_CHECKING:
    from .resources import organizations, prompts, reports, content, agents, knowledge_bases
    from .resources.organizations import OrganizationsResource, AsyncOrganizationsResource
    from .resources.prompts import PromptsResource, AsyncPromptsResource
    from .resources.reports import ReportsResource, AsyncReportsResource
    from .resources.content import ContentResource, AsyncContentResource
    from .resources.agents import AgentsResource, AsyncAgentsResource
    from .resources.knowledge_bases import KnowledgeBasesResource, AsyncKnowledgeBasesResource

# Serializes lazy resource imports so concurrent cold access from multiple
# threads cannot deadlock on CPython import locks (see CPython 3.14).
_RESOURCE_IMPORT_LOCK = threading.RLock()

__all__ = [
    "Profound",
    "AsyncProfound",
    "Client",
    "AsyncClient",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
]


class Profound(SyncAPIClient):
    # client options
    access_token: str | None
    api_key: str | None

    def __init__(
        self,
        *,
        access_token: str | None = None,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Profound client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `access_token` from `PROFOUND_ACCESS_TOKEN`
        - `api_key` from `PROFOUND_API_KEY`
        """
        if access_token is None:
            access_token = os.environ.get("PROFOUND_ACCESS_TOKEN")
        self.access_token = access_token
        if api_key is None:
            api_key = os.environ.get("PROFOUND_API_KEY")
        self.api_key = api_key
        if base_url is None:
            base_url = os.environ.get("PROFOUND_BASE_URL")
        if base_url is None:
            base_url = "https://api.tryprofound.com"
        custom_headers_env = os.environ.get("PROFOUND_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = Stream

    @cached_property
    def organizations(self) -> "OrganizationsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import OrganizationsResource
        return OrganizationsResource(self)

    @cached_property
    def prompts(self) -> "PromptsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.prompts import PromptsResource
        return PromptsResource(self)

    @cached_property
    def reports(self) -> "ReportsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.reports import ReportsResource
        return ReportsResource(self)

    @cached_property
    def content(self) -> "ContentResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.content import ContentResource
        return ContentResource(self)

    @cached_property
    def agents(self) -> "AgentsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.agents import AgentsResource
        return AgentsResource(self)

    @cached_property
    def knowledge_bases(self) -> "KnowledgeBasesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.knowledge_bases import KnowledgeBasesResource
        return KnowledgeBasesResource(self)

    @cached_property
    def with_raw_response(self) -> ProfoundWithRawResponse:
        return ProfoundWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfoundWithStreamedResponse:
        return ProfoundWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._access_token_header_auth,
            **self._api_key_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _access_token_header_auth(self) -> dict[str, str]:
        value = self.access_token
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _api_key_header_auth(self) -> dict[str, str]:
        value = self.api_key
        if value is None:
            return {}
        return {"X-API-Key": value}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        if headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected either access_token or api_key to be set. Or for one of the `Authorization` or `X-API-Key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        access_token: str | None = None,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncProfound(AsyncAPIClient):
    # client options
    access_token: str | None
    api_key: str | None

    def __init__(
        self,
        *,
        access_token: str | None = None,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncProfound client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `access_token` from `PROFOUND_ACCESS_TOKEN`
        - `api_key` from `PROFOUND_API_KEY`
        """
        if access_token is None:
            access_token = os.environ.get("PROFOUND_ACCESS_TOKEN")
        self.access_token = access_token
        if api_key is None:
            api_key = os.environ.get("PROFOUND_API_KEY")
        self.api_key = api_key
        if base_url is None:
            base_url = os.environ.get("PROFOUND_BASE_URL")
        if base_url is None:
            base_url = "https://api.tryprofound.com"
        custom_headers_env = os.environ.get("PROFOUND_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = AsyncStream

    @cached_property
    def organizations(self) -> "AsyncOrganizationsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import AsyncOrganizationsResource
        return AsyncOrganizationsResource(self)

    @cached_property
    def prompts(self) -> "AsyncPromptsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.prompts import AsyncPromptsResource
        return AsyncPromptsResource(self)

    @cached_property
    def reports(self) -> "AsyncReportsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.reports import AsyncReportsResource
        return AsyncReportsResource(self)

    @cached_property
    def content(self) -> "AsyncContentResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.content import AsyncContentResource
        return AsyncContentResource(self)

    @cached_property
    def agents(self) -> "AsyncAgentsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.agents import AsyncAgentsResource
        return AsyncAgentsResource(self)

    @cached_property
    def knowledge_bases(self) -> "AsyncKnowledgeBasesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.knowledge_bases import AsyncKnowledgeBasesResource
        return AsyncKnowledgeBasesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncProfoundWithRawResponse:
        return AsyncProfoundWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfoundWithStreamedResponse:
        return AsyncProfoundWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._access_token_header_auth,
            **self._api_key_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _access_token_header_auth(self) -> dict[str, str]:
        value = self.access_token
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _api_key_header_auth(self) -> dict[str, str]:
        value = self.api_key
        if value is None:
            return {}
        return {"X-API-Key": value}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        if headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected either access_token or api_key to be set. Or for one of the `Authorization` or `X-API-Key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        access_token: str | None = None,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ProfoundWithRawResponse:
    _client: Profound

    def __init__(self, client: Profound) -> None:
        self._client = client

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import OrganizationsResourceWithRawResponse
        return OrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.prompts import PromptsResourceWithRawResponse
        return PromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def reports(self) -> reports.ReportsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.reports import ReportsResourceWithRawResponse
        return ReportsResourceWithRawResponse(self._client.reports)

    @cached_property
    def content(self) -> content.ContentResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.content import ContentResourceWithRawResponse
        return ContentResourceWithRawResponse(self._client.content)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.agents import AgentsResourceWithRawResponse
        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def knowledge_bases(self) -> knowledge_bases.KnowledgeBasesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.knowledge_bases import KnowledgeBasesResourceWithRawResponse
        return KnowledgeBasesResourceWithRawResponse(self._client.knowledge_bases)


class AsyncProfoundWithRawResponse:
    _client: AsyncProfound

    def __init__(self, client: AsyncProfound) -> None:
        self._client = client

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import AsyncOrganizationsResourceWithRawResponse
        return AsyncOrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.prompts import AsyncPromptsResourceWithRawResponse
        return AsyncPromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def reports(self) -> reports.AsyncReportsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.reports import AsyncReportsResourceWithRawResponse
        return AsyncReportsResourceWithRawResponse(self._client.reports)

    @cached_property
    def content(self) -> content.AsyncContentResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.content import AsyncContentResourceWithRawResponse
        return AsyncContentResourceWithRawResponse(self._client.content)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.agents import AsyncAgentsResourceWithRawResponse
        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def knowledge_bases(self) -> knowledge_bases.AsyncKnowledgeBasesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.knowledge_bases import AsyncKnowledgeBasesResourceWithRawResponse
        return AsyncKnowledgeBasesResourceWithRawResponse(self._client.knowledge_bases)


class ProfoundWithStreamedResponse:
    _client: Profound

    def __init__(self, client: Profound) -> None:
        self._client = client

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import OrganizationsResourceWithStreamingResponse
        return OrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.prompts import PromptsResourceWithStreamingResponse
        return PromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def reports(self) -> reports.ReportsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.reports import ReportsResourceWithStreamingResponse
        return ReportsResourceWithStreamingResponse(self._client.reports)

    @cached_property
    def content(self) -> content.ContentResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.content import ContentResourceWithStreamingResponse
        return ContentResourceWithStreamingResponse(self._client.content)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.agents import AgentsResourceWithStreamingResponse
        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def knowledge_bases(self) -> knowledge_bases.KnowledgeBasesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.knowledge_bases import KnowledgeBasesResourceWithStreamingResponse
        return KnowledgeBasesResourceWithStreamingResponse(self._client.knowledge_bases)


class AsyncProfoundWithStreamedResponse:
    _client: AsyncProfound

    def __init__(self, client: AsyncProfound) -> None:
        self._client = client

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import AsyncOrganizationsResourceWithStreamingResponse
        return AsyncOrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.prompts import AsyncPromptsResourceWithStreamingResponse
        return AsyncPromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def reports(self) -> reports.AsyncReportsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.reports import AsyncReportsResourceWithStreamingResponse
        return AsyncReportsResourceWithStreamingResponse(self._client.reports)

    @cached_property
    def content(self) -> content.AsyncContentResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.content import AsyncContentResourceWithStreamingResponse
        return AsyncContentResourceWithStreamingResponse(self._client.content)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.agents import AsyncAgentsResourceWithStreamingResponse
        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def knowledge_bases(self) -> knowledge_bases.AsyncKnowledgeBasesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.knowledge_bases import AsyncKnowledgeBasesResourceWithStreamingResponse
        return AsyncKnowledgeBasesResourceWithStreamingResponse(self._client.knowledge_bases)


# Alias names for the documented `Client` / `AsyncClient` symbols.
Client = Profound
AsyncClient = AsyncProfound
