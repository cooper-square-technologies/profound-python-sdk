# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PromptAnswersResponse", "Data"]


class Data(BaseModel):
    asset: Optional[str] = None

    citations: Optional[List[str]] = None

    created_at: Optional[datetime] = None

    mentions: Optional[List[str]] = None

    model: Optional[str] = None

    persona: Optional[str] = None

    prompt: Optional[str] = None

    prompt_id: Optional[str] = None

    prompt_type: Optional[str] = None

    region: Optional[str] = None

    response: Optional[str] = None

    run_id: Optional[str] = None

    search_queries: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    themes: Optional[List[str]] = None

    topic: Optional[str] = None


class PromptAnswersResponse(BaseModel):
    data: List[Data]

    info: Dict[str, object]
