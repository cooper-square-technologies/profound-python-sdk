# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OptimizationRetrieveResponse", "ContentAnalysis", "DocumentContent", "AeoScore", "AeoScoreTargetZone", "AnalysisSummary", "AnalysisBreakdown", "Recommendation", "RecommendationImpact", "RecommendationSuggestion", "AnalysisInputs", "TopicInput", "PromptInput", "UserInput"]


class UserInput(BaseModel):

    type: Literal["file", "text", "url"]

    value: str

    metadata: Dict[str, Union[int, str]]

class PromptInput(BaseModel):

    id: str

    name: str

class TopicInput(BaseModel):

    id: str

    name: str

class AnalysisInputs(BaseModel):

    topic: Optional[TopicInput] = None

    prompt: Optional[PromptInput] = None

    top_citations: List[str]

    user: UserInput

class RecommendationSuggestion(BaseModel):

    text: str

    rationale: str

class RecommendationImpact(BaseModel):

    section: str

    score: float

class Recommendation(BaseModel):

    title: str

    status: Literal["done", "pending"]

    impact: Optional[RecommendationImpact] = None

    suggestion: RecommendationSuggestion

class AnalysisBreakdown(BaseModel):

    title: str

    weight: float

    score: float

class AnalysisSummary(BaseModel):

    breakdown: List[AnalysisBreakdown]

class AeoScoreTargetZone(BaseModel):

    low: float

    high: float

class AeoScore(BaseModel):

    target_zone: AeoScoreTargetZone

    value: float

class DocumentContent(BaseModel):

    format: Literal["markdown", "html"]

    value: str

class ContentAnalysis(BaseModel):

    content: DocumentContent

    aeo_content_score: Optional[AeoScore] = None

    analysis: AnalysisSummary

    recommendations: List[Recommendation]

    inputs: AnalysisInputs



class OptimizationRetrieveResponse(BaseModel):

    data: ContentAnalysis
