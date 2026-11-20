# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestAdAccount:
    @smoke_case(
        "ads.openaiAds.adAccount.retrieveInsights:required",
        operation="retrieveInsights",
        path="/v1/ads/openai-ads/ad-account/insights",
    )
    def test_method_retrieve_insights(self) -> None:
        ad_account = client.ads.openai_ads.ad_account.retrieve_insights()

    @smoke_case(
        "ads.openaiAds.adAccount.retrieveInsights:all",
        operation="retrieveInsights",
        path="/v1/ads/openai-ads/ad-account/insights",
    )
    def test_method_retrieve_insights_with_all_params(self) -> None:
        ad_account = client.ads.openai_ads.ad_account.retrieve_insights(
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            aggregation_level="ad_account",
            time_granularity="hourly",
            time_ranges=["time_range"],
            limit=1,
            after="after",
            before="before",
        )
