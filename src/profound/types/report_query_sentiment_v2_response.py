# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ReportQuerySentimentV2Response",
    "Info",
    "Data",
    "DataScores",
    "DataScoresCurrent",
    "DataScoresPrevious",
    "DataGroupMetadata",
]


class Info(BaseModel):
    query: Dict[str, object]

    total_rows: int


class DataScoresCurrent(BaseModel):
    assessment_count: int

    negative_sentiment: float

    positive_sentiment: float

    occurrence: Optional[float] = None

    response_count: Optional[int] = None

    total_response_count: Optional[int] = None


class DataScoresPrevious(BaseModel):
    assessment_count: int

    negative_sentiment: float

    positive_sentiment: float

    occurrence: Optional[float] = None

    response_count: Optional[int] = None

    total_response_count: Optional[int] = None


class DataScores(BaseModel):
    current: Optional[DataScoresCurrent] = None

    previous: Optional[DataScoresPrevious] = None


class DataGroupMetadata(BaseModel):
    asset_name: Optional[str] = None

    child_count_matching: Optional[int] = None

    child_count_total: Optional[int] = None

    child_matches_search: Optional[bool] = None

    claim: Optional[str] = None

    claim_id: Optional[str] = None

    created_at: Optional[str] = None

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)

    parent_matches_search: Optional[bool] = None

    persona_id: Optional[str] = None

    prompt_id: Optional[str] = None

    prompt_text: Optional[str] = None

    region_id: Optional[str] = None

    run_id: Optional[str] = None

    sentiment: Optional[Literal["positive", "negative"]] = None

    theme: Optional[str] = None

    theme_id: Optional[str] = None

    topic_id: Optional[str] = None


class Data(BaseModel):
    scores: DataScores

    cited_website_hrefs: Optional[List[str]] = None

    date: Optional[str] = None

    group_ids: Optional[Dict[str, str]] = None

    group_metadata: Optional[DataGroupMetadata] = None

    group_names: Optional[Dict[str, str]] = None

    prev_date: Optional[str] = None

    total_count: Optional[int] = None


class ReportQuerySentimentV2Response(BaseModel):
    info: Info

    data: Optional[List[Data]] = None
