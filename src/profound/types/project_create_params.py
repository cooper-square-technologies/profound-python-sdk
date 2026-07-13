# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

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

    attachments: Iterable[Attachment]

    focus: Optional[str]

    generation_context: Optional[GenerationContext]

    project_name: Optional[str]

    title: Optional[str]

    topics: SequenceNotStr[str]


class Attachment(TypedDict, total=False):
    id: Required[str]

    data_base64: Required[str]

    mime_type: Required[str]

    name: Required[str]

    size_bytes: Required[int]


class GenerationContextDateRange(TypedDict, total=False):
    label: Required[str]

    preset: Required[str]

    end_date: Annotated[Optional[str], PropertyInfo(alias="endDate")]

    mode: Optional[Literal["custom", "relative"]]

    start_date: Annotated[Optional[str], PropertyInfo(alias="startDate")]


class GenerationContextPlatform(TypedDict, total=False):
    id: Required[str]

    name: Required[str]

    slug: Optional[str]


class GenerationContextRegion(TypedDict, total=False):
    id: Required[str]

    name: Required[str]

    slug: Optional[str]


class GenerationContextTag(TypedDict, total=False):
    id: Required[str]

    name: Required[str]

    slug: Optional[str]


class GenerationContext(TypedDict, total=False):
    date_range: Annotated[Optional[GenerationContextDateRange], PropertyInfo(alias="dateRange")]

    platforms: Iterable[GenerationContextPlatform]

    project_categories: Annotated[
        List[Literal["creative", "earned", "publish", "refresh", "social"]], PropertyInfo(alias="projectCategories")
    ]

    regions: Iterable[GenerationContextRegion]

    tags: Iterable[GenerationContextTag]
