# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccuracyTopicIdsV1ReportsTopicIdsPostParams"]


class AccuracyTopicIdsV1ReportsTopicIdsPostParams(TypedDict, total=False):

    category_id: Required[str]

    start_date: Required[str]

    end_date: Required[str]
