# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from profound import Profound, AsyncProfound
from tests.utils import assert_matches_type
from profound.types.reports import (
    AccuracyCreateOverviewResponse,
    AccuracyCreateTopicIDsResponse,
    AccuracyCreateBreakdownResponse,
    AccuracyCreateClaimBreakdownResponse,
    AccuracyCreateClaimCitationsResponse,
    AccuracyCreateCitationAnalysisResponse,
    AccuracyCreateInaccurateThemesResponse,
    AccuracyCreateInaccuracyDriversResponse,
    AccuracyCreateClusterExampleRunsResponse,
    AccuracyCreateInaccurateClustersResponse,
    AccuracyCreateTopInaccurateClaimsResponse,
    AccuracyCreateFactcheckSetupStatusResponse,
    AccuracyCreateClusterVerificationPairsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccuracy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_breakdown(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateBreakdownResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_breakdown_with_all_params(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            breakdown_by="citation",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            limit=1,
            offset=0,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            search_query="search_query",
            sort_by="citationShare",
            sort_order="asc",
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateBreakdownResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_breakdown(self, client: Profound) -> None:
        response = client.reports.accuracy.with_raw_response.create_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = response.parse()
        assert_matches_type(AccuracyCreateBreakdownResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_breakdown(self, client: Profound) -> None:
        with client.reports.accuracy.with_streaming_response.create_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = response.parse()
            assert_matches_type(AccuracyCreateBreakdownResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_citation_analysis(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_citation_analysis(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            clean_href="clean_href",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateCitationAnalysisResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_citation_analysis(self, client: Profound) -> None:
        response = client.reports.accuracy.with_raw_response.create_citation_analysis(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            clean_href="clean_href",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = response.parse()
        assert_matches_type(AccuracyCreateCitationAnalysisResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_citation_analysis(self, client: Profound) -> None:
        with client.reports.accuracy.with_streaming_response.create_citation_analysis(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            clean_href="clean_href",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = response.parse()
            assert_matches_type(AccuracyCreateCitationAnalysisResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_claim_breakdown(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_claim_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateClaimBreakdownResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_claim_breakdown_with_all_params(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_claim_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateClaimBreakdownResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_claim_breakdown(self, client: Profound) -> None:
        response = client.reports.accuracy.with_raw_response.create_claim_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = response.parse()
        assert_matches_type(AccuracyCreateClaimBreakdownResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_claim_breakdown(self, client: Profound) -> None:
        with client.reports.accuracy.with_streaming_response.create_claim_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = response.parse()
            assert_matches_type(AccuracyCreateClaimBreakdownResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_claim_citations(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_claim_citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateClaimCitationsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_claim_citations_with_all_params(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_claim_citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            limit=1,
            offset=0,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            search_query="search_query",
            sort_order="asc",
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateClaimCitationsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_claim_citations(self, client: Profound) -> None:
        response = client.reports.accuracy.with_raw_response.create_claim_citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = response.parse()
        assert_matches_type(AccuracyCreateClaimCitationsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_claim_citations(self, client: Profound) -> None:
        with client.reports.accuracy.with_streaming_response.create_claim_citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = response.parse()
            assert_matches_type(AccuracyCreateClaimCitationsResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_cluster_example_runs(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_cluster_example_runs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateClusterExampleRunsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_cluster_example_runs_with_all_params(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_cluster_example_runs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            limit=1,
            offset=0,
        )
        assert_matches_type(AccuracyCreateClusterExampleRunsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_cluster_example_runs(self, client: Profound) -> None:
        response = client.reports.accuracy.with_raw_response.create_cluster_example_runs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = response.parse()
        assert_matches_type(AccuracyCreateClusterExampleRunsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_cluster_example_runs(self, client: Profound) -> None:
        with client.reports.accuracy.with_streaming_response.create_cluster_example_runs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = response.parse()
            assert_matches_type(AccuracyCreateClusterExampleRunsResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_cluster_verification_pairs(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_cluster_verification_pairs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccuracyCreateClusterVerificationPairsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_cluster_verification_pairs(self, client: Profound) -> None:
        response = client.reports.accuracy.with_raw_response.create_cluster_verification_pairs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = response.parse()
        assert_matches_type(AccuracyCreateClusterVerificationPairsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_cluster_verification_pairs(self, client: Profound) -> None:
        with client.reports.accuracy.with_streaming_response.create_cluster_verification_pairs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = response.parse()
            assert_matches_type(AccuracyCreateClusterVerificationPairsResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_factcheck_setup_status(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_factcheck_setup_status(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccuracyCreateFactcheckSetupStatusResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_factcheck_setup_status(self, client: Profound) -> None:
        response = client.reports.accuracy.with_raw_response.create_factcheck_setup_status(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = response.parse()
        assert_matches_type(AccuracyCreateFactcheckSetupStatusResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_factcheck_setup_status(self, client: Profound) -> None:
        with client.reports.accuracy.with_streaming_response.create_factcheck_setup_status(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = response.parse()
            assert_matches_type(AccuracyCreateFactcheckSetupStatusResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_inaccuracy_drivers(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_inaccuracy_drivers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateInaccuracyDriversResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_inaccuracy_drivers_with_all_params(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_inaccuracy_drivers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            limit=1,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateInaccuracyDriversResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_inaccuracy_drivers(self, client: Profound) -> None:
        response = client.reports.accuracy.with_raw_response.create_inaccuracy_drivers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = response.parse()
        assert_matches_type(AccuracyCreateInaccuracyDriversResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_inaccuracy_drivers(self, client: Profound) -> None:
        with client.reports.accuracy.with_streaming_response.create_inaccuracy_drivers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = response.parse()
            assert_matches_type(AccuracyCreateInaccuracyDriversResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_inaccurate_clusters(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_inaccurate_clusters(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            theme_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccuracyCreateInaccurateClustersResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_inaccurate_clusters_with_all_params(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_inaccurate_clusters(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            theme_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            limit=1,
            offset=0,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            search_query="search_query",
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateInaccurateClustersResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_inaccurate_clusters(self, client: Profound) -> None:
        response = client.reports.accuracy.with_raw_response.create_inaccurate_clusters(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            theme_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = response.parse()
        assert_matches_type(AccuracyCreateInaccurateClustersResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_inaccurate_clusters(self, client: Profound) -> None:
        with client.reports.accuracy.with_streaming_response.create_inaccurate_clusters(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            theme_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = response.parse()
            assert_matches_type(AccuracyCreateInaccurateClustersResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_inaccurate_themes(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_inaccurate_themes(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateInaccurateThemesResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_inaccurate_themes_with_all_params(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_inaccurate_themes(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            limit=1,
            offset=0,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            search_query="search_query",
            sort_by="response_share",
            sort_order="asc",
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateInaccurateThemesResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_inaccurate_themes(self, client: Profound) -> None:
        response = client.reports.accuracy.with_raw_response.create_inaccurate_themes(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = response.parse()
        assert_matches_type(AccuracyCreateInaccurateThemesResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_inaccurate_themes(self, client: Profound) -> None:
        with client.reports.accuracy.with_streaming_response.create_inaccurate_themes(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = response.parse()
            assert_matches_type(AccuracyCreateInaccurateThemesResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overview(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_overview(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateOverviewResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overview_with_all_params(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_overview(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            date_bucket="date_bucket",
            exclude_topic_ids=True,
            group_by="period",
            include_no_persona=True,
            include_no_tag=True,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateOverviewResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overview(self, client: Profound) -> None:
        response = client.reports.accuracy.with_raw_response.create_overview(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = response.parse()
        assert_matches_type(AccuracyCreateOverviewResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overview(self, client: Profound) -> None:
        with client.reports.accuracy.with_streaming_response.create_overview(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = response.parse()
            assert_matches_type(AccuracyCreateOverviewResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_top_inaccurate_claims(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_top_inaccurate_claims(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateTopInaccurateClaimsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_top_inaccurate_claims_with_all_params(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_top_inaccurate_claims(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            limit=1,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateTopInaccurateClaimsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_top_inaccurate_claims(self, client: Profound) -> None:
        response = client.reports.accuracy.with_raw_response.create_top_inaccurate_claims(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = response.parse()
        assert_matches_type(AccuracyCreateTopInaccurateClaimsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_top_inaccurate_claims(self, client: Profound) -> None:
        with client.reports.accuracy.with_streaming_response.create_top_inaccurate_claims(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = response.parse()
            assert_matches_type(AccuracyCreateTopInaccurateClaimsResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_topic_ids(self, client: Profound) -> None:
        accuracy = client.reports.accuracy.create_topic_ids(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateTopicIDsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_topic_ids(self, client: Profound) -> None:
        response = client.reports.accuracy.with_raw_response.create_topic_ids(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = response.parse()
        assert_matches_type(AccuracyCreateTopicIDsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_topic_ids(self, client: Profound) -> None:
        with client.reports.accuracy.with_streaming_response.create_topic_ids(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = response.parse()
            assert_matches_type(AccuracyCreateTopicIDsResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccuracy:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_breakdown(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateBreakdownResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_breakdown_with_all_params(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            breakdown_by="citation",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            limit=1,
            offset=0,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            search_query="search_query",
            sort_by="citationShare",
            sort_order="asc",
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateBreakdownResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_breakdown(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.accuracy.with_raw_response.create_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = await response.parse()
        assert_matches_type(AccuracyCreateBreakdownResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_breakdown(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.accuracy.with_streaming_response.create_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = await response.parse()
            assert_matches_type(AccuracyCreateBreakdownResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_citation_analysis(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_citation_analysis(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            clean_href="clean_href",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateCitationAnalysisResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_citation_analysis(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.accuracy.with_raw_response.create_citation_analysis(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            clean_href="clean_href",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = await response.parse()
        assert_matches_type(AccuracyCreateCitationAnalysisResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_citation_analysis(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.accuracy.with_streaming_response.create_citation_analysis(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            clean_href="clean_href",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = await response.parse()
            assert_matches_type(AccuracyCreateCitationAnalysisResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_claim_breakdown(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_claim_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateClaimBreakdownResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_claim_breakdown_with_all_params(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_claim_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateClaimBreakdownResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_claim_breakdown(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.accuracy.with_raw_response.create_claim_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = await response.parse()
        assert_matches_type(AccuracyCreateClaimBreakdownResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_claim_breakdown(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.accuracy.with_streaming_response.create_claim_breakdown(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = await response.parse()
            assert_matches_type(AccuracyCreateClaimBreakdownResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_claim_citations(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_claim_citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateClaimCitationsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_claim_citations_with_all_params(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_claim_citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            limit=1,
            offset=0,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            search_query="search_query",
            sort_order="asc",
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateClaimCitationsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_claim_citations(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.accuracy.with_raw_response.create_claim_citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = await response.parse()
        assert_matches_type(AccuracyCreateClaimCitationsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_claim_citations(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.accuracy.with_streaming_response.create_claim_citations(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = await response.parse()
            assert_matches_type(AccuracyCreateClaimCitationsResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_cluster_example_runs(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_cluster_example_runs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateClusterExampleRunsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_cluster_example_runs_with_all_params(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_cluster_example_runs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            limit=1,
            offset=0,
        )
        assert_matches_type(AccuracyCreateClusterExampleRunsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_cluster_example_runs(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.accuracy.with_raw_response.create_cluster_example_runs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = await response.parse()
        assert_matches_type(AccuracyCreateClusterExampleRunsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_cluster_example_runs(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.accuracy.with_streaming_response.create_cluster_example_runs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = await response.parse()
            assert_matches_type(AccuracyCreateClusterExampleRunsResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_cluster_verification_pairs(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_cluster_verification_pairs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccuracyCreateClusterVerificationPairsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_cluster_verification_pairs(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.accuracy.with_raw_response.create_cluster_verification_pairs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = await response.parse()
        assert_matches_type(AccuracyCreateClusterVerificationPairsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_cluster_verification_pairs(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.accuracy.with_streaming_response.create_cluster_verification_pairs(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = await response.parse()
            assert_matches_type(AccuracyCreateClusterVerificationPairsResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_factcheck_setup_status(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_factcheck_setup_status(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccuracyCreateFactcheckSetupStatusResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_factcheck_setup_status(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.accuracy.with_raw_response.create_factcheck_setup_status(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = await response.parse()
        assert_matches_type(AccuracyCreateFactcheckSetupStatusResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_factcheck_setup_status(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.accuracy.with_streaming_response.create_factcheck_setup_status(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = await response.parse()
            assert_matches_type(AccuracyCreateFactcheckSetupStatusResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_inaccuracy_drivers(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_inaccuracy_drivers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateInaccuracyDriversResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_inaccuracy_drivers_with_all_params(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_inaccuracy_drivers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            limit=1,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateInaccuracyDriversResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_inaccuracy_drivers(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.accuracy.with_raw_response.create_inaccuracy_drivers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = await response.parse()
        assert_matches_type(AccuracyCreateInaccuracyDriversResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_inaccuracy_drivers(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.accuracy.with_streaming_response.create_inaccuracy_drivers(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = await response.parse()
            assert_matches_type(AccuracyCreateInaccuracyDriversResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_inaccurate_clusters(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_inaccurate_clusters(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            theme_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccuracyCreateInaccurateClustersResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_inaccurate_clusters_with_all_params(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_inaccurate_clusters(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            theme_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            limit=1,
            offset=0,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            search_query="search_query",
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateInaccurateClustersResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_inaccurate_clusters(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.accuracy.with_raw_response.create_inaccurate_clusters(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            theme_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = await response.parse()
        assert_matches_type(AccuracyCreateInaccurateClustersResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_inaccurate_clusters(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.accuracy.with_streaming_response.create_inaccurate_clusters(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            theme_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = await response.parse()
            assert_matches_type(AccuracyCreateInaccurateClustersResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_inaccurate_themes(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_inaccurate_themes(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateInaccurateThemesResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_inaccurate_themes_with_all_params(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_inaccurate_themes(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            limit=1,
            offset=0,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            search_query="search_query",
            sort_by="response_share",
            sort_order="asc",
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateInaccurateThemesResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_inaccurate_themes(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.accuracy.with_raw_response.create_inaccurate_themes(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = await response.parse()
        assert_matches_type(AccuracyCreateInaccurateThemesResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_inaccurate_themes(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.accuracy.with_streaming_response.create_inaccurate_themes(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = await response.parse()
            assert_matches_type(AccuracyCreateInaccurateThemesResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overview(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_overview(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateOverviewResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overview_with_all_params(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_overview(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            date_bucket="date_bucket",
            exclude_topic_ids=True,
            group_by="period",
            include_no_persona=True,
            include_no_tag=True,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateOverviewResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overview(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.accuracy.with_raw_response.create_overview(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = await response.parse()
        assert_matches_type(AccuracyCreateOverviewResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overview(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.accuracy.with_streaming_response.create_overview(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = await response.parse()
            assert_matches_type(AccuracyCreateOverviewResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_top_inaccurate_claims(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_top_inaccurate_claims(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateTopInaccurateClaimsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_top_inaccurate_claims_with_all_params(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_top_inaccurate_claims(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
            citation_categories=["string"],
            comparison_end_date="comparison_end_date",
            comparison_start_date="comparison_start_date",
            exclude_topic_ids=True,
            include_no_persona=True,
            include_no_tag=True,
            limit=1,
            persona_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            platform_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            prompt_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            region_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            tag_filter_type="all",
            tag_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AccuracyCreateTopInaccurateClaimsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_top_inaccurate_claims(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.accuracy.with_raw_response.create_top_inaccurate_claims(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = await response.parse()
        assert_matches_type(AccuracyCreateTopInaccurateClaimsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_top_inaccurate_claims(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.accuracy.with_streaming_response.create_top_inaccurate_claims(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = await response.parse()
            assert_matches_type(AccuracyCreateTopInaccurateClaimsResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_topic_ids(self, async_client: AsyncProfound) -> None:
        accuracy = await async_client.reports.accuracy.create_topic_ids(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AccuracyCreateTopicIDsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_topic_ids(self, async_client: AsyncProfound) -> None:
        response = await async_client.reports.accuracy.with_raw_response.create_topic_ids(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accuracy = await response.parse()
        assert_matches_type(AccuracyCreateTopicIDsResponse, accuracy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_topic_ids(self, async_client: AsyncProfound) -> None:
        async with async_client.reports.accuracy.with_streaming_response.create_topic_ids(
            category_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accuracy = await response.parse()
            assert_matches_type(AccuracyCreateTopicIDsResponse, accuracy, path=["response"])

        assert cast(Any, response.is_closed) is True
