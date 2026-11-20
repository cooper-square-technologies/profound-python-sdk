# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccuracyCreateClusterVerificationPairsParams"]


class AccuracyCreateClusterVerificationPairsParams(TypedDict, total=False):
    category_id: Required[str]
    """Category UUID. Access is enforced before the tool runs."""

    cluster_id: Required[str]
    """Claim cluster UUID returned by a FactCheck table."""
