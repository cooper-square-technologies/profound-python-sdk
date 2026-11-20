# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestPrompts:
    @smoke_case("prompts.answers:required", operation="answers", path="/v1/prompts/answers")
    def test_method_answers(self) -> None:
        prompt = client.prompts.answers(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
        )

    @smoke_case("prompts.answers:all", operation="answers", path="/v1/prompts/answers")
    def test_method_answers_with_all_params(self) -> None:
        prompt = client.prompts.answers(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="2024-01-01T00:00:00.000Z",
            end_date="2024-01-01T00:00:00.000Z",
            pagination={"limit": 10000, "offset": 0},
            filters=[{"field": "region_id", "operator": "is", "value": "7c9e6679-7425-40de-944b-e07fc1f90ae7"}],
            include={
                "run_id": False,
                "created_at": True,
                "prompt": True,
                "prompt_id": False,
                "mentions": True,
                "analysis_types": False,
                "prompt_type": True,
                "response": True,
                "citations": True,
                "citation_details": False,
                "web_search_results": False,
                "search_triggered": False,
                "themes": True,
                "sentiment_themes": False,
                "topic": True,
                "topic_id": False,
                "region": True,
                "model": True,
                "model_id": True,
                "asset": True,
                "asset_id": False,
                "tags": False,
                "search_queries": False,
                "persona": False,
            },
        )

    @smoke_case("prompts.answersV2:required", operation="answersV2", path="/v2/prompts/answers")
    def test_method_answers_v2(self) -> None:
        prompt = client.prompts.answers_v2(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
        )

    @smoke_case("prompts.answersV2:all", operation="answersV2", path="/v2/prompts/answers")
    def test_method_answers_v2_with_all_params(self) -> None:
        prompt = client.prompts.answers_v2(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            include=["run_id"],
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

    @smoke_case("prompts.streamAnswersV2:required", operation="streamAnswersV2", path="/v2/prompts/answers/stream")
    def test_method_stream_answers_v2(self) -> None:
        stream = client.prompts.stream_answers_v2(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
        )

        for event in stream:
            print(event)

    @smoke_case("prompts.streamAnswersV2:all", operation="streamAnswersV2", path="/v2/prompts/answers/stream")
    def test_method_stream_answers_v2_with_all_params(self) -> None:
        stream = client.prompts.stream_answers_v2(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
            include=["run_id"],
            filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
            limit=1,
            max_results=1,
            cursor="",
        )

        for event in stream:
            print(event)
