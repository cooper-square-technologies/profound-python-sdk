# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, List, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = [
    "ProjectCreateParams",
    "Attachment",
    "GenerationContext",
    "GenerationContextDateRange",
    "GenerationContextPlatform",
    "GenerationContextRegion",
    "GenerationContextTag",
]


class ProjectCreateParams(TypedDict, total=False):
    category_id: Required[str]

    title: Optional[str]

    project_name: Optional[str]

    focus: Optional[str]

    topics: SequenceNotStr[str]

    attachments: Iterable[Attachment]

    generation_context: Optional[GenerationContext]


class GenerationContextTag(TypedDict, total=False):
    id: Required[str]

    name: Required[str]

    slug: Optional[str]


class GenerationContextRegion(TypedDict, total=False):
    id: Required[str]

    name: Required[str]

    slug: Optional[str]


class GenerationContextPlatform(TypedDict, total=False):
    id: Required[str]

    name: Required[str]

    slug: Optional[str]


class GenerationContextDateRange(TypedDict, total=False):
    end_date: Annotated[Optional[str], PropertyInfo(alias="endDate")]

    label: Required[str]

    mode: Optional[Literal["custom", "relative"]]

    preset: Required[str]

    start_date: Annotated[Optional[str], PropertyInfo(alias="startDate")]


class GenerationContext(TypedDict, total=False):
    date_range: Annotated[Optional[GenerationContextDateRange], PropertyInfo(alias="dateRange")]

    platforms: Iterable[GenerationContextPlatform]

    project_categories: Annotated[
        List[Literal["creative", "earned", "publish", "refresh", "social"]], PropertyInfo(alias="projectCategories")
    ]

    regions: Iterable[GenerationContextRegion]

    tags: Iterable[GenerationContextTag]


class Attachment(TypedDict, total=False):
    id: Required[str]

    name: Required[str]

    mime_type: Required[str]

    size_bytes: Required[int]

    data_base64: Required[str]
