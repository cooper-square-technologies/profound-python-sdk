# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.reports import (
    accuracy_create_overview_params,
    accuracy_create_breakdown_params,
    accuracy_create_topic_ids_params,
    accuracy_create_claim_breakdown_params,
    accuracy_create_claim_citations_params,
    accuracy_create_citation_analysis_params,
    accuracy_create_inaccurate_themes_params,
    accuracy_create_inaccuracy_drivers_params,
    accuracy_create_inaccurate_clusters_params,
    accuracy_create_cluster_example_runs_params,
    accuracy_create_top_inaccurate_claims_params,
    accuracy_create_factcheck_setup_status_params,
    accuracy_create_cluster_verification_pairs_params,
)
from ...types.reports.accuracy_create_overview_response import AccuracyCreateOverviewResponse
from ...types.reports.accuracy_create_breakdown_response import AccuracyCreateBreakdownResponse
from ...types.reports.accuracy_create_topic_ids_response import AccuracyCreateTopicIDsResponse
from ...types.reports.accuracy_create_claim_breakdown_response import AccuracyCreateClaimBreakdownResponse
from ...types.reports.accuracy_create_claim_citations_response import AccuracyCreateClaimCitationsResponse
from ...types.reports.accuracy_create_citation_analysis_response import AccuracyCreateCitationAnalysisResponse
from ...types.reports.accuracy_create_inaccurate_themes_response import AccuracyCreateInaccurateThemesResponse
from ...types.reports.accuracy_create_inaccuracy_drivers_response import AccuracyCreateInaccuracyDriversResponse
from ...types.reports.accuracy_create_inaccurate_clusters_response import AccuracyCreateInaccurateClustersResponse
from ...types.reports.accuracy_create_cluster_example_runs_response import AccuracyCreateClusterExampleRunsResponse
from ...types.reports.accuracy_create_top_inaccurate_claims_response import AccuracyCreateTopInaccurateClaimsResponse
from ...types.reports.accuracy_create_factcheck_setup_status_response import AccuracyCreateFactcheckSetupStatusResponse
from ...types.reports.accuracy_create_cluster_verification_pairs_response import (
    AccuracyCreateClusterVerificationPairsResponse,
)

__all__ = ["AccuracyResource", "AsyncAccuracyResource"]


class AccuracyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccuracyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AccuracyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccuracyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AccuracyResourceWithStreamingResponse(self)

    def create_breakdown(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        breakdown_by: Literal["citation", "platform", "topic", "prompt", "tag", "region", "persona"] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        sort_by: Literal["citationShare", "accuracy"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/accuracy/breakdown",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "breakdown_by": breakdown_by,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "limit": limit,
                    "offset": offset,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "search_query": search_query,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
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
        end_date: str,
        start_date: str,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/accuracy/citation-analysis",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "clean_href": clean_href,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                accuracy_create_citation_analysis_params.AccuracyCreateCitationAnalysisParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateCitationAnalysisResponse,
        )

    def create_claim_breakdown(
        self,
        *,
        category_id: str,
        cluster_id: str,
        end_date: str,
        start_date: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/accuracy/claim-breakdown",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "cluster_id": cluster_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
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
        category_id: str,
        cluster_id: str,
        end_date: str,
        start_date: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/accuracy/claim-citations",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "cluster_id": cluster_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "limit": limit,
                    "offset": offset,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "search_query": search_query,
                    "sort_order": sort_order,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
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
        category_id: str,
        cluster_id: str,
        end_date: str,
        start_date: str,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/accuracy/cluster-example-runs",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "cluster_id": cluster_id,
                    "end_date": end_date,
                    "start_date": start_date,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

    def create_inaccuracy_drivers(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        limit: int | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/accuracy/inaccuracy-drivers",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "limit": limit,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
                },
                accuracy_create_inaccuracy_drivers_params.AccuracyCreateInaccuracyDriversParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateInaccuracyDriversResponse,
        )

    def create_inaccurate_clusters(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        theme_id: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/accuracy/inaccurate-clusters",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "theme_id": theme_id,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "limit": limit,
                    "offset": offset,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "search_query": search_query,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
                },
                accuracy_create_inaccurate_clusters_params.AccuracyCreateInaccurateClustersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateInaccurateClustersResponse,
        )

    def create_inaccurate_themes(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        sort_by: Literal["response_share"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/accuracy/inaccurate-themes",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "limit": limit,
                    "offset": offset,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "search_query": search_query,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
                },
                accuracy_create_inaccurate_themes_params.AccuracyCreateInaccurateThemesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateInaccurateThemesResponse,
        )

    def create_overview(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        date_bucket: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        group_by: Literal["period", "theme"] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/accuracy/overview",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_bucket": date_bucket,
                    "exclude_topic_ids": exclude_topic_ids,
                    "group_by": group_by,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
                },
                accuracy_create_overview_params.AccuracyCreateOverviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateOverviewResponse,
        )

    def create_top_inaccurate_claims(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        limit: int | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/accuracy/top-inaccurate-claims",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "limit": limit,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
                },
                accuracy_create_top_inaccurate_claims_params.AccuracyCreateTopInaccurateClaimsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateTopInaccurateClaimsResponse,
        )

    def create_topic_ids(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reports/accuracy/topic-ids",
            body=maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                accuracy_create_topic_ids_params.AccuracyCreateTopicIDsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateTopicIDsResponse,
        )


class AsyncAccuracyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccuracyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAccuracyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccuracyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cooper-square-technologies/profound-python-sdk#with_streaming_response
        """
        return AsyncAccuracyResourceWithStreamingResponse(self)

    async def create_breakdown(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        breakdown_by: Literal["citation", "platform", "topic", "prompt", "tag", "region", "persona"] | Omit = omit,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        sort_by: Literal["citationShare", "accuracy"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/accuracy/breakdown",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "breakdown_by": breakdown_by,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "limit": limit,
                    "offset": offset,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "search_query": search_query,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
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
        end_date: str,
        start_date: str,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/accuracy/citation-analysis",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "clean_href": clean_href,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                accuracy_create_citation_analysis_params.AccuracyCreateCitationAnalysisParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateCitationAnalysisResponse,
        )

    async def create_claim_breakdown(
        self,
        *,
        category_id: str,
        cluster_id: str,
        end_date: str,
        start_date: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/accuracy/claim-breakdown",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "cluster_id": cluster_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
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
        category_id: str,
        cluster_id: str,
        end_date: str,
        start_date: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/accuracy/claim-citations",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "cluster_id": cluster_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "limit": limit,
                    "offset": offset,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "search_query": search_query,
                    "sort_order": sort_order,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
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
        category_id: str,
        cluster_id: str,
        end_date: str,
        start_date: str,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/accuracy/cluster-example-runs",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "cluster_id": cluster_id,
                    "end_date": end_date,
                    "start_date": start_date,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

    async def create_inaccuracy_drivers(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        limit: int | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/accuracy/inaccuracy-drivers",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "limit": limit,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
                },
                accuracy_create_inaccuracy_drivers_params.AccuracyCreateInaccuracyDriversParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateInaccuracyDriversResponse,
        )

    async def create_inaccurate_clusters(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        theme_id: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/accuracy/inaccurate-clusters",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "theme_id": theme_id,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "limit": limit,
                    "offset": offset,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "search_query": search_query,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
                },
                accuracy_create_inaccurate_clusters_params.AccuracyCreateInaccurateClustersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateInaccurateClustersResponse,
        )

    async def create_inaccurate_themes(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        search_query: Optional[str] | Omit = omit,
        sort_by: Literal["response_share"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/accuracy/inaccurate-themes",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "limit": limit,
                    "offset": offset,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "search_query": search_query,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
                },
                accuracy_create_inaccurate_themes_params.AccuracyCreateInaccurateThemesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateInaccurateThemesResponse,
        )

    async def create_overview(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        date_bucket: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        group_by: Literal["period", "theme"] | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/accuracy/overview",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "date_bucket": date_bucket,
                    "exclude_topic_ids": exclude_topic_ids,
                    "group_by": group_by,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
                },
                accuracy_create_overview_params.AccuracyCreateOverviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateOverviewResponse,
        )

    async def create_top_inaccurate_claims(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
        citation_categories: Optional[SequenceNotStr[str]] | Omit = omit,
        comparison_end_date: Optional[str] | Omit = omit,
        comparison_start_date: Optional[str] | Omit = omit,
        exclude_topic_ids: bool | Omit = omit,
        include_no_persona: bool | Omit = omit,
        include_no_tag: bool | Omit = omit,
        limit: int | Omit = omit,
        persona_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        platform_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        prompt_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        region_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tag_filter_type: Literal["all", "any"] | Omit = omit,
        tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        topic_ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/accuracy/top-inaccurate-claims",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                    "citation_categories": citation_categories,
                    "comparison_end_date": comparison_end_date,
                    "comparison_start_date": comparison_start_date,
                    "exclude_topic_ids": exclude_topic_ids,
                    "include_no_persona": include_no_persona,
                    "include_no_tag": include_no_tag,
                    "limit": limit,
                    "persona_ids": persona_ids,
                    "platform_ids": platform_ids,
                    "prompt_ids": prompt_ids,
                    "region_ids": region_ids,
                    "tag_filter_type": tag_filter_type,
                    "tag_ids": tag_ids,
                    "topic_ids": topic_ids,
                },
                accuracy_create_top_inaccurate_claims_params.AccuracyCreateTopInaccurateClaimsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateTopInaccurateClaimsResponse,
        )

    async def create_topic_ids(
        self,
        *,
        category_id: str,
        end_date: str,
        start_date: str,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reports/accuracy/topic-ids",
            body=await async_maybe_transform(
                {
                    "category_id": category_id,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                accuracy_create_topic_ids_params.AccuracyCreateTopicIDsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccuracyCreateTopicIDsResponse,
        )


class AccuracyResourceWithRawResponse:
    def __init__(self, accuracy: AccuracyResource) -> None:
        self._accuracy = accuracy

        self.create_breakdown = to_raw_response_wrapper(
            accuracy.create_breakdown,
        )
        self.create_citation_analysis = to_raw_response_wrapper(
            accuracy.create_citation_analysis,
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
        self.create_inaccuracy_drivers = to_raw_response_wrapper(
            accuracy.create_inaccuracy_drivers,
        )
        self.create_inaccurate_clusters = to_raw_response_wrapper(
            accuracy.create_inaccurate_clusters,
        )
        self.create_inaccurate_themes = to_raw_response_wrapper(
            accuracy.create_inaccurate_themes,
        )
        self.create_overview = to_raw_response_wrapper(
            accuracy.create_overview,
        )
        self.create_top_inaccurate_claims = to_raw_response_wrapper(
            accuracy.create_top_inaccurate_claims,
        )
        self.create_topic_ids = to_raw_response_wrapper(
            accuracy.create_topic_ids,
        )


class AsyncAccuracyResourceWithRawResponse:
    def __init__(self, accuracy: AsyncAccuracyResource) -> None:
        self._accuracy = accuracy

        self.create_breakdown = async_to_raw_response_wrapper(
            accuracy.create_breakdown,
        )
        self.create_citation_analysis = async_to_raw_response_wrapper(
            accuracy.create_citation_analysis,
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
        self.create_inaccuracy_drivers = async_to_raw_response_wrapper(
            accuracy.create_inaccuracy_drivers,
        )
        self.create_inaccurate_clusters = async_to_raw_response_wrapper(
            accuracy.create_inaccurate_clusters,
        )
        self.create_inaccurate_themes = async_to_raw_response_wrapper(
            accuracy.create_inaccurate_themes,
        )
        self.create_overview = async_to_raw_response_wrapper(
            accuracy.create_overview,
        )
        self.create_top_inaccurate_claims = async_to_raw_response_wrapper(
            accuracy.create_top_inaccurate_claims,
        )
        self.create_topic_ids = async_to_raw_response_wrapper(
            accuracy.create_topic_ids,
        )


class AccuracyResourceWithStreamingResponse:
    def __init__(self, accuracy: AccuracyResource) -> None:
        self._accuracy = accuracy

        self.create_breakdown = to_streamed_response_wrapper(
            accuracy.create_breakdown,
        )
        self.create_citation_analysis = to_streamed_response_wrapper(
            accuracy.create_citation_analysis,
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
        self.create_inaccuracy_drivers = to_streamed_response_wrapper(
            accuracy.create_inaccuracy_drivers,
        )
        self.create_inaccurate_clusters = to_streamed_response_wrapper(
            accuracy.create_inaccurate_clusters,
        )
        self.create_inaccurate_themes = to_streamed_response_wrapper(
            accuracy.create_inaccurate_themes,
        )
        self.create_overview = to_streamed_response_wrapper(
            accuracy.create_overview,
        )
        self.create_top_inaccurate_claims = to_streamed_response_wrapper(
            accuracy.create_top_inaccurate_claims,
        )
        self.create_topic_ids = to_streamed_response_wrapper(
            accuracy.create_topic_ids,
        )


class AsyncAccuracyResourceWithStreamingResponse:
    def __init__(self, accuracy: AsyncAccuracyResource) -> None:
        self._accuracy = accuracy

        self.create_breakdown = async_to_streamed_response_wrapper(
            accuracy.create_breakdown,
        )
        self.create_citation_analysis = async_to_streamed_response_wrapper(
            accuracy.create_citation_analysis,
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
        self.create_inaccuracy_drivers = async_to_streamed_response_wrapper(
            accuracy.create_inaccuracy_drivers,
        )
        self.create_inaccurate_clusters = async_to_streamed_response_wrapper(
            accuracy.create_inaccurate_clusters,
        )
        self.create_inaccurate_themes = async_to_streamed_response_wrapper(
            accuracy.create_inaccurate_themes,
        )
        self.create_overview = async_to_streamed_response_wrapper(
            accuracy.create_overview,
        )
        self.create_top_inaccurate_claims = async_to_streamed_response_wrapper(
            accuracy.create_top_inaccurate_claims,
        )
        self.create_topic_ids = async_to_streamed_response_wrapper(
            accuracy.create_topic_ids,
        )
