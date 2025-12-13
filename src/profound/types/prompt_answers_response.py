# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PromptAnswersResponse", "Data", "DataSentimentTheme"]


class DataSentimentTheme(BaseModel):
    name: str

    type: Literal["positive", "negative"]


class Data(BaseModel):
    """Raw data for the answers endpoint."""

    asset: Optional[str] = None

    citations: Optional[List[str]] = None

    created_at: Optional[datetime] = None

    mentions: Optional[List[str]] = None

    model: Optional[str] = None

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)

    persona: Optional[str] = None

    prompt: Optional[str] = None

    prompt_id: Optional[str] = None

    prompt_type: Optional[str] = None

    region: Optional[str] = None

    response: Optional[str] = None

    run_id: Optional[str] = None

    search_queries: Optional[List[str]] = None

    sentiment_themes: Optional[List[DataSentimentTheme]] = None

    tags: Optional[List[str]] = None

    themes: Optional[List[str]] = None

    topic: Optional[str] = None


class PromptAnswersResponse(BaseModel):
    """Response for the answers endpoint."""

    data: List[Data]

    info: Dict[str, object]
