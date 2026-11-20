# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestVolume:
    @smoke_case(
        "promptVolumes.volume.onTheFly:required", operation="onTheFly", path="/v2/prompt-volumes/volume/on-the-fly"
    )
    def test_method_on_the_fly(self) -> None:
        volume = client.prompt_volumes.volume.on_the_fly(
            matching_type="exact_match",
            start_date="2024-01-01",
            end_date="2024-01-01",
            keyword="x",
        )

    @smoke_case("promptVolumes.volume.onTheFly:all", operation="onTheFly", path="/v2/prompt-volumes/volume/on-the-fly")
    def test_method_on_the_fly_with_all_params(self) -> None:
        volume = client.prompt_volumes.volume.on_the_fly(
            matching_type="exact_match",
            start_date="2024-01-01",
            end_date="2024-01-01",
            regions=[""],
            platforms=["chatgpt.com"],
            keyword="x",
            organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        )
