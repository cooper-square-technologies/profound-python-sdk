# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ReportSentimentV2Response",
    "Info",
    "Data",
    "DataScores",
    "DataScoresCurrent",
    "DataScoresPrevious",
    "DataGroupMetadata",
]


class DataGroupMetadata(BaseModel):
    theme: Optional[str] = None

    claim: Optional[str] = None

    sentiment: Optional[Literal["positive", "negative"]] = None

    prompt_id: Optional[str] = None

    prompt_text: Optional[str] = None

    topic_id: Optional[str] = None

    run_id: Optional[str] = None

    created_at: Optional[str] = None

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)

    region_id: Optional[str] = None

    persona_id: Optional[str] = None

    asset_name: Optional[str] = None

    child_count_total: Optional[int] = None

    child_count_matching: Optional[int] = None

    parent_matches_search: Optional[bool] = None

    child_matches_search: Optional[bool] = None


class DataScoresPrevious(BaseModel):
    positive_sentiment: float

    negative_sentiment: float

    assessment_count: int

    occurrence: Optional[float] = None

    response_count: Optional[int] = None

    total_response_count: Optional[int] = None


class DataScoresCurrent(BaseModel):
    positive_sentiment: float

    negative_sentiment: float

    assessment_count: int

    occurrence: Optional[float] = None

    response_count: Optional[int] = None

    total_response_count: Optional[int] = None


class DataScores(BaseModel):
    current: Optional[DataScoresCurrent] = None

    previous: Optional[DataScoresPrevious] = None


class Data(BaseModel):
    scores: DataScores

    date: Optional[str] = None

    prev_date: Optional[str] = None

    group_ids: Optional[Dict[str, str]] = None

    group_names: Optional[Dict[str, str]] = None

    group_metadata: Optional[DataGroupMetadata] = None

    cited_website_hrefs: Optional[List[str]] = None

    total_count: Optional[int] = None


class Info(BaseModel):
    query: Dict[str, object]

    total_rows: int


class ReportSentimentV2Response(BaseModel):
    info: Info

    data: Optional[List[Data]] = None
