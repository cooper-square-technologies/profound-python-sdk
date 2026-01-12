# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "OptimizationRetrieveResponse",
    "Data",
    "DataAeoContentScore",
    "DataAeoContentScoreTargetZone",
    "DataAnalysis",
    "DataAnalysisBreakdown",
    "DataContent",
    "DataInputs",
    "DataInputsPrompt",
    "DataInputsTopic",
    "DataInputsUser",
    "DataRecommendation",
    "DataRecommendationImpact",
    "DataRecommendationSuggestion",
]


class DataAeoContentScoreTargetZone(BaseModel):
    high: float

    low: float


class DataAeoContentScore(BaseModel):
    target_zone: DataAeoContentScoreTargetZone

    value: float


class DataAnalysisBreakdown(BaseModel):
    score: float

    title: str

    weight: float


class DataAnalysis(BaseModel):
    breakdown: List[DataAnalysisBreakdown]


class DataContent(BaseModel):
    format: Literal["markdown", "html"]

    value: str


class DataInputsPrompt(BaseModel):
    id: str

    name: str


class DataInputsTopic(BaseModel):
    id: str

    name: str


class DataInputsUser(BaseModel):
    metadata: Dict[str, Union[int, str]]

    type: Literal["file", "text", "url"]

    value: str


class DataInputs(BaseModel):
    prompt: DataInputsPrompt

    top_citations: List[str]

    topic: DataInputsTopic

    user: DataInputsUser


class DataRecommendationImpact(BaseModel):
    score: float

    section: str


class DataRecommendationSuggestion(BaseModel):
    rationale: str

    text: str


class DataRecommendation(BaseModel):
    impact: Optional[DataRecommendationImpact] = None

    status: Literal["done", "pending"]

    suggestion: DataRecommendationSuggestion

    title: str


class Data(BaseModel):
    aeo_content_score: Optional[DataAeoContentScore] = None

    analysis: DataAnalysis

    content: DataContent

    inputs: DataInputs

    recommendations: List[DataRecommendation]


class OptimizationRetrieveResponse(BaseModel):
    data: Data
