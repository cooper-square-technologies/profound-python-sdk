# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CreatePromptsBody", "CreatePromptInput"]


class CreatePromptInput(BaseModel):

    prompt: str
    """The prompt text to be sent to AI platforms."""

    topic: object
    """Topic to assign. A new topic is created if the name doesn't exist."""

    language: str
    """Language code (e.g. 'en-US')"""

    tags: Optional[List[object]] = None
    """Tags to assign. New tags are created if names don't exist."""

    regions: List[object]
    """Regions where the prompt will be collected."""

    platforms: List[object]
    """AI platforms where the prompt will be collected."""

    personas: Optional[List[object]] = None
    """Personas to use when collecting. Omit for default (no persona)."""

    analysis_types: Optional[List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]] = None
    """Analysis types: 'visibility', 'sentiment', 'accuracy'. Defaults to ['visibility']."""

    prompt_type: Optional[str] = None
    """Deprecated. Use analysis_types instead. 'Visibility' or 'Sentiment'."""

    asset: Optional[object] = None
    """Required for Sentiment prompts. The brand asset to evaluate."""



class CreatePromptsBody(BaseModel):

    prompts: List[CreatePromptInput]
    """List of prompts to create."""

    dry_run: Optional[bool] = None
    """When true, validate and preview changes without persisting them."""
