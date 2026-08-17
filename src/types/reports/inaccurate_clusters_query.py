# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InaccurateClustersQuery"]


class InaccurateClustersQuery(BaseModel):

    start_date: str

    end_date: str

    comparison_start_date: Optional[str] = None

    comparison_end_date: Optional[str] = None

    category_id: str

    topic_ids: Optional[List[str]] = None

    exclude_topic_ids: Optional[bool] = None

    tag_ids: Optional[List[str]] = None

    tag_filter_type: Optional[Literal["all", "any"]] = None

    include_no_tag: Optional[bool] = None

    region_ids: Optional[List[str]] = None

    platform_ids: Optional[List[str]] = None

    persona_ids: Optional[List[str]] = None

    include_no_persona: Optional[bool] = None

    prompt_ids: Optional[List[str]] = None

    citation_categories: Optional[List[str]] = None

    theme_id: str

    limit: Optional[int] = None

    offset: Optional[int] = None

    search_query: Optional[str] = None
