---
name: profound-python-sdk
description: "Python SDK for profound API. Use when writing Python code that calls profound API with the profound package: installing it, constructing and authenticating the client, and calling API operations."
---

# profound Python SDK

Generated Python client for profound API, published as `profound`. Use the generated client instead of hand-writing HTTP requests.

## Install

```sh
pip install profound
```

## Client setup and authentication

```python
import os

from profound import Profound

client = Profound(
    api_key=os.environ.get("PROFOUND_API_KEY"),
)
```

Provide credentials using the options below. Environment variables are read automatically when the target runtime supports them:

- `api_key` (env: `PROFOUND_API_KEY`) — Credential for the APIKeyHeader scheme.
- `access_token` (env: `PROFOUND_ACCESS_TOKEN`) — Credential for the BearerAuth scheme.

## Calling operations

```python
import os

from profound import Profound

client = Profound(
    api_key=os.environ.get("PROFOUND_API_KEY"),
)

organization = client.organizations.regions()

print(organization)
```

Method names, parameter shapes, and response types are generated from the API description — do not guess them. Look up the exact call signature in [api.md](./api.md) before writing a call.

## Streaming

Streaming endpoints return an iterator that yields results as the server emits them.

```python
stream = client.prompts.stream_answers_v2(
    category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    start_date="",
    end_date="",
)

for event in stream:
    print(event)
```

## Error handling

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from profound import APIStatusError

try:
    organization = client.organizations.regions()
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

## Requirements

- Python 3.8 or newer

## Reference files

- [README.md](./README.md) — full feature tour: client options, retries and timeouts, logging.
- [api.md](./api.md) — complete catalogue of every operation with request and response types.
