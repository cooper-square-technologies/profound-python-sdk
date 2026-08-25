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
    label: str
    status: str
    durationMs: int
    error: str


class _SmokeCaseBase(TypedDict):
    operation: str
    method: str
    path: str
    run: Callable[[], Any]


# `label` says which of an operation's two calls this is — "required params" or "all params".
# It sits in a total=False extension because it is absent when the operation contributed a
# single case, while the fields above are always present.
class SmokeCase(_SmokeCaseBase, total=False):
    label: str


def _smoke_case_0() -> None:
    organization = client.organizations.regions()


def _smoke_case_1() -> None:
    organization = client.organizations.regions(
        organization_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
    )


def _smoke_case_2() -> None:
    organization = client.organizations.models()


def _smoke_case_3() -> None:
    organization = client.organizations.domains()


def _smoke_case_4() -> None:
    organization = client.organizations.domains(
        organization_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
    )


def _smoke_case_5() -> None:
    organization = client.organizations.list_assets()


def _smoke_case_6() -> None:
    organization = client.organizations.list_assets(
        organization_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
    )


def _smoke_case_7() -> None:
    organization = client.organizations.get_personas()


def _smoke_case_8() -> None:
    organization = client.organizations.get_personas(
        organization_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
    )


def _smoke_case_9() -> None:
    organization = client.organizations.list()


def _smoke_case_10() -> None:
    category = client.organizations.categories.list()


def _smoke_case_11() -> None:
    category = client.organizations.categories.list(
        organization_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
    )


def _smoke_case_12() -> None:
    category = client.organizations.categories.topics(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_13() -> None:
    category = client.organizations.categories.tags(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_14() -> None:
    category = client.organizations.categories.prompts(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=10000,
        status=["active"],
    )


def _smoke_case_15() -> None:
    category = client.organizations.categories.prompts(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=10000,
        cursor="cursor",
        order_by="created_at",
        order_dir="asc",
        analysis_type=["visibility"],
        prompt_type=["visibility"],
        status=["active"],
        topic_id=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        tag_id=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        region_id=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        platform_id=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
        persona_id=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
    )


def _smoke_case_16() -> None:
    category = client.organizations.categories.assets(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_17() -> None:
    category = client.organizations.categories.get_category_personas(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_18() -> None:
    category = client.organizations.categories.create_prompts(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        prompts=[],
        dry_run=False,
    )


def _smoke_case_19() -> None:
    category = client.organizations.categories.update_prompts(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        prompts=[],
        dry_run=False,
    )


def _smoke_case_20() -> None:
    category = client.organizations.categories.update_prompt_status(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        prompt_ids=[],
        status="active",
        dry_run=False,
    )


def _smoke_case_21() -> None:
    category = client.organizations.categories.retrieve_regions(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_22() -> None:
    category = client.organizations.categories.get_citation_categories(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_23() -> None:
    prompt = client.prompts.answers(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_24() -> None:
    prompt = client.prompts.answers(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        pagination={"limit": 10000, "offset": 0},
        filters=[],
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


def _smoke_case_25() -> None:
    prompt = client.prompts.answers_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_26() -> None:
    prompt = client.prompts.answers_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        include=[],
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )


def _smoke_case_27() -> None:
    stream = client.prompts.stream_answers_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )

    for event in stream:
        print(event)


def _smoke_case_28() -> None:
    stream = client.prompts.stream_answers_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        include=[],
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )

    for event in stream:
        print(event)


def _smoke_case_29() -> None:
    report = client.reports.citations(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_30() -> None:
    report = client.reports.citations(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        filters=[],
    )


def _smoke_case_31() -> None:
    report = client.reports.visibility(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_32() -> None:
    report = client.reports.visibility(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        filters=[],
    )


def _smoke_case_33() -> None:
    report = client.reports.sentiment(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_34() -> None:
    report = client.reports.sentiment(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        filters=[],
    )


def _smoke_case_35() -> None:
    report = client.reports.sentiment_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        asset_name="",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_bucket="day",
        metrics=[],
    )


def _smoke_case_36() -> None:
    report = client.reports.sentiment_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        asset_name="",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        comparison_start_date="2024-01-01T00:00:00.000Z",
        comparison_end_date="2024-01-01T00:00:00.000Z",
        date_bucket="day",
        dimensions=[],
        metrics=[],
        filters=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
    )


def _smoke_case_37() -> None:
    report = client.reports.get_referrals_report(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_38() -> None:
    report = client.reports.get_referrals_report(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        metric_filters=[],
        filters=[],
    )


def _smoke_case_39() -> None:
    report = client.reports.get_bots_report(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_40() -> None:
    report = client.reports.get_bots_report(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        metric_filters=[],
        filters=[],
    )


def _smoke_case_41() -> None:
    report = client.reports.query_fanouts(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_42() -> None:
    report = client.reports.query_fanouts(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        filters=[],
    )


def _smoke_case_43() -> None:
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


def _smoke_case_44() -> None:
    stream = client.reports.stream_citations(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        filters=[],
    )

    for event in stream:
        print(event)


def _smoke_case_45() -> None:
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


def _smoke_case_46() -> None:
    stream = client.reports.stream_visibility(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        filters=[],
    )

    for event in stream:
        print(event)


def _smoke_case_47() -> None:
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


def _smoke_case_48() -> None:
    stream = client.reports.stream_sentiment(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        filters=[],
    )

    for event in stream:
        print(event)


def _smoke_case_49() -> None:
    stream = client.reports.stream_citations_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        entity="domain",
        interval="day",
        scope="all",
    )

    for event in stream:
        print(event)


def _smoke_case_50() -> None:
    stream = client.reports.stream_citations_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        entity="domain",
        group_by=[],
        metrics=[],
        interval="day",
        scope="all",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )

    for event in stream:
        print(event)


def _smoke_case_51() -> None:
    stream = client.reports.stream_visibility_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )

    for event in stream:
        print(event)


def _smoke_case_52() -> None:
    stream = client.reports.stream_visibility_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        scope="owned",
        assets="",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        sort={"field": "visibility_score"},
        limit=0,
        max_results=0,
        cursor="",
    )

    for event in stream:
        print(event)


def _smoke_case_53() -> None:
    stream = client.reports.stream_sentiment_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        asset="",
        start_date="",
        end_date="",
        interval="day",
        include_cited_websites=False,
    )

    for event in stream:
        print(event)


def _smoke_case_54() -> None:
    stream = client.reports.stream_sentiment_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        asset="",
        start_date="",
        end_date="",
        comparison_start_date="",
        comparison_end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        sort={"field": "positive_sentiment", "dir": "desc"},
        include_cited_websites=False,
        limit=0,
        max_results=0,
        cursor="",
    )

    for event in stream:
        print(event)


def _smoke_case_55() -> None:
    stream = client.reports.stream_query_fanouts(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )

    for event in stream:
        print(event)


def _smoke_case_56() -> None:
    stream = client.reports.stream_query_fanouts(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        sort={"field": "", "dir": "desc"},
        limit=0,
        max_results=0,
        cursor="",
    )

    for event in stream:
        print(event)


def _smoke_case_57() -> None:
    report = client.reports.get_referrals_report_v2(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
        timezone="UTC",
    )


def _smoke_case_58() -> None:
    report = client.reports.get_referrals_report_v2(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        timezone="UTC",
        view_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        metric_filters=[],
        filters=[],
    )


def _smoke_case_59() -> None:
    report = client.reports.get_bots_report_v2(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
        timezone="UTC",
    )


def _smoke_case_60() -> None:
    report = client.reports.get_bots_report_v2(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        timezone="UTC",
        view_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        metric_filters=[],
        filters=[],
        domain_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        tags=[],
    )


def _smoke_case_61() -> None:
    report = client.reports.query_visibility(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )


def _smoke_case_62() -> None:
    report = client.reports.query_visibility(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        scope="owned",
        assets="",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        sort={"field": "visibility_score"},
        limit=0,
        max_results=0,
        cursor="",
    )


def _smoke_case_63() -> None:
    report = client.reports.query_citations(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        entity="domain",
        interval="day",
        scope="all",
    )


def _smoke_case_64() -> None:
    report = client.reports.query_citations(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        entity="domain",
        group_by=[],
        metrics=[],
        interval="day",
        scope="all",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )


def _smoke_case_65() -> None:
    report = client.reports.query_sentiment(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        asset="",
        start_date="",
        end_date="",
        interval="day",
        include_cited_websites=False,
    )


def _smoke_case_66() -> None:
    report = client.reports.query_sentiment(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        asset="",
        start_date="",
        end_date="",
        comparison_start_date="",
        comparison_end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        sort={"field": "positive_sentiment", "dir": "desc"},
        include_cited_websites=False,
        limit=0,
        max_results=0,
        cursor="",
    )


def _smoke_case_67() -> None:
    report = client.reports.query_query_fanouts(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )


def _smoke_case_68() -> None:
    report = client.reports.query_query_fanouts(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        sort={"field": "", "dir": "desc"},
        limit=0,
        max_results=0,
        cursor="",
    )


def _smoke_case_69() -> None:
    web_search_result = client.reports.web_search_results.query(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_70() -> None:
    web_search_result = client.reports.web_search_results.query(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        filters=[],
    )


def _smoke_case_71() -> None:
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


def _smoke_case_72() -> None:
    stream = client.reports.web_search_results.stream(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        pagination={"limit": 10000, "offset": 0},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        filters=[],
    )

    for event in stream:
        print(event)


def _smoke_case_73() -> None:
    shopping = client.reports.shopping.brands(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )


def _smoke_case_74() -> None:
    shopping = client.reports.shopping.brands(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        scope="owned",
        assets="",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )


def _smoke_case_75() -> None:
    stream = client.reports.shopping.stream_brands(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )

    for event in stream:
        print(event)


def _smoke_case_76() -> None:
    stream = client.reports.shopping.stream_brands(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        scope="owned",
        assets="",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )

    for event in stream:
        print(event)


def _smoke_case_77() -> None:
    shopping = client.reports.shopping.products(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        include_merchants=False,
        competitor_limit=5,
    )


def _smoke_case_78() -> None:
    shopping = client.reports.shopping.products(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        include_merchants=False,
        target_product="x",
        competitor_limit=5,
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )


def _smoke_case_79() -> None:
    stream = client.reports.shopping.stream_products(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        include_merchants=False,
        competitor_limit=5,
    )

    for event in stream:
        print(event)


def _smoke_case_80() -> None:
    stream = client.reports.shopping.stream_products(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        include_merchants=False,
        target_product="x",
        competitor_limit=5,
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )

    for event in stream:
        print(event)


def _smoke_case_81() -> None:
    shopping = client.reports.shopping.merchants(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )


def _smoke_case_82() -> None:
    shopping = client.reports.shopping.merchants(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )


def _smoke_case_83() -> None:
    stream = client.reports.shopping.stream_merchants(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )

    for event in stream:
        print(event)


def _smoke_case_84() -> None:
    stream = client.reports.shopping.stream_merchants(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )

    for event in stream:
        print(event)


def _smoke_case_85() -> None:
    shopping = client.reports.shopping.trigger_rate(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )


def _smoke_case_86() -> None:
    shopping = client.reports.shopping.trigger_rate(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )


def _smoke_case_87() -> None:
    stream = client.reports.shopping.stream_trigger_rate(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )

    for event in stream:
        print(event)


def _smoke_case_88() -> None:
    stream = client.reports.shopping.stream_trigger_rate(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        metrics=[],
        interval="day",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )

    for event in stream:
        print(event)


def _smoke_case_89() -> None:
    accuracy = client.reports.accuracy.create_overview(
        start_date="",
        end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=False,
        include_no_persona=False,
        group_by="period",
    )


def _smoke_case_90() -> None:
    accuracy = client.reports.accuracy.create_overview(
        start_date="",
        end_date="",
        comparison_start_date="",
        comparison_end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        topic_ids=[],
        exclude_topic_ids=False,
        tag_ids=[],
        tag_filter_type="any",
        include_no_tag=False,
        region_ids=[],
        platform_ids=[],
        persona_ids=[],
        include_no_persona=False,
        prompt_ids=[],
        citation_categories=[],
        date_bucket="",
        group_by="period",
    )


def _smoke_case_91() -> None:
    accuracy = client.reports.accuracy.create_breakdown(
        start_date="",
        end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=False,
        include_no_persona=False,
        breakdown_by="citation",
        limit=10,
        offset=0,
        sort_by="citationShare",
        sort_order="desc",
    )


def _smoke_case_92() -> None:
    accuracy = client.reports.accuracy.create_breakdown(
        start_date="",
        end_date="",
        comparison_start_date="",
        comparison_end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        topic_ids=[],
        exclude_topic_ids=False,
        tag_ids=[],
        tag_filter_type="any",
        include_no_tag=False,
        region_ids=[],
        platform_ids=[],
        persona_ids=[],
        include_no_persona=False,
        prompt_ids=[],
        citation_categories=[],
        breakdown_by="citation",
        group_by=[],
        date_bucket="",
        limit=10,
        offset=0,
        search_query="",
        sort_by="citationShare",
        sort_order="desc",
        pagination={"dimension": "group", "metric": "accuracy", "mode": "current", "direction": "asc"},
    )


def _smoke_case_93() -> None:
    accuracy = client.reports.accuracy.create_citation_analysis(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        clean_href="",
        start_date="",
        end_date="",
    )


def _smoke_case_94() -> None:
    accuracy = client.reports.accuracy.create_topic_ids(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_95() -> None:
    accuracy = client.reports.accuracy.create_inaccurate_themes(
        start_date="",
        end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=False,
        include_no_persona=False,
        limit=10,
        offset=0,
        sort_by="response_share",
        sort_order="desc",
    )


def _smoke_case_96() -> None:
    accuracy = client.reports.accuracy.create_inaccurate_themes(
        start_date="",
        end_date="",
        comparison_start_date="",
        comparison_end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        topic_ids=[],
        exclude_topic_ids=False,
        tag_ids=[],
        tag_filter_type="any",
        include_no_tag=False,
        region_ids=[],
        platform_ids=[],
        persona_ids=[],
        include_no_persona=False,
        prompt_ids=[],
        citation_categories=[],
        limit=10,
        offset=0,
        sort_by="response_share",
        sort_order="desc",
        search_query="",
    )


def _smoke_case_97() -> None:
    accuracy = client.reports.accuracy.create_inaccurate_clusters(
        start_date="",
        end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=False,
        include_no_persona=False,
        limit=5000,
        offset=0,
        include_models=False,
    )


def _smoke_case_98() -> None:
    accuracy = client.reports.accuracy.create_inaccurate_clusters(
        start_date="",
        end_date="",
        comparison_start_date="",
        comparison_end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        topic_ids=[],
        exclude_topic_ids=False,
        tag_ids=[],
        tag_filter_type="any",
        include_no_tag=False,
        region_ids=[],
        platform_ids=[],
        persona_ids=[],
        include_no_persona=False,
        prompt_ids=[],
        citation_categories=[],
        theme_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=5000,
        offset=0,
        search_query="",
        include_models=False,
    )


def _smoke_case_99() -> None:
    accuracy = client.reports.accuracy.create_inaccuracy_drivers(
        start_date="",
        end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=False,
        include_no_persona=False,
        limit=5,
    )


def _smoke_case_100() -> None:
    accuracy = client.reports.accuracy.create_inaccuracy_drivers(
        start_date="",
        end_date="",
        comparison_start_date="",
        comparison_end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        topic_ids=[],
        exclude_topic_ids=False,
        tag_ids=[],
        tag_filter_type="any",
        include_no_tag=False,
        region_ids=[],
        platform_ids=[],
        persona_ids=[],
        include_no_persona=False,
        prompt_ids=[],
        citation_categories=[],
        limit=5,
    )


def _smoke_case_101() -> None:
    accuracy = client.reports.accuracy.create_top_inaccurate_claims(
        start_date="",
        end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=False,
        include_no_persona=False,
        limit=5,
    )


def _smoke_case_102() -> None:
    accuracy = client.reports.accuracy.create_top_inaccurate_claims(
        start_date="",
        end_date="",
        comparison_start_date="",
        comparison_end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        topic_ids=[],
        exclude_topic_ids=False,
        tag_ids=[],
        tag_filter_type="any",
        include_no_tag=False,
        region_ids=[],
        platform_ids=[],
        persona_ids=[],
        include_no_persona=False,
        prompt_ids=[],
        citation_categories=[],
        limit=5,
    )


def _smoke_case_103() -> None:
    accuracy = client.reports.accuracy.create_claim_breakdown(
        start_date="",
        end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=False,
        include_no_persona=False,
        cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_104() -> None:
    accuracy = client.reports.accuracy.create_claim_breakdown(
        start_date="",
        end_date="",
        comparison_start_date="",
        comparison_end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        topic_ids=[],
        exclude_topic_ids=False,
        tag_ids=[],
        tag_filter_type="any",
        include_no_tag=False,
        region_ids=[],
        platform_ids=[],
        persona_ids=[],
        include_no_persona=False,
        prompt_ids=[],
        citation_categories=[],
        cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_105() -> None:
    accuracy = client.reports.accuracy.create_claim_citations(
        start_date="",
        end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=False,
        include_no_persona=False,
        cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=10,
        offset=0,
        sort_order="desc",
    )


def _smoke_case_106() -> None:
    accuracy = client.reports.accuracy.create_claim_citations(
        start_date="",
        end_date="",
        comparison_start_date="",
        comparison_end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        topic_ids=[],
        exclude_topic_ids=False,
        tag_ids=[],
        tag_filter_type="any",
        include_no_tag=False,
        region_ids=[],
        platform_ids=[],
        persona_ids=[],
        include_no_persona=False,
        prompt_ids=[],
        citation_categories=[],
        cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=10,
        offset=0,
        search_query="",
        sort_order="desc",
    )


def _smoke_case_107() -> None:
    accuracy = client.reports.accuracy.create_cluster_example_runs(
        start_date="",
        end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=False,
        include_no_persona=False,
        cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=20,
        offset=0,
    )


def _smoke_case_108() -> None:
    accuracy = client.reports.accuracy.create_cluster_example_runs(
        start_date="",
        end_date="",
        comparison_start_date="",
        comparison_end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        topic_ids=[],
        exclude_topic_ids=False,
        tag_ids=[],
        tag_filter_type="any",
        include_no_tag=False,
        region_ids=[],
        platform_ids=[],
        persona_ids=[],
        include_no_persona=False,
        prompt_ids=[],
        citation_categories=[],
        cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=20,
        offset=0,
    )


def _smoke_case_109() -> None:
    accuracy = client.reports.accuracy.create_cluster_verification_pairs(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_110() -> None:
    accuracy = client.reports.accuracy.create_factcheck_setup_status(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_111() -> None:
    factcheck = client.reports.factcheck.query_scores(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_112() -> None:
    factcheck = client.reports.factcheck.query_scores(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )


def _smoke_case_113() -> None:
    stream = client.reports.factcheck.stream_scores(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )

    for event in stream:
        print(event)


def _smoke_case_114() -> None:
    stream = client.reports.factcheck.stream_scores(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        max_results=0,
        cursor="",
    )

    for event in stream:
        print(event)


def _smoke_case_115() -> None:
    claim = client.reports.factcheck.claims.query_claims(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_116() -> None:
    claim = client.reports.factcheck.claims.query_claims(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        include=[],
        limit=0,
        max_results=0,
        cursor="",
    )


def _smoke_case_117() -> None:
    stream = client.reports.factcheck.claims.stream_claims(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )

    for event in stream:
        print(event)


def _smoke_case_118() -> None:
    stream = client.reports.factcheck.claims.stream_claims(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        group_by=[],
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        include=[],
        limit=0,
        max_results=0,
        cursor="",
    )

    for event in stream:
        print(event)


def _smoke_case_119() -> None:
    youtube = client.reports.social.youtube.get_channels(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_120() -> None:
    youtube = client.reports.social.youtube.get_channels(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        cursor="",
        source_types=[],
        group_by=[],
        interval="day",
    )


def _smoke_case_121() -> None:
    youtube = client.reports.social.youtube.get_videos(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        attribution="attributed",
    )


def _smoke_case_122() -> None:
    youtube = client.reports.social.youtube.get_videos(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
        limit=0,
        cursor="",
        source_types=[],
        attribution="attributed",
    )


def _smoke_case_123() -> None:
    youtube = client.reports.social.youtube.get_summary(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_124() -> None:
    youtube = client.reports.social.youtube.get_summary(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        filter={"and_": [], "or_": [], "not_": {}, "field": "", "op": "", "value": {}},
    )


def _smoke_case_125() -> None:
    optimization = client.content.optimization.list(
        asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=10000,
        offset=0,
    )


def _smoke_case_126() -> None:
    optimization = client.content.optimization.retrieve(
        asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        content_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_127() -> None:
    agent = client.agents.list(
        limit=100,
    )


def _smoke_case_128() -> None:
    agent = client.agents.list(
        statuses=["published"],
        limit=100,
        next_cursor="next_cursor",
    )


def _smoke_case_129() -> None:
    agent = client.agents.retrieve(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_130() -> None:
    agent = client.agents.retrieve(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        version="published",
    )


def _smoke_case_131() -> None:
    agent = client.agents.create(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
    )


def _smoke_case_132() -> None:
    agent = client.agents.create(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        description="",
        graph={},
    )


def _smoke_case_133() -> None:
    agent = client.agents.publish(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_134() -> None:
    agent = client.agents.update(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        graph={},
    )


def _smoke_case_135() -> None:
    agent = client.agents.retrieve_graph(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_136() -> None:
    agent = client.agents.retrieve_graph(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        version="published",
    )


def _smoke_case_137() -> None:
    run = client.agents.runs.create(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_138() -> None:
    run = client.agents.runs.create(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        inputs={},
    )


def _smoke_case_139() -> None:
    run = client.agents.runs.retrieve(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        verbose=False,
    )


def _smoke_case_140() -> None:
    node_type = client.agents.node_types.list()


def _smoke_case_141() -> None:
    node_type = client.agents.node_types.retrieve_schema(
        node_type="nodeType",
    )


def _smoke_case_142() -> None:
    knowledge_base = client.knowledge_bases.list()


def _smoke_case_143() -> None:
    knowledge_base = client.knowledge_bases.list(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_144() -> None:
    knowledge_base = client.knowledge_bases.search(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        query="x",
        top_k=0,
        return_full_page=False,
    )


def _smoke_case_145() -> None:
    knowledge_base = client.knowledge_bases.search(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        query="x",
        top_k=0,
        return_full_page=False,
        filters={"tags": [], "folders": []},
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_146() -> None:
    document = client.knowledge_bases.documents.create(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        text="x",
    )


def _smoke_case_147() -> None:
    document = client.knowledge_bases.documents.create(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        text="x",
        folder="x",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_148() -> None:
    document = client.knowledge_bases.documents.update(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        text="x",
    )


def _smoke_case_149() -> None:
    document = client.knowledge_bases.documents.update(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        text="x",
        folder="x",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_150() -> None:
    document = client.knowledge_bases.documents.delete(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
    )


def _smoke_case_151() -> None:
    document = client.knowledge_bases.documents.delete(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_152() -> None:
    folder = client.knowledge_bases.folders.create(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        path="x",
    )


def _smoke_case_153() -> None:
    folder = client.knowledge_bases.folders.create(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        path="x",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_154() -> None:
    folder = client.knowledge_bases.folders.delete(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        path="x",
        recursive=False,
    )


def _smoke_case_155() -> None:
    folder = client.knowledge_bases.folders.delete(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        path="x",
        recursive=False,
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_156() -> None:
    project = client.projects.list(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=100,
        offset=0,
    )


def _smoke_case_157() -> None:
    project = client.projects.list(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        status="status",
        limit=100,
        offset=0,
    )


def _smoke_case_158() -> None:
    project = client.projects.create(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_159() -> None:
    project = client.projects.create(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        title="x",
        project_name="x",
        focus="x",
        topics=[],
        attachments=[],
        generation_context={
            "date_range": {"label": "x", "preset": "x"},
            "platforms": [],
            "project_categories": [],
            "regions": [],
            "tags": [],
        },
    )


def _smoke_case_160() -> None:
    project = client.projects.retrieve(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_161() -> None:
    client.projects.delete(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_162() -> None:
    project = client.projects.get_status(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_163() -> None:
    project = client.projects.archive(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_164() -> None:
    project = client.projects.archive(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        reason="x",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_165() -> None:
    project = client.projects.unarchive(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_166() -> None:
    generation = client.projects.generations.list(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=100,
        offset=0,
    )


def _smoke_case_167() -> None:
    generation = client.projects.generations.list(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        status="status",
        limit=100,
        offset=0,
    )


def _smoke_case_168() -> None:
    generation = client.projects.generations.retrieve(
        run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_169() -> None:
    task = client.projects.tasks.list(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_170() -> None:
    task = client.projects.tasks.create(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        title="x",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_171() -> None:
    task = client.projects.tasks.create(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        title="x",
        summary="x",
        brief="x",
        type="x",
        topic="x",
        impact=0,
        reference_url="x",
        reference_label="x",
        position=0,
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_172() -> None:
    task = client.projects.tasks.retrieve(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_173() -> None:
    task = client.projects.tasks.update(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_174() -> None:
    task = client.projects.tasks.update(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        title="x",
        summary="x",
        brief="x",
        type="x",
        topic="x",
        impact=0,
        reference_url="x",
        reference_label="x",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_175() -> None:
    client.projects.tasks.delete(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_176() -> None:
    task = client.projects.tasks.update_status(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        status="not_started",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_177() -> None:
    task = client.projects.tasks.update_status(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        status="not_started",
        note="x",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_178() -> None:
    integration = client.integrations.list()


def _smoke_case_179() -> None:
    integration = client.integrations.list(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        provider="provider",
        status_filter="active",
    )


def _smoke_case_180() -> None:
    document = client.documents.create(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        content_markdown="x",
    )


def _smoke_case_181() -> None:
    document = client.documents.list(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=20,
    )


def _smoke_case_182() -> None:
    document = client.documents.list(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        q="q",
        sort="sort",
        limit=20,
        next_cursor="next_cursor",
    )


def _smoke_case_183() -> None:
    document = client.documents.retrieve(
        document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        include_tabs=True,
        include_comments=True,
        preview=True,
    )


def _smoke_case_184() -> None:
    document = client.documents.update(
        document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_185() -> None:
    document = client.documents.update(
        document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        visibility="invited_only",
    )


def _smoke_case_186() -> None:
    client.documents.delete(
        document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_187() -> None:
    document = client.documents.replace_content(
        document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        content_markdown="",
        skip_title_sync=False,
    )


def _smoke_case_188() -> None:
    ad_account = client.ads.openai_ads.ad_account.retrieve_insights()


def _smoke_case_189() -> None:
    ad_account = client.ads.openai_ads.ad_account.retrieve_insights(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        aggregation_level="ad_account",
        time_granularity="hourly",
        time_ranges=["time_range"],
        limit=1,
        after="after",
        before="before",
    )


cases: list[SmokeCase] = [
    {
        "operation": "regions",
        "method": "GET",
        "path": "/v1/org/regions",
        "label": "required params",
        "run": _smoke_case_0,
    },
    {
        "operation": "regions",
        "method": "GET",
        "path": "/v1/org/regions",
        "label": "all params",
        "run": _smoke_case_1,
    },
    {
        "operation": "models",
        "method": "GET",
        "path": "/v1/org/models",
        "run": _smoke_case_2,
    },
    {
        "operation": "domains",
        "method": "GET",
        "path": "/v1/org/domains",
        "label": "required params",
        "run": _smoke_case_3,
    },
    {
        "operation": "domains",
        "method": "GET",
        "path": "/v1/org/domains",
        "label": "all params",
        "run": _smoke_case_4,
    },
    {
        "operation": "listAssets",
        "method": "GET",
        "path": "/v1/org/assets",
        "label": "required params",
        "run": _smoke_case_5,
    },
    {
        "operation": "listAssets",
        "method": "GET",
        "path": "/v1/org/assets",
        "label": "all params",
        "run": _smoke_case_6,
    },
    {
        "operation": "getPersonas",
        "method": "GET",
        "path": "/v1/org/personas",
        "label": "required params",
        "run": _smoke_case_7,
    },
    {
        "operation": "getPersonas",
        "method": "GET",
        "path": "/v1/org/personas",
        "label": "all params",
        "run": _smoke_case_8,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/org",
        "run": _smoke_case_9,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/org/categories",
        "label": "required params",
        "run": _smoke_case_10,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/org/categories",
        "label": "all params",
        "run": _smoke_case_11,
    },
    {
        "operation": "topics",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/topics",
        "run": _smoke_case_12,
    },
    {
        "operation": "tags",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/tags",
        "run": _smoke_case_13,
    },
    {
        "operation": "prompts",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/prompts",
        "label": "required params",
        "run": _smoke_case_14,
    },
    {
        "operation": "prompts",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/prompts",
        "label": "all params",
        "run": _smoke_case_15,
    },
    {
        "operation": "assets",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/assets",
        "run": _smoke_case_16,
    },
    {
        "operation": "getCategoryPersonas",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/personas",
        "run": _smoke_case_17,
    },
    {
        "operation": "createPrompts",
        "method": "POST",
        "path": "/v1/org/categories/{category_id}/prompts",
        "run": _smoke_case_18,
    },
    {
        "operation": "updatePrompts",
        "method": "PATCH",
        "path": "/v1/org/categories/{category_id}/prompts",
        "run": _smoke_case_19,
    },
    {
        "operation": "updatePromptStatus",
        "method": "PATCH",
        "path": "/v1/org/categories/{category_id}/prompts/status",
        "run": _smoke_case_20,
    },
    {
        "operation": "retrieveRegions",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/regions",
        "run": _smoke_case_21,
    },
    {
        "operation": "getCitationCategories",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/citation-categories",
        "run": _smoke_case_22,
    },
    {
        "operation": "answers",
        "method": "POST",
        "path": "/v1/prompts/answers",
        "label": "required params",
        "run": _smoke_case_23,
    },
    {
        "operation": "answers",
        "method": "POST",
        "path": "/v1/prompts/answers",
        "label": "all params",
        "run": _smoke_case_24,
    },
    {
        "operation": "answersV2",
        "method": "POST",
        "path": "/v2/prompts/answers",
        "label": "required params",
        "run": _smoke_case_25,
    },
    {
        "operation": "answersV2",
        "method": "POST",
        "path": "/v2/prompts/answers",
        "label": "all params",
        "run": _smoke_case_26,
    },
    {
        "operation": "streamAnswersV2",
        "method": "POST",
        "path": "/v2/prompts/answers/stream",
        "label": "required params",
        "run": _smoke_case_27,
    },
    {
        "operation": "streamAnswersV2",
        "method": "POST",
        "path": "/v2/prompts/answers/stream",
        "label": "all params",
        "run": _smoke_case_28,
    },
    {
        "operation": "citations",
        "method": "POST",
        "path": "/v1/reports/citations",
        "label": "required params",
        "run": _smoke_case_29,
    },
    {
        "operation": "citations",
        "method": "POST",
        "path": "/v1/reports/citations",
        "label": "all params",
        "run": _smoke_case_30,
    },
    {
        "operation": "visibility",
        "method": "POST",
        "path": "/v1/reports/visibility",
        "label": "required params",
        "run": _smoke_case_31,
    },
    {
        "operation": "visibility",
        "method": "POST",
        "path": "/v1/reports/visibility",
        "label": "all params",
        "run": _smoke_case_32,
    },
    {
        "operation": "sentiment",
        "method": "POST",
        "path": "/v1/reports/sentiment",
        "label": "required params",
        "run": _smoke_case_33,
    },
    {
        "operation": "sentiment",
        "method": "POST",
        "path": "/v1/reports/sentiment",
        "label": "all params",
        "run": _smoke_case_34,
    },
    {
        "operation": "sentimentV2",
        "method": "POST",
        "path": "/v1/reports/sentiment-v2",
        "label": "required params",
        "run": _smoke_case_35,
    },
    {
        "operation": "sentimentV2",
        "method": "POST",
        "path": "/v1/reports/sentiment-v2",
        "label": "all params",
        "run": _smoke_case_36,
    },
    {
        "operation": "getReferralsReport",
        "method": "POST",
        "path": "/v1/reports/referrals",
        "label": "required params",
        "run": _smoke_case_37,
    },
    {
        "operation": "getReferralsReport",
        "method": "POST",
        "path": "/v1/reports/referrals",
        "label": "all params",
        "run": _smoke_case_38,
    },
    {
        "operation": "getBotsReport",
        "method": "POST",
        "path": "/v1/reports/bots",
        "label": "required params",
        "run": _smoke_case_39,
    },
    {
        "operation": "getBotsReport",
        "method": "POST",
        "path": "/v1/reports/bots",
        "label": "all params",
        "run": _smoke_case_40,
    },
    {
        "operation": "queryFanouts",
        "method": "POST",
        "path": "/v1/reports/query-fanouts",
        "label": "required params",
        "run": _smoke_case_41,
    },
    {
        "operation": "queryFanouts",
        "method": "POST",
        "path": "/v1/reports/query-fanouts",
        "label": "all params",
        "run": _smoke_case_42,
    },
    {
        "operation": "streamCitations",
        "method": "POST",
        "path": "/v1/reports/citations/stream",
        "label": "required params",
        "run": _smoke_case_43,
    },
    {
        "operation": "streamCitations",
        "method": "POST",
        "path": "/v1/reports/citations/stream",
        "label": "all params",
        "run": _smoke_case_44,
    },
    {
        "operation": "streamVisibility",
        "method": "POST",
        "path": "/v1/reports/visibility/stream",
        "label": "required params",
        "run": _smoke_case_45,
    },
    {
        "operation": "streamVisibility",
        "method": "POST",
        "path": "/v1/reports/visibility/stream",
        "label": "all params",
        "run": _smoke_case_46,
    },
    {
        "operation": "streamSentiment",
        "method": "POST",
        "path": "/v1/reports/sentiment/stream",
        "label": "required params",
        "run": _smoke_case_47,
    },
    {
        "operation": "streamSentiment",
        "method": "POST",
        "path": "/v1/reports/sentiment/stream",
        "label": "all params",
        "run": _smoke_case_48,
    },
    {
        "operation": "streamCitationsV2",
        "method": "POST",
        "path": "/v2/reports/citations/stream",
        "label": "required params",
        "run": _smoke_case_49,
    },
    {
        "operation": "streamCitationsV2",
        "method": "POST",
        "path": "/v2/reports/citations/stream",
        "label": "all params",
        "run": _smoke_case_50,
    },
    {
        "operation": "streamVisibilityV2",
        "method": "POST",
        "path": "/v2/reports/visibility/stream",
        "label": "required params",
        "run": _smoke_case_51,
    },
    {
        "operation": "streamVisibilityV2",
        "method": "POST",
        "path": "/v2/reports/visibility/stream",
        "label": "all params",
        "run": _smoke_case_52,
    },
    {
        "operation": "streamSentimentV2",
        "method": "POST",
        "path": "/v2/reports/sentiment/stream",
        "label": "required params",
        "run": _smoke_case_53,
    },
    {
        "operation": "streamSentimentV2",
        "method": "POST",
        "path": "/v2/reports/sentiment/stream",
        "label": "all params",
        "run": _smoke_case_54,
    },
    {
        "operation": "streamQueryFanouts",
        "method": "POST",
        "path": "/v2/reports/query-fanouts/stream",
        "label": "required params",
        "run": _smoke_case_55,
    },
    {
        "operation": "streamQueryFanouts",
        "method": "POST",
        "path": "/v2/reports/query-fanouts/stream",
        "label": "all params",
        "run": _smoke_case_56,
    },
    {
        "operation": "getReferralsReportV2",
        "method": "POST",
        "path": "/v2/reports/referrals",
        "label": "required params",
        "run": _smoke_case_57,
    },
    {
        "operation": "getReferralsReportV2",
        "method": "POST",
        "path": "/v2/reports/referrals",
        "label": "all params",
        "run": _smoke_case_58,
    },
    {
        "operation": "getBotsReportV2",
        "method": "POST",
        "path": "/v2/reports/bots",
        "label": "required params",
        "run": _smoke_case_59,
    },
    {
        "operation": "getBotsReportV2",
        "method": "POST",
        "path": "/v2/reports/bots",
        "label": "all params",
        "run": _smoke_case_60,
    },
    {
        "operation": "queryVisibility",
        "method": "POST",
        "path": "/v2/reports/visibility",
        "label": "required params",
        "run": _smoke_case_61,
    },
    {
        "operation": "queryVisibility",
        "method": "POST",
        "path": "/v2/reports/visibility",
        "label": "all params",
        "run": _smoke_case_62,
    },
    {
        "operation": "queryCitations",
        "method": "POST",
        "path": "/v2/reports/citations",
        "label": "required params",
        "run": _smoke_case_63,
    },
    {
        "operation": "queryCitations",
        "method": "POST",
        "path": "/v2/reports/citations",
        "label": "all params",
        "run": _smoke_case_64,
    },
    {
        "operation": "querySentiment",
        "method": "POST",
        "path": "/v2/reports/sentiment",
        "label": "required params",
        "run": _smoke_case_65,
    },
    {
        "operation": "querySentiment",
        "method": "POST",
        "path": "/v2/reports/sentiment",
        "label": "all params",
        "run": _smoke_case_66,
    },
    {
        "operation": "queryQueryFanouts",
        "method": "POST",
        "path": "/v2/reports/query-fanouts",
        "label": "required params",
        "run": _smoke_case_67,
    },
    {
        "operation": "queryQueryFanouts",
        "method": "POST",
        "path": "/v2/reports/query-fanouts",
        "label": "all params",
        "run": _smoke_case_68,
    },
    {
        "operation": "query",
        "method": "POST",
        "path": "/v1/reports/web-search-results",
        "label": "required params",
        "run": _smoke_case_69,
    },
    {
        "operation": "query",
        "method": "POST",
        "path": "/v1/reports/web-search-results",
        "label": "all params",
        "run": _smoke_case_70,
    },
    {
        "operation": "stream",
        "method": "POST",
        "path": "/v1/reports/web-search-results/stream",
        "label": "required params",
        "run": _smoke_case_71,
    },
    {
        "operation": "stream",
        "method": "POST",
        "path": "/v1/reports/web-search-results/stream",
        "label": "all params",
        "run": _smoke_case_72,
    },
    {
        "operation": "brands",
        "method": "POST",
        "path": "/v2/reports/shopping/brands",
        "label": "required params",
        "run": _smoke_case_73,
    },
    {
        "operation": "brands",
        "method": "POST",
        "path": "/v2/reports/shopping/brands",
        "label": "all params",
        "run": _smoke_case_74,
    },
    {
        "operation": "streamBrands",
        "method": "POST",
        "path": "/v2/reports/shopping/brands/stream",
        "label": "required params",
        "run": _smoke_case_75,
    },
    {
        "operation": "streamBrands",
        "method": "POST",
        "path": "/v2/reports/shopping/brands/stream",
        "label": "all params",
        "run": _smoke_case_76,
    },
    {
        "operation": "products",
        "method": "POST",
        "path": "/v2/reports/shopping/products",
        "label": "required params",
        "run": _smoke_case_77,
    },
    {
        "operation": "products",
        "method": "POST",
        "path": "/v2/reports/shopping/products",
        "label": "all params",
        "run": _smoke_case_78,
    },
    {
        "operation": "streamProducts",
        "method": "POST",
        "path": "/v2/reports/shopping/products/stream",
        "label": "required params",
        "run": _smoke_case_79,
    },
    {
        "operation": "streamProducts",
        "method": "POST",
        "path": "/v2/reports/shopping/products/stream",
        "label": "all params",
        "run": _smoke_case_80,
    },
    {
        "operation": "merchants",
        "method": "POST",
        "path": "/v2/reports/shopping/merchants",
        "label": "required params",
        "run": _smoke_case_81,
    },
    {
        "operation": "merchants",
        "method": "POST",
        "path": "/v2/reports/shopping/merchants",
        "label": "all params",
        "run": _smoke_case_82,
    },
    {
        "operation": "streamMerchants",
        "method": "POST",
        "path": "/v2/reports/shopping/merchants/stream",
        "label": "required params",
        "run": _smoke_case_83,
    },
    {
        "operation": "streamMerchants",
        "method": "POST",
        "path": "/v2/reports/shopping/merchants/stream",
        "label": "all params",
        "run": _smoke_case_84,
    },
    {
        "operation": "triggerRate",
        "method": "POST",
        "path": "/v2/reports/shopping/trigger-rate",
        "label": "required params",
        "run": _smoke_case_85,
    },
    {
        "operation": "triggerRate",
        "method": "POST",
        "path": "/v2/reports/shopping/trigger-rate",
        "label": "all params",
        "run": _smoke_case_86,
    },
    {
        "operation": "streamTriggerRate",
        "method": "POST",
        "path": "/v2/reports/shopping/trigger-rate/stream",
        "label": "required params",
        "run": _smoke_case_87,
    },
    {
        "operation": "streamTriggerRate",
        "method": "POST",
        "path": "/v2/reports/shopping/trigger-rate/stream",
        "label": "all params",
        "run": _smoke_case_88,
    },
    {
        "operation": "createOverview",
        "method": "POST",
        "path": "/v1/reports/accuracy/overview",
        "label": "required params",
        "run": _smoke_case_89,
    },
    {
        "operation": "createOverview",
        "method": "POST",
        "path": "/v1/reports/accuracy/overview",
        "label": "all params",
        "run": _smoke_case_90,
    },
    {
        "operation": "createBreakdown",
        "method": "POST",
        "path": "/v1/reports/accuracy/breakdown",
        "label": "required params",
        "run": _smoke_case_91,
    },
    {
        "operation": "createBreakdown",
        "method": "POST",
        "path": "/v1/reports/accuracy/breakdown",
        "label": "all params",
        "run": _smoke_case_92,
    },
    {
        "operation": "createCitationAnalysis",
        "method": "POST",
        "path": "/v1/reports/accuracy/citation-analysis",
        "run": _smoke_case_93,
    },
    {
        "operation": "createTopicIds",
        "method": "POST",
        "path": "/v1/reports/accuracy/topic-ids",
        "run": _smoke_case_94,
    },
    {
        "operation": "createInaccurateThemes",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccurate-themes",
        "label": "required params",
        "run": _smoke_case_95,
    },
    {
        "operation": "createInaccurateThemes",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccurate-themes",
        "label": "all params",
        "run": _smoke_case_96,
    },
    {
        "operation": "createInaccurateClusters",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccurate-clusters",
        "label": "required params",
        "run": _smoke_case_97,
    },
    {
        "operation": "createInaccurateClusters",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccurate-clusters",
        "label": "all params",
        "run": _smoke_case_98,
    },
    {
        "operation": "createInaccuracyDrivers",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccuracy-drivers",
        "label": "required params",
        "run": _smoke_case_99,
    },
    {
        "operation": "createInaccuracyDrivers",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccuracy-drivers",
        "label": "all params",
        "run": _smoke_case_100,
    },
    {
        "operation": "createTopInaccurateClaims",
        "method": "POST",
        "path": "/v1/reports/accuracy/top-inaccurate-claims",
        "label": "required params",
        "run": _smoke_case_101,
    },
    {
        "operation": "createTopInaccurateClaims",
        "method": "POST",
        "path": "/v1/reports/accuracy/top-inaccurate-claims",
        "label": "all params",
        "run": _smoke_case_102,
    },
    {
        "operation": "createClaimBreakdown",
        "method": "POST",
        "path": "/v1/reports/accuracy/claim-breakdown",
        "label": "required params",
        "run": _smoke_case_103,
    },
    {
        "operation": "createClaimBreakdown",
        "method": "POST",
        "path": "/v1/reports/accuracy/claim-breakdown",
        "label": "all params",
        "run": _smoke_case_104,
    },
    {
        "operation": "createClaimCitations",
        "method": "POST",
        "path": "/v1/reports/accuracy/claim-citations",
        "label": "required params",
        "run": _smoke_case_105,
    },
    {
        "operation": "createClaimCitations",
        "method": "POST",
        "path": "/v1/reports/accuracy/claim-citations",
        "label": "all params",
        "run": _smoke_case_106,
    },
    {
        "operation": "createClusterExampleRuns",
        "method": "POST",
        "path": "/v1/reports/accuracy/cluster-example-runs",
        "label": "required params",
        "run": _smoke_case_107,
    },
    {
        "operation": "createClusterExampleRuns",
        "method": "POST",
        "path": "/v1/reports/accuracy/cluster-example-runs",
        "label": "all params",
        "run": _smoke_case_108,
    },
    {
        "operation": "createClusterVerificationPairs",
        "method": "POST",
        "path": "/v1/reports/accuracy/cluster-verification-pairs",
        "run": _smoke_case_109,
    },
    {
        "operation": "createFactcheckSetupStatus",
        "method": "POST",
        "path": "/v1/reports/accuracy/factcheck-setup-status",
        "run": _smoke_case_110,
    },
    {
        "operation": "queryScores",
        "method": "POST",
        "path": "/v2/reports/factcheck",
        "label": "required params",
        "run": _smoke_case_111,
    },
    {
        "operation": "queryScores",
        "method": "POST",
        "path": "/v2/reports/factcheck",
        "label": "all params",
        "run": _smoke_case_112,
    },
    {
        "operation": "streamScores",
        "method": "POST",
        "path": "/v2/reports/factcheck/stream",
        "label": "required params",
        "run": _smoke_case_113,
    },
    {
        "operation": "streamScores",
        "method": "POST",
        "path": "/v2/reports/factcheck/stream",
        "label": "all params",
        "run": _smoke_case_114,
    },
    {
        "operation": "queryClaims",
        "method": "POST",
        "path": "/v2/reports/factcheck/claims",
        "label": "required params",
        "run": _smoke_case_115,
    },
    {
        "operation": "queryClaims",
        "method": "POST",
        "path": "/v2/reports/factcheck/claims",
        "label": "all params",
        "run": _smoke_case_116,
    },
    {
        "operation": "streamClaims",
        "method": "POST",
        "path": "/v2/reports/factcheck/claims/stream",
        "label": "required params",
        "run": _smoke_case_117,
    },
    {
        "operation": "streamClaims",
        "method": "POST",
        "path": "/v2/reports/factcheck/claims/stream",
        "label": "all params",
        "run": _smoke_case_118,
    },
    {
        "operation": "getChannels",
        "method": "POST",
        "path": "/v2/reports/social/youtube/channels",
        "label": "required params",
        "run": _smoke_case_119,
    },
    {
        "operation": "getChannels",
        "method": "POST",
        "path": "/v2/reports/social/youtube/channels",
        "label": "all params",
        "run": _smoke_case_120,
    },
    {
        "operation": "getVideos",
        "method": "POST",
        "path": "/v2/reports/social/youtube/videos",
        "label": "required params",
        "run": _smoke_case_121,
    },
    {
        "operation": "getVideos",
        "method": "POST",
        "path": "/v2/reports/social/youtube/videos",
        "label": "all params",
        "run": _smoke_case_122,
    },
    {
        "operation": "getSummary",
        "method": "POST",
        "path": "/v2/reports/social/youtube/summary",
        "label": "required params",
        "run": _smoke_case_123,
    },
    {
        "operation": "getSummary",
        "method": "POST",
        "path": "/v2/reports/social/youtube/summary",
        "label": "all params",
        "run": _smoke_case_124,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/content/{asset_id}/optimization",
        "run": _smoke_case_125,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/content/{asset_id}/optimization/{content_id}",
        "run": _smoke_case_126,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents",
        "label": "required params",
        "run": _smoke_case_127,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents",
        "label": "all params",
        "run": _smoke_case_128,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agent_id}",
        "label": "required params",
        "run": _smoke_case_129,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agent_id}",
        "label": "all params",
        "run": _smoke_case_130,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents",
        "label": "required params",
        "run": _smoke_case_131,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents",
        "label": "all params",
        "run": _smoke_case_132,
    },
    {
        "operation": "publish",
        "method": "POST",
        "path": "/v1/agents/{agent_id}/publish",
        "run": _smoke_case_133,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/agents/{agent_id}",
        "run": _smoke_case_134,
    },
    {
        "operation": "retrieveGraph",
        "method": "GET",
        "path": "/v1/agents/{agent_id}/graph",
        "label": "required params",
        "run": _smoke_case_135,
    },
    {
        "operation": "retrieveGraph",
        "method": "GET",
        "path": "/v1/agents/{agent_id}/graph",
        "label": "all params",
        "run": _smoke_case_136,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents/{agent_id}/runs",
        "label": "required params",
        "run": _smoke_case_137,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents/{agent_id}/runs",
        "label": "all params",
        "run": _smoke_case_138,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agent_id}/runs/{run_id}",
        "run": _smoke_case_139,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents/node-types",
        "run": _smoke_case_140,
    },
    {
        "operation": "retrieveSchema",
        "method": "GET",
        "path": "/v1/agents/node-types/{node_type}/schema",
        "run": _smoke_case_141,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/knowledge-bases",
        "label": "required params",
        "run": _smoke_case_142,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/knowledge-bases",
        "label": "all params",
        "run": _smoke_case_143,
    },
    {
        "operation": "search",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/search",
        "label": "required params",
        "run": _smoke_case_144,
    },
    {
        "operation": "search",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/search",
        "label": "all params",
        "run": _smoke_case_145,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "label": "required params",
        "run": _smoke_case_146,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "label": "all params",
        "run": _smoke_case_147,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "label": "required params",
        "run": _smoke_case_148,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "label": "all params",
        "run": _smoke_case_149,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "label": "required params",
        "run": _smoke_case_150,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "label": "all params",
        "run": _smoke_case_151,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/folders",
        "label": "required params",
        "run": _smoke_case_152,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/folders",
        "label": "all params",
        "run": _smoke_case_153,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/folders",
        "label": "required params",
        "run": _smoke_case_154,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/folders",
        "label": "all params",
        "run": _smoke_case_155,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects",
        "label": "required params",
        "run": _smoke_case_156,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects",
        "label": "all params",
        "run": _smoke_case_157,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/projects",
        "label": "required params",
        "run": _smoke_case_158,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/projects",
        "label": "all params",
        "run": _smoke_case_159,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/projects/{project_id}",
        "run": _smoke_case_160,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/projects/{project_id}",
        "run": _smoke_case_161,
    },
    {
        "operation": "getStatus",
        "method": "GET",
        "path": "/v1/projects/{project_id}/status",
        "run": _smoke_case_162,
    },
    {
        "operation": "archive",
        "method": "POST",
        "path": "/v1/projects/{project_id}/archive",
        "label": "required params",
        "run": _smoke_case_163,
    },
    {
        "operation": "archive",
        "method": "POST",
        "path": "/v1/projects/{project_id}/archive",
        "label": "all params",
        "run": _smoke_case_164,
    },
    {
        "operation": "unarchive",
        "method": "POST",
        "path": "/v1/projects/{project_id}/unarchive",
        "run": _smoke_case_165,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects/generations",
        "label": "required params",
        "run": _smoke_case_166,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects/generations",
        "label": "all params",
        "run": _smoke_case_167,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/projects/generations/{run_id}",
        "run": _smoke_case_168,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects/{project_id}/tasks",
        "run": _smoke_case_169,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/projects/{project_id}/tasks",
        "label": "required params",
        "run": _smoke_case_170,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/projects/{project_id}/tasks",
        "label": "all params",
        "run": _smoke_case_171,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/projects/{project_id}/tasks/{task_id}",
        "run": _smoke_case_172,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/projects/{project_id}/tasks/{task_id}",
        "label": "required params",
        "run": _smoke_case_173,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/projects/{project_id}/tasks/{task_id}",
        "label": "all params",
        "run": _smoke_case_174,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/projects/{project_id}/tasks/{task_id}",
        "run": _smoke_case_175,
    },
    {
        "operation": "updateStatus",
        "method": "POST",
        "path": "/v1/projects/{project_id}/tasks/{task_id}/status",
        "label": "required params",
        "run": _smoke_case_176,
    },
    {
        "operation": "updateStatus",
        "method": "POST",
        "path": "/v1/projects/{project_id}/tasks/{task_id}/status",
        "label": "all params",
        "run": _smoke_case_177,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/integrations",
        "label": "required params",
        "run": _smoke_case_178,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/integrations",
        "label": "all params",
        "run": _smoke_case_179,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/documents",
        "run": _smoke_case_180,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/documents",
        "label": "required params",
        "run": _smoke_case_181,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/documents",
        "label": "all params",
        "run": _smoke_case_182,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/documents/{document_id}",
        "run": _smoke_case_183,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/documents/{document_id}",
        "label": "required params",
        "run": _smoke_case_184,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/documents/{document_id}",
        "label": "all params",
        "run": _smoke_case_185,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/documents/{document_id}",
        "run": _smoke_case_186,
    },
    {
        "operation": "replaceContent",
        "method": "POST",
        "path": "/v1/documents/{document_id}/content",
        "run": _smoke_case_187,
    },
    {
        "operation": "retrieveInsights",
        "method": "GET",
        "path": "/v1/ads/openai-ads/ad-account/insights",
        "label": "required params",
        "run": _smoke_case_188,
    },
    {
        "operation": "retrieveInsights",
        "method": "GET",
        "path": "/v1/ads/openai-ads/ad-account/insights",
        "label": "all params",
        "run": _smoke_case_189,
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


def _case_identity(case: SmokeCase) -> SmokeResult:
    # `label` is carried through only when the operation contributed both of its calls, so a
    # single-case operation reports exactly as it did before there were two.
    identity: SmokeResult = {
        "operation": case["operation"],
        "method": case["method"],
        "path": case["path"],
    }
    label = case.get("label")
    if label:
        identity["label"] = label
    return identity


def _run_case(case: SmokeCase) -> SmokeResult:
    started_at = time.monotonic()
    identity = _case_identity(case)
    try:
        case["run"]()
        return {
            **identity,
            "status": "passed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
        }
    except Exception:
        return {
            **identity,
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
            suffix = f" [{result['label']}]" if result.get("label") else ""
            if result["status"] == "passed":
                print(
                    f"PASS {result['operation']}{suffix} ({result['method']} {result['path']}) {result['durationMs']}ms"
                )
            else:
                print(
                    f"FAIL {result['operation']}{suffix} ({result['method']} {result['path']})\n{result.get('error', '')}",
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
