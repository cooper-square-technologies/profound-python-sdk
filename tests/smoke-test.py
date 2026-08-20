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
    category = client.organizations.categories.retrieve_regions(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_16() -> None:
    category = client.organizations.categories.get_citation_categories(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_17() -> None:
    prompt = client.prompts.answers(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_18() -> None:
    prompt = client.prompts.answers_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_19() -> None:
    stream = client.prompts.stream_answers_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )

    for event in stream:
        print(event)


def _smoke_case_20() -> None:
    report = client.reports.citations(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_21() -> None:
    report = client.reports.visibility(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_22() -> None:
    report = client.reports.sentiment(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_23() -> None:
    report = client.reports.sentiment_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        asset_name="",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_bucket="day",
        metrics=[],
    )


def _smoke_case_24() -> None:
    report = client.reports.get_referrals_report(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_25() -> None:
    report = client.reports.get_bots_report(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_26() -> None:
    report = client.reports.query_fanouts(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_27() -> None:
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


def _smoke_case_28() -> None:
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


def _smoke_case_29() -> None:
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


def _smoke_case_30() -> None:
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


def _smoke_case_31() -> None:
    stream = client.reports.stream_visibility_v2(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )

    for event in stream:
        print(event)


def _smoke_case_32() -> None:
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


def _smoke_case_33() -> None:
    stream = client.reports.stream_query_fanouts(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )

    for event in stream:
        print(event)


def _smoke_case_34() -> None:
    report = client.reports.get_referrals_report_v2(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
        timezone="UTC",
    )


def _smoke_case_35() -> None:
    report = client.reports.get_bots_report_v2(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
        timezone="UTC",
    )


def _smoke_case_36() -> None:
    report = client.reports.query_visibility(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )


def _smoke_case_37() -> None:
    report = client.reports.query_citations(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        entity="domain",
        interval="day",
        scope="all",
    )


def _smoke_case_38() -> None:
    report = client.reports.query_sentiment(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        asset="",
        start_date="",
        end_date="",
        interval="day",
        include_cited_websites=False,
    )


def _smoke_case_39() -> None:
    report = client.reports.query_query_fanouts(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )


def _smoke_case_40() -> None:
    web_search_result = client.reports.web_search_results.query(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_41() -> None:
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


def _smoke_case_42() -> None:
    shopping = client.reports.shopping.brands(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )


def _smoke_case_43() -> None:
    stream = client.reports.shopping.stream_brands(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )

    for event in stream:
        print(event)


def _smoke_case_44() -> None:
    shopping = client.reports.shopping.products(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        include_merchants=False,
        competitor_limit=5,
    )


def _smoke_case_45() -> None:
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


def _smoke_case_46() -> None:
    shopping = client.reports.shopping.merchants(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )


def _smoke_case_47() -> None:
    stream = client.reports.shopping.stream_merchants(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )

    for event in stream:
        print(event)


def _smoke_case_48() -> None:
    shopping = client.reports.shopping.trigger_rate(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )


def _smoke_case_49() -> None:
    stream = client.reports.shopping.stream_trigger_rate(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )

    for event in stream:
        print(event)


def _smoke_case_50() -> None:
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


def _smoke_case_51() -> None:
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


def _smoke_case_52() -> None:
    accuracy = client.reports.accuracy.create_citation_analysis(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        clean_href="",
        start_date="",
        end_date="",
    )


def _smoke_case_53() -> None:
    accuracy = client.reports.accuracy.create_topic_ids(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_54() -> None:
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


def _smoke_case_55() -> None:
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


def _smoke_case_56() -> None:
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


def _smoke_case_57() -> None:
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


def _smoke_case_58() -> None:
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


def _smoke_case_59() -> None:
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


def _smoke_case_60() -> None:
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


def _smoke_case_61() -> None:
    accuracy = client.reports.accuracy.create_cluster_verification_pairs(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_62() -> None:
    accuracy = client.reports.accuracy.create_factcheck_setup_status(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_63() -> None:
    factcheck = client.reports.factcheck.query_scores(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_64() -> None:
    stream = client.reports.factcheck.stream_scores(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )

    for event in stream:
        print(event)


def _smoke_case_65() -> None:
    claim = client.reports.factcheck.claims.query_claims(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_66() -> None:
    stream = client.reports.factcheck.claims.stream_claims(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )

    for event in stream:
        print(event)


def _smoke_case_67() -> None:
    youtube = client.reports.social.youtube.get_channels(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_68() -> None:
    youtube = client.reports.social.youtube.get_videos(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        attribution="attributed",
    )


def _smoke_case_69() -> None:
    youtube = client.reports.social.youtube.get_summary(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_70() -> None:
    optimization = client.content.optimization.list(
        asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=10000,
        offset=0,
    )


def _smoke_case_71() -> None:
    optimization = client.content.optimization.retrieve(
        asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        content_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_72() -> None:
    agent = client.agents.list(
        limit=100,
    )


def _smoke_case_73() -> None:
    agent = client.agents.retrieve(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_74() -> None:
    agent = client.agents.create(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
    )


def _smoke_case_75() -> None:
    agent = client.agents.publish(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_76() -> None:
    agent = client.agents.update(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        graph={},
    )


def _smoke_case_77() -> None:
    agent = client.agents.retrieve_graph(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_78() -> None:
    run = client.agents.runs.create(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_79() -> None:
    run = client.agents.runs.retrieve(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        verbose=False,
    )


def _smoke_case_80() -> None:
    node_type = client.agents.node_types.list()


def _smoke_case_81() -> None:
    node_type = client.agents.node_types.retrieve_schema(
        node_type="nodeType",
    )


def _smoke_case_82() -> None:
    knowledge_base = client.knowledge_bases.list()


def _smoke_case_83() -> None:
    knowledge_base = client.knowledge_bases.search(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        query="x",
        top_k=0,
        return_full_page=False,
    )


def _smoke_case_84() -> None:
    document = client.knowledge_bases.documents.create(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        text="x",
    )


def _smoke_case_85() -> None:
    document = client.knowledge_bases.documents.update(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        text="x",
    )


def _smoke_case_86() -> None:
    document = client.knowledge_bases.documents.delete(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
    )


def _smoke_case_87() -> None:
    folder = client.knowledge_bases.folders.create(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        path="x",
    )


def _smoke_case_88() -> None:
    folder = client.knowledge_bases.folders.delete(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        path="x",
        recursive=False,
    )


def _smoke_case_89() -> None:
    project = client.projects.list(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=100,
        offset=0,
    )


def _smoke_case_90() -> None:
    project = client.projects.create(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_91() -> None:
    project = client.projects.retrieve(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_92() -> None:
    client.projects.delete(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_93() -> None:
    project = client.projects.get_status(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_94() -> None:
    project = client.projects.archive(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_95() -> None:
    project = client.projects.unarchive(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_96() -> None:
    generation = client.projects.generations.list(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=100,
        offset=0,
    )


def _smoke_case_97() -> None:
    generation = client.projects.generations.retrieve(
        run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_98() -> None:
    task = client.projects.tasks.list(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_99() -> None:
    task = client.projects.tasks.create(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        title="x",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_100() -> None:
    task = client.projects.tasks.retrieve(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_101() -> None:
    task = client.projects.tasks.update(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_102() -> None:
    client.projects.tasks.delete(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_103() -> None:
    task = client.projects.tasks.update_status(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        status="not_started",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_104() -> None:
    integration = client.integrations.list()


def _smoke_case_105() -> None:
    document = client.documents.create(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        content_markdown="x",
    )


def _smoke_case_106() -> None:
    document = client.documents.list(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=20,
    )


def _smoke_case_107() -> None:
    document = client.documents.retrieve(
        document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        include_tabs=True,
        include_comments=True,
        preview=True,
    )


def _smoke_case_108() -> None:
    document = client.documents.update(
        document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_109() -> None:
    client.documents.delete(
        document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_110() -> None:
    document = client.documents.replace_content(
        document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        content_markdown="",
        skip_title_sync=False,
    )


def _smoke_case_111() -> None:
    ad_account = client.ads.openai_ads.ad_account.retrieve_insights()


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
        "operation": "retrieveRegions",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/regions",
        "run": _smoke_case_15,
    },
    {
        "operation": "getCitationCategories",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/citation-categories",
        "run": _smoke_case_16,
    },
    {
        "operation": "answers",
        "method": "POST",
        "path": "/v1/prompts/answers",
        "run": _smoke_case_17,
    },
    {
        "operation": "answersV2",
        "method": "POST",
        "path": "/v2/prompts/answers",
        "run": _smoke_case_18,
    },
    {
        "operation": "streamAnswersV2",
        "method": "POST",
        "path": "/v2/prompts/answers/stream",
        "run": _smoke_case_19,
    },
    {
        "operation": "citations",
        "method": "POST",
        "path": "/v1/reports/citations",
        "run": _smoke_case_20,
    },
    {
        "operation": "visibility",
        "method": "POST",
        "path": "/v1/reports/visibility",
        "run": _smoke_case_21,
    },
    {
        "operation": "sentiment",
        "method": "POST",
        "path": "/v1/reports/sentiment",
        "run": _smoke_case_22,
    },
    {
        "operation": "sentimentV2",
        "method": "POST",
        "path": "/v1/reports/sentiment-v2",
        "run": _smoke_case_23,
    },
    {
        "operation": "getReferralsReport",
        "method": "POST",
        "path": "/v1/reports/referrals",
        "run": _smoke_case_24,
    },
    {
        "operation": "getBotsReport",
        "method": "POST",
        "path": "/v1/reports/bots",
        "run": _smoke_case_25,
    },
    {
        "operation": "queryFanouts",
        "method": "POST",
        "path": "/v1/reports/query-fanouts",
        "run": _smoke_case_26,
    },
    {
        "operation": "streamCitations",
        "method": "POST",
        "path": "/v1/reports/citations/stream",
        "run": _smoke_case_27,
    },
    {
        "operation": "streamVisibility",
        "method": "POST",
        "path": "/v1/reports/visibility/stream",
        "run": _smoke_case_28,
    },
    {
        "operation": "streamSentiment",
        "method": "POST",
        "path": "/v1/reports/sentiment/stream",
        "run": _smoke_case_29,
    },
    {
        "operation": "streamCitationsV2",
        "method": "POST",
        "path": "/v2/reports/citations/stream",
        "run": _smoke_case_30,
    },
    {
        "operation": "streamVisibilityV2",
        "method": "POST",
        "path": "/v2/reports/visibility/stream",
        "run": _smoke_case_31,
    },
    {
        "operation": "streamSentimentV2",
        "method": "POST",
        "path": "/v2/reports/sentiment/stream",
        "run": _smoke_case_32,
    },
    {
        "operation": "streamQueryFanouts",
        "method": "POST",
        "path": "/v2/reports/query-fanouts/stream",
        "run": _smoke_case_33,
    },
    {
        "operation": "getReferralsReportV2",
        "method": "POST",
        "path": "/v2/reports/referrals",
        "run": _smoke_case_34,
    },
    {
        "operation": "getBotsReportV2",
        "method": "POST",
        "path": "/v2/reports/bots",
        "run": _smoke_case_35,
    },
    {
        "operation": "queryVisibility",
        "method": "POST",
        "path": "/v2/reports/visibility",
        "run": _smoke_case_36,
    },
    {
        "operation": "queryCitations",
        "method": "POST",
        "path": "/v2/reports/citations",
        "run": _smoke_case_37,
    },
    {
        "operation": "querySentiment",
        "method": "POST",
        "path": "/v2/reports/sentiment",
        "run": _smoke_case_38,
    },
    {
        "operation": "queryQueryFanouts",
        "method": "POST",
        "path": "/v2/reports/query-fanouts",
        "run": _smoke_case_39,
    },
    {
        "operation": "query",
        "method": "POST",
        "path": "/v1/reports/web-search-results",
        "run": _smoke_case_40,
    },
    {
        "operation": "stream",
        "method": "POST",
        "path": "/v1/reports/web-search-results/stream",
        "run": _smoke_case_41,
    },
    {
        "operation": "brands",
        "method": "POST",
        "path": "/v2/reports/shopping/brands",
        "run": _smoke_case_42,
    },
    {
        "operation": "streamBrands",
        "method": "POST",
        "path": "/v2/reports/shopping/brands/stream",
        "run": _smoke_case_43,
    },
    {
        "operation": "products",
        "method": "POST",
        "path": "/v2/reports/shopping/products",
        "run": _smoke_case_44,
    },
    {
        "operation": "streamProducts",
        "method": "POST",
        "path": "/v2/reports/shopping/products/stream",
        "run": _smoke_case_45,
    },
    {
        "operation": "merchants",
        "method": "POST",
        "path": "/v2/reports/shopping/merchants",
        "run": _smoke_case_46,
    },
    {
        "operation": "streamMerchants",
        "method": "POST",
        "path": "/v2/reports/shopping/merchants/stream",
        "run": _smoke_case_47,
    },
    {
        "operation": "triggerRate",
        "method": "POST",
        "path": "/v2/reports/shopping/trigger-rate",
        "run": _smoke_case_48,
    },
    {
        "operation": "streamTriggerRate",
        "method": "POST",
        "path": "/v2/reports/shopping/trigger-rate/stream",
        "run": _smoke_case_49,
    },
    {
        "operation": "createOverview",
        "method": "POST",
        "path": "/v1/reports/accuracy/overview",
        "run": _smoke_case_50,
    },
    {
        "operation": "createBreakdown",
        "method": "POST",
        "path": "/v1/reports/accuracy/breakdown",
        "run": _smoke_case_51,
    },
    {
        "operation": "createCitationAnalysis",
        "method": "POST",
        "path": "/v1/reports/accuracy/citation-analysis",
        "run": _smoke_case_52,
    },
    {
        "operation": "createTopicIds",
        "method": "POST",
        "path": "/v1/reports/accuracy/topic-ids",
        "run": _smoke_case_53,
    },
    {
        "operation": "createInaccurateThemes",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccurate-themes",
        "run": _smoke_case_54,
    },
    {
        "operation": "createInaccurateClusters",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccurate-clusters",
        "run": _smoke_case_55,
    },
    {
        "operation": "createInaccuracyDrivers",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccuracy-drivers",
        "run": _smoke_case_56,
    },
    {
        "operation": "createTopInaccurateClaims",
        "method": "POST",
        "path": "/v1/reports/accuracy/top-inaccurate-claims",
        "run": _smoke_case_57,
    },
    {
        "operation": "createClaimBreakdown",
        "method": "POST",
        "path": "/v1/reports/accuracy/claim-breakdown",
        "run": _smoke_case_58,
    },
    {
        "operation": "createClaimCitations",
        "method": "POST",
        "path": "/v1/reports/accuracy/claim-citations",
        "run": _smoke_case_59,
    },
    {
        "operation": "createClusterExampleRuns",
        "method": "POST",
        "path": "/v1/reports/accuracy/cluster-example-runs",
        "run": _smoke_case_60,
    },
    {
        "operation": "createClusterVerificationPairs",
        "method": "POST",
        "path": "/v1/reports/accuracy/cluster-verification-pairs",
        "run": _smoke_case_61,
    },
    {
        "operation": "createFactcheckSetupStatus",
        "method": "POST",
        "path": "/v1/reports/accuracy/factcheck-setup-status",
        "run": _smoke_case_62,
    },
    {
        "operation": "queryScores",
        "method": "POST",
        "path": "/v2/reports/factcheck",
        "run": _smoke_case_63,
    },
    {
        "operation": "streamScores",
        "method": "POST",
        "path": "/v2/reports/factcheck/stream",
        "run": _smoke_case_64,
    },
    {
        "operation": "queryClaims",
        "method": "POST",
        "path": "/v2/reports/factcheck/claims",
        "run": _smoke_case_65,
    },
    {
        "operation": "streamClaims",
        "method": "POST",
        "path": "/v2/reports/factcheck/claims/stream",
        "run": _smoke_case_66,
    },
    {
        "operation": "getChannels",
        "method": "POST",
        "path": "/v2/reports/social/youtube/channels",
        "run": _smoke_case_67,
    },
    {
        "operation": "getVideos",
        "method": "POST",
        "path": "/v2/reports/social/youtube/videos",
        "run": _smoke_case_68,
    },
    {
        "operation": "getSummary",
        "method": "POST",
        "path": "/v2/reports/social/youtube/summary",
        "run": _smoke_case_69,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/content/{asset_id}/optimization",
        "run": _smoke_case_70,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/content/{asset_id}/optimization/{content_id}",
        "run": _smoke_case_71,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents",
        "run": _smoke_case_72,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agent_id}",
        "run": _smoke_case_73,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents",
        "run": _smoke_case_74,
    },
    {
        "operation": "publish",
        "method": "POST",
        "path": "/v1/agents/{agent_id}/publish",
        "run": _smoke_case_75,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/agents/{agent_id}",
        "run": _smoke_case_76,
    },
    {
        "operation": "retrieveGraph",
        "method": "GET",
        "path": "/v1/agents/{agent_id}/graph",
        "run": _smoke_case_77,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents/{agent_id}/runs",
        "run": _smoke_case_78,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agent_id}/runs/{run_id}",
        "run": _smoke_case_79,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents/node-types",
        "run": _smoke_case_80,
    },
    {
        "operation": "retrieveSchema",
        "method": "GET",
        "path": "/v1/agents/node-types/{node_type}/schema",
        "run": _smoke_case_81,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/knowledge-bases",
        "run": _smoke_case_82,
    },
    {
        "operation": "search",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/search",
        "run": _smoke_case_83,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "run": _smoke_case_84,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "run": _smoke_case_85,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "run": _smoke_case_86,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/folders",
        "run": _smoke_case_87,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/folders",
        "run": _smoke_case_88,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects",
        "run": _smoke_case_89,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/projects",
        "run": _smoke_case_90,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/projects/{project_id}",
        "run": _smoke_case_91,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/projects/{project_id}",
        "run": _smoke_case_92,
    },
    {
        "operation": "getStatus",
        "method": "GET",
        "path": "/v1/projects/{project_id}/status",
        "run": _smoke_case_93,
    },
    {
        "operation": "archive",
        "method": "POST",
        "path": "/v1/projects/{project_id}/archive",
        "run": _smoke_case_94,
    },
    {
        "operation": "unarchive",
        "method": "POST",
        "path": "/v1/projects/{project_id}/unarchive",
        "run": _smoke_case_95,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects/generations",
        "run": _smoke_case_96,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/projects/generations/{run_id}",
        "run": _smoke_case_97,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/projects/{project_id}/tasks",
        "run": _smoke_case_98,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/projects/{project_id}/tasks",
        "run": _smoke_case_99,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/projects/{project_id}/tasks/{task_id}",
        "run": _smoke_case_100,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/projects/{project_id}/tasks/{task_id}",
        "run": _smoke_case_101,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/projects/{project_id}/tasks/{task_id}",
        "run": _smoke_case_102,
    },
    {
        "operation": "updateStatus",
        "method": "POST",
        "path": "/v1/projects/{project_id}/tasks/{task_id}/status",
        "run": _smoke_case_103,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/integrations",
        "run": _smoke_case_104,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/documents",
        "run": _smoke_case_105,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/documents",
        "run": _smoke_case_106,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/documents/{document_id}",
        "run": _smoke_case_107,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/documents/{document_id}",
        "run": _smoke_case_108,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/documents/{document_id}",
        "run": _smoke_case_109,
    },
    {
        "operation": "replaceContent",
        "method": "POST",
        "path": "/v1/documents/{document_id}/content",
        "run": _smoke_case_110,
    },
    {
        "operation": "retrieveInsights",
        "method": "GET",
        "path": "/v1/ads/openai-ads/ad-account/insights",
        "run": _smoke_case_111,
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
