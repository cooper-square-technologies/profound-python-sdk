# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccuracyCitationAnalysisV1CitationAnalysisPostParams"]


class AccuracyCitationAnalysisV1CitationAnalysisPostParams(TypedDict, total=False):
    category_id: Required[str]

    clean_href: Required[str]

    start_date: Required[str]

    end_date: Required[str]
