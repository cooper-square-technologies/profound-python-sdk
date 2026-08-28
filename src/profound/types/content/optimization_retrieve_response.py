# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "OptimizationRetrieveResponse",
    "Data",
    "DataContent",
    "DataAeoContentScore",
    "DataAeoContentScoreTargetZone",
    "DataAnalysis",
    "DataAnalysisBreakdown",
    "DataRecommendation",
    "DataRecommendationImpact",
    "DataRecommendationSuggestion",
    "DataInputs",
    "DataInputsTopic",
    "DataInputsPrompt",
    "DataInputsUser",
]


class DataInputsUser(BaseModel):
    type: Literal["file", "text", "url"]

    value: str

    metadata: Dict[str, Union[int, str]]


class DataInputsPrompt(BaseModel):
    id: str

    name: str


class DataInputsTopic(BaseModel):
    id: str

    name: str


class DataInputs(BaseModel):
    topic: Optional[DataInputsTopic] = None

    prompt: Optional[DataInputsPrompt] = None

    top_citations: List[str]

    user: DataInputsUser


class DataRecommendationSuggestion(BaseModel):
    text: str

    rationale: str


class DataRecommendationImpact(BaseModel):
    section: str

    score: float


class DataRecommendation(BaseModel):
    title: str

    status: Literal["done", "pending"]

    impact: Optional[DataRecommendationImpact] = None

    suggestion: DataRecommendationSuggestion


class DataAnalysisBreakdown(BaseModel):
    title: str

    weight: float

    score: float


class DataAnalysis(BaseModel):
    breakdown: List[DataAnalysisBreakdown]


class DataAeoContentScoreTargetZone(BaseModel):
    low: float

    high: float


class DataAeoContentScore(BaseModel):
    target_zone: DataAeoContentScoreTargetZone

    value: float


class DataContent(BaseModel):
    format: Literal["markdown", "html"]

    value: str


class Data(BaseModel):
    content: DataContent

    aeo_content_score: Optional[DataAeoContentScore] = None

    analysis: DataAnalysis

    recommendations: List[DataRecommendation]

    inputs: DataInputs


class OptimizationRetrieveResponse(BaseModel):
    data: Data
