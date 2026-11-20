# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestAccuracy:
    @smoke_case(
        "reports.accuracy.createOverview:required", operation="createOverview", path="/v1/reports/accuracy/overview"
    )
    def test_method_create_overview(self) -> None:
        accuracy = client.reports.accuracy.create_overview(
            citation_category_taxonomy="legacy",
            start_date="",
            end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            exclude_topic_ids=False,
            tag_filter_type="any",
            include_no_tag=True,
            include_no_persona=True,
            group_by="period",
        )

    @smoke_case("reports.accuracy.createOverview:all", operation="createOverview", path="/v1/reports/accuracy/overview")
    def test_method_create_overview_with_all_params(self) -> None:
        accuracy = client.reports.accuracy.create_overview(
            citation_categories=[""],
            citation_category_taxonomy="legacy",
            citation_category_pairs=[[{}, {}]],
            start_date="",
            end_date="",
            comparison_start_date="",
            comparison_end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            languages=[""],
            topic_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            exclude_topic_ids=False,
            tag_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            tag_filter_type="any",
            include_no_tag=True,
            region_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            platform_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            persona_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            include_no_persona=True,
            prompt_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            date_bucket="",
            group_by="period",
        )

    @smoke_case(
        "reports.accuracy.createBreakdown:required", operation="createBreakdown", path="/v1/reports/accuracy/breakdown"
    )
    def test_method_create_breakdown(self) -> None:
        accuracy = client.reports.accuracy.create_breakdown(
            citation_category_taxonomy="legacy",
            start_date="",
            end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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

    @smoke_case(
        "reports.accuracy.createBreakdown:all", operation="createBreakdown", path="/v1/reports/accuracy/breakdown"
    )
    def test_method_create_breakdown_with_all_params(self) -> None:
        accuracy = client.reports.accuracy.create_breakdown(
            citation_categories=[""],
            citation_category_taxonomy="legacy",
            citation_category_pairs=[[{}, {}]],
            start_date="",
            end_date="",
            comparison_start_date="",
            comparison_end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            languages=[""],
            topic_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            exclude_topic_ids=False,
            tag_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            tag_filter_type="any",
            include_no_tag=True,
            region_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            platform_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            persona_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            include_no_persona=True,
            prompt_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            breakdown_by="citation",
            group_by=["platform"],
            date_bucket="",
            limit=10,
            offset=0,
            search_query="",
            sort_by="citationShare",
            sort_order="desc",
            pagination={"dimension": "group", "metric": "accuracy", "mode": "current", "direction": "asc"},
        )

    @smoke_case(
        "reports.accuracy.createCitationAnalysis:single",
        operation="createCitationAnalysis",
        path="/v1/reports/accuracy/citation-analysis",
    )
    def test_method_create_citation_analysis(self) -> None:
        accuracy = client.reports.accuracy.create_citation_analysis(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            clean_href="x",
            start_date="",
            end_date="",
        )

    @smoke_case(
        "reports.accuracy.createTopicIds:single", operation="createTopicIds", path="/v1/reports/accuracy/topic-ids"
    )
    def test_method_create_topic_ids(self) -> None:
        accuracy = client.reports.accuracy.create_topic_ids(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            start_date="",
            end_date="",
        )

    @smoke_case(
        "reports.accuracy.createInaccurateThemes:required",
        operation="createInaccurateThemes",
        path="/v1/reports/accuracy/inaccurate-themes",
    )
    def test_method_create_inaccurate_themes(self) -> None:
        accuracy = client.reports.accuracy.create_inaccurate_themes(
            citation_category_taxonomy="legacy",
            start_date="",
            end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            exclude_topic_ids=False,
            tag_filter_type="any",
            include_no_tag=True,
            include_no_persona=True,
            verification_status="inaccurate",
            limit=10,
            offset=0,
            sort_by="response_share",
            sort_order="desc",
        )

    @smoke_case(
        "reports.accuracy.createInaccurateThemes:all",
        operation="createInaccurateThemes",
        path="/v1/reports/accuracy/inaccurate-themes",
    )
    def test_method_create_inaccurate_themes_with_all_params(self) -> None:
        accuracy = client.reports.accuracy.create_inaccurate_themes(
            citation_categories=[""],
            citation_category_taxonomy="legacy",
            citation_category_pairs=[[{}, {}]],
            start_date="",
            end_date="",
            comparison_start_date="",
            comparison_end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            languages=[""],
            topic_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            exclude_topic_ids=False,
            tag_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            tag_filter_type="any",
            include_no_tag=True,
            region_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            platform_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            persona_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            include_no_persona=True,
            prompt_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            verification_status="inaccurate",
            limit=10,
            offset=0,
            sort_by="response_share",
            sort_order="desc",
            search_query="",
        )

    @smoke_case(
        "reports.accuracy.createInaccurateClusters:required",
        operation="createInaccurateClusters",
        path="/v1/reports/accuracy/inaccurate-clusters",
    )
    def test_method_create_inaccurate_clusters(self) -> None:
        accuracy = client.reports.accuracy.create_inaccurate_clusters(
            citation_category_taxonomy="legacy",
            start_date="",
            end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            exclude_topic_ids=False,
            tag_filter_type="any",
            include_no_tag=True,
            include_no_persona=True,
            verification_status="inaccurate",
            limit=5000,
            offset=0,
            include_models=False,
            include_citations=True,
            include_citation_hostnames=True,
        )

    @smoke_case(
        "reports.accuracy.createInaccurateClusters:all",
        operation="createInaccurateClusters",
        path="/v1/reports/accuracy/inaccurate-clusters",
    )
    def test_method_create_inaccurate_clusters_with_all_params(self) -> None:
        accuracy = client.reports.accuracy.create_inaccurate_clusters(
            citation_categories=[""],
            citation_category_taxonomy="legacy",
            citation_category_pairs=[[{}, {}]],
            start_date="",
            end_date="",
            comparison_start_date="",
            comparison_end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            languages=[""],
            topic_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            exclude_topic_ids=False,
            tag_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            tag_filter_type="any",
            include_no_tag=True,
            region_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            platform_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            persona_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            include_no_persona=True,
            prompt_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            verification_status="inaccurate",
            theme_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            limit=5000,
            offset=0,
            search_query="",
            include_models=False,
            include_citations=True,
            include_citation_hostnames=True,
        )

    @smoke_case(
        "reports.accuracy.createInaccuracyDrivers:required",
        operation="createInaccuracyDrivers",
        path="/v1/reports/accuracy/inaccuracy-drivers",
    )
    def test_method_create_inaccuracy_drivers(self) -> None:
        accuracy = client.reports.accuracy.create_inaccuracy_drivers(
            citation_category_taxonomy="legacy",
            start_date="",
            end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            exclude_topic_ids=False,
            tag_filter_type="any",
            include_no_tag=True,
            include_no_persona=True,
            limit=5,
        )

    @smoke_case(
        "reports.accuracy.createInaccuracyDrivers:all",
        operation="createInaccuracyDrivers",
        path="/v1/reports/accuracy/inaccuracy-drivers",
    )
    def test_method_create_inaccuracy_drivers_with_all_params(self) -> None:
        accuracy = client.reports.accuracy.create_inaccuracy_drivers(
            citation_categories=[""],
            citation_category_taxonomy="legacy",
            citation_category_pairs=[[{}, {}]],
            start_date="",
            end_date="",
            comparison_start_date="",
            comparison_end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            languages=[""],
            topic_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            exclude_topic_ids=False,
            tag_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            tag_filter_type="any",
            include_no_tag=True,
            region_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            platform_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            persona_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            include_no_persona=True,
            prompt_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            limit=5,
        )

    @smoke_case(
        "reports.accuracy.createTopInaccurateClaims:required",
        operation="createTopInaccurateClaims",
        path="/v1/reports/accuracy/top-inaccurate-claims",
    )
    def test_method_create_top_inaccurate_claims(self) -> None:
        accuracy = client.reports.accuracy.create_top_inaccurate_claims(
            citation_category_taxonomy="legacy",
            start_date="",
            end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            exclude_topic_ids=False,
            tag_filter_type="any",
            include_no_tag=True,
            include_no_persona=True,
            limit=5,
        )

    @smoke_case(
        "reports.accuracy.createTopInaccurateClaims:all",
        operation="createTopInaccurateClaims",
        path="/v1/reports/accuracy/top-inaccurate-claims",
    )
    def test_method_create_top_inaccurate_claims_with_all_params(self) -> None:
        accuracy = client.reports.accuracy.create_top_inaccurate_claims(
            citation_categories=[""],
            citation_category_taxonomy="legacy",
            citation_category_pairs=[[{}, {}]],
            start_date="",
            end_date="",
            comparison_start_date="",
            comparison_end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            languages=[""],
            topic_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            exclude_topic_ids=False,
            tag_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            tag_filter_type="any",
            include_no_tag=True,
            region_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            platform_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            persona_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            include_no_persona=True,
            prompt_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            limit=5,
        )

    @smoke_case(
        "reports.accuracy.createClaimBreakdown:required",
        operation="createClaimBreakdown",
        path="/v1/reports/accuracy/claim-breakdown",
    )
    def test_method_create_claim_breakdown(self) -> None:
        accuracy = client.reports.accuracy.create_claim_breakdown(
            citation_category_taxonomy="legacy",
            start_date="",
            end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            exclude_topic_ids=False,
            tag_filter_type="any",
            include_no_tag=True,
            include_no_persona=True,
            cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            verification_status="inaccurate",
        )

    @smoke_case(
        "reports.accuracy.createClaimBreakdown:all",
        operation="createClaimBreakdown",
        path="/v1/reports/accuracy/claim-breakdown",
    )
    def test_method_create_claim_breakdown_with_all_params(self) -> None:
        accuracy = client.reports.accuracy.create_claim_breakdown(
            citation_categories=[""],
            citation_category_taxonomy="legacy",
            citation_category_pairs=[[{}, {}]],
            start_date="",
            end_date="",
            comparison_start_date="",
            comparison_end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            languages=[""],
            topic_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            exclude_topic_ids=False,
            tag_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            tag_filter_type="any",
            include_no_tag=True,
            region_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            platform_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            persona_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            include_no_persona=True,
            prompt_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            verification_status="inaccurate",
        )

    @smoke_case(
        "reports.accuracy.createClaimCitations:required",
        operation="createClaimCitations",
        path="/v1/reports/accuracy/claim-citations",
    )
    def test_method_create_claim_citations(self) -> None:
        accuracy = client.reports.accuracy.create_claim_citations(
            citation_category_taxonomy="legacy",
            start_date="",
            end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            exclude_topic_ids=False,
            tag_filter_type="any",
            include_no_tag=True,
            include_no_persona=True,
            cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            limit=10,
            offset=0,
            sort_order="desc",
        )

    @smoke_case(
        "reports.accuracy.createClaimCitations:all",
        operation="createClaimCitations",
        path="/v1/reports/accuracy/claim-citations",
    )
    def test_method_create_claim_citations_with_all_params(self) -> None:
        accuracy = client.reports.accuracy.create_claim_citations(
            citation_categories=[""],
            citation_category_taxonomy="legacy",
            citation_category_pairs=[[{}, {}]],
            start_date="",
            end_date="",
            comparison_start_date="",
            comparison_end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            languages=[""],
            topic_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            exclude_topic_ids=False,
            tag_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            tag_filter_type="any",
            include_no_tag=True,
            region_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            platform_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            persona_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            include_no_persona=True,
            prompt_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            limit=10,
            offset=0,
            search_query="",
            sort_order="desc",
        )

    @smoke_case(
        "reports.accuracy.createClusterExampleRuns:required",
        operation="createClusterExampleRuns",
        path="/v1/reports/accuracy/cluster-example-runs",
    )
    def test_method_create_cluster_example_runs(self) -> None:
        cluster_example_runs = client.reports.accuracy.create_cluster_example_runs(
            citation_category_taxonomy="legacy",
            start_date="",
            end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            exclude_topic_ids=False,
            tag_filter_type="any",
            include_no_tag=True,
            include_no_persona=True,
            cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            limit=20,
            offset=0,
        )

    @smoke_case(
        "reports.accuracy.createClusterExampleRuns:all",
        operation="createClusterExampleRuns",
        path="/v1/reports/accuracy/cluster-example-runs",
    )
    def test_method_create_cluster_example_runs_with_all_params(self) -> None:
        cluster_example_runs = client.reports.accuracy.create_cluster_example_runs(
            citation_categories=[""],
            citation_category_taxonomy="legacy",
            citation_category_pairs=[[{}, {}]],
            start_date="",
            end_date="",
            comparison_start_date="",
            comparison_end_date="",
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            languages=[""],
            topic_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            exclude_topic_ids=False,
            tag_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            tag_filter_type="any",
            include_no_tag=True,
            region_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            platform_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            persona_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            include_no_persona=True,
            prompt_ids=["7c9e6679-7425-40de-944b-e07fc1f90ae7"],
            cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            limit=20,
            offset=0,
        )

    @smoke_case(
        "reports.accuracy.createClusterVerificationPairs:single",
        operation="createClusterVerificationPairs",
        path="/v1/reports/accuracy/cluster-verification-pairs",
    )
    def test_method_create_cluster_verification_pairs(self) -> None:
        cluster_verification_pairs = client.reports.accuracy.create_cluster_verification_pairs(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )

    @smoke_case(
        "reports.accuracy.createFactcheckSetupStatus:single",
        operation="createFactcheckSetupStatus",
        path="/v1/reports/accuracy/factcheck-setup-status",
    )
    def test_method_create_factcheck_setup_status(self) -> None:
        accuracy = client.reports.accuracy.create_factcheck_setup_status(
            category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )
