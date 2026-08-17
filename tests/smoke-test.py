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
    organization = client.organization.list_category_regions_v1_org_categories_category_regions_get(
        category_id="categoryId",
    )

def _smoke_case_1() -> None:
    answer = client.prompts.answers.create_v1_prompts_post(
        category_id="",
        start_date="",
        end_date="",
    )

def _smoke_case_2() -> None:
    answer = client.prompts.answers.query_v2_v2_prompts_post(
        category_id="",
        start_date="",
        end_date="",
    )

def _smoke_case_3() -> None:
    stream = client.prompts.answers.stream_v2_v2_prompts_stream_post(
        category_id="",
        start_date="",
        end_date="",
    )
    for event in stream:
        print(event)

def _smoke_case_4() -> None:
    report = client.reports.query_sentiment_v2_v1_sentiment_v2_post(
        category_id="",
        asset_name="",
        start_date="",
        end_date="",
        date_interval="day",
        metrics=[],
    )

def _smoke_case_5() -> None:
    citation = client.reports.citations.query_v1_reports_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="",
        start_date="",
        end_date="",
    )

def _smoke_case_6() -> None:
    stream = client.reports.citations.stream_v1_reports_stream_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="",
        start_date="",
        end_date="",
    )
    for event in stream:
        print(event)

def _smoke_case_7() -> None:
    citation = client.reports.citations.query_v2_v2_reports_post(
        category_id="",
        start_date="",
        end_date="",
        interval="day",
        scope="all",
    )

def _smoke_case_8() -> None:
    stream = client.reports.citations.stream_v2_v2_reports_stream_post(
        category_id="",
        start_date="",
        end_date="",
        interval="day",
        scope="all",
    )
    for event in stream:
        print(event)

def _smoke_case_9() -> None:
    visibility = client.reports.visibility.query_v1_reports_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="",
        start_date="",
        end_date="",
    )

def _smoke_case_10() -> None:
    stream = client.reports.visibility.stream_v1_reports_stream_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="",
        start_date="",
        end_date="",
    )
    for event in stream:
        print(event)

def _smoke_case_11() -> None:
    visibility = client.reports.visibility.query_v2_v2_reports_post(
        category_id="",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )

def _smoke_case_12() -> None:
    stream = client.reports.visibility.stream_v2_v2_reports_stream_post(
        category_id="",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )
    for event in stream:
        print(event)

def _smoke_case_13() -> None:
    sentiment = client.reports.sentiment.query_v1_reports_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="",
        start_date="",
        end_date="",
    )

def _smoke_case_14() -> None:
    stream = client.reports.sentiment.stream_v1_reports_stream_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="",
        start_date="",
        end_date="",
    )
    for event in stream:
        print(event)

def _smoke_case_15() -> None:
    sentiment = client.reports.sentiment.query_v2_v2_reports_post(
        category_id="",
        asset="",
        start_date="",
        end_date="",
        interval="day",
        include_cited_websites=False,
    )

def _smoke_case_16() -> None:
    stream = client.reports.sentiment.stream_v2_v2_reports_stream_post(
        category_id="",
        asset="",
        start_date="",
        end_date="",
        interval="day",
        include_cited_websites=False,
    )
    for event in stream:
        print(event)

def _smoke_case_17() -> None:
    web_search_result = client.reports.web_search_results.query(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="",
        start_date="",
        end_date="",
    )

def _smoke_case_18() -> None:
    stream = client.reports.web_search_results.stream(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="",
        start_date="",
        end_date="",
    )
    for event in stream:
        print(event)

def _smoke_case_19() -> None:
    referral = client.reports.referrals.create_report_v1_v1_reports_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="",
    )

def _smoke_case_20() -> None:
    referral = client.reports.referrals.create_report_v2_v2_reports_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="",
    )

def _smoke_case_21() -> None:
    bot = client.reports.bots.create_report_v1_v1_reports_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="",
    )

def _smoke_case_22() -> None:
    bot = client.reports.bots.create_report_v2_v2_reports_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="",
    )

def _smoke_case_23() -> None:
    query_fanout = client.reports.query_fanouts.v1_reports_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="",
        start_date="",
        end_date="",
    )

def _smoke_case_24() -> None:
    query_fanout = client.reports.query_fanouts.v2_v2_reports_post(
        category_id="",
        start_date="",
        end_date="",
        interval="day",
    )

def _smoke_case_25() -> None:
    stream = client.reports.query_fanouts.stream_v2_v2_reports_stream_post(
        category_id="",
        start_date="",
        end_date="",
        interval="day",
    )
    for event in stream:
        print(event)

def _smoke_case_26() -> None:
    shopping = client.reports.shopping.visibility(
        category_id="",
        start_date="",
        end_date="",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
        include_asset_only=False,
        rank_by="visibility_score",
        include_position_frequency=False,
    )

def _smoke_case_27() -> None:
    shopping = client.reports.shopping.item_visibility(
        category_id="",
        start_date="",
        end_date="",
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

def _smoke_case_28() -> None:
    shopping = client.reports.shopping.merchant_distribution(
        category_id="",
        start_date="",
        end_date="",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )

def _smoke_case_29() -> None:
    shopping = client.reports.shopping.merchant_visibility_by_brand(
        category_id="",
        start_date="",
        end_date="",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
        include_brand_only=False,
    )

def _smoke_case_30() -> None:
    shopping = client.reports.shopping.merchant_by_items(
        category_id="",
        start_date="",
        end_date="",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )

def _smoke_case_31() -> None:
    shopping = client.reports.shopping.all_items_with_merchants(
        category_id="",
        start_date="",
        end_date="",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
        merchant_filter_type="any",
        rank_by="visibility",
        sort_order="desc",
    )

def _smoke_case_32() -> None:
    shopping = client.reports.shopping.trigger_rate(
        category_id="",
        start_date="",
        end_date="",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )

def _smoke_case_33() -> None:
    shopping = client.reports.shopping.merchant_share(
        category_id="",
        start_date="",
        end_date="",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )

def _smoke_case_34() -> None:
    shopping = client.reports.shopping.product_merchant_urls(
        category_id="",
        product_names=[],
        start_date="",
        end_date="",
    )

def _smoke_case_35() -> None:
    shopping = client.reports.shopping.executions(
        category_id="",
        start_date="",
        end_date="",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
        analysis_filter_type="any",
    )

def _smoke_case_36() -> None:
    accuracy = client.reports.accuracy.overview_v1_reports_overview_post(
        start_date="",
        end_date="",
        category_id="",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=True,
        include_no_persona=True,
        group_by="period",
    )

def _smoke_case_37() -> None:
    accuracy = client.reports.accuracy.breakdown_v1_reports_breakdown_post(
        start_date="",
        end_date="",
        category_id="",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=True,
        include_no_persona=True,
        breakdown_by="citation",
        limit=10,
        offset=0,
        sort_by="citationShare",
        sort_order="desc",
    )

def _smoke_case_38() -> None:
    accuracy = client.reports.accuracy.citation_analysis_v1_reports_citation_analysis_post(
        category_id="",
        clean_href="",
        start_date="",
        end_date="",
    )

def _smoke_case_39() -> None:
    accuracy = client.reports.accuracy.topic_ids_v1_reports_topic_ids_post(
        category_id="",
        start_date="",
        end_date="",
    )

def _smoke_case_40() -> None:
    accuracy = client.reports.accuracy.inaccurate_themes_v1_reports_inaccurate_themes_post(
        start_date="",
        end_date="",
        category_id="",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=True,
        include_no_persona=True,
        limit=10,
        offset=0,
        sort_by="response_share",
        sort_order="desc",
    )

def _smoke_case_41() -> None:
    accuracy = client.reports.accuracy.inaccurate_clusters_v1_reports_inaccurate_clusters_post(
        start_date="",
        end_date="",
        category_id="",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=True,
        include_no_persona=True,
        theme_id="",
        limit=5000,
        offset=0,
    )

def _smoke_case_42() -> None:
    accuracy = client.reports.accuracy.inaccuracy_drivers_v1_reports_inaccuracy_drivers_post(
        start_date="",
        end_date="",
        category_id="",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=True,
        include_no_persona=True,
        limit=5,
    )

def _smoke_case_43() -> None:
    accuracy = client.reports.accuracy.top_inaccurate_claims_v1_reports_top_inaccurate_claims_post(
        start_date="",
        end_date="",
        category_id="",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=True,
        include_no_persona=True,
        limit=5,
    )

def _smoke_case_44() -> None:
    accuracy = client.reports.accuracy.claim_breakdown_v1_reports_claim_breakdown_post(
        start_date="",
        end_date="",
        category_id="",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=True,
        include_no_persona=True,
        cluster_id="",
    )

def _smoke_case_45() -> None:
    accuracy = client.reports.accuracy.claim_citations_v1_reports_claim_citations_post(
        start_date="",
        end_date="",
        category_id="",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=True,
        include_no_persona=True,
        cluster_id="",
        limit=10,
        offset=0,
        sort_order="desc",
    )

def _smoke_case_46() -> None:
    accuracy = client.reports.accuracy.cluster_example_runs_v1_reports_cluster_example_runs_post(
        category_id="",
        cluster_id="",
        start_date="",
        end_date="",
        limit=20,
        offset=0,
    )

def _smoke_case_47() -> None:
    accuracy = client.reports.accuracy.cluster_verification_pairs_v1_reports_cluster_verification_pairs_post(
        category_id="",
        cluster_id="",
    )

def _smoke_case_48() -> None:
    accuracy = client.reports.accuracy.factcheck_setup_status_v1_reports_factcheck_setup_status_post(
        category_id="",
    )

def _smoke_case_49() -> None:
    optimization = client.content.optimization.list(
        asset_id="assetId",
        limit=10000,
        offset=0,
    )

def _smoke_case_50() -> None:
    optimization = client.content.optimization.retrieve(
        asset_id="assetId",
        content_id="contentId",
    )

def _smoke_case_51() -> None:
    knowledge_base = client.knowledge_bases.list()

def _smoke_case_52() -> None:
    knowledge_base = client.knowledge_bases.search(
        knowledge_base_id="knowledgeBaseId",
        query="",
        top_k=0,
        return_full_page=False,
    )

def _smoke_case_53() -> None:
    document = client.knowledge_bases.documents.create(
        knowledge_base_id="knowledgeBaseId",
        name="",
        text="",
    )

def _smoke_case_54() -> None:
    document = client.knowledge_bases.documents.update(
        knowledge_base_id="knowledgeBaseId",
        name="",
        text="",
    )

def _smoke_case_55() -> None:
    document = client.knowledge_bases.documents.delete(
        knowledge_base_id="knowledgeBaseId",
        name="",
    )

def _smoke_case_56() -> None:
    folder = client.knowledge_bases.folders.create(
        knowledge_base_id="knowledgeBaseId",
        path="",
    )

def _smoke_case_57() -> None:
    folder = client.knowledge_bases.folders.delete(
        knowledge_base_id="knowledgeBaseId",
        path="",
        recursive=False,
    )

def _smoke_case_58() -> None:
    agent = client.agents.list(
        limit=100,
    )

def _smoke_case_59() -> None:
    agent = client.agents.create_v1_post(
        organization_id="",
        name="",
    )

def _smoke_case_60() -> None:
    agent = client.agents.publish_v1_id_publish_post(
        agent_id="agentId",
    )

def _smoke_case_61() -> None:
    agent = client.agents.retrieve(
        agent_id="agentId",
    )

def _smoke_case_62() -> None:
    agent = client.agents.update_v1_id_patch(
        agent_id="agentId",
        graph={},
    )

def _smoke_case_63() -> None:
    agent = client.agents.list_graph_v1_graph_get(
        agent_id="agentId",
    )

def _smoke_case_64() -> None:
    node_type = client.agents.node_types.list_v1_agents_get()

def _smoke_case_65() -> None:
    node_type = client.agents.node_types.list_schema_v1_agents_schema_get(
        node_type="nodeType",
    )

def _smoke_case_66() -> None:
    run = client.agents.runs.create(
        agent_id="agentId",
    )

def _smoke_case_67() -> None:
    run = client.agents.runs.retrieve(
        agent_id="agentId",
        run_id="runId",
    )

def _smoke_case_68() -> None:
    organization = client.organizations.list()

def _smoke_case_69() -> None:
    organization = client.organizations.regions()

def _smoke_case_70() -> None:
    organization = client.organizations.models()

def _smoke_case_71() -> None:
    organization = client.organizations.domains()

def _smoke_case_72() -> None:
    organization = client.organizations.list_assets()

def _smoke_case_73() -> None:
    organization = client.organizations.get_personas()

def _smoke_case_74() -> None:
    category = client.organizations.categories.list()

def _smoke_case_75() -> None:
    category = client.organizations.categories.topics(
        category_id="categoryId",
    )

def _smoke_case_76() -> None:
    category = client.organizations.categories.tags(
        category_id="categoryId",
    )

def _smoke_case_77() -> None:
    category = client.organizations.categories.prompts(
        category_id="categoryId",
        limit=10000,
        status=["active"],
    )

def _smoke_case_78() -> None:
    category = client.organizations.categories.create_prompts(
        category_id="categoryId",
        prompts=[],
        dry_run=False,
    )

def _smoke_case_79() -> None:
    category = client.organizations.categories.update_prompts(
        category_id="categoryId",
        prompts=[],
        dry_run=False,
    )

def _smoke_case_80() -> None:
    category = client.organizations.categories.update_prompt_status(
        category_id="categoryId",
        prompt_ids=[],
        status="active",
        dry_run=False,
    )

def _smoke_case_81() -> None:
    category = client.organizations.categories.assets(
        category_id="categoryId",
    )

def _smoke_case_82() -> None:
    category = client.organizations.categories.get_category_personas(
        category_id="categoryId",
    )


cases: list[SmokeCase] = [
    {
        "operation": "listCategoryRegionsV1OrgCategoriesCategoryRegionsGet",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/regions",
        "run": _smoke_case_0,
    },

    {
        "operation": "createV1PromptsPost",
        "method": "POST",
        "path": "/v1/prompts/answers",
        "run": _smoke_case_1,
    },

    {
        "operation": "queryV2V2PromptsPost",
        "method": "POST",
        "path": "/v2/prompts/answers",
        "run": _smoke_case_2,
    },

    {
        "operation": "streamV2V2PromptsStreamPost",
        "method": "POST",
        "path": "/v2/prompts/answers/stream",
        "run": _smoke_case_3,
    },

    {
        "operation": "querySentimentV2V1SentimentV2Post",
        "method": "POST",
        "path": "/v1/reports/sentiment-v2",
        "run": _smoke_case_4,
    },

    {
        "operation": "queryV1ReportsPost",
        "method": "POST",
        "path": "/v1/reports/citations",
        "run": _smoke_case_5,
    },

    {
        "operation": "streamV1ReportsStreamPost",
        "method": "POST",
        "path": "/v1/reports/citations/stream",
        "run": _smoke_case_6,
    },

    {
        "operation": "queryV2V2ReportsPost",
        "method": "POST",
        "path": "/v2/reports/citations",
        "run": _smoke_case_7,
    },

    {
        "operation": "streamV2V2ReportsStreamPost",
        "method": "POST",
        "path": "/v2/reports/citations/stream",
        "run": _smoke_case_8,
    },

    {
        "operation": "queryV1ReportsPost",
        "method": "POST",
        "path": "/v1/reports/visibility",
        "run": _smoke_case_9,
    },

    {
        "operation": "streamV1ReportsStreamPost",
        "method": "POST",
        "path": "/v1/reports/visibility/stream",
        "run": _smoke_case_10,
    },

    {
        "operation": "queryV2V2ReportsPost",
        "method": "POST",
        "path": "/v2/reports/visibility",
        "run": _smoke_case_11,
    },

    {
        "operation": "streamV2V2ReportsStreamPost",
        "method": "POST",
        "path": "/v2/reports/visibility/stream",
        "run": _smoke_case_12,
    },

    {
        "operation": "queryV1ReportsPost",
        "method": "POST",
        "path": "/v1/reports/sentiment",
        "run": _smoke_case_13,
    },

    {
        "operation": "streamV1ReportsStreamPost",
        "method": "POST",
        "path": "/v1/reports/sentiment/stream",
        "run": _smoke_case_14,
    },

    {
        "operation": "queryV2V2ReportsPost",
        "method": "POST",
        "path": "/v2/reports/sentiment",
        "run": _smoke_case_15,
    },

    {
        "operation": "streamV2V2ReportsStreamPost",
        "method": "POST",
        "path": "/v2/reports/sentiment/stream",
        "run": _smoke_case_16,
    },

    {
        "operation": "query",
        "method": "POST",
        "path": "/v1/reports/web-search-results",
        "run": _smoke_case_17,
    },

    {
        "operation": "stream",
        "method": "POST",
        "path": "/v1/reports/web-search-results/stream",
        "run": _smoke_case_18,
    },

    {
        "operation": "createReportV1V1ReportsPost",
        "method": "POST",
        "path": "/v1/reports/referrals",
        "run": _smoke_case_19,
    },

    {
        "operation": "createReportV2V2ReportsPost",
        "method": "POST",
        "path": "/v2/reports/referrals",
        "run": _smoke_case_20,
    },

    {
        "operation": "createReportV1V1ReportsPost",
        "method": "POST",
        "path": "/v1/reports/bots",
        "run": _smoke_case_21,
    },

    {
        "operation": "createReportV2V2ReportsPost",
        "method": "POST",
        "path": "/v2/reports/bots",
        "run": _smoke_case_22,
    },

    {
        "operation": "v1ReportsPost",
        "method": "POST",
        "path": "/v1/reports/query-fanouts",
        "run": _smoke_case_23,
    },

    {
        "operation": "v2V2ReportsPost",
        "method": "POST",
        "path": "/v2/reports/query-fanouts",
        "run": _smoke_case_24,
    },

    {
        "operation": "streamV2V2ReportsStreamPost",
        "method": "POST",
        "path": "/v2/reports/query-fanouts/stream",
        "run": _smoke_case_25,
    },

    {
        "operation": "visibility",
        "method": "POST",
        "path": "/v1/reports/shopping/visibility",
        "run": _smoke_case_26,
    },

    {
        "operation": "itemVisibility",
        "method": "POST",
        "path": "/v1/reports/shopping/item-visibility",
        "run": _smoke_case_27,
    },

    {
        "operation": "merchantDistribution",
        "method": "POST",
        "path": "/v1/reports/shopping/merchant-distribution",
        "run": _smoke_case_28,
    },

    {
        "operation": "merchantVisibilityByBrand",
        "method": "POST",
        "path": "/v1/reports/shopping/merchant-visibility-by-brand",
        "run": _smoke_case_29,
    },

    {
        "operation": "merchantByItems",
        "method": "POST",
        "path": "/v1/reports/shopping/merchant-by-items",
        "run": _smoke_case_30,
    },

    {
        "operation": "allItemsWithMerchants",
        "method": "POST",
        "path": "/v1/reports/shopping/all-items-with-merchants",
        "run": _smoke_case_31,
    },

    {
        "operation": "triggerRate",
        "method": "POST",
        "path": "/v1/reports/shopping/trigger-rate",
        "run": _smoke_case_32,
    },

    {
        "operation": "merchantShare",
        "method": "POST",
        "path": "/v1/reports/shopping/merchant-share",
        "run": _smoke_case_33,
    },

    {
        "operation": "productMerchantUrls",
        "method": "POST",
        "path": "/v1/reports/shopping/product-merchant-urls",
        "run": _smoke_case_34,
    },

    {
        "operation": "executions",
        "method": "POST",
        "path": "/v1/reports/shopping/executions",
        "run": _smoke_case_35,
    },

    {
        "operation": "overviewV1ReportsOverviewPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/overview",
        "run": _smoke_case_36,
    },

    {
        "operation": "breakdownV1ReportsBreakdownPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/breakdown",
        "run": _smoke_case_37,
    },

    {
        "operation": "citationAnalysisV1ReportsCitationAnalysisPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/citation-analysis",
        "run": _smoke_case_38,
    },

    {
        "operation": "topicIdsV1ReportsTopicIdsPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/topic-ids",
        "run": _smoke_case_39,
    },

    {
        "operation": "inaccurateThemesV1ReportsInaccurateThemesPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccurate-themes",
        "run": _smoke_case_40,
    },

    {
        "operation": "inaccurateClustersV1ReportsInaccurateClustersPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccurate-clusters",
        "run": _smoke_case_41,
    },

    {
        "operation": "inaccuracyDriversV1ReportsInaccuracyDriversPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccuracy-drivers",
        "run": _smoke_case_42,
    },

    {
        "operation": "topInaccurateClaimsV1ReportsTopInaccurateClaimsPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/top-inaccurate-claims",
        "run": _smoke_case_43,
    },

    {
        "operation": "claimBreakdownV1ReportsClaimBreakdownPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/claim-breakdown",
        "run": _smoke_case_44,
    },

    {
        "operation": "claimCitationsV1ReportsClaimCitationsPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/claim-citations",
        "run": _smoke_case_45,
    },

    {
        "operation": "clusterExampleRunsV1ReportsClusterExampleRunsPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/cluster-example-runs",
        "run": _smoke_case_46,
    },

    {
        "operation": "clusterVerificationPairsV1ReportsClusterVerificationPairsPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/cluster-verification-pairs",
        "run": _smoke_case_47,
    },

    {
        "operation": "factcheckSetupStatusV1ReportsFactcheckSetupStatusPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/factcheck-setup-status",
        "run": _smoke_case_48,
    },

    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/content/{asset_id}/optimization",
        "run": _smoke_case_49,
    },

    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/content/{asset_id}/optimization/{content_id}",
        "run": _smoke_case_50,
    },

    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/knowledge-bases",
        "run": _smoke_case_51,
    },

    {
        "operation": "search",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/search",
        "run": _smoke_case_52,
    },

    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "run": _smoke_case_53,
    },

    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "run": _smoke_case_54,
    },

    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "run": _smoke_case_55,
    },

    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/folders",
        "run": _smoke_case_56,
    },

    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/folders",
        "run": _smoke_case_57,
    },

    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/agents",
        "run": _smoke_case_58,
    },

    {
        "operation": "createV1Post",
        "method": "POST",
        "path": "/v1/agents",
        "run": _smoke_case_59,
    },

    {
        "operation": "publishV1IdPublishPost",
        "method": "POST",
        "path": "/v1/agents/{agent_id}/publish",
        "run": _smoke_case_60,
    },

    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agent_id}",
        "run": _smoke_case_61,
    },

    {
        "operation": "updateV1IdPatch",
        "method": "PATCH",
        "path": "/v1/agents/{agent_id}",
        "run": _smoke_case_62,
    },

    {
        "operation": "listGraphV1GraphGet",
        "method": "GET",
        "path": "/v1/agents/{agent_id}/graph",
        "run": _smoke_case_63,
    },

    {
        "operation": "listV1AgentsGet",
        "method": "GET",
        "path": "/v1/agents/node-types",
        "run": _smoke_case_64,
    },

    {
        "operation": "listSchemaV1AgentsSchemaGet",
        "method": "GET",
        "path": "/v1/agents/node-types/{node_type}/schema",
        "run": _smoke_case_65,
    },

    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/agents/{agent_id}/runs",
        "run": _smoke_case_66,
    },

    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/agents/{agent_id}/runs/{run_id}",
        "run": _smoke_case_67,
    },

    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/org",
        "run": _smoke_case_68,
    },

    {
        "operation": "regions",
        "method": "GET",
        "path": "/v1/org/regions",
        "run": _smoke_case_69,
    },

    {
        "operation": "models",
        "method": "GET",
        "path": "/v1/org/models",
        "run": _smoke_case_70,
    },

    {
        "operation": "domains",
        "method": "GET",
        "path": "/v1/org/domains",
        "run": _smoke_case_71,
    },

    {
        "operation": "listAssets",
        "method": "GET",
        "path": "/v1/org/assets",
        "run": _smoke_case_72,
    },

    {
        "operation": "getPersonas",
        "method": "GET",
        "path": "/v1/org/personas",
        "run": _smoke_case_73,
    },

    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/org/categories",
        "run": _smoke_case_74,
    },

    {
        "operation": "topics",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/topics",
        "run": _smoke_case_75,
    },

    {
        "operation": "tags",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/tags",
        "run": _smoke_case_76,
    },

    {
        "operation": "prompts",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/prompts",
        "run": _smoke_case_77,
    },

    {
        "operation": "createPrompts",
        "method": "POST",
        "path": "/v1/org/categories/{category_id}/prompts",
        "run": _smoke_case_78,
    },

    {
        "operation": "updatePrompts",
        "method": "PATCH",
        "path": "/v1/org/categories/{category_id}/prompts",
        "run": _smoke_case_79,
    },

    {
        "operation": "updatePromptStatus",
        "method": "PATCH",
        "path": "/v1/org/categories/{category_id}/prompts/status",
        "run": _smoke_case_80,
    },

    {
        "operation": "assets",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/assets",
        "run": _smoke_case_81,
    },

    {
        "operation": "getCategoryPersonas",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/personas",
        "run": _smoke_case_82,
    },

]

DEFAULT_SMOKE_CONCURRENCY = 32


def _selected_cases() -> list[SmokeCase]:
    filter_value = os.environ.get("SCALAR_SMOKE_FILTER")
    needles = [needle.strip() for needle in filter_value.split(",") if needle.strip()] if filter_value else []
    if not needles:
        return cases
    return [
        case
        for case in cases
        if any(needle in case["operation"] or needle in case["path"] for needle in needles)
    ]


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
        Path(report_path).write_text(json.dumps({"total": len(results), "failed": len(failed), "results": results}), encoding="utf-8")
    else:
        for result in results:
            if result["status"] == "passed":
                print(f"PASS {result['operation']} ({result['method']} {result['path']}) {result['durationMs']}ms")
            else:
                print(f"FAIL {result['operation']} ({result['method']} {result['path']})\n{result.get('error', '')}", file=sys.stderr)
        if not results:
            print("No code samples ran (empty SDK or a SCALAR_SMOKE_FILTER that matched nothing).", file=sys.stderr)
        else:
            print(f"\n{len(results) - len(failed)}/{len(results)} samples passed")

    if failed or not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
