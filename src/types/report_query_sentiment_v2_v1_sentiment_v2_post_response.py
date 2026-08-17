# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ReportQuerySentimentV2V1SentimentV2PostResponse", "SentimentV2ReportInfo", "Query", "SentimentDataPoint", "SentimentPeriodScores", "SentimentScores", "SentimentGroupMetadata"]


class SentimentGroupMetadata(BaseModel):

    theme_id: Optional[str] = None

    theme: Optional[str] = None

    claim_id: Optional[str] = None

    claim: Optional[str] = None

    sentiment: Optional[Literal["positive", "negative"]] = None

    prompt_id: Optional[str] = None

    prompt_text: Optional[str] = None

    topic_id: Optional[str] = None

    run_id: Optional[str] = None

    created_at: Optional[str] = None

    model_id: Optional[str] = None

    region_id: Optional[str] = None

    persona_id: Optional[str] = None

    asset_name: Optional[str] = None

    child_count_total: Optional[int] = None

    child_count_matching: Optional[int] = None

    parent_matches_search: Optional[bool] = None

    child_matches_search: Optional[bool] = None

class SentimentScores(BaseModel):

    positive_sentiment: float

    negative_sentiment: float

    assessment_count: int

    occurrence: Optional[float] = None

    response_count: Optional[int] = None

    total_response_count: Optional[int] = None

class SentimentPeriodScores(BaseModel):

    current: Optional[SentimentScores] = None

    previous: Optional[SentimentScores] = None

class SentimentDataPoint(BaseModel):

    scores: SentimentPeriodScores

    date: Optional[str] = None

    prev_date: Optional[str] = None

    group_ids: Optional[Dict[str, str]] = None

    group_names: Optional[Dict[str, str]] = None

    group_metadata: Optional[SentimentGroupMetadata] = None

    cited_website_hrefs: Optional[List[str]] = None

    total_count: Optional[int] = None

class Query(BaseModel):
    pass

class SentimentV2ReportInfo(BaseModel):

    query: Query

    total_rows: int



class ReportQuerySentimentV2V1SentimentV2PostResponse(BaseModel):

    info: SentimentV2ReportInfo

    data: Optional[List[SentimentDataPoint]] = None
