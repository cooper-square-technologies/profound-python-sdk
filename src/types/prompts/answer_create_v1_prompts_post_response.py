# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AnswerCreateV1PromptsPostResponse", "AnswersResponseInfo", "AnswersRawData", "CitationDetail", "CitationDetailGroup", "SentimentTheme"]


class SentimentTheme(BaseModel):

    type: Union[Literal["positive"], Literal["negative"]]

    name: str

class CitationDetailGroup(BaseModel):

    group_id: int

    group_position: int

class CitationDetail(BaseModel):

    url: str

    clean_url: str

    title: str

    text: Optional[str] = None

    hostname: str

    path: str

    first_cited_at: Optional[str] = None

    positions: Optional[List[int]] = None

    groups: Optional[List[CitationDetailGroup]] = None

    citation_category: Optional[str] = None

class AnswersRawData(BaseModel):

    run_id: Optional[str] = None

    created_at: Optional[datetime] = None

    prompt: Optional[str] = None

    prompt_id: Optional[str] = None

    mentions: Optional[List[str]] = None

    analysis_types: Optional[List[str]] = None

    prompt_type: Optional[str] = None

    response: Optional[str] = None

    citations: Optional[List[str]] = None

    citation_details: Optional[List[CitationDetail]] = None

    web_search_results: Optional[List[str]] = None

    search_triggered: Optional[bool] = None

    themes: Optional[List[str]] = None

    sentiment_themes: Optional[List[SentimentTheme]] = None
    """Uses legacy sentiment data."""

    search_queries: Optional[List[str]] = None

    topic: Optional[str] = None

    topic_id: Optional[str] = None

    region: Optional[str] = None

    model: Optional[str] = None

    model_id: Optional[str] = None

    asset: Optional[str] = None

    asset_id: Optional[str] = None

    tags: Optional[List[str]] = None

    persona: Optional[str] = None

class AnswersResponseInfo(BaseModel):

    total_rows: int



class AnswerCreateV1PromptsPostResponse(BaseModel):

    info: AnswersResponseInfo

    data: List[AnswersRawData]
