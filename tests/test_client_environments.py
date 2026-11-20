# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

import httpx

from profound import ENVIRONMENTS

from tests.smoke_support import client, smoke_case


class TestClientEnvironments:
    @smoke_case(
        "$check.environment.production",
        operation='with_options(environment="production")',
        path="https://api.tryprofound.com",
    )
    def test_with_options_environment_production(self) -> None:
        original = client.base_url
        copied = client.with_options(environment="production")
        expected = str(httpx.URL(ENVIRONMENTS["production"])).rstrip("/")
        assert str(copied.base_url).rstrip("/") == expected, f"copy kept {copied.base_url}, expected {expected}"
        assert client.base_url == original, f"copy moved the original client to {client.base_url}"

    @smoke_case(
        "$check.environment.development",
        operation='with_options(environment="development")',
        path="https://dev.api.tryprofound.com",
    )
    def test_with_options_environment_development(self) -> None:
        original = client.base_url
        copied = client.with_options(environment="development")
        expected = str(httpx.URL(ENVIRONMENTS["development"])).rstrip("/")
        assert str(copied.base_url).rstrip("/") == expected, f"copy kept {copied.base_url}, expected {expected}"
        assert client.base_url == original, f"copy moved the original client to {client.base_url}"
