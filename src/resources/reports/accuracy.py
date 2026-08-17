# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Optional
from typing_extensions import Literal
from ..._types import SequenceNotStr

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.reports.accuracy_overview_v1_reports_overview_post_response import AccuracyOverviewV1ReportsOverviewPostResponse, AccuracyTrendPoint, AccuracyScoreBreakdown, AccuracyThemeTrendSeries, AccuracyThemeTrendPoint, AccuracyTrendSeriesMeta
from ...types.reports import accuracy_overview_v1_reports_overview_post_params
from ...types.reports.accuracy_breakdown_v1_reports_breakdown_post_response import AccuracyBreakdownV1ReportsBreakdownPostResponse, AccuracyBreakdownRow
from ...types.reports import accuracy_breakdown_v1_reports_breakdown_post_params
from ...types.reports.accuracy_citation_analysis_v1_reports_citation_analysis_post_response import AccuracyCitationAnalysisV1ReportsCitationAnalysisPostResponse, AccuracyCitationClaim, AccuracyCitationEvidence
from ...types.reports import accuracy_citation_analysis_v1_reports_citation_analysis_post_params
from ...types.reports.accuracy_topic_ids_v1_reports_topic_ids_post_response import AccuracyTopicIdsV1ReportsTopicIdsPostResponse
from ...types.reports import accuracy_topic_ids_v1_reports_topic_ids_post_params
from ...types.reports.accuracy_inaccurate_themes_v1_reports_inaccurate_themes_post_response import AccuracyInaccurateThemesV1ReportsInaccurateThemesPostResponse, InaccurateThemeRow
from ...types.reports import accuracy_inaccurate_themes_v1_reports_inaccurate_themes_post_params
from ...types.reports.accuracy_inaccurate_clusters_v1_reports_inaccurate_clusters_post_response import AccuracyInaccurateClustersV1ReportsInaccurateClustersPostResponse, InaccurateClusterRow
from ...types.reports import accuracy_inaccurate_clusters_v1_reports_inaccurate_clusters_post_params
from ...types.reports.accuracy_inaccuracy_drivers_v1_reports_inaccuracy_drivers_post_response import AccuracyInaccuracyDriversV1ReportsInaccuracyDriversPostResponse, InaccuracyDriverRow
from ...types.reports import accuracy_inaccuracy_drivers_v1_reports_inaccuracy_drivers_post_params
from ...types.reports.accuracy_top_inaccurate_claims_v1_reports_top_inaccurate_claims_post_response import AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostResponse, TopInaccurateClaimRow
from ...types.reports import accuracy_top_inaccurate_claims_v1_reports_top_inaccurate_claims_post_params
from ...types.reports.accuracy_claim_breakdown_v1_reports_claim_breakdown_post_response import AccuracyClaimBreakdownV1ReportsClaimBreakdownPostResponse, ClaimBreakdownRow, ClaimPromptBreakdownRow
from ...types.reports import accuracy_claim_breakdown_v1_reports_claim_breakdown_post_params
from ...types.reports.accuracy_claim_citations_v1_reports_claim_citations_post_response import AccuracyClaimCitationsV1ReportsClaimCitationsPostResponse, ClaimCitationRow
from ...types.reports import accuracy_claim_citations_v1_reports_claim_citations_post_params
from ...types.reports.accuracy_cluster_example_runs_v1_reports_cluster_example_runs_post_response import AccuracyClusterExampleRunsV1ReportsClusterExampleRunsPostResponse, ClusterExampleRun
from ...types.reports import accuracy_cluster_example_runs_v1_reports_cluster_example_runs_post_params
from ...types.reports.accuracy_cluster_verification_pairs_v1_reports_cluster_verification_pairs_post_response import AccuracyClusterVerificationPairsV1ReportsClusterVerificationPairsPostResponse, ClusterVerificationPair
from ...types.reports import accuracy_cluster_verification_pairs_v1_reports_cluster_verification_pairs_post_params
from ...types.reports.accuracy_factcheck_setup_status_v1_reports_factcheck_setup_status_post_response import AccuracyFactcheckSetupStatusV1ReportsFactcheckSetupStatusPostResponse
from ...types.reports import accuracy_factcheck_setup_status_v1_reports_factcheck_setup_status_post_params

__all__ = ["AccuracyResource", "AsyncAccuracyResource"]


class AccuracyResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AccuracyResourceWithRawResponse:
        return AccuracyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccuracyResourceWithStreamingResponse:
        return AccuracyResourceWithStreamingResponse(self)

    def overview_v1_reports_overview_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        date_bucket: Optional[str] | Omit = omit,
        group_by: Literal["period", "theme"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyOverviewV1ReportsOverviewPostResponse:
        """
        Accuracy Overview
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            date_bucket: Body parameter.
            group_by: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyOverviewV1ReportsOverviewPostResponse: Successful Response
        
        Example:
            ```python
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
            ```
        """
        return self._post(
            "/v1/reports/accuracy/overview",
            body=maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "date_bucket": date_bucket,
            "group_by": group_by,
        },
            accuracy_overview_v1_reports_overview_post_params.AccuracyOverviewV1ReportsOverviewPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyOverviewV1ReportsOverviewPostResponse,
        )

    def breakdown_v1_reports_breakdown_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        breakdown_by: Literal["citation", "platform", "topic", "prompt", "tag", "region", "persona"] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        sort_by: Literal["citationShare", "accuracy"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyBreakdownV1ReportsBreakdownPostResponse:
        """
        Accuracy Breakdown
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            breakdown_by: Body parameter.
            limit: Body parameter.
            offset: Body parameter.
            search_query: Body parameter.
            sort_by: Body parameter.
            sort_order: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyBreakdownV1ReportsBreakdownPostResponse: Successful Response
        
        Example:
            ```python
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
            ```
        """
        return self._post(
            "/v1/reports/accuracy/breakdown",
            body=maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "breakdown_by": breakdown_by,
            "limit": limit,
            "offset": offset,
            "search_query": search_query,
            "sort_by": sort_by,
            "sort_order": sort_order,
        },
            accuracy_breakdown_v1_reports_breakdown_post_params.AccuracyBreakdownV1ReportsBreakdownPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyBreakdownV1ReportsBreakdownPostResponse,
        )

    def citation_analysis_v1_reports_citation_analysis_post(
        self,
        *,
        category_id: str,
        clean_href: str,
        start_date: str,
        end_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCitationAnalysisV1ReportsCitationAnalysisPostResponse:
        """
        Accuracy Citation Analysis
        
        Args:
            category_id: Body parameter.
            clean_href: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyCitationAnalysisV1ReportsCitationAnalysisPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = client.reports.accuracy.citation_analysis_v1_reports_citation_analysis_post(
                category_id="",
                clean_href="",
                start_date="",
                end_date="",
            )
            ```
        """
        return self._post(
            "/v1/reports/accuracy/citation-analysis",
            body=maybe_transform(
            {
            "category_id": category_id,
            "clean_href": clean_href,
            "start_date": start_date,
            "end_date": end_date,
        },
            accuracy_citation_analysis_v1_reports_citation_analysis_post_params.AccuracyCitationAnalysisV1ReportsCitationAnalysisPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyCitationAnalysisV1ReportsCitationAnalysisPostResponse,
        )

    def topic_ids_v1_reports_topic_ids_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyTopicIdsV1ReportsTopicIdsPostResponse:
        """
        Accuracy Topic Ids
        
        Args:
            category_id: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyTopicIdsV1ReportsTopicIdsPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = client.reports.accuracy.topic_ids_v1_reports_topic_ids_post(
                category_id="",
                start_date="",
                end_date="",
            )
            ```
        """
        return self._post(
            "/v1/reports/accuracy/topic-ids",
            body=maybe_transform(
            {
            "category_id": category_id,
            "start_date": start_date,
            "end_date": end_date,
        },
            accuracy_topic_ids_v1_reports_topic_ids_post_params.AccuracyTopicIdsV1ReportsTopicIdsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyTopicIdsV1ReportsTopicIdsPostResponse,
        )

    def inaccurate_themes_v1_reports_inaccurate_themes_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: Literal["response_share"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyInaccurateThemesV1ReportsInaccurateThemesPostResponse:
        """
        Accuracy Inaccurate Themes
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            limit: Body parameter.
            offset: Body parameter.
            sort_by: Body parameter.
            sort_order: Body parameter.
            search_query: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyInaccurateThemesV1ReportsInaccurateThemesPostResponse: Successful Response
        
        Example:
            ```python
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
            ```
        """
        return self._post(
            "/v1/reports/accuracy/inaccurate-themes",
            body=maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "limit": limit,
            "offset": offset,
            "sort_by": sort_by,
            "sort_order": sort_order,
            "search_query": search_query,
        },
            accuracy_inaccurate_themes_v1_reports_inaccurate_themes_post_params.AccuracyInaccurateThemesV1ReportsInaccurateThemesPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyInaccurateThemesV1ReportsInaccurateThemesPostResponse,
        )

    def inaccurate_clusters_v1_reports_inaccurate_clusters_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        theme_id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyInaccurateClustersV1ReportsInaccurateClustersPostResponse:
        """
        Accuracy Inaccurate Clusters
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            theme_id: Body parameter.
            limit: Body parameter.
            offset: Body parameter.
            search_query: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyInaccurateClustersV1ReportsInaccurateClustersPostResponse: Successful Response
        
        Example:
            ```python
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
            ```
        """
        return self._post(
            "/v1/reports/accuracy/inaccurate-clusters",
            body=maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "theme_id": theme_id,
            "limit": limit,
            "offset": offset,
            "search_query": search_query,
        },
            accuracy_inaccurate_clusters_v1_reports_inaccurate_clusters_post_params.AccuracyInaccurateClustersV1ReportsInaccurateClustersPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyInaccurateClustersV1ReportsInaccurateClustersPostResponse,
        )

    def inaccuracy_drivers_v1_reports_inaccuracy_drivers_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyInaccuracyDriversV1ReportsInaccuracyDriversPostResponse:
        """
        Accuracy Inaccuracy Drivers
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            limit: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyInaccuracyDriversV1ReportsInaccuracyDriversPostResponse: Successful Response
        
        Example:
            ```python
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
            ```
        """
        return self._post(
            "/v1/reports/accuracy/inaccuracy-drivers",
            body=maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "limit": limit,
        },
            accuracy_inaccuracy_drivers_v1_reports_inaccuracy_drivers_post_params.AccuracyInaccuracyDriversV1ReportsInaccuracyDriversPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyInaccuracyDriversV1ReportsInaccuracyDriversPostResponse,
        )

    def top_inaccurate_claims_v1_reports_top_inaccurate_claims_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostResponse:
        """
        Accuracy Top Inaccurate Claims
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            limit: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostResponse: Successful Response
        
        Example:
            ```python
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
            ```
        """
        return self._post(
            "/v1/reports/accuracy/top-inaccurate-claims",
            body=maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "limit": limit,
        },
            accuracy_top_inaccurate_claims_v1_reports_top_inaccurate_claims_post_params.AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostResponse,
        )

    def claim_breakdown_v1_reports_claim_breakdown_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        cluster_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyClaimBreakdownV1ReportsClaimBreakdownPostResponse:
        """
        Accuracy Claim Breakdown
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            cluster_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyClaimBreakdownV1ReportsClaimBreakdownPostResponse: Successful Response
        
        Example:
            ```python
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
            ```
        """
        return self._post(
            "/v1/reports/accuracy/claim-breakdown",
            body=maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "cluster_id": cluster_id,
        },
            accuracy_claim_breakdown_v1_reports_claim_breakdown_post_params.AccuracyClaimBreakdownV1ReportsClaimBreakdownPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyClaimBreakdownV1ReportsClaimBreakdownPostResponse,
        )

    def claim_citations_v1_reports_claim_citations_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        cluster_id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyClaimCitationsV1ReportsClaimCitationsPostResponse:
        """
        Accuracy Claim Citations
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            cluster_id: Body parameter.
            limit: Body parameter.
            offset: Body parameter.
            search_query: Body parameter.
            sort_order: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyClaimCitationsV1ReportsClaimCitationsPostResponse: Successful Response
        
        Example:
            ```python
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
            ```
        """
        return self._post(
            "/v1/reports/accuracy/claim-citations",
            body=maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "cluster_id": cluster_id,
            "limit": limit,
            "offset": offset,
            "search_query": search_query,
            "sort_order": sort_order,
        },
            accuracy_claim_citations_v1_reports_claim_citations_post_params.AccuracyClaimCitationsV1ReportsClaimCitationsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyClaimCitationsV1ReportsClaimCitationsPostResponse,
        )

    def cluster_example_runs_v1_reports_cluster_example_runs_post(
        self,
        *,
        category_id: str,
        cluster_id: str,
        start_date: str,
        end_date: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyClusterExampleRunsV1ReportsClusterExampleRunsPostResponse:
        """
        Accuracy Cluster Example Runs
        
        Args:
            category_id: Body parameter.
            cluster_id: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            limit: Body parameter.
            offset: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyClusterExampleRunsV1ReportsClusterExampleRunsPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = client.reports.accuracy.cluster_example_runs_v1_reports_cluster_example_runs_post(
                category_id="",
                cluster_id="",
                start_date="",
                end_date="",
                limit=20,
                offset=0,
            )
            ```
        """
        return self._post(
            "/v1/reports/accuracy/cluster-example-runs",
            body=maybe_transform(
            {
            "category_id": category_id,
            "cluster_id": cluster_id,
            "start_date": start_date,
            "end_date": end_date,
            "limit": limit,
            "offset": offset,
        },
            accuracy_cluster_example_runs_v1_reports_cluster_example_runs_post_params.AccuracyClusterExampleRunsV1ReportsClusterExampleRunsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyClusterExampleRunsV1ReportsClusterExampleRunsPostResponse,
        )

    def cluster_verification_pairs_v1_reports_cluster_verification_pairs_post(
        self,
        *,
        category_id: str,
        cluster_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyClusterVerificationPairsV1ReportsClusterVerificationPairsPostResponse:
        """
        Accuracy Cluster Verification Pairs
        
        Args:
            category_id: Body parameter.
            cluster_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyClusterVerificationPairsV1ReportsClusterVerificationPairsPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = client.reports.accuracy.cluster_verification_pairs_v1_reports_cluster_verification_pairs_post(
                category_id="",
                cluster_id="",
            )
            ```
        """
        return self._post(
            "/v1/reports/accuracy/cluster-verification-pairs",
            body=maybe_transform(
            {
            "category_id": category_id,
            "cluster_id": cluster_id,
        },
            accuracy_cluster_verification_pairs_v1_reports_cluster_verification_pairs_post_params.AccuracyClusterVerificationPairsV1ReportsClusterVerificationPairsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyClusterVerificationPairsV1ReportsClusterVerificationPairsPostResponse,
        )

    def factcheck_setup_status_v1_reports_factcheck_setup_status_post(
        self,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyFactcheckSetupStatusV1ReportsFactcheckSetupStatusPostResponse:
        """
        Accuracy Factcheck Setup Status
        
        Args:
            category_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyFactcheckSetupStatusV1ReportsFactcheckSetupStatusPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = client.reports.accuracy.factcheck_setup_status_v1_reports_factcheck_setup_status_post(
                category_id="",
            )
            ```
        """
        return self._post(
            "/v1/reports/accuracy/factcheck-setup-status",
            body=maybe_transform(
            {"category_id": category_id},
            accuracy_factcheck_setup_status_v1_reports_factcheck_setup_status_post_params.AccuracyFactcheckSetupStatusV1ReportsFactcheckSetupStatusPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyFactcheckSetupStatusV1ReportsFactcheckSetupStatusPostResponse,
        )


class AsyncAccuracyResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncAccuracyResourceWithRawResponse:
        return AsyncAccuracyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccuracyResourceWithStreamingResponse:
        return AsyncAccuracyResourceWithStreamingResponse(self)

    async def overview_v1_reports_overview_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        date_bucket: Optional[str] | Omit = omit,
        group_by: Literal["period", "theme"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyOverviewV1ReportsOverviewPostResponse:
        """
        Accuracy Overview
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            date_bucket: Body parameter.
            group_by: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyOverviewV1ReportsOverviewPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = await client.reports.accuracy.overview_v1_reports_overview_post(
                start_date="",
                end_date="",
                category_id="",
                exclude_topic_ids=False,
                tag_filter_type="any",
                include_no_tag=True,
                include_no_persona=True,
                group_by="period",
            )
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/overview",
            body=await async_maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "date_bucket": date_bucket,
            "group_by": group_by,
        },
            accuracy_overview_v1_reports_overview_post_params.AccuracyOverviewV1ReportsOverviewPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyOverviewV1ReportsOverviewPostResponse,
        )

    async def breakdown_v1_reports_breakdown_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        breakdown_by: Literal["citation", "platform", "topic", "prompt", "tag", "region", "persona"] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        sort_by: Literal["citationShare", "accuracy"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyBreakdownV1ReportsBreakdownPostResponse:
        """
        Accuracy Breakdown
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            breakdown_by: Body parameter.
            limit: Body parameter.
            offset: Body parameter.
            search_query: Body parameter.
            sort_by: Body parameter.
            sort_order: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyBreakdownV1ReportsBreakdownPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = await client.reports.accuracy.breakdown_v1_reports_breakdown_post(
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
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/breakdown",
            body=await async_maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "breakdown_by": breakdown_by,
            "limit": limit,
            "offset": offset,
            "search_query": search_query,
            "sort_by": sort_by,
            "sort_order": sort_order,
        },
            accuracy_breakdown_v1_reports_breakdown_post_params.AccuracyBreakdownV1ReportsBreakdownPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyBreakdownV1ReportsBreakdownPostResponse,
        )

    async def citation_analysis_v1_reports_citation_analysis_post(
        self,
        *,
        category_id: str,
        clean_href: str,
        start_date: str,
        end_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCitationAnalysisV1ReportsCitationAnalysisPostResponse:
        """
        Accuracy Citation Analysis
        
        Args:
            category_id: Body parameter.
            clean_href: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyCitationAnalysisV1ReportsCitationAnalysisPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = await client.reports.accuracy.citation_analysis_v1_reports_citation_analysis_post(
                category_id="",
                clean_href="",
                start_date="",
                end_date="",
            )
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/citation-analysis",
            body=await async_maybe_transform(
            {
            "category_id": category_id,
            "clean_href": clean_href,
            "start_date": start_date,
            "end_date": end_date,
        },
            accuracy_citation_analysis_v1_reports_citation_analysis_post_params.AccuracyCitationAnalysisV1ReportsCitationAnalysisPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyCitationAnalysisV1ReportsCitationAnalysisPostResponse,
        )

    async def topic_ids_v1_reports_topic_ids_post(
        self,
        *,
        category_id: str,
        start_date: str,
        end_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyTopicIdsV1ReportsTopicIdsPostResponse:
        """
        Accuracy Topic Ids
        
        Args:
            category_id: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyTopicIdsV1ReportsTopicIdsPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = await client.reports.accuracy.topic_ids_v1_reports_topic_ids_post(
                category_id="",
                start_date="",
                end_date="",
            )
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/topic-ids",
            body=await async_maybe_transform(
            {
            "category_id": category_id,
            "start_date": start_date,
            "end_date": end_date,
        },
            accuracy_topic_ids_v1_reports_topic_ids_post_params.AccuracyTopicIdsV1ReportsTopicIdsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyTopicIdsV1ReportsTopicIdsPostResponse,
        )

    async def inaccurate_themes_v1_reports_inaccurate_themes_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        sort_by: Literal["response_share"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyInaccurateThemesV1ReportsInaccurateThemesPostResponse:
        """
        Accuracy Inaccurate Themes
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            limit: Body parameter.
            offset: Body parameter.
            sort_by: Body parameter.
            sort_order: Body parameter.
            search_query: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyInaccurateThemesV1ReportsInaccurateThemesPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = await client.reports.accuracy.inaccurate_themes_v1_reports_inaccurate_themes_post(
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
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/inaccurate-themes",
            body=await async_maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "limit": limit,
            "offset": offset,
            "sort_by": sort_by,
            "sort_order": sort_order,
            "search_query": search_query,
        },
            accuracy_inaccurate_themes_v1_reports_inaccurate_themes_post_params.AccuracyInaccurateThemesV1ReportsInaccurateThemesPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyInaccurateThemesV1ReportsInaccurateThemesPostResponse,
        )

    async def inaccurate_clusters_v1_reports_inaccurate_clusters_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        theme_id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyInaccurateClustersV1ReportsInaccurateClustersPostResponse:
        """
        Accuracy Inaccurate Clusters
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            theme_id: Body parameter.
            limit: Body parameter.
            offset: Body parameter.
            search_query: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyInaccurateClustersV1ReportsInaccurateClustersPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = await client.reports.accuracy.inaccurate_clusters_v1_reports_inaccurate_clusters_post(
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
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/inaccurate-clusters",
            body=await async_maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "theme_id": theme_id,
            "limit": limit,
            "offset": offset,
            "search_query": search_query,
        },
            accuracy_inaccurate_clusters_v1_reports_inaccurate_clusters_post_params.AccuracyInaccurateClustersV1ReportsInaccurateClustersPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyInaccurateClustersV1ReportsInaccurateClustersPostResponse,
        )

    async def inaccuracy_drivers_v1_reports_inaccuracy_drivers_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyInaccuracyDriversV1ReportsInaccuracyDriversPostResponse:
        """
        Accuracy Inaccuracy Drivers
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            limit: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyInaccuracyDriversV1ReportsInaccuracyDriversPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = await client.reports.accuracy.inaccuracy_drivers_v1_reports_inaccuracy_drivers_post(
                start_date="",
                end_date="",
                category_id="",
                exclude_topic_ids=False,
                tag_filter_type="any",
                include_no_tag=True,
                include_no_persona=True,
                limit=5,
            )
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/inaccuracy-drivers",
            body=await async_maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "limit": limit,
        },
            accuracy_inaccuracy_drivers_v1_reports_inaccuracy_drivers_post_params.AccuracyInaccuracyDriversV1ReportsInaccuracyDriversPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyInaccuracyDriversV1ReportsInaccuracyDriversPostResponse,
        )

    async def top_inaccurate_claims_v1_reports_top_inaccurate_claims_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostResponse:
        """
        Accuracy Top Inaccurate Claims
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            limit: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = await client.reports.accuracy.top_inaccurate_claims_v1_reports_top_inaccurate_claims_post(
                start_date="",
                end_date="",
                category_id="",
                exclude_topic_ids=False,
                tag_filter_type="any",
                include_no_tag=True,
                include_no_persona=True,
                limit=5,
            )
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/top-inaccurate-claims",
            body=await async_maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "limit": limit,
        },
            accuracy_top_inaccurate_claims_v1_reports_top_inaccurate_claims_post_params.AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyTopInaccurateClaimsV1ReportsTopInaccurateClaimsPostResponse,
        )

    async def claim_breakdown_v1_reports_claim_breakdown_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        cluster_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyClaimBreakdownV1ReportsClaimBreakdownPostResponse:
        """
        Accuracy Claim Breakdown
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            cluster_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyClaimBreakdownV1ReportsClaimBreakdownPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = await client.reports.accuracy.claim_breakdown_v1_reports_claim_breakdown_post(
                start_date="",
                end_date="",
                category_id="",
                exclude_topic_ids=False,
                tag_filter_type="any",
                include_no_tag=True,
                include_no_persona=True,
                cluster_id="",
            )
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/claim-breakdown",
            body=await async_maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "cluster_id": cluster_id,
        },
            accuracy_claim_breakdown_v1_reports_claim_breakdown_post_params.AccuracyClaimBreakdownV1ReportsClaimBreakdownPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyClaimBreakdownV1ReportsClaimBreakdownPostResponse,
        )

    async def claim_citations_v1_reports_claim_citations_post(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[Iterable[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[Iterable[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[Iterable[str]] | Omit = omit,
        platform_ids: Optional[Iterable[str]] | Omit = omit,
        persona_ids: Optional[Iterable[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[Iterable[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        cluster_id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyClaimCitationsV1ReportsClaimCitationsPostResponse:
        """
        Accuracy Claim Citations
        
        Args:
            start_date: Body parameter.
            end_date: Body parameter.
            comparison_start_date: Body parameter.
            comparison_end_date: Body parameter.
            category_id: Body parameter.
            topic_ids: Body parameter.
            exclude_topic_ids: Body parameter.
            tag_ids: Body parameter.
            tag_filter_type: Body parameter.
            include_no_tag: Body parameter.
            region_ids: Body parameter.
            platform_ids: Body parameter.
            persona_ids: Body parameter.
            include_no_persona: Body parameter.
            prompt_ids: Body parameter.
            citation_categories: Body parameter.
            cluster_id: Body parameter.
            limit: Body parameter.
            offset: Body parameter.
            search_query: Body parameter.
            sort_order: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyClaimCitationsV1ReportsClaimCitationsPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = await client.reports.accuracy.claim_citations_v1_reports_claim_citations_post(
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
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/claim-citations",
            body=await async_maybe_transform(
            {
            "start_date": start_date,
            "end_date": end_date,
            "comparison_start_date": comparison_start_date,
            "comparison_end_date": comparison_end_date,
            "category_id": category_id,
            "topic_ids": topic_ids,
            "exclude_topic_ids": exclude_topic_ids,
            "tag_ids": tag_ids,
            "tag_filter_type": tag_filter_type,
            "include_no_tag": include_no_tag,
            "region_ids": region_ids,
            "platform_ids": platform_ids,
            "persona_ids": persona_ids,
            "include_no_persona": include_no_persona,
            "prompt_ids": prompt_ids,
            "citation_categories": citation_categories,
            "cluster_id": cluster_id,
            "limit": limit,
            "offset": offset,
            "search_query": search_query,
            "sort_order": sort_order,
        },
            accuracy_claim_citations_v1_reports_claim_citations_post_params.AccuracyClaimCitationsV1ReportsClaimCitationsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyClaimCitationsV1ReportsClaimCitationsPostResponse,
        )

    async def cluster_example_runs_v1_reports_cluster_example_runs_post(
        self,
        *,
        category_id: str,
        cluster_id: str,
        start_date: str,
        end_date: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyClusterExampleRunsV1ReportsClusterExampleRunsPostResponse:
        """
        Accuracy Cluster Example Runs
        
        Args:
            category_id: Body parameter.
            cluster_id: Body parameter.
            start_date: Body parameter.
            end_date: Body parameter.
            limit: Body parameter.
            offset: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyClusterExampleRunsV1ReportsClusterExampleRunsPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = await client.reports.accuracy.cluster_example_runs_v1_reports_cluster_example_runs_post(
                category_id="",
                cluster_id="",
                start_date="",
                end_date="",
                limit=20,
                offset=0,
            )
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/cluster-example-runs",
            body=await async_maybe_transform(
            {
            "category_id": category_id,
            "cluster_id": cluster_id,
            "start_date": start_date,
            "end_date": end_date,
            "limit": limit,
            "offset": offset,
        },
            accuracy_cluster_example_runs_v1_reports_cluster_example_runs_post_params.AccuracyClusterExampleRunsV1ReportsClusterExampleRunsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyClusterExampleRunsV1ReportsClusterExampleRunsPostResponse,
        )

    async def cluster_verification_pairs_v1_reports_cluster_verification_pairs_post(
        self,
        *,
        category_id: str,
        cluster_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyClusterVerificationPairsV1ReportsClusterVerificationPairsPostResponse:
        """
        Accuracy Cluster Verification Pairs
        
        Args:
            category_id: Body parameter.
            cluster_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyClusterVerificationPairsV1ReportsClusterVerificationPairsPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = await client.reports.accuracy.cluster_verification_pairs_v1_reports_cluster_verification_pairs_post(
                category_id="",
                cluster_id="",
            )
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/cluster-verification-pairs",
            body=await async_maybe_transform(
            {
            "category_id": category_id,
            "cluster_id": cluster_id,
        },
            accuracy_cluster_verification_pairs_v1_reports_cluster_verification_pairs_post_params.AccuracyClusterVerificationPairsV1ReportsClusterVerificationPairsPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyClusterVerificationPairsV1ReportsClusterVerificationPairsPostResponse,
        )

    async def factcheck_setup_status_v1_reports_factcheck_setup_status_post(
        self,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyFactcheckSetupStatusV1ReportsFactcheckSetupStatusPostResponse:
        """
        Accuracy Factcheck Setup Status
        
        Args:
            category_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            AccuracyFactcheckSetupStatusV1ReportsFactcheckSetupStatusPostResponse: Successful Response
        
        Example:
            ```python
            accuracy = await client.reports.accuracy.factcheck_setup_status_v1_reports_factcheck_setup_status_post(
                category_id="",
            )
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/factcheck-setup-status",
            body=await async_maybe_transform(
            {"category_id": category_id},
            accuracy_factcheck_setup_status_v1_reports_factcheck_setup_status_post_params.AccuracyFactcheckSetupStatusV1ReportsFactcheckSetupStatusPostParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AccuracyFactcheckSetupStatusV1ReportsFactcheckSetupStatusPostResponse,
        )


class AccuracyResourceWithRawResponse:
    def __init__(self, accuracy: AccuracyResource) -> None:
        self._accuracy = accuracy

        self.overview_v1_reports_overview_post = to_raw_response_wrapper(
            accuracy.overview_v1_reports_overview_post,
        )
        self.breakdown_v1_reports_breakdown_post = to_raw_response_wrapper(
            accuracy.breakdown_v1_reports_breakdown_post,
        )
        self.citation_analysis_v1_reports_citation_analysis_post = to_raw_response_wrapper(
            accuracy.citation_analysis_v1_reports_citation_analysis_post,
        )
        self.topic_ids_v1_reports_topic_ids_post = to_raw_response_wrapper(
            accuracy.topic_ids_v1_reports_topic_ids_post,
        )
        self.inaccurate_themes_v1_reports_inaccurate_themes_post = to_raw_response_wrapper(
            accuracy.inaccurate_themes_v1_reports_inaccurate_themes_post,
        )
        self.inaccurate_clusters_v1_reports_inaccurate_clusters_post = to_raw_response_wrapper(
            accuracy.inaccurate_clusters_v1_reports_inaccurate_clusters_post,
        )
        self.inaccuracy_drivers_v1_reports_inaccuracy_drivers_post = to_raw_response_wrapper(
            accuracy.inaccuracy_drivers_v1_reports_inaccuracy_drivers_post,
        )
        self.top_inaccurate_claims_v1_reports_top_inaccurate_claims_post = to_raw_response_wrapper(
            accuracy.top_inaccurate_claims_v1_reports_top_inaccurate_claims_post,
        )
        self.claim_breakdown_v1_reports_claim_breakdown_post = to_raw_response_wrapper(
            accuracy.claim_breakdown_v1_reports_claim_breakdown_post,
        )
        self.claim_citations_v1_reports_claim_citations_post = to_raw_response_wrapper(
            accuracy.claim_citations_v1_reports_claim_citations_post,
        )
        self.cluster_example_runs_v1_reports_cluster_example_runs_post = to_raw_response_wrapper(
            accuracy.cluster_example_runs_v1_reports_cluster_example_runs_post,
        )
        self.cluster_verification_pairs_v1_reports_cluster_verification_pairs_post = to_raw_response_wrapper(
            accuracy.cluster_verification_pairs_v1_reports_cluster_verification_pairs_post,
        )
        self.factcheck_setup_status_v1_reports_factcheck_setup_status_post = to_raw_response_wrapper(
            accuracy.factcheck_setup_status_v1_reports_factcheck_setup_status_post,
        )


class AsyncAccuracyResourceWithRawResponse:
    def __init__(self, accuracy: AsyncAccuracyResource) -> None:
        self._accuracy = accuracy

        self.overview_v1_reports_overview_post = async_to_raw_response_wrapper(
            accuracy.overview_v1_reports_overview_post,
        )
        self.breakdown_v1_reports_breakdown_post = async_to_raw_response_wrapper(
            accuracy.breakdown_v1_reports_breakdown_post,
        )
        self.citation_analysis_v1_reports_citation_analysis_post = async_to_raw_response_wrapper(
            accuracy.citation_analysis_v1_reports_citation_analysis_post,
        )
        self.topic_ids_v1_reports_topic_ids_post = async_to_raw_response_wrapper(
            accuracy.topic_ids_v1_reports_topic_ids_post,
        )
        self.inaccurate_themes_v1_reports_inaccurate_themes_post = async_to_raw_response_wrapper(
            accuracy.inaccurate_themes_v1_reports_inaccurate_themes_post,
        )
        self.inaccurate_clusters_v1_reports_inaccurate_clusters_post = async_to_raw_response_wrapper(
            accuracy.inaccurate_clusters_v1_reports_inaccurate_clusters_post,
        )
        self.inaccuracy_drivers_v1_reports_inaccuracy_drivers_post = async_to_raw_response_wrapper(
            accuracy.inaccuracy_drivers_v1_reports_inaccuracy_drivers_post,
        )
        self.top_inaccurate_claims_v1_reports_top_inaccurate_claims_post = async_to_raw_response_wrapper(
            accuracy.top_inaccurate_claims_v1_reports_top_inaccurate_claims_post,
        )
        self.claim_breakdown_v1_reports_claim_breakdown_post = async_to_raw_response_wrapper(
            accuracy.claim_breakdown_v1_reports_claim_breakdown_post,
        )
        self.claim_citations_v1_reports_claim_citations_post = async_to_raw_response_wrapper(
            accuracy.claim_citations_v1_reports_claim_citations_post,
        )
        self.cluster_example_runs_v1_reports_cluster_example_runs_post = async_to_raw_response_wrapper(
            accuracy.cluster_example_runs_v1_reports_cluster_example_runs_post,
        )
        self.cluster_verification_pairs_v1_reports_cluster_verification_pairs_post = async_to_raw_response_wrapper(
            accuracy.cluster_verification_pairs_v1_reports_cluster_verification_pairs_post,
        )
        self.factcheck_setup_status_v1_reports_factcheck_setup_status_post = async_to_raw_response_wrapper(
            accuracy.factcheck_setup_status_v1_reports_factcheck_setup_status_post,
        )


class AccuracyResourceWithStreamingResponse:
    def __init__(self, accuracy: AccuracyResource) -> None:
        self._accuracy = accuracy

        self.overview_v1_reports_overview_post = to_streamed_response_wrapper(
            accuracy.overview_v1_reports_overview_post,
        )
        self.breakdown_v1_reports_breakdown_post = to_streamed_response_wrapper(
            accuracy.breakdown_v1_reports_breakdown_post,
        )
        self.citation_analysis_v1_reports_citation_analysis_post = to_streamed_response_wrapper(
            accuracy.citation_analysis_v1_reports_citation_analysis_post,
        )
        self.topic_ids_v1_reports_topic_ids_post = to_streamed_response_wrapper(
            accuracy.topic_ids_v1_reports_topic_ids_post,
        )
        self.inaccurate_themes_v1_reports_inaccurate_themes_post = to_streamed_response_wrapper(
            accuracy.inaccurate_themes_v1_reports_inaccurate_themes_post,
        )
        self.inaccurate_clusters_v1_reports_inaccurate_clusters_post = to_streamed_response_wrapper(
            accuracy.inaccurate_clusters_v1_reports_inaccurate_clusters_post,
        )
        self.inaccuracy_drivers_v1_reports_inaccuracy_drivers_post = to_streamed_response_wrapper(
            accuracy.inaccuracy_drivers_v1_reports_inaccuracy_drivers_post,
        )
        self.top_inaccurate_claims_v1_reports_top_inaccurate_claims_post = to_streamed_response_wrapper(
            accuracy.top_inaccurate_claims_v1_reports_top_inaccurate_claims_post,
        )
        self.claim_breakdown_v1_reports_claim_breakdown_post = to_streamed_response_wrapper(
            accuracy.claim_breakdown_v1_reports_claim_breakdown_post,
        )
        self.claim_citations_v1_reports_claim_citations_post = to_streamed_response_wrapper(
            accuracy.claim_citations_v1_reports_claim_citations_post,
        )
        self.cluster_example_runs_v1_reports_cluster_example_runs_post = to_streamed_response_wrapper(
            accuracy.cluster_example_runs_v1_reports_cluster_example_runs_post,
        )
        self.cluster_verification_pairs_v1_reports_cluster_verification_pairs_post = to_streamed_response_wrapper(
            accuracy.cluster_verification_pairs_v1_reports_cluster_verification_pairs_post,
        )
        self.factcheck_setup_status_v1_reports_factcheck_setup_status_post = to_streamed_response_wrapper(
            accuracy.factcheck_setup_status_v1_reports_factcheck_setup_status_post,
        )


class AsyncAccuracyResourceWithStreamingResponse:
    def __init__(self, accuracy: AsyncAccuracyResource) -> None:
        self._accuracy = accuracy

        self.overview_v1_reports_overview_post = async_to_streamed_response_wrapper(
            accuracy.overview_v1_reports_overview_post,
        )
        self.breakdown_v1_reports_breakdown_post = async_to_streamed_response_wrapper(
            accuracy.breakdown_v1_reports_breakdown_post,
        )
        self.citation_analysis_v1_reports_citation_analysis_post = async_to_streamed_response_wrapper(
            accuracy.citation_analysis_v1_reports_citation_analysis_post,
        )
        self.topic_ids_v1_reports_topic_ids_post = async_to_streamed_response_wrapper(
            accuracy.topic_ids_v1_reports_topic_ids_post,
        )
        self.inaccurate_themes_v1_reports_inaccurate_themes_post = async_to_streamed_response_wrapper(
            accuracy.inaccurate_themes_v1_reports_inaccurate_themes_post,
        )
        self.inaccurate_clusters_v1_reports_inaccurate_clusters_post = async_to_streamed_response_wrapper(
            accuracy.inaccurate_clusters_v1_reports_inaccurate_clusters_post,
        )
        self.inaccuracy_drivers_v1_reports_inaccuracy_drivers_post = async_to_streamed_response_wrapper(
            accuracy.inaccuracy_drivers_v1_reports_inaccuracy_drivers_post,
        )
        self.top_inaccurate_claims_v1_reports_top_inaccurate_claims_post = async_to_streamed_response_wrapper(
            accuracy.top_inaccurate_claims_v1_reports_top_inaccurate_claims_post,
        )
        self.claim_breakdown_v1_reports_claim_breakdown_post = async_to_streamed_response_wrapper(
            accuracy.claim_breakdown_v1_reports_claim_breakdown_post,
        )
        self.claim_citations_v1_reports_claim_citations_post = async_to_streamed_response_wrapper(
            accuracy.claim_citations_v1_reports_claim_citations_post,
        )
        self.cluster_example_runs_v1_reports_cluster_example_runs_post = async_to_streamed_response_wrapper(
            accuracy.cluster_example_runs_v1_reports_cluster_example_runs_post,
        )
        self.cluster_verification_pairs_v1_reports_cluster_verification_pairs_post = async_to_streamed_response_wrapper(
            accuracy.cluster_verification_pairs_v1_reports_cluster_verification_pairs_post,
        )
        self.factcheck_setup_status_v1_reports_factcheck_setup_status_post = async_to_streamed_response_wrapper(
            accuracy.factcheck_setup_status_v1_reports_factcheck_setup_status_post,
        )
