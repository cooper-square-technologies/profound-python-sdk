# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types import (
    ProjectListResponse,
    ProjectCreateResponse,
    ProjectArchiveResponse,
    ProjectRetrieveResponse,
    ProjectGetStatusResponse,
    ProjectUnarchiveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Profound) -> None:
        project = client.projects.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Profound) -> None:
        project = client.projects.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attachments=[
                {
                    "id": "x",
                    "data_base64": "x",
                    "mime_type": "x",
                    "name": "x",
                    "size_bytes": 1,
                }
            ],
            focus="x",
            generation_context={
                "date_range": {
                    "label": "x",
                    "preset": "x",
                    "end_date": "endDate",
                    "mode": "custom",
                    "start_date": "startDate",
                },
                "platforms": [
                    {
                        "id": "x",
                        "name": "x",
                        "slug": "slug",
                    }
                ],
                "project_categories": ["creative"],
                "regions": [
                    {
                        "id": "x",
                        "name": "x",
                        "slug": "slug",
                    }
                ],
                "tags": [
                    {
                        "id": "x",
                        "name": "x",
                        "slug": "slug",
                    }
                ],
            },
            project_name="x",
            title="x",
            topics=["x"],
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Profound) -> None:
        response = client.projects.with_raw_response.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Profound) -> None:
        with client.projects.with_streaming_response.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Profound) -> None:
        project = client.projects.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Profound) -> None:
        response = client.projects.with_raw_response.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Profound) -> None:
        with client.projects.with_streaming_response.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.retrieve(
                project_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Profound) -> None:
        project = client.projects.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Profound) -> None:
        project = client.projects.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
            status="status",
        )
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Profound) -> None:
        response = client.projects.with_raw_response.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Profound) -> None:
        with client.projects.with_streaming_response.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Profound) -> None:
        project = client.projects.delete(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Profound) -> None:
        response = client.projects.with_raw_response.delete(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Profound) -> None:
        with client.projects.with_streaming_response.delete(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.delete(
                project_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Profound) -> None:
        project = client.projects.archive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectArchiveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive_with_all_params(self, client: Profound) -> None:
        project = client.projects.archive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="x",
        )
        assert_matches_type(ProjectArchiveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Profound) -> None:
        response = client.projects.with_raw_response.archive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectArchiveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Profound) -> None:
        with client.projects.with_streaming_response.archive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectArchiveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.archive(
                project_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: Profound) -> None:
        project = client.projects.get_status(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectGetStatusResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: Profound) -> None:
        response = client.projects.with_raw_response.get_status(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectGetStatusResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: Profound) -> None:
        with client.projects.with_streaming_response.get_status(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectGetStatusResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.get_status(
                project_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unarchive(self, client: Profound) -> None:
        project = client.projects.unarchive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectUnarchiveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unarchive(self, client: Profound) -> None:
        response = client.projects.with_raw_response.unarchive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectUnarchiveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unarchive(self, client: Profound) -> None:
        with client.projects.with_streaming_response.unarchive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectUnarchiveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unarchive(self, client: Profound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.unarchive(
                project_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncProjects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncProfound) -> None:
        project = await async_client.projects.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncProfound) -> None:
        project = await async_client.projects.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attachments=[
                {
                    "id": "x",
                    "data_base64": "x",
                    "mime_type": "x",
                    "name": "x",
                    "size_bytes": 1,
                }
            ],
            focus="x",
            generation_context={
                "date_range": {
                    "label": "x",
                    "preset": "x",
                    "end_date": "endDate",
                    "mode": "custom",
                    "start_date": "startDate",
                },
                "platforms": [
                    {
                        "id": "x",
                        "name": "x",
                        "slug": "slug",
                    }
                ],
                "project_categories": ["creative"],
                "regions": [
                    {
                        "id": "x",
                        "name": "x",
                        "slug": "slug",
                    }
                ],
                "tags": [
                    {
                        "id": "x",
                        "name": "x",
                        "slug": "slug",
                    }
                ],
            },
            project_name="x",
            title="x",
            topics=["x"],
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncProfound) -> None:
        response = await async_client.projects.with_raw_response.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncProfound) -> None:
        async with async_client.projects.with_streaming_response.create(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncProfound) -> None:
        project = await async_client.projects.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncProfound) -> None:
        response = await async_client.projects.with_raw_response.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncProfound) -> None:
        async with async_client.projects.with_streaming_response.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.retrieve(
                project_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncProfound) -> None:
        project = await async_client.projects.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncProfound) -> None:
        project = await async_client.projects.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
            status="status",
        )
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncProfound) -> None:
        response = await async_client.projects.with_raw_response.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncProfound) -> None:
        async with async_client.projects.with_streaming_response.list(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncProfound) -> None:
        project = await async_client.projects.delete(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncProfound) -> None:
        response = await async_client.projects.with_raw_response.delete(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncProfound) -> None:
        async with async_client.projects.with_streaming_response.delete(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.delete(
                project_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncProfound) -> None:
        project = await async_client.projects.archive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectArchiveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive_with_all_params(self, async_client: AsyncProfound) -> None:
        project = await async_client.projects.archive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="x",
        )
        assert_matches_type(ProjectArchiveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncProfound) -> None:
        response = await async_client.projects.with_raw_response.archive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectArchiveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncProfound) -> None:
        async with async_client.projects.with_streaming_response.archive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectArchiveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.archive(
                project_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncProfound) -> None:
        project = await async_client.projects.get_status(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectGetStatusResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncProfound) -> None:
        response = await async_client.projects.with_raw_response.get_status(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectGetStatusResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncProfound) -> None:
        async with async_client.projects.with_streaming_response.get_status(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectGetStatusResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.get_status(
                project_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unarchive(self, async_client: AsyncProfound) -> None:
        project = await async_client.projects.unarchive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectUnarchiveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncProfound) -> None:
        response = await async_client.projects.with_raw_response.unarchive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectUnarchiveResponse, project, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncProfound) -> None:
        async with async_client.projects.with_streaming_response.unarchive(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectUnarchiveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncProfound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.unarchive(
                project_id="",
                category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
