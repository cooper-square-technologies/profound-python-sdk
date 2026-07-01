# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

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
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import agents, content, prompts, reports, organizations, knowledge_bases
    from .resources.prompts import PromptsResource, AsyncPromptsResource
    from .resources.agents.agents import AgentsResource, AsyncAgentsResource
    from .resources.content.content import ContentResource, AsyncContentResource
    from .resources.reports.reports import ReportsResource, AsyncReportsResource
    from .resources.organizations.organizations import OrganizationsResource, AsyncOrganizationsResource
    from .resources.knowledge_bases.knowledge_bases import KnowledgeBasesResource, AsyncKnowledgeBasesResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Profound",
    "AsyncProfound",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.tryprofound.com",
    "development": "https://dev.api.tryprofound.com",
}


class Profound(SyncAPIClient):
    # client options
    access_token: str | None
    api_key: str | None

    _environment: Literal["production", "development"] | NotGiven

    def __init__(
        self,
        *,
        access_token: str | None = None,
        api_key: str | None = None,
        environment: Literal["production", "development"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
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

        self._environment = environment

        base_url_env = os.environ.get("PROFOUND_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PROFOUND_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

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

    @cached_property
    def organizations(self) -> OrganizationsResource:
        from .resources.organizations import OrganizationsResource

        return OrganizationsResource(self)

    @cached_property
    def prompts(self) -> PromptsResource:
        from .resources.prompts import PromptsResource

        return PromptsResource(self)

    @cached_property
    def reports(self) -> ReportsResource:
        from .resources.reports import ReportsResource

        return ReportsResource(self)

    @cached_property
    def content(self) -> ContentResource:
        from .resources.content import ContentResource

        return ContentResource(self)

    @cached_property
    def agents(self) -> AgentsResource:
        from .resources.agents import AgentsResource

        return AgentsResource(self)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResource:
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
        return {**self._bearer_auth, **self._api_key_header}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        access_token = self.access_token
        if access_token is None:
            return {}
        return {"Authorization": f"Bearer {access_token}"}

    @property
    def _api_key_header(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        if headers.get("X-API-Key") or isinstance(custom_headers.get("X-API-Key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either access_token or api_key to be set. Or for one of the `Authorization` or `X-API-Key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        access_token: str | None = None,
        api_key: str | None = None,
        environment: Literal["production", "development"] | None = None,
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
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
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
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
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

    _environment: Literal["production", "development"] | NotGiven

    def __init__(
        self,
        *,
        access_token: str | None = None,
        api_key: str | None = None,
        environment: Literal["production", "development"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
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

        self._environment = environment

        base_url_env = os.environ.get("PROFOUND_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PROFOUND_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

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

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        from .resources.organizations import AsyncOrganizationsResource

        return AsyncOrganizationsResource(self)

    @cached_property
    def prompts(self) -> AsyncPromptsResource:
        from .resources.prompts import AsyncPromptsResource

        return AsyncPromptsResource(self)

    @cached_property
    def reports(self) -> AsyncReportsResource:
        from .resources.reports import AsyncReportsResource

        return AsyncReportsResource(self)

    @cached_property
    def content(self) -> AsyncContentResource:
        from .resources.content import AsyncContentResource

        return AsyncContentResource(self)

    @cached_property
    def agents(self) -> AsyncAgentsResource:
        from .resources.agents import AsyncAgentsResource

        return AsyncAgentsResource(self)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResource:
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
        return {**self._bearer_auth, **self._api_key_header}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        access_token = self.access_token
        if access_token is None:
            return {}
        return {"Authorization": f"Bearer {access_token}"}

    @property
    def _api_key_header(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        if headers.get("X-API-Key") or isinstance(custom_headers.get("X-API-Key"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either access_token or api_key to be set. Or for one of the `Authorization` or `X-API-Key` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        access_token: str | None = None,
        api_key: str | None = None,
        environment: Literal["production", "development"] | None = None,
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
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
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
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
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
        from .resources.organizations import OrganizationsResourceWithRawResponse

        return OrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithRawResponse:
        from .resources.prompts import PromptsResourceWithRawResponse

        return PromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def reports(self) -> reports.ReportsResourceWithRawResponse:
        from .resources.reports import ReportsResourceWithRawResponse

        return ReportsResourceWithRawResponse(self._client.reports)

    @cached_property
    def content(self) -> content.ContentResourceWithRawResponse:
        from .resources.content import ContentResourceWithRawResponse

        return ContentResourceWithRawResponse(self._client.content)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        from .resources.agents import AgentsResourceWithRawResponse

        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def knowledge_bases(self) -> knowledge_bases.KnowledgeBasesResourceWithRawResponse:
        from .resources.knowledge_bases import KnowledgeBasesResourceWithRawResponse

        return KnowledgeBasesResourceWithRawResponse(self._client.knowledge_bases)


class AsyncProfoundWithRawResponse:
    _client: AsyncProfound

    def __init__(self, client: AsyncProfound) -> None:
        self._client = client

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithRawResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithRawResponse

        return AsyncOrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithRawResponse:
        from .resources.prompts import AsyncPromptsResourceWithRawResponse

        return AsyncPromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def reports(self) -> reports.AsyncReportsResourceWithRawResponse:
        from .resources.reports import AsyncReportsResourceWithRawResponse

        return AsyncReportsResourceWithRawResponse(self._client.reports)

    @cached_property
    def content(self) -> content.AsyncContentResourceWithRawResponse:
        from .resources.content import AsyncContentResourceWithRawResponse

        return AsyncContentResourceWithRawResponse(self._client.content)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        from .resources.agents import AsyncAgentsResourceWithRawResponse

        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def knowledge_bases(self) -> knowledge_bases.AsyncKnowledgeBasesResourceWithRawResponse:
        from .resources.knowledge_bases import AsyncKnowledgeBasesResourceWithRawResponse

        return AsyncKnowledgeBasesResourceWithRawResponse(self._client.knowledge_bases)


class ProfoundWithStreamedResponse:
    _client: Profound

    def __init__(self, client: Profound) -> None:
        self._client = client

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithStreamingResponse:
        from .resources.organizations import OrganizationsResourceWithStreamingResponse

        return OrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithStreamingResponse:
        from .resources.prompts import PromptsResourceWithStreamingResponse

        return PromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def reports(self) -> reports.ReportsResourceWithStreamingResponse:
        from .resources.reports import ReportsResourceWithStreamingResponse

        return ReportsResourceWithStreamingResponse(self._client.reports)

    @cached_property
    def content(self) -> content.ContentResourceWithStreamingResponse:
        from .resources.content import ContentResourceWithStreamingResponse

        return ContentResourceWithStreamingResponse(self._client.content)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        from .resources.agents import AgentsResourceWithStreamingResponse

        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def knowledge_bases(self) -> knowledge_bases.KnowledgeBasesResourceWithStreamingResponse:
        from .resources.knowledge_bases import KnowledgeBasesResourceWithStreamingResponse

        return KnowledgeBasesResourceWithStreamingResponse(self._client.knowledge_bases)


class AsyncProfoundWithStreamedResponse:
    _client: AsyncProfound

    def __init__(self, client: AsyncProfound) -> None:
        self._client = client

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithStreamingResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithStreamingResponse

        return AsyncOrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithStreamingResponse:
        from .resources.prompts import AsyncPromptsResourceWithStreamingResponse

        return AsyncPromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def reports(self) -> reports.AsyncReportsResourceWithStreamingResponse:
        from .resources.reports import AsyncReportsResourceWithStreamingResponse

        return AsyncReportsResourceWithStreamingResponse(self._client.reports)

    @cached_property
    def content(self) -> content.AsyncContentResourceWithStreamingResponse:
        from .resources.content import AsyncContentResourceWithStreamingResponse

        return AsyncContentResourceWithStreamingResponse(self._client.content)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        from .resources.agents import AsyncAgentsResourceWithStreamingResponse

        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def knowledge_bases(self) -> knowledge_bases.AsyncKnowledgeBasesResourceWithStreamingResponse:
        from .resources.knowledge_bases import AsyncKnowledgeBasesResourceWithStreamingResponse

        return AsyncKnowledgeBasesResourceWithStreamingResponse(self._client.knowledge_bases)


Client = Profound

AsyncClient = AsyncProfound
