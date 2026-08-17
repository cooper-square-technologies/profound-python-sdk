# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke test: calls every generated operation once to confirm the SDK can reach each endpoint.
# Run it from this repo with `python tests/smoke-test.py`. The generator also runs this file
# against a mock server and reads the JSON report produced via SCALAR_SMOKE_REPORT.
from __future__ import annotations

import json
import os
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, TypedDict

from profound import Profound

# The shared smoke-test runner injects base URL and credentials through the same
# environment variables the generated client reads in normal use.
client = Profound(max_retries=0, timeout=30)


class SmokeResult(TypedDict, total=False):
    operation: str
    method: str
    path: str
    status: str
    durationMs: int
    error: str


class SmokeCase(TypedDict):
    operation: str
    method: str
    path: str
    run: Callable[[], Any]


def _smoke_case_0() -> None:
    organization = client.organizations.regions()


def _smoke_case_1() -> None:
    organization = client.organizations.models()


def _smoke_case_2() -> None:
    organization = client.organizations.domains()


def _smoke_case_3() -> None:
    organization = client.organizations.list_assets()


def _smoke_case_4() -> None:
    organization = client.organizations.get_personas()


def _smoke_case_5() -> None:
    organization = client.organizations.list()


def _smoke_case_6() -> None:
    category = client.organizations.categories.list()


def _smoke_case_7() -> None:
    category = client.organizations.categories.topics(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_8() -> None:
    category = client.organizations.categories.tags(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_9() -> None:
    category = client.organizations.categories.prompts(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=10000,
        status=["active"],
    )


def _smoke_case_10() -> None:
    category = client.organizations.categories.assets(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_11() -> None:
    category = client.organizations.categories.get_category_personas(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_12() -> None:
    category = client.organizations.categories.create_prompts(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        prompts=[],
        dry_run=False,
    )


def _smoke_case_13() -> None:
    category = client.organizations.categories.update_prompts(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        prompts=[],
        dry_run=False,
    )


def _smoke_case_14() -> None:
    category = client.organizations.categories.update_prompt_status(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        prompt_ids=[],
        status="active",
        dry_run=False,
    )


def _smoke_case_15() -> None:
    prompt = client.prompts.answers(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_16() -> None:
    report = client.reports.citations(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_17() -> None:
    report = client.reports.visibility(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_18() -> None:
    report = client.reports.sentiment(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_19() -> None:
    report = client.reports.get_referrals_report(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_20() -> None:
    report = client.reports.get_bots_report(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_21() -> None:
    report = client.reports.get_referrals_report_v2(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
        timezone="UTC",
    )


def _smoke_case_22() -> None:
    report = client.reports.get_bots_report_v2(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
        timezone="UTC",
    )


def _smoke_case_23() -> None:
    report = client.reports.query_fanouts(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_24() -> None:
    stream = client.reports.stream_citations(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )

    for event in stream:
        print(event)


def _smoke_case_25() -> None:
    stream = client.reports.stream_visibility(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )

    for event in stream:
        print(event)


def _smoke_case_26() -> None:
    stream = client.reports.stream_sentiment(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )

    for event in stream:
        print(event)


def _smoke_case_27() -> None:
    web_search_result = client.reports.web_search_results.query(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_28() -> None:
    stream = client.reports.web_search_results.stream(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )

    for event in stream:
        print(event)


def _smoke_case_29() -> None:
    shopping = client.reports.shopping.visibility(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
        include_asset_only=False,
        rank_by="visibility_score",
        include_position_frequency=False,
    )


def _smoke_case_30() -> None:
    shopping = client.reports.shopping.item_visibility(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
        merchant_filter_type="any",
        include_competitors=False,
        competitor_limit=5,
        include_position_frequency=False,
    )


def _smoke_case_31() -> None:
    shopping = client.reports.shopping.merchant_distribution(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )


def _smoke_case_32() -> None:
    shopping = client.reports.shopping.merchant_visibility_by_brand(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
        include_brand_only=False,
    )


def _smoke_case_33() -> None:
    shopping = client.reports.shopping.merchant_by_items(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )


def _smoke_case_34() -> None:
    shopping = client.reports.shopping.all_items_with_merchants(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
        merchant_filter_type="any",
        rank_by="visibility",
        sort_order="desc",
    )


def _smoke_case_35() -> None:
    shopping = client.reports.shopping.trigger_rate(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )


def _smoke_case_36() -> None:
    shopping = client.reports.shopping.merchant_share(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )


def _smoke_case_37() -> None:
    shopping = client.reports.shopping.product_merchant_urls(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        product_names=[],
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_38() -> None:
    shopping = client.reports.shopping.executions(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
        analysis_filter_type="any",
    )


def _smoke_case_39() -> None:
    optimization = client.content.optimization.list(
        asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=10000,
        offset=0,
    )


def _smoke_case_40() -> None:
    optimization = client.content.optimization.retrieve(
        asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        content_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_41() -> None:
    agent = client.agents.list(
        limit=100,
    )


def _smoke_case_42() -> None:
    agent = client.agents.retrieve(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_43() -> None:
    run = client.agents.runs.create(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_44() -> None:
    run = client.agents.runs.retrieve(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        verbose=False,
    )


def _smoke_case_45() -> None:
    knowledge_base = client.knowledge_bases.list()


def _smoke_case_46() -> None:
    knowledge_base = client.knowledge_bases.search(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        query="x",
        top_k=0,
        return_full_page=False,
    )


def _smoke_case_47() -> None:
    document = client.knowledge_bases.documents.create(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        text="x",
    )


def _smoke_case_48() -> None:
    document = client.knowledge_bases.documents.update(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        text="x",
    )


def _smoke_case_49() -> None:
    document = client.knowledge_bases.documents.delete(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
    )


def _smoke_case_50() -> None:
    folder = client.knowledge_bases.folders.create(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        path="x",
    )


def _smoke_case_51() -> None:
    folder = client.knowledge_bases.folders.delete(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        path="x",
        recursive=False,
    )


cases: list[SmokeCase] = [
    {
        "operation": "regions",
        "method": "GET",
        "path": "/v1/org/regions",
        "run": _smoke_case_0,
    },
    {
        "operation": "models",
        "method": "GET",
        "path": "/v1/org/models",
        "run": _smoke_case_1,
    },
    {
        "operation": "domains",
        "method": "GET",
        "path": "/v1/org/domains",
        "run": _smoke_case_2,
    },
    {
        "operation": "listAssets",
        "method": "GET",
        "path": "/v1/org/assets",
        "run": _smoke_case_3,
    },
    {
        "operation": "getPersonas",
        "method": "GET",
        "path": "/v1/org/personas",
        "run": _smoke_case_4,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/org",
        "run": _smoke_case_5,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/org/categories",
        "run": _smoke_case_6,
    },
    {
        "operation": "topics",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/topics",
        "run": _smoke_case_7,
    },
    {
        "operation": "tags",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/tags",
        "run": _smoke_case_8,
    },
    {
        "operation": "prompts",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/prompts",
        "run": _smoke_case_9,
    },
    {
        "operation": "assets",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/assets",
        "run": _smoke_case_10,
    },
    {
        "operation": "getCategoryPersonas",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/personas",
        "run": _smoke_case_11,
    },
    {
        "operation": "createPrompts",
        "method": "POST",
        "path": "/v1/org/categories/{category_id}/prompts",
        "run": _smoke_case_12,
    },
    {
        "operation": "updatePrompts",
        "method": "PATCH",
        "path": "/v1/org/categories/{category_id}/prompts",
        "run": _smoke_case_13,
    },
    {
        "operation": "updatePromptStatus",
        "method": "PATCH",
        "path": "/v1/org/categories/{category_id}/prompts/status",
        "run": _smoke_case_14,
    },
    {
        "operation": "answers",
        "method": "POST",
        "path": "/v1/prompts/answers",
        "run": _smoke_case_15,
    },
    {
        "operation": "citations",
        "method": "POST",
        "path": "/v1/reports/citations",
        "run": _smoke_case_16,
    },
    {
        "operation": "visibility",
        "method": "POST",
        "path": "/v1/reports/visibility",
        "run": _smoke_case_17,
    },
    {
        "operation": "sentiment",
        "method": "POST",
        "path": "/v1/reports/sentiment",
        "run": _smoke_case_18,
    },
    {
        "operation": "getReferralsReport",
        "method": "POST",
        "path": "/v1/reports/referrals",
        "run": _smoke_case_19,
    },
    {
        "operation": "getBotsReport",
        "method": "POST",
        "path": "/v1/reports/bots",
        "run": _smoke_case_20,
    },
    {
        "operation": "getReferralsReportV2",
        "method": "POST",
        "path": "/v2/reports/referrals",
        "run": _smoke_case_21,
    },
    {
        "operation": "getBotsReportV2",
        "method": "POST",
        "path": "/v2/reports/bots",
        "run": _smoke_case_22,
    },
    {
        "operation": "queryFanouts",
        "method": "POST",
        "path": "/v1/reports/query-fanouts",
        "run": _smoke_case_23,
    },
    {
        "operation": "streamCitations",
        "method": "POST",
        "path": "/v1/reports/citations/stream",
        "run": _smoke_case_24,
    },
    {
        "operation": "streamVisibility",
        "method": "POST",
        "path": "/v1/reports/visibility/stream",
        "run": _smoke_case_25,
    },
    {
        "operation": "streamSentiment",
        "method": "POST",
        "path": "/v1/reports/sentiment/stream",
        "run": _smoke_case_26,
    },
    {
        "operation": "query",
        "method": "POST",
        "path": "/v1/reports/web-search-results",
        "run": _smoke_case_27,
    },
    {
        "operation": "stream",
        "method": "POST",
        "path": "/v1/reports/web-search-results/stream",
        "run": _smoke_case_28,
    },
    {
        "operation": "visibility",
        "method": "POST",
        "path": "/v1/reports/shopping/visibility",
        "run": _smoke_case_29,
    },
    {
        "operation": "itemVisibility",
        "method": "POST",
        "path": "/v1/reports/shopping/item-visibility",
        "run": _smoke_case_30,
    },
    {
        "operation": "merchantDistribution",
        "method": "POST",
        "path": "/v1/reports/shopping/merchant-distribution",
        "run": _smoke_case_31,
    },
    {
        "operation": "merchantVisibilityByBrand",
        "method": "POST",
        "path": "/v1/reports/shopping/merchant-visibility-by-brand",
        "run": _smoke_case_32,
    },
    {
        "operation": "merchantByItems",
        "method": "POST",
        "path": "/v1/reports/shopping/merchant-by-items",
        "run": _smoke_case_33,
    },
    {
        "operation": "allItemsWithMerchants",
        "method": "POST",
        "path": "/v1/reports/shopping/all-items-with-merchants",
        "run": _smoke_case_34,
    },
    {
        "operation": "triggerRate",
        "method": "POST",
        "path": "/v1/reports/shopping/trigger-rate",
        "run": _smoke_case_35,
    },
    {
        "operation": "merchantShare",
        "method": "POST",
        "path": "/v1/reports/shopping/merchant-share",
        "run": _smoke_case_36,
    },
    {
        "operation": "productMerchantUrls",
        "method": "POST",
        "path": "/v1/reports/shopping/product-merchant-urls",
        "run": _smoke_case_37,
    },
    {
        "operation": "executions",
        "method": "POST",
        "path": "/v1/reports/shopping/executions",
        "run": _smoke_case_38,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/content/{asset_id}/optimization",
        "run": _smoke_case_39,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/content/{asset_id}/optimization/{content_id}",
        "run": _smoke_case_40,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents",
        "run": _smoke_case_41,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agent_id}",
        "run": _smoke_case_42,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents/{agent_id}/runs",
        "run": _smoke_case_43,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agent_id}/runs/{run_id}",
        "run": _smoke_case_44,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/knowledge-bases",
        "run": _smoke_case_45,
    },
    {
        "operation": "search",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/search",
        "run": _smoke_case_46,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "run": _smoke_case_47,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "run": _smoke_case_48,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "run": _smoke_case_49,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/folders",
        "run": _smoke_case_50,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/folders",
        "run": _smoke_case_51,
    },
]

DEFAULT_SMOKE_CONCURRENCY = 32


def _selected_cases() -> list[SmokeCase]:
    filter_value = os.environ.get("SCALAR_SMOKE_FILTER")
    needles = [needle.strip() for needle in filter_value.split(",") if needle.strip()] if filter_value else []
    if not needles:
        return cases
    return [case for case in cases if any(needle in case["operation"] or needle in case["path"] for needle in needles)]


def _smoke_concurrency(case_count: int) -> int:
    override = os.environ.get("SCALAR_SMOKE_CONCURRENCY")
    if override:
        try:
            parsed = int(override)
            if parsed > 0:
                return min(parsed, case_count)
        except ValueError:
            pass
    return min(DEFAULT_SMOKE_CONCURRENCY, case_count)


def _run_case(case: SmokeCase) -> SmokeResult:
    started_at = time.monotonic()
    try:
        case["run"]()
        return {
            "operation": case["operation"],
            "method": case["method"],
            "path": case["path"],
            "status": "passed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
        }
    except Exception:
        return {
            "operation": case["operation"],
            "method": case["method"],
            "path": case["path"],
            "status": "failed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
            "error": traceback.format_exc(),
        }


def main() -> None:
    selected = _selected_cases()
    if selected:
        # Keep enough parallelism to catch generated SDK concurrency bugs without overwhelming
        # CI runners or the in-process mock server for large SDKs.
        with ThreadPoolExecutor(max_workers=_smoke_concurrency(len(selected))) as executor:
            results = list(executor.map(_run_case, selected))
    else:
        results = []
    failed = [result for result in results if result["status"] == "failed"]

    report_path = os.environ.get("SCALAR_SMOKE_REPORT")
    if report_path:
        Path(report_path).write_text(
            json.dumps({"total": len(results), "failed": len(failed), "results": results}), encoding="utf-8"
        )
    else:
        for result in results:
            if result["status"] == "passed":
                print(f"PASS {result['operation']} ({result['method']} {result['path']}) {result['durationMs']}ms")
            else:
                print(
                    f"FAIL {result['operation']} ({result['method']} {result['path']})\n{result.get('error', '')}",
                    file=sys.stderr,
                )
        if not results:
            print("No code samples ran (empty SDK or a SCALAR_SMOKE_FILTER that matched nothing).", file=sys.stderr)
        else:
            print(f"\n{len(results) - len(failed)}/{len(results)} samples passed")

    if failed or not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
