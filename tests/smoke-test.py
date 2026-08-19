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
    organization = client.organization.list_v1_org_get()


def _smoke_case_1() -> None:
    organization = client.organization.list_regions_v1_org_regions_get()


def _smoke_case_2() -> None:
    organization = client.organization.list_models_v1_org_models_get()


def _smoke_case_3() -> None:
    organization = client.organization.list_domains_v1_org_domains_get()


def _smoke_case_4() -> None:
    organization = client.organization.list_assets_v1_org_assets_get()


def _smoke_case_5() -> None:
    organization = client.organization.list_personas_v1_org_personas_get()


def _smoke_case_6() -> None:
    organization = client.organization.list_categories_v1_org_categories_get()


def _smoke_case_7() -> None:
    organization = client.organization.list_category_topics_v1_org_categories_category_topics_get(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_8() -> None:
    organization = client.organization.list_category_tags_v1_org_categories_category_tags_get(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_9() -> None:
    organization = client.organization.list_category_regions_v1_org_categories_category_regions_get(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_10() -> None:
    organization = (
        client.organization.list_category_citation_categories_v1_org_categories_category_citation_categories_get(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )
    )


def _smoke_case_11() -> None:
    organization = client.organization.list_category_citation_tags_v1_org_categories_category_citation_tags_get(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_12() -> None:
    organization = client.organization.list_category_prompts_v1_org_categories_category_prompts_get(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=10000,
        status=["active"],
    )


def _smoke_case_13() -> None:
    organization = client.organization.create_category_prompts_v1_org_categories_category_id_prompts_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        prompts=[],
        dry_run=False,
    )


def _smoke_case_14() -> None:
    organization = client.organization.update_category_prompts_v1_org_categories_category_id_prompts_patch(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        prompts=[],
        dry_run=False,
    )


def _smoke_case_15() -> None:
    organization = client.organization.update_category_prompt_status_v1_org_categories_category_id_prompts_status_patch(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        prompt_ids=[],
        status="active",
        dry_run=False,
    )


def _smoke_case_16() -> None:
    organization = client.organization.list_category_assets_v1_org_categories_category_assets_get(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_17() -> None:
    organization = client.organization.list_category_personas_v1_org_categories_category_personas_get(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_18() -> None:
    answer = client.prompts.answers.create_v1_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_19() -> None:
    answer = client.prompts.answers.query_v2_v2_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_20() -> None:
    stream = client.prompts.answers.stream_v2_v2_stream_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )

    for event in stream:
        print(event)


def _smoke_case_21() -> None:
    report = client.reports.query_sentiment_v2_v1_sentiment_v2_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        asset_name="",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_bucket="day",
        metrics=[],
    )


def _smoke_case_22() -> None:
    citation = client.reports.citations.query_v1_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_23() -> None:
    stream = client.reports.citations.stream_v1_stream_post(
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


def _smoke_case_24() -> None:
    citation = client.reports.citations.query_v2_v2_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        entity="domain",
        interval="day",
        scope="all",
    )


def _smoke_case_25() -> None:
    stream = client.reports.citations.stream_v2_v2_stream_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        entity="domain",
        interval="day",
        scope="all",
    )

    for event in stream:
        print(event)


def _smoke_case_26() -> None:
    visibility = client.reports.visibility.query_v1_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_27() -> None:
    stream = client.reports.visibility.stream_v1_stream_post(
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
    visibility = client.reports.visibility.query_v2_v2_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )


def _smoke_case_29() -> None:
    stream = client.reports.visibility.stream_v2_v2_stream_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )

    for event in stream:
        print(event)


def _smoke_case_30() -> None:
    sentiment = client.reports.sentiment.query_v1_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_31() -> None:
    stream = client.reports.sentiment.stream_v1_stream_post(
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


def _smoke_case_32() -> None:
    sentiment = client.reports.sentiment.query_v2_v2_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        asset="",
        start_date="",
        end_date="",
        interval="day",
        include_cited_websites=False,
    )


def _smoke_case_33() -> None:
    stream = client.reports.sentiment.stream_v2_v2_stream_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        asset="",
        start_date="",
        end_date="",
        interval="day",
        include_cited_websites=False,
    )

    for event in stream:
        print(event)


def _smoke_case_34() -> None:
    web_search_result = client.reports.web_search_results.query_v1_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_35() -> None:
    stream = client.reports.web_search_results.stream_v1_stream_post(
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


def _smoke_case_36() -> None:
    referral = client.reports.referrals.create_v1_v1_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_37() -> None:
    referral = client.reports.referrals.create_v2_v2_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
        timezone="UTC",
    )


def _smoke_case_38() -> None:
    bot = client.reports.bots.create_v1_v1_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_39() -> None:
    bot = client.reports.bots.create_v2_v2_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        domain="",
        start_date="2024-01-01T00:00:00.000Z",
        timezone="UTC",
    )


def _smoke_case_40() -> None:
    query_fanout = client.reports.query_fanouts.v1_post(
        date_interval="day",
        dimensions=[],
        metrics=[],
        order_by={},
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_41() -> None:
    query_fanout = client.reports.query_fanouts.v2_v2_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )


def _smoke_case_42() -> None:
    stream = client.reports.query_fanouts.stream_v2_v2_stream_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )

    for event in stream:
        print(event)


def _smoke_case_43() -> None:
    shopping = client.reports.shopping.visibility_v1_visibility_post(
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


def _smoke_case_44() -> None:
    shopping = client.reports.shopping.item_visibility_v1_item_visibility_post(
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


def _smoke_case_45() -> None:
    shopping = client.reports.shopping.merchant_distribution_v1_merchant_distribution_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )


def _smoke_case_46() -> None:
    shopping = client.reports.shopping.merchant_visibility_by_brand_v1_merchant_visibility_by_brand_post(
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


def _smoke_case_47() -> None:
    shopping = client.reports.shopping.merchant_by_items_v1_merchant_by_items_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )


def _smoke_case_48() -> None:
    shopping = client.reports.shopping.all_items_with_merchants_v1_all_items_with_merchants_post(
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


def _smoke_case_49() -> None:
    shopping = client.reports.shopping.trigger_rate_v1_trigger_rate_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )


def _smoke_case_50() -> None:
    shopping = client.reports.shopping.triggered_prompts_v1_triggered_prompts_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )


def _smoke_case_51() -> None:
    shopping = client.reports.shopping.triggered_topics_v1_triggered_topics_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )


def _smoke_case_52() -> None:
    shopping = client.reports.shopping.merchant_share_v1_merchant_share_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
        date_interval="day",
        include_count=False,
        tag_filter_type="any",
        include_no_tag=False,
        exclude_topic_ids=False,
    )


def _smoke_case_53() -> None:
    shopping = client.reports.shopping.product_merchant_urls_v1_product_merchant_urls_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        product_names=[],
        start_date="2024-01-01T00:00:00.000Z",
        end_date="2024-01-01T00:00:00.000Z",
    )


def _smoke_case_54() -> None:
    shopping = client.reports.shopping.executions_v1_executions_post(
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


def _smoke_case_55() -> None:
    shopping = client.reports.shopping.query_brands_v2_v2_brands_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )


def _smoke_case_56() -> None:
    stream = client.reports.shopping.stream_brands_v2_v2_brands_stream_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        scope="owned",
    )

    for event in stream:
        print(event)


def _smoke_case_57() -> None:
    shopping = client.reports.shopping.query_products_v2_v2_products_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        include_merchants=False,
        competitor_limit=5,
    )


def _smoke_case_58() -> None:
    stream = client.reports.shopping.stream_products_v2_v2_products_stream_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
        include_merchants=False,
        competitor_limit=5,
    )

    for event in stream:
        print(event)


def _smoke_case_59() -> None:
    shopping = client.reports.shopping.query_merchants_v2_v2_merchants_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )


def _smoke_case_60() -> None:
    stream = client.reports.shopping.stream_merchants_v2_v2_merchants_stream_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )

    for event in stream:
        print(event)


def _smoke_case_61() -> None:
    shopping = client.reports.shopping.query_trigger_rate_v2_v2_trigger_rate_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )


def _smoke_case_62() -> None:
    stream = client.reports.shopping.stream_trigger_rate_v2_v2_trigger_rate_stream_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        interval="day",
    )

    for event in stream:
        print(event)


def _smoke_case_63() -> None:
    accuracy = client.reports.accuracy.overview_v1_overview_post(
        start_date="",
        end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=False,
        include_no_persona=False,
        group_by="period",
    )


def _smoke_case_64() -> None:
    accuracy = client.reports.accuracy.breakdown_v1_breakdown_post(
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


def _smoke_case_65() -> None:
    accuracy = client.reports.accuracy.citation_analysis_v1_citation_analysis_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        clean_href="",
        start_date="",
        end_date="",
    )


def _smoke_case_66() -> None:
    accuracy = client.reports.accuracy.topic_ids_v1_topic_ids_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_67() -> None:
    accuracy = client.reports.accuracy.inaccurate_themes_v1_inaccurate_themes_post(
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


def _smoke_case_68() -> None:
    accuracy = client.reports.accuracy.inaccurate_clusters_v1_inaccurate_clusters_post(
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


def _smoke_case_69() -> None:
    accuracy = client.reports.accuracy.inaccuracy_drivers_v1_inaccuracy_drivers_post(
        start_date="",
        end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=False,
        include_no_persona=False,
        limit=5,
    )


def _smoke_case_70() -> None:
    accuracy = client.reports.accuracy.top_inaccurate_claims_v1_top_inaccurate_claims_post(
        start_date="",
        end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=False,
        include_no_persona=False,
        limit=5,
    )


def _smoke_case_71() -> None:
    accuracy = client.reports.accuracy.claim_breakdown_v1_claim_breakdown_post(
        start_date="",
        end_date="",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        exclude_topic_ids=False,
        tag_filter_type="any",
        include_no_tag=False,
        include_no_persona=False,
        cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_72() -> None:
    accuracy = client.reports.accuracy.claim_citations_v1_claim_citations_post(
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


def _smoke_case_73() -> None:
    accuracy = client.reports.accuracy.cluster_example_runs_v1_cluster_example_runs_post(
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


def _smoke_case_74() -> None:
    accuracy = client.reports.accuracy.cluster_verification_pairs_v1_cluster_verification_pairs_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_75() -> None:
    accuracy = client.reports.accuracy.factcheck_setup_status_v1_factcheck_setup_status_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_76() -> None:
    factcheck = client.reports.factcheck.query_scores_v2_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_77() -> None:
    stream = client.reports.factcheck.stream_scores_v2_stream_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )

    for event in stream:
        print(event)


def _smoke_case_78() -> None:
    factcheck = client.reports.factcheck.query_claims_v2_claims_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_79() -> None:
    stream = client.reports.factcheck.stream_claims_v2_claims_stream_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )

    for event in stream:
        print(event)


def _smoke_case_80() -> None:
    social = client.reports.social.query_youtube_channels_v2_youtube_channels_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_81() -> None:
    social = client.reports.social.query_youtube_videos_v2_youtube_videos_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
        attribution="attributed",
    )


def _smoke_case_82() -> None:
    social = client.reports.social.query_youtube_summary_v2_youtube_summary_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        start_date="",
        end_date="",
    )


def _smoke_case_83() -> None:
    optimization = client.content.optimization.list_v1_asset_id_get(
        asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=10000,
        offset=0,
    )


def _smoke_case_84() -> None:
    optimization = client.content.optimization.analysis_v1_asset_id_id_get(
        asset_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        content_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_85() -> None:
    knowledge_base = client.knowledge_bases.list_v1_get()


def _smoke_case_86() -> None:
    knowledge_base = client.knowledge_bases.search(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        query="x",
        top_k=0,
        return_full_page=False,
    )


def _smoke_case_87() -> None:
    document = client.knowledge_bases.documents.create_v1_id_post(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        text="x",
    )


def _smoke_case_88() -> None:
    document = client.knowledge_bases.documents.update_v1_id_put(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        text="x",
    )


def _smoke_case_89() -> None:
    document = client.knowledge_bases.documents.delete_v1_id_delete(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
    )


def _smoke_case_90() -> None:
    folder = client.knowledge_bases.folders.create_v1_id_post(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        path="x",
    )


def _smoke_case_91() -> None:
    folder = client.knowledge_bases.folders.delete_v1_id_delete(
        knowledge_base_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        path="x",
        recursive=False,
    )


def _smoke_case_92() -> None:
    integration = client.integrations.list_v1_get()


def _smoke_case_93() -> None:
    document = client.documents.list_v1_get(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=20,
    )


def _smoke_case_94() -> None:
    document = client.documents.create_v1_post(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
        content_markdown="x",
    )


def _smoke_case_95() -> None:
    document = client.documents.read_v1_id_get(
        document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        include_tabs=True,
        include_comments=True,
        preview=True,
    )


def _smoke_case_96() -> None:
    document = client.documents.patch_v1_id_patch(
        document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_97() -> None:
    client.documents.delete_v1_id_delete(
        document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_98() -> None:
    document = client.documents.replace_content_v1_id_content_post(
        document_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        content_markdown="",
        skip_title_sync=False,
    )


def _smoke_case_99() -> None:
    open_ai_ad = client.open_ai_ads.list_account_insights_v1_openai_account_insights_get()


def _smoke_case_100() -> None:
    project = client.projects.list_v1_get(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=100,
        offset=0,
    )


def _smoke_case_101() -> None:
    project = client.projects.create_v1_post(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_102() -> None:
    project = client.projects.retrieve_v1_get(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_103() -> None:
    client.projects.delete_v1_id_delete(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_104() -> None:
    project = client.projects.list_status_v1_status_get(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_105() -> None:
    project = client.projects.archive_v1_id_archive_post(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_106() -> None:
    project = client.projects.unarchive_v1_id_unarchive_post(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_107() -> None:
    generation = client.projects.generations.list_v1_get(
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        limit=100,
        offset=0,
    )


def _smoke_case_108() -> None:
    generation = client.projects.generations.retrieve_status_v1_run_get(
        run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_109() -> None:
    task = client.projects.tasks.list_v1_id_get(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_110() -> None:
    task = client.projects.tasks.create_v1_id_post(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        title="x",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_111() -> None:
    task = client.projects.tasks.retrieve_v1_get(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_112() -> None:
    task = client.projects.tasks.update_v1_id_id_patch(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_113() -> None:
    client.projects.tasks.delete_v1_id_id_delete(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_114() -> None:
    task = client.projects.tasks.update_status_v1_id_id_status_post(
        project_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        task_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        status="not_started",
        category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_115() -> None:
    agent = client.agents.list_v1_get(
        limit=100,
    )


def _smoke_case_116() -> None:
    agent = client.agents.create_v1_post(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="x",
    )


def _smoke_case_117() -> None:
    agent = client.agents.publish_v1_id_publish_post(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_118() -> None:
    agent = client.agents.retrieve_v1_get(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_119() -> None:
    agent = client.agents.update_v1_id_patch(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        graph={},
    )


def _smoke_case_120() -> None:
    agent = client.agents.list_graph_v1_graph_get(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_121() -> None:
    node_type = client.agents.node_types.list_v1_get()


def _smoke_case_122() -> None:
    node_type = client.agents.node_types.list_schema_v1_schema_get(
        node_type="nodeType",
    )


def _smoke_case_123() -> None:
    run = client.agents.runs.v1_id_post(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_124() -> None:
    run = client.agents.runs.retrieve_v1_get(
        agent_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        run_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        verbose=False,
    )


def _smoke_case_125() -> None:
    domain_segment = client.domain_segments.list_v2_get()


cases: list[SmokeCase] = [
    {
        "operation": "listV1OrgGet",
        "method": "GET",
        "path": "/v1/org",
        "run": _smoke_case_0,
    },
    {
        "operation": "listRegionsV1OrgRegionsGet",
        "method": "GET",
        "path": "/v1/org/regions",
        "run": _smoke_case_1,
    },
    {
        "operation": "listModelsV1OrgModelsGet",
        "method": "GET",
        "path": "/v1/org/models",
        "run": _smoke_case_2,
    },
    {
        "operation": "listDomainsV1OrgDomainsGet",
        "method": "GET",
        "path": "/v1/org/domains",
        "run": _smoke_case_3,
    },
    {
        "operation": "listAssetsV1OrgAssetsGet",
        "method": "GET",
        "path": "/v1/org/assets",
        "run": _smoke_case_4,
    },
    {
        "operation": "listPersonasV1OrgPersonasGet",
        "method": "GET",
        "path": "/v1/org/personas",
        "run": _smoke_case_5,
    },
    {
        "operation": "listCategoriesV1OrgCategoriesGet",
        "method": "GET",
        "path": "/v1/org/categories",
        "run": _smoke_case_6,
    },
    {
        "operation": "listCategoryTopicsV1OrgCategoriesCategoryTopicsGet",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/topics",
        "run": _smoke_case_7,
    },
    {
        "operation": "listCategoryTagsV1OrgCategoriesCategoryTagsGet",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/tags",
        "run": _smoke_case_8,
    },
    {
        "operation": "listCategoryRegionsV1OrgCategoriesCategoryRegionsGet",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/regions",
        "run": _smoke_case_9,
    },
    {
        "operation": "listCategoryCitationCategoriesV1OrgCategoriesCategoryCitationCategoriesGet",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/citation-categories",
        "run": _smoke_case_10,
    },
    {
        "operation": "listCategoryCitationTagsV1OrgCategoriesCategoryCitationTagsGet",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/citation-tags",
        "run": _smoke_case_11,
    },
    {
        "operation": "listCategoryPromptsV1OrgCategoriesCategoryPromptsGet",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/prompts",
        "run": _smoke_case_12,
    },
    {
        "operation": "createCategoryPromptsV1OrgCategoriesCategoryIdPromptsPost",
        "method": "POST",
        "path": "/v1/org/categories/{category_id}/prompts",
        "run": _smoke_case_13,
    },
    {
        "operation": "updateCategoryPromptsV1OrgCategoriesCategoryIdPromptsPatch",
        "method": "PATCH",
        "path": "/v1/org/categories/{category_id}/prompts",
        "run": _smoke_case_14,
    },
    {
        "operation": "updateCategoryPromptStatusV1OrgCategoriesCategoryIdPromptsStatusPatch",
        "method": "PATCH",
        "path": "/v1/org/categories/{category_id}/prompts/status",
        "run": _smoke_case_15,
    },
    {
        "operation": "listCategoryAssetsV1OrgCategoriesCategoryAssetsGet",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/assets",
        "run": _smoke_case_16,
    },
    {
        "operation": "listCategoryPersonasV1OrgCategoriesCategoryPersonasGet",
        "method": "GET",
        "path": "/v1/org/categories/{category_id}/personas",
        "run": _smoke_case_17,
    },
    {
        "operation": "createV1Post",
        "method": "POST",
        "path": "/v1/prompts/answers",
        "run": _smoke_case_18,
    },
    {
        "operation": "queryV2V2Post",
        "method": "POST",
        "path": "/v2/prompts/answers",
        "run": _smoke_case_19,
    },
    {
        "operation": "streamV2V2StreamPost",
        "method": "POST",
        "path": "/v2/prompts/answers/stream",
        "run": _smoke_case_20,
    },
    {
        "operation": "querySentimentV2V1SentimentV2Post",
        "method": "POST",
        "path": "/v1/reports/sentiment-v2",
        "run": _smoke_case_21,
    },
    {
        "operation": "queryV1Post",
        "method": "POST",
        "path": "/v1/reports/citations",
        "run": _smoke_case_22,
    },
    {
        "operation": "streamV1StreamPost",
        "method": "POST",
        "path": "/v1/reports/citations/stream",
        "run": _smoke_case_23,
    },
    {
        "operation": "queryV2V2Post",
        "method": "POST",
        "path": "/v2/reports/citations",
        "run": _smoke_case_24,
    },
    {
        "operation": "streamV2V2StreamPost",
        "method": "POST",
        "path": "/v2/reports/citations/stream",
        "run": _smoke_case_25,
    },
    {
        "operation": "queryV1Post",
        "method": "POST",
        "path": "/v1/reports/visibility",
        "run": _smoke_case_26,
    },
    {
        "operation": "streamV1StreamPost",
        "method": "POST",
        "path": "/v1/reports/visibility/stream",
        "run": _smoke_case_27,
    },
    {
        "operation": "queryV2V2Post",
        "method": "POST",
        "path": "/v2/reports/visibility",
        "run": _smoke_case_28,
    },
    {
        "operation": "streamV2V2StreamPost",
        "method": "POST",
        "path": "/v2/reports/visibility/stream",
        "run": _smoke_case_29,
    },
    {
        "operation": "queryV1Post",
        "method": "POST",
        "path": "/v1/reports/sentiment",
        "run": _smoke_case_30,
    },
    {
        "operation": "streamV1StreamPost",
        "method": "POST",
        "path": "/v1/reports/sentiment/stream",
        "run": _smoke_case_31,
    },
    {
        "operation": "queryV2V2Post",
        "method": "POST",
        "path": "/v2/reports/sentiment",
        "run": _smoke_case_32,
    },
    {
        "operation": "streamV2V2StreamPost",
        "method": "POST",
        "path": "/v2/reports/sentiment/stream",
        "run": _smoke_case_33,
    },
    {
        "operation": "queryV1Post",
        "method": "POST",
        "path": "/v1/reports/web-search-results",
        "run": _smoke_case_34,
    },
    {
        "operation": "streamV1StreamPost",
        "method": "POST",
        "path": "/v1/reports/web-search-results/stream",
        "run": _smoke_case_35,
    },
    {
        "operation": "createV1V1Post",
        "method": "POST",
        "path": "/v1/reports/referrals",
        "run": _smoke_case_36,
    },
    {
        "operation": "createV2V2Post",
        "method": "POST",
        "path": "/v2/reports/referrals",
        "run": _smoke_case_37,
    },
    {
        "operation": "createV1V1Post",
        "method": "POST",
        "path": "/v1/reports/bots",
        "run": _smoke_case_38,
    },
    {
        "operation": "createV2V2Post",
        "method": "POST",
        "path": "/v2/reports/bots",
        "run": _smoke_case_39,
    },
    {
        "operation": "v1Post",
        "method": "POST",
        "path": "/v1/reports/query-fanouts",
        "run": _smoke_case_40,
    },
    {
        "operation": "v2V2Post",
        "method": "POST",
        "path": "/v2/reports/query-fanouts",
        "run": _smoke_case_41,
    },
    {
        "operation": "streamV2V2StreamPost",
        "method": "POST",
        "path": "/v2/reports/query-fanouts/stream",
        "run": _smoke_case_42,
    },
    {
        "operation": "visibilityV1VisibilityPost",
        "method": "POST",
        "path": "/v1/reports/shopping/visibility",
        "run": _smoke_case_43,
    },
    {
        "operation": "itemVisibilityV1ItemVisibilityPost",
        "method": "POST",
        "path": "/v1/reports/shopping/item-visibility",
        "run": _smoke_case_44,
    },
    {
        "operation": "merchantDistributionV1MerchantDistributionPost",
        "method": "POST",
        "path": "/v1/reports/shopping/merchant-distribution",
        "run": _smoke_case_45,
    },
    {
        "operation": "merchantVisibilityByBrandV1MerchantVisibilityByBrandPost",
        "method": "POST",
        "path": "/v1/reports/shopping/merchant-visibility-by-brand",
        "run": _smoke_case_46,
    },
    {
        "operation": "merchantByItemsV1MerchantByItemsPost",
        "method": "POST",
        "path": "/v1/reports/shopping/merchant-by-items",
        "run": _smoke_case_47,
    },
    {
        "operation": "allItemsWithMerchantsV1AllItemsWithMerchantsPost",
        "method": "POST",
        "path": "/v1/reports/shopping/all-items-with-merchants",
        "run": _smoke_case_48,
    },
    {
        "operation": "triggerRateV1TriggerRatePost",
        "method": "POST",
        "path": "/v1/reports/shopping/trigger-rate",
        "run": _smoke_case_49,
    },
    {
        "operation": "triggeredPromptsV1TriggeredPromptsPost",
        "method": "POST",
        "path": "/v1/reports/shopping/triggered-prompts",
        "run": _smoke_case_50,
    },
    {
        "operation": "triggeredTopicsV1TriggeredTopicsPost",
        "method": "POST",
        "path": "/v1/reports/shopping/triggered-topics",
        "run": _smoke_case_51,
    },
    {
        "operation": "merchantShareV1MerchantSharePost",
        "method": "POST",
        "path": "/v1/reports/shopping/merchant-share",
        "run": _smoke_case_52,
    },
    {
        "operation": "productMerchantUrlsV1ProductMerchantUrlsPost",
        "method": "POST",
        "path": "/v1/reports/shopping/product-merchant-urls",
        "run": _smoke_case_53,
    },
    {
        "operation": "executionsV1ExecutionsPost",
        "method": "POST",
        "path": "/v1/reports/shopping/executions",
        "run": _smoke_case_54,
    },
    {
        "operation": "queryBrandsV2V2BrandsPost",
        "method": "POST",
        "path": "/v2/reports/shopping/brands",
        "run": _smoke_case_55,
    },
    {
        "operation": "streamBrandsV2V2BrandsStreamPost",
        "method": "POST",
        "path": "/v2/reports/shopping/brands/stream",
        "run": _smoke_case_56,
    },
    {
        "operation": "queryProductsV2V2ProductsPost",
        "method": "POST",
        "path": "/v2/reports/shopping/products",
        "run": _smoke_case_57,
    },
    {
        "operation": "streamProductsV2V2ProductsStreamPost",
        "method": "POST",
        "path": "/v2/reports/shopping/products/stream",
        "run": _smoke_case_58,
    },
    {
        "operation": "queryMerchantsV2V2MerchantsPost",
        "method": "POST",
        "path": "/v2/reports/shopping/merchants",
        "run": _smoke_case_59,
    },
    {
        "operation": "streamMerchantsV2V2MerchantsStreamPost",
        "method": "POST",
        "path": "/v2/reports/shopping/merchants/stream",
        "run": _smoke_case_60,
    },
    {
        "operation": "queryTriggerRateV2V2TriggerRatePost",
        "method": "POST",
        "path": "/v2/reports/shopping/trigger-rate",
        "run": _smoke_case_61,
    },
    {
        "operation": "streamTriggerRateV2V2TriggerRateStreamPost",
        "method": "POST",
        "path": "/v2/reports/shopping/trigger-rate/stream",
        "run": _smoke_case_62,
    },
    {
        "operation": "overviewV1OverviewPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/overview",
        "run": _smoke_case_63,
    },
    {
        "operation": "breakdownV1BreakdownPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/breakdown",
        "run": _smoke_case_64,
    },
    {
        "operation": "citationAnalysisV1CitationAnalysisPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/citation-analysis",
        "run": _smoke_case_65,
    },
    {
        "operation": "topicIdsV1TopicIdsPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/topic-ids",
        "run": _smoke_case_66,
    },
    {
        "operation": "inaccurateThemesV1InaccurateThemesPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccurate-themes",
        "run": _smoke_case_67,
    },
    {
        "operation": "inaccurateClustersV1InaccurateClustersPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccurate-clusters",
        "run": _smoke_case_68,
    },
    {
        "operation": "inaccuracyDriversV1InaccuracyDriversPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/inaccuracy-drivers",
        "run": _smoke_case_69,
    },
    {
        "operation": "topInaccurateClaimsV1TopInaccurateClaimsPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/top-inaccurate-claims",
        "run": _smoke_case_70,
    },
    {
        "operation": "claimBreakdownV1ClaimBreakdownPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/claim-breakdown",
        "run": _smoke_case_71,
    },
    {
        "operation": "claimCitationsV1ClaimCitationsPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/claim-citations",
        "run": _smoke_case_72,
    },
    {
        "operation": "clusterExampleRunsV1ClusterExampleRunsPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/cluster-example-runs",
        "run": _smoke_case_73,
    },
    {
        "operation": "clusterVerificationPairsV1ClusterVerificationPairsPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/cluster-verification-pairs",
        "run": _smoke_case_74,
    },
    {
        "operation": "factcheckSetupStatusV1FactcheckSetupStatusPost",
        "method": "POST",
        "path": "/v1/reports/accuracy/factcheck-setup-status",
        "run": _smoke_case_75,
    },
    {
        "operation": "queryScoresV2Post",
        "method": "POST",
        "path": "/v2/reports/factcheck",
        "run": _smoke_case_76,
    },
    {
        "operation": "streamScoresV2StreamPost",
        "method": "POST",
        "path": "/v2/reports/factcheck/stream",
        "run": _smoke_case_77,
    },
    {
        "operation": "queryClaimsV2ClaimsPost",
        "method": "POST",
        "path": "/v2/reports/factcheck/claims",
        "run": _smoke_case_78,
    },
    {
        "operation": "streamClaimsV2ClaimsStreamPost",
        "method": "POST",
        "path": "/v2/reports/factcheck/claims/stream",
        "run": _smoke_case_79,
    },
    {
        "operation": "queryYoutubeChannelsV2YoutubeChannelsPost",
        "method": "POST",
        "path": "/v2/reports/social/youtube/channels",
        "run": _smoke_case_80,
    },
    {
        "operation": "queryYoutubeVideosV2YoutubeVideosPost",
        "method": "POST",
        "path": "/v2/reports/social/youtube/videos",
        "run": _smoke_case_81,
    },
    {
        "operation": "queryYoutubeSummaryV2YoutubeSummaryPost",
        "method": "POST",
        "path": "/v2/reports/social/youtube/summary",
        "run": _smoke_case_82,
    },
    {
        "operation": "listV1AssetIdGet",
        "method": "GET",
        "path": "/v1/content/{asset_id}/optimization",
        "run": _smoke_case_83,
    },
    {
        "operation": "analysisV1AssetIdIdGet",
        "method": "GET",
        "path": "/v1/content/{asset_id}/optimization/{content_id}",
        "run": _smoke_case_84,
    },
    {
        "operation": "listV1Get",
        "method": "GET",
        "path": "/v1/knowledge-bases",
        "run": _smoke_case_85,
    },
    {
        "operation": "search",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/search",
        "run": _smoke_case_86,
    },
    {
        "operation": "createV1IdPost",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "run": _smoke_case_87,
    },
    {
        "operation": "updateV1IdPut",
        "method": "PUT",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "run": _smoke_case_88,
    },
    {
        "operation": "deleteV1IdDelete",
        "method": "DELETE",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/documents",
        "run": _smoke_case_89,
    },
    {
        "operation": "createV1IdPost",
        "method": "POST",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/folders",
        "run": _smoke_case_90,
    },
    {
        "operation": "deleteV1IdDelete",
        "method": "DELETE",
        "path": "/v1/knowledge-bases/{knowledge_base_id}/folders",
        "run": _smoke_case_91,
    },
    {
        "operation": "listV1Get",
        "method": "GET",
        "path": "/v1/integrations",
        "run": _smoke_case_92,
    },
    {
        "operation": "listV1Get",
        "method": "GET",
        "path": "/v1/documents",
        "run": _smoke_case_93,
    },
    {
        "operation": "createV1Post",
        "method": "POST",
        "path": "/v1/documents",
        "run": _smoke_case_94,
    },
    {
        "operation": "readV1IdGet",
        "method": "GET",
        "path": "/v1/documents/{document_id}",
        "run": _smoke_case_95,
    },
    {
        "operation": "patchV1IdPatch",
        "method": "PATCH",
        "path": "/v1/documents/{document_id}",
        "run": _smoke_case_96,
    },
    {
        "operation": "deleteV1IdDelete",
        "method": "DELETE",
        "path": "/v1/documents/{document_id}",
        "run": _smoke_case_97,
    },
    {
        "operation": "replaceContentV1IdContentPost",
        "method": "POST",
        "path": "/v1/documents/{document_id}/content",
        "run": _smoke_case_98,
    },
    {
        "operation": "listAccountInsightsV1OpenaiAccountInsightsGet",
        "method": "GET",
        "path": "/v1/ads/openai-ads/ad-account/insights",
        "run": _smoke_case_99,
    },
    {
        "operation": "listV1Get",
        "method": "GET",
        "path": "/v1/projects",
        "run": _smoke_case_100,
    },
    {
        "operation": "createV1Post",
        "method": "POST",
        "path": "/v1/projects",
        "run": _smoke_case_101,
    },
    {
        "operation": "retrieveV1Get",
        "method": "GET",
        "path": "/v1/projects/{project_id}",
        "run": _smoke_case_102,
    },
    {
        "operation": "deleteV1IdDelete",
        "method": "DELETE",
        "path": "/v1/projects/{project_id}",
        "run": _smoke_case_103,
    },
    {
        "operation": "listStatusV1StatusGet",
        "method": "GET",
        "path": "/v1/projects/{project_id}/status",
        "run": _smoke_case_104,
    },
    {
        "operation": "archiveV1IdArchivePost",
        "method": "POST",
        "path": "/v1/projects/{project_id}/archive",
        "run": _smoke_case_105,
    },
    {
        "operation": "unarchiveV1IdUnarchivePost",
        "method": "POST",
        "path": "/v1/projects/{project_id}/unarchive",
        "run": _smoke_case_106,
    },
    {
        "operation": "listV1Get",
        "method": "GET",
        "path": "/v1/projects/generations",
        "run": _smoke_case_107,
    },
    {
        "operation": "retrieveStatusV1RunGet",
        "method": "GET",
        "path": "/v1/projects/generations/{run_id}",
        "run": _smoke_case_108,
    },
    {
        "operation": "listV1IdGet",
        "method": "GET",
        "path": "/v1/projects/{project_id}/tasks",
        "run": _smoke_case_109,
    },
    {
        "operation": "createV1IdPost",
        "method": "POST",
        "path": "/v1/projects/{project_id}/tasks",
        "run": _smoke_case_110,
    },
    {
        "operation": "retrieveV1Get",
        "method": "GET",
        "path": "/v1/projects/{project_id}/tasks/{task_id}",
        "run": _smoke_case_111,
    },
    {
        "operation": "updateV1IdIdPatch",
        "method": "PATCH",
        "path": "/v1/projects/{project_id}/tasks/{task_id}",
        "run": _smoke_case_112,
    },
    {
        "operation": "deleteV1IdIdDelete",
        "method": "DELETE",
        "path": "/v1/projects/{project_id}/tasks/{task_id}",
        "run": _smoke_case_113,
    },
    {
        "operation": "updateStatusV1IdIdStatusPost",
        "method": "POST",
        "path": "/v1/projects/{project_id}/tasks/{task_id}/status",
        "run": _smoke_case_114,
    },
    {
        "operation": "listV1Get",
        "method": "GET",
        "path": "/v1/agents",
        "run": _smoke_case_115,
    },
    {
        "operation": "createV1Post",
        "method": "POST",
        "path": "/v1/agents",
        "run": _smoke_case_116,
    },
    {
        "operation": "publishV1IdPublishPost",
        "method": "POST",
        "path": "/v1/agents/{agent_id}/publish",
        "run": _smoke_case_117,
    },
    {
        "operation": "retrieveV1Get",
        "method": "GET",
        "path": "/v1/agents/{agent_id}",
        "run": _smoke_case_118,
    },
    {
        "operation": "updateV1IdPatch",
        "method": "PATCH",
        "path": "/v1/agents/{agent_id}",
        "run": _smoke_case_119,
    },
    {
        "operation": "listGraphV1GraphGet",
        "method": "GET",
        "path": "/v1/agents/{agent_id}/graph",
        "run": _smoke_case_120,
    },
    {
        "operation": "listV1Get",
        "method": "GET",
        "path": "/v1/agents/node-types",
        "run": _smoke_case_121,
    },
    {
        "operation": "listSchemaV1SchemaGet",
        "method": "GET",
        "path": "/v1/agents/node-types/{node_type}/schema",
        "run": _smoke_case_122,
    },
    {
        "operation": "v1IdPost",
        "method": "POST",
        "path": "/v1/agents/{agent_id}/runs",
        "run": _smoke_case_123,
    },
    {
        "operation": "retrieveV1Get",
        "method": "GET",
        "path": "/v1/agents/{agent_id}/runs/{run_id}",
        "run": _smoke_case_124,
    },
    {
        "operation": "listV2Get",
        "method": "GET",
        "path": "/v2/domain-segments",
        "run": _smoke_case_125,
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
