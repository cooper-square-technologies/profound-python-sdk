# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["UpdatePromptsBody", "UpdatePromptInput"]


class UpdatePromptInput(BaseModel):

    id: str
    """ID of the prompt to update."""

    prompt: Optional[str] = None
    """New prompt text."""

    topic: Optional[object] = None
    """New topic. A new topic is created if the name doesn't exist."""

    language: Optional[str] = None
    """New language code. Must be enabled for the organization."""

    tags: Optional[List[object]] = None
    """New tag set. Replaces all existing tags on the prompt."""

    regions: Optional[List[object]] = None
    """New region set. Replaces all existing regions."""

    platforms: Optional[List[object]] = None
    """New platform set. Replaces all existing platforms."""

    personas: Optional[List[object]] = None
    """New persona set. Replaces all existing personas."""

    analysis_types: Optional[List[Literal["visibility", "sentiment", "sentiment_v2", "accuracy"]]] = None
    """New analysis types. Replaces all existing analysis types on the prompt."""

    prompt_type: Optional[str] = None
    """Deprecated. Use analysis_types instead."""

    asset: Optional[object] = None
    """Asset reference. Required when analysis_types includes 'sentiment'."""



class UpdatePromptsBody(BaseModel):

    prompts: List[UpdatePromptInput]
    """List of prompt updates. Each entry must include an `id` and at least one field to change."""

    dry_run: Optional[bool] = None
    """When true, validate and preview changes without persisting them."""
