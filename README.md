# profound

This library provides convenient access to the profound REST API from Python.

The full API of this library can be found in [api.md](./api.md).

<br />

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](./api.md)
- [Async](#async)
- [Streaming](#streaming)
- [Authentication](#authentication)
- [Errors](#errors)
- [Client Options](#client-options)
- [Retries and Timeouts](#retries-and-timeouts)
- [Helpers](#helpers)
- [Logging](#logging)
- [Requirements](#requirements)

<br />

## Installation

```sh
pip install profound
```

<br />

## Usage

```python
import os

from profound import Profound

client = Profound(
    api_key=os.environ.get("PROFOUND_API_KEY"),
)

organization = client.organizations.regions()

print(organization)
```

The examples in the following sections assume a `client` configured as shown above.

See the [API reference](./api.md) for every available operation.

<br />

## Async

Every client has an `Async` counterpart (`AsyncProfound`) exposing the same resource tree with `await`.

```python
import asyncio

from profound import AsyncProfound


async def main() -> None:
    client = AsyncProfound()
    organization = await client.organizations.regions()


asyncio.run(main())
```

<br />

## Streaming

Streaming endpoints return an async iterator that yields results as the server emits them.

```python
stream = client.prompts.stream_answers_v2(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)

for event in stream:
    print(event)
```

<br />

## Authentication

Pass credentials to the generated client constructor. Environment variables are read automatically when supported by the target runtime.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `string \| provider` | - | Credential for the APIKeyHeader scheme. Defaults to PROFOUND_API_KEY. |
| `access_token` | `string \| provider` | - | Credential for the BearerAuth scheme. Defaults to PROFOUND_ACCESS_TOKEN. |

Declared schemes:

- `APIKeyHeader` API key in header `X-API-Key`
- `BearerAuth` bearer token

<br />

## Errors

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from profound import APIStatusError

try:
    organization = client.organizations.regions()
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

Documented error statuses: `422`.

<br />

## Client Options

Configure the generated client by setting any of these options when you create it.

```python
from profound import Profound

client = Profound(
    timeout=60.0,
    max_retries=2,
)
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `api_key` | `str \| None` | `os.environ.get("PROFOUND_API_KEY")` | Credential for the APIKeyHeader scheme. |
| `access_token` | `str \| None` | `os.environ.get("PROFOUND_ACCESS_TOKEN")` | Credential for the BearerAuth scheme. |
| `base_url` | `str \| httpx.URL \| None` | - | Override the default API base URL. |
| `timeout` | `float \| Timeout \| None` | `60.0` | Maximum time in seconds to wait for a response before aborting a request. |
| `max_retries` | `int` | `2` | Number of retries for temporary failures. |
| `default_headers` | `Mapping[str, str] \| None` | - | Headers sent with every request. |
| `default_query` | `Mapping[str, object] \| None` | - | Query parameters sent with every request. |

<br />

## Retries and Timeouts

Generated clients support request timeouts and retry temporary failures such as network errors, 408, 409, 429, and 5xx responses. Retry delays honor `Retry-After` headers when present. Tune the retry and timeout client options shown above, or override them per request.

<br />

## Helpers

- Use `client.with_raw_response.<resource>.<method>(...)` to access the raw `httpx.Response` and parse it yourself.
- Use `client.with_streaming_response.<resource>.<method>(...)` to stream a response body without buffering it.

<br />

## Logging

- Set the `PROFOUND_LOG` environment variable to `info` or `debug` to enable HTTP logging.
- Logs are emitted through the standard `logging` module under the `profound` logger.

<br />

## Requirements

- Python 3.8 or newer

Powered by Scalar.
