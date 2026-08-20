# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional
from typing_extensions import Literal
from ..._types import SequenceNotStr

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.reports.accuracy_create_overview_response import AccuracyCreateOverviewResponse
from ...types.reports import (
    accuracy_create_overview_params,
    accuracy_create_breakdown_params,
    accuracy_create_citation_analysis_params,
    accuracy_create_topic_ids_params,
    accuracy_create_inaccurate_themes_params,
    accuracy_create_inaccurate_clusters_params,
    accuracy_create_inaccuracy_drivers_params,
    accuracy_create_top_inaccurate_claims_params,
    accuracy_create_claim_breakdown_params,
    accuracy_create_claim_citations_params,
    accuracy_create_cluster_example_runs_params,
    accuracy_create_cluster_verification_pairs_params,
    accuracy_create_factcheck_setup_status_params,
)
from ...types.reports.accuracy_create_breakdown_response import AccuracyCreateBreakdownResponse
from ...types.reports.accuracy_create_citation_analysis_response import AccuracyCreateCitationAnalysisResponse
from ...types.reports.accuracy_create_topic_ids_response import AccuracyCreateTopicIDsResponse
from ...types.reports.accuracy_create_inaccurate_themes_response import AccuracyCreateInaccurateThemesResponse
from ...types.reports.accuracy_create_inaccurate_clusters_response import AccuracyCreateInaccurateClustersResponse
from ...types.reports.accuracy_create_inaccuracy_drivers_response import AccuracyCreateInaccuracyDriversResponse
from ...types.reports.accuracy_create_top_inaccurate_claims_response import AccuracyCreateTopInaccurateClaimsResponse
from ...types.reports.accuracy_create_claim_breakdown_response import AccuracyCreateClaimBreakdownResponse
from ...types.reports.accuracy_create_claim_citations_response import AccuracyCreateClaimCitationsResponse
from ...types.reports.accuracy_create_cluster_example_runs_response import AccuracyCreateClusterExampleRunsResponse
from ...types.reports.accuracy_create_cluster_verification_pairs_response import (
    AccuracyCreateClusterVerificationPairsResponse,
)
from ...types.reports.accuracy_create_factcheck_setup_status_response import AccuracyCreateFactcheckSetupStatusResponse

__all__ = ["AccuracyResource", "AsyncAccuracyResource"]


class AccuracyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccuracyResourceWithRawResponse:
        return AccuracyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccuracyResourceWithStreamingResponse:
        return AccuracyResourceWithStreamingResponse(self)

    def create_overview(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        date_bucket: Optional[str] | Omit = omit,
        group_by: Literal["period", "theme"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateOverviewResponse:
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
            AccuracyCreateOverviewResponse: Successful Response

        Example:
            ```python
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
                accuracy_create_overview_params.AccuracyCreateOverviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateOverviewResponse,
        )

    def create_breakdown(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        breakdown_by: Literal["citation", "platform", "topic", "prompt", "tag", "region", "persona", "theme"]
        | Omit = omit,
        group_by: Optional[List[Literal["platform", "topic", "prompt", "tag", "region", "persona", "theme", "date"]]]
        | Omit = omit,
        date_bucket: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        sort_by: Literal["citationShare", "accuracy"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        pagination: Optional[accuracy_create_breakdown_params.Pagination] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateBreakdownResponse:
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
            group_by: Body parameter.
            date_bucket: Body parameter.
            limit: Body parameter.
            offset: Body parameter.
            search_query: Body parameter.
            sort_by: Body parameter.
            sort_order: Body parameter.
            pagination: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccuracyCreateBreakdownResponse: Successful Response

        Example:
            ```python
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
                    "group_by": group_by,
                    "date_bucket": date_bucket,
                    "limit": limit,
                    "offset": offset,
                    "search_query": search_query,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                    "pagination": pagination,
                },
                accuracy_create_breakdown_params.AccuracyCreateBreakdownParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateBreakdownResponse,
        )

    def create_citation_analysis(
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
    ) -> AccuracyCreateCitationAnalysisResponse:
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
            AccuracyCreateCitationAnalysisResponse: Successful Response

        Example:
            ```python
            accuracy = client.reports.accuracy.create_citation_analysis(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
                accuracy_create_citation_analysis_params.AccuracyCreateCitationAnalysisParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateCitationAnalysisResponse,
        )

    def create_topic_ids(
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
    ) -> AccuracyCreateTopicIDsResponse:
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
            AccuracyCreateTopicIDsResponse: Successful Response

        Example:
            ```python
            accuracy = client.reports.accuracy.create_topic_ids(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
                accuracy_create_topic_ids_params.AccuracyCreateTopicIDsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateTopicIDsResponse,
        )

    def create_inaccurate_themes(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
    ) -> AccuracyCreateInaccurateThemesResponse:
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
            AccuracyCreateInaccurateThemesResponse: Successful Response

        Example:
            ```python
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
                accuracy_create_inaccurate_themes_params.AccuracyCreateInaccurateThemesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateInaccurateThemesResponse,
        )

    def create_inaccurate_clusters(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        theme_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        include_models: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateInaccurateClustersResponse:
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
            include_models: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccuracyCreateInaccurateClustersResponse: Successful Response

        Example:
            ```python
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
                    "include_models": include_models,
                },
                accuracy_create_inaccurate_clusters_params.AccuracyCreateInaccurateClustersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateInaccurateClustersResponse,
        )

    def create_inaccuracy_drivers(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateInaccuracyDriversResponse:
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
            AccuracyCreateInaccuracyDriversResponse: Successful Response

        Example:
            ```python
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
                accuracy_create_inaccuracy_drivers_params.AccuracyCreateInaccuracyDriversParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateInaccuracyDriversResponse,
        )

    def create_top_inaccurate_claims(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateTopInaccurateClaimsResponse:
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
            AccuracyCreateTopInaccurateClaimsResponse: Successful Response

        Example:
            ```python
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
                accuracy_create_top_inaccurate_claims_params.AccuracyCreateTopInaccurateClaimsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateTopInaccurateClaimsResponse,
        )

    def create_claim_breakdown(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        cluster_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateClaimBreakdownResponse:
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
            AccuracyCreateClaimBreakdownResponse: Successful Response

        Example:
            ```python
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
                accuracy_create_claim_breakdown_params.AccuracyCreateClaimBreakdownParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateClaimBreakdownResponse,
        )

    def create_claim_citations(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
    ) -> AccuracyCreateClaimCitationsResponse:
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
            AccuracyCreateClaimCitationsResponse: Successful Response

        Example:
            ```python
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
                accuracy_create_claim_citations_params.AccuracyCreateClaimCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateClaimCitationsResponse,
        )

    def create_cluster_example_runs(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        cluster_id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateClusterExampleRunsResponse:
        """
        Accuracy Cluster Example Runs

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
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccuracyCreateClusterExampleRunsResponse: Successful Response

        Example:
            ```python
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
            ```
        """
        return self._post(
            "/v1/reports/accuracy/cluster-example-runs",
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
                },
                accuracy_create_cluster_example_runs_params.AccuracyCreateClusterExampleRunsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateClusterExampleRunsResponse,
        )

    def create_cluster_verification_pairs(
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
    ) -> AccuracyCreateClusterVerificationPairsResponse:
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
            AccuracyCreateClusterVerificationPairsResponse: Successful Response

        Example:
            ```python
            accuracy = client.reports.accuracy.create_cluster_verification_pairs(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
                accuracy_create_cluster_verification_pairs_params.AccuracyCreateClusterVerificationPairsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateClusterVerificationPairsResponse,
        )

    def create_factcheck_setup_status(
        self,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateFactcheckSetupStatusResponse:
        """
        Accuracy Factcheck Setup Status

        Args:
            category_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccuracyCreateFactcheckSetupStatusResponse: Successful Response

        Example:
            ```python
            accuracy = client.reports.accuracy.create_factcheck_setup_status(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        return self._post(
            "/v1/reports/accuracy/factcheck-setup-status",
            body=maybe_transform(
                {"category_id": category_id},
                accuracy_create_factcheck_setup_status_params.AccuracyCreateFactcheckSetupStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateFactcheckSetupStatusResponse,
        )


class AsyncAccuracyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccuracyResourceWithRawResponse:
        return AsyncAccuracyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccuracyResourceWithStreamingResponse:
        return AsyncAccuracyResourceWithStreamingResponse(self)

    async def create_overview(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        date_bucket: Optional[str] | Omit = omit,
        group_by: Literal["period", "theme"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateOverviewResponse:
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
            AccuracyCreateOverviewResponse: Successful Response

        Example:
            ```python
            accuracy = await client.reports.accuracy.create_overview(
                start_date="",
                end_date="",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                exclude_topic_ids=False,
                tag_filter_type="any",
                include_no_tag=False,
                include_no_persona=False,
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
                accuracy_create_overview_params.AccuracyCreateOverviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateOverviewResponse,
        )

    async def create_breakdown(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        breakdown_by: Literal["citation", "platform", "topic", "prompt", "tag", "region", "persona", "theme"]
        | Omit = omit,
        group_by: Optional[List[Literal["platform", "topic", "prompt", "tag", "region", "persona", "theme", "date"]]]
        | Omit = omit,
        date_bucket: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        sort_by: Literal["citationShare", "accuracy"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        pagination: Optional[accuracy_create_breakdown_params.Pagination] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateBreakdownResponse:
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
            group_by: Body parameter.
            date_bucket: Body parameter.
            limit: Body parameter.
            offset: Body parameter.
            search_query: Body parameter.
            sort_by: Body parameter.
            sort_order: Body parameter.
            pagination: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccuracyCreateBreakdownResponse: Successful Response

        Example:
            ```python
            accuracy = await client.reports.accuracy.create_breakdown(
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
                    "group_by": group_by,
                    "date_bucket": date_bucket,
                    "limit": limit,
                    "offset": offset,
                    "search_query": search_query,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                    "pagination": pagination,
                },
                accuracy_create_breakdown_params.AccuracyCreateBreakdownParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateBreakdownResponse,
        )

    async def create_citation_analysis(
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
    ) -> AccuracyCreateCitationAnalysisResponse:
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
            AccuracyCreateCitationAnalysisResponse: Successful Response

        Example:
            ```python
            accuracy = await client.reports.accuracy.create_citation_analysis(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
                accuracy_create_citation_analysis_params.AccuracyCreateCitationAnalysisParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateCitationAnalysisResponse,
        )

    async def create_topic_ids(
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
    ) -> AccuracyCreateTopicIDsResponse:
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
            AccuracyCreateTopicIDsResponse: Successful Response

        Example:
            ```python
            accuracy = await client.reports.accuracy.create_topic_ids(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
                accuracy_create_topic_ids_params.AccuracyCreateTopicIDsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateTopicIDsResponse,
        )

    async def create_inaccurate_themes(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
    ) -> AccuracyCreateInaccurateThemesResponse:
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
            AccuracyCreateInaccurateThemesResponse: Successful Response

        Example:
            ```python
            accuracy = await client.reports.accuracy.create_inaccurate_themes(
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
                accuracy_create_inaccurate_themes_params.AccuracyCreateInaccurateThemesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateInaccurateThemesResponse,
        )

    async def create_inaccurate_clusters(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        theme_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        include_models: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateInaccurateClustersResponse:
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
            include_models: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccuracyCreateInaccurateClustersResponse: Successful Response

        Example:
            ```python
            accuracy = await client.reports.accuracy.create_inaccurate_clusters(
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
                    "include_models": include_models,
                },
                accuracy_create_inaccurate_clusters_params.AccuracyCreateInaccurateClustersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateInaccurateClustersResponse,
        )

    async def create_inaccuracy_drivers(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateInaccuracyDriversResponse:
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
            AccuracyCreateInaccuracyDriversResponse: Successful Response

        Example:
            ```python
            accuracy = await client.reports.accuracy.create_inaccuracy_drivers(
                start_date="",
                end_date="",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                exclude_topic_ids=False,
                tag_filter_type="any",
                include_no_tag=False,
                include_no_persona=False,
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
                accuracy_create_inaccuracy_drivers_params.AccuracyCreateInaccuracyDriversParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateInaccuracyDriversResponse,
        )

    async def create_top_inaccurate_claims(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateTopInaccurateClaimsResponse:
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
            AccuracyCreateTopInaccurateClaimsResponse: Successful Response

        Example:
            ```python
            accuracy = await client.reports.accuracy.create_top_inaccurate_claims(
                start_date="",
                end_date="",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                exclude_topic_ids=False,
                tag_filter_type="any",
                include_no_tag=False,
                include_no_persona=False,
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
                accuracy_create_top_inaccurate_claims_params.AccuracyCreateTopInaccurateClaimsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateTopInaccurateClaimsResponse,
        )

    async def create_claim_breakdown(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        cluster_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateClaimBreakdownResponse:
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
            AccuracyCreateClaimBreakdownResponse: Successful Response

        Example:
            ```python
            accuracy = await client.reports.accuracy.create_claim_breakdown(
                start_date="",
                end_date="",
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                exclude_topic_ids=False,
                tag_filter_type="any",
                include_no_tag=False,
                include_no_persona=False,
                cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
                accuracy_create_claim_breakdown_params.AccuracyCreateClaimBreakdownParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateClaimBreakdownResponse,
        )

    async def create_claim_citations(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
    ) -> AccuracyCreateClaimCitationsResponse:
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
            AccuracyCreateClaimCitationsResponse: Successful Response

        Example:
            ```python
            accuracy = await client.reports.accuracy.create_claim_citations(
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
                accuracy_create_claim_citations_params.AccuracyCreateClaimCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateClaimCitationsResponse,
        )

    async def create_cluster_example_runs(
        self,
        *,
        start_date: str,
        end_date: str,
        comparison_start_date: Optional[str] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        category_id: str,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        include_no_tag: bool | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        cluster_id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateClusterExampleRunsResponse:
        """
        Accuracy Cluster Example Runs

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
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccuracyCreateClusterExampleRunsResponse: Successful Response

        Example:
            ```python
            accuracy = await client.reports.accuracy.create_cluster_example_runs(
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
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/cluster-example-runs",
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
                },
                accuracy_create_cluster_example_runs_params.AccuracyCreateClusterExampleRunsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateClusterExampleRunsResponse,
        )

    async def create_cluster_verification_pairs(
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
    ) -> AccuracyCreateClusterVerificationPairsResponse:
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
            AccuracyCreateClusterVerificationPairsResponse: Successful Response

        Example:
            ```python
            accuracy = await client.reports.accuracy.create_cluster_verification_pairs(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                cluster_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
                accuracy_create_cluster_verification_pairs_params.AccuracyCreateClusterVerificationPairsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateClusterVerificationPairsResponse,
        )

    async def create_factcheck_setup_status(
        self,
        *,
        category_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccuracyCreateFactcheckSetupStatusResponse:
        """
        Accuracy Factcheck Setup Status

        Args:
            category_id: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccuracyCreateFactcheckSetupStatusResponse: Successful Response

        Example:
            ```python
            accuracy = await client.reports.accuracy.create_factcheck_setup_status(
                category_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        return await self._post(
            "/v1/reports/accuracy/factcheck-setup-status",
            body=await async_maybe_transform(
                {"category_id": category_id},
                accuracy_create_factcheck_setup_status_params.AccuracyCreateFactcheckSetupStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateFactcheckSetupStatusResponse,
        )


class AccuracyResourceWithRawResponse:
    def __init__(self, accuracy: AccuracyResource) -> None:
        self._accuracy = accuracy

        self.create_overview = to_raw_response_wrapper(
            accuracy.create_overview,
        )
        self.create_breakdown = to_raw_response_wrapper(
            accuracy.create_breakdown,
        )
        self.create_citation_analysis = to_raw_response_wrapper(
            accuracy.create_citation_analysis,
        )
        self.create_topic_ids = to_raw_response_wrapper(
            accuracy.create_topic_ids,
        )
        self.create_inaccurate_themes = to_raw_response_wrapper(
            accuracy.create_inaccurate_themes,
        )
        self.create_inaccurate_clusters = to_raw_response_wrapper(
            accuracy.create_inaccurate_clusters,
        )
        self.create_inaccuracy_drivers = to_raw_response_wrapper(
            accuracy.create_inaccuracy_drivers,
        )
        self.create_top_inaccurate_claims = to_raw_response_wrapper(
            accuracy.create_top_inaccurate_claims,
        )
        self.create_claim_breakdown = to_raw_response_wrapper(
            accuracy.create_claim_breakdown,
        )
        self.create_claim_citations = to_raw_response_wrapper(
            accuracy.create_claim_citations,
        )
        self.create_cluster_example_runs = to_raw_response_wrapper(
            accuracy.create_cluster_example_runs,
        )
        self.create_cluster_verification_pairs = to_raw_response_wrapper(
            accuracy.create_cluster_verification_pairs,
        )
        self.create_factcheck_setup_status = to_raw_response_wrapper(
            accuracy.create_factcheck_setup_status,
        )


class AsyncAccuracyResourceWithRawResponse:
    def __init__(self, accuracy: AsyncAccuracyResource) -> None:
        self._accuracy = accuracy

        self.create_overview = async_to_raw_response_wrapper(
            accuracy.create_overview,
        )
        self.create_breakdown = async_to_raw_response_wrapper(
            accuracy.create_breakdown,
        )
        self.create_citation_analysis = async_to_raw_response_wrapper(
            accuracy.create_citation_analysis,
        )
        self.create_topic_ids = async_to_raw_response_wrapper(
            accuracy.create_topic_ids,
        )
        self.create_inaccurate_themes = async_to_raw_response_wrapper(
            accuracy.create_inaccurate_themes,
        )
        self.create_inaccurate_clusters = async_to_raw_response_wrapper(
            accuracy.create_inaccurate_clusters,
        )
        self.create_inaccuracy_drivers = async_to_raw_response_wrapper(
            accuracy.create_inaccuracy_drivers,
        )
        self.create_top_inaccurate_claims = async_to_raw_response_wrapper(
            accuracy.create_top_inaccurate_claims,
        )
        self.create_claim_breakdown = async_to_raw_response_wrapper(
            accuracy.create_claim_breakdown,
        )
        self.create_claim_citations = async_to_raw_response_wrapper(
            accuracy.create_claim_citations,
        )
        self.create_cluster_example_runs = async_to_raw_response_wrapper(
            accuracy.create_cluster_example_runs,
        )
        self.create_cluster_verification_pairs = async_to_raw_response_wrapper(
            accuracy.create_cluster_verification_pairs,
        )
        self.create_factcheck_setup_status = async_to_raw_response_wrapper(
            accuracy.create_factcheck_setup_status,
        )


class AccuracyResourceWithStreamingResponse:
    def __init__(self, accuracy: AccuracyResource) -> None:
        self._accuracy = accuracy

        self.create_overview = to_streamed_response_wrapper(
            accuracy.create_overview,
        )
        self.create_breakdown = to_streamed_response_wrapper(
            accuracy.create_breakdown,
        )
        self.create_citation_analysis = to_streamed_response_wrapper(
            accuracy.create_citation_analysis,
        )
        self.create_topic_ids = to_streamed_response_wrapper(
            accuracy.create_topic_ids,
        )
        self.create_inaccurate_themes = to_streamed_response_wrapper(
            accuracy.create_inaccurate_themes,
        )
        self.create_inaccurate_clusters = to_streamed_response_wrapper(
            accuracy.create_inaccurate_clusters,
        )
        self.create_inaccuracy_drivers = to_streamed_response_wrapper(
            accuracy.create_inaccuracy_drivers,
        )
        self.create_top_inaccurate_claims = to_streamed_response_wrapper(
            accuracy.create_top_inaccurate_claims,
        )
        self.create_claim_breakdown = to_streamed_response_wrapper(
            accuracy.create_claim_breakdown,
        )
        self.create_claim_citations = to_streamed_response_wrapper(
            accuracy.create_claim_citations,
        )
        self.create_cluster_example_runs = to_streamed_response_wrapper(
            accuracy.create_cluster_example_runs,
        )
        self.create_cluster_verification_pairs = to_streamed_response_wrapper(
            accuracy.create_cluster_verification_pairs,
        )
        self.create_factcheck_setup_status = to_streamed_response_wrapper(
            accuracy.create_factcheck_setup_status,
        )


class AsyncAccuracyResourceWithStreamingResponse:
    def __init__(self, accuracy: AsyncAccuracyResource) -> None:
        self._accuracy = accuracy

        self.create_overview = async_to_streamed_response_wrapper(
            accuracy.create_overview,
        )
        self.create_breakdown = async_to_streamed_response_wrapper(
            accuracy.create_breakdown,
        )
        self.create_citation_analysis = async_to_streamed_response_wrapper(
            accuracy.create_citation_analysis,
        )
        self.create_topic_ids = async_to_streamed_response_wrapper(
            accuracy.create_topic_ids,
        )
        self.create_inaccurate_themes = async_to_streamed_response_wrapper(
            accuracy.create_inaccurate_themes,
        )
        self.create_inaccurate_clusters = async_to_streamed_response_wrapper(
            accuracy.create_inaccurate_clusters,
        )
        self.create_inaccuracy_drivers = async_to_streamed_response_wrapper(
            accuracy.create_inaccuracy_drivers,
        )
        self.create_top_inaccurate_claims = async_to_streamed_response_wrapper(
            accuracy.create_top_inaccurate_claims,
        )
        self.create_claim_breakdown = async_to_streamed_response_wrapper(
            accuracy.create_claim_breakdown,
        )
        self.create_claim_citations = async_to_streamed_response_wrapper(
            accuracy.create_claim_citations,
        )
        self.create_cluster_example_runs = async_to_streamed_response_wrapper(
            accuracy.create_cluster_example_runs,
        )
        self.create_cluster_verification_pairs = async_to_streamed_response_wrapper(
            accuracy.create_cluster_verification_pairs,
        )
        self.create_factcheck_setup_status = async_to_streamed_response_wrapper(
            accuracy.create_factcheck_setup_status,
        )
