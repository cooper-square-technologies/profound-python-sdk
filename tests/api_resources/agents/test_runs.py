# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types.agents import RunCreateResponse, RunRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Profound) -> None:
        run = client.agents.runs.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Profound) -> None:
        run = client.agents.runs.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs={"foo": "bar"},
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Profound) -> None:
        response = client.agents.runs.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Profound) -> None:
        with client.agents.runs.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.runs.with_raw_response.create(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Profound) -> None:
        run = client.agents.runs.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Profound) -> None:
        response = client.agents.runs.with_raw_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Profound) -> None:
        with client.agents.runs.with_streaming_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunRetrieveResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.runs.with_raw_response.retrieve(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agents.runs.with_raw_response.retrieve(
                run_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncProfound) -> None:
        run = await async_client.agents.runs.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncProfound) -> None:
        run = await async_client.agents.runs.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs={"foo": "bar"},
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncProfound) -> None:
        response = await async_client.agents.runs.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncProfound) -> None:
        async with async_client.agents.runs.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.runs.with_raw_response.create(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncProfound) -> None:
        run = await async_client.agents.runs.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncProfound) -> None:
        response = await async_client.agents.runs.with_raw_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncProfound) -> None:
        async with async_client.agents.runs.with_streaming_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunRetrieveResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.runs.with_raw_response.retrieve(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agents.runs.with_raw_response.retrieve(
                run_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
