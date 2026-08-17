# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal
from .._utils import PropertyInfo

from .._models import BaseModel
from .pagination import Pagination

__all__ = ["SentimentV2ReportQuery", "SentimentV2ModelIdFilter", "SentimentV2RegionIdFilter", "SentimentV2TopicIdFilter", "SentimentV2PromptIdFilter", "SentimentV2PersonaIdFilter", "SentimentV2TagIdFilter", "SentimentV2RunIdFilter", "SentimentV2ThemeIdFilter", "SentimentV2ThemeFilter", "SentimentV2ClaimIdFilter", "SentimentV2ClaimFilter", "SentimentV2SentimentFilter"]


class SentimentV2SentimentFilter(BaseModel):

    field: Literal["sentiment"]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[Literal["positive", "negative"], List[Literal["positive", "negative"]]]

class SentimentV2ClaimFilter(BaseModel):

    field: Literal["claim"]

    operator: Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]

    value: Union[str, List[str]]

class SentimentV2ClaimIdFilter(BaseModel):

    field: Literal["claim_id"]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]

class SentimentV2ThemeFilter(BaseModel):

    field: Literal["theme"]

    operator: Literal["is", "not_is", "in", "not_in", "contains", "not_contains", "matches", "contains_case_insensitive", "not_contains_case_insensitive"]

    value: Union[str, List[str]]

class SentimentV2ThemeIdFilter(BaseModel):

    field: Literal["theme_id"]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]

class SentimentV2RunIdFilter(BaseModel):

    field: Literal["run_id"]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]

class SentimentV2TagIdFilter(BaseModel):

    field: Literal["tag_id"]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]

class SentimentV2PersonaIdFilter(BaseModel):

    field: Literal["persona_id"]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]

class SentimentV2PromptIdFilter(BaseModel):

    field: Literal["prompt_id"]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]

class SentimentV2TopicIdFilter(BaseModel):

    field: Literal["topic_id"]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]

class SentimentV2RegionIdFilter(BaseModel):

    field: Literal["region_id"]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]

class SentimentV2ModelIdFilter(BaseModel):

    field: Literal["model_id"]

    operator: Literal["is", "not_is", "in", "not_in"]

    value: Union[str, List[str]]



class SentimentV2ReportQuery(BaseModel):

    category_id: str

    asset_name: str

    start_date: datetime
    """Start date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    end_date: datetime
    """End date for the report. Accepts formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, or full ISO timestamp."""

    comparison_start_date: Optional[datetime] = None
    """Start of the previous period for delta computation."""

    comparison_end_date: Optional[datetime] = None
    """End of the previous period for delta computation."""

    date_interval: Optional[Literal["hour", "day", "week", "month", "quarter", "year", "relative_week"]] = None
    """Date interval for the report. Only used when dimensions includes date."""

    dimensions: Optional[List[Literal["date", "topic", "region", "model", "prompt", "persona", "tag", "theme", "claim", "run", "asset_name"]]] = None
    """Dimensions to group the report by."""

    metrics: List[Literal["sentiment", "occurrence"]]

    filters: Optional[List[Annotated[Union[SentimentV2ModelIdFilter, SentimentV2RegionIdFilter, SentimentV2TopicIdFilter, SentimentV2PromptIdFilter, SentimentV2PersonaIdFilter, SentimentV2TagIdFilter, SentimentV2RunIdFilter, SentimentV2ThemeIdFilter, SentimentV2ThemeFilter, SentimentV2ClaimIdFilter, SentimentV2ClaimFilter, SentimentV2SentimentFilter], PropertyInfo(discriminator="field")]]] = None
    """List of filters to apply to the sentiment-v2 report."""

    order_by: Optional[Dict[str, Literal["asc", "desc"]]] = None
    """Custom ordering of report results. Dimension keys must also be present in dimensions. The sentiment metric orders by positive_sentiment."""

    pagination: Optional[Pagination] = None
    """Pagination settings for the report results."""
