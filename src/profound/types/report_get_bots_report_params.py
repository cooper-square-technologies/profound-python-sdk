# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.pagination import Pagination

__all__ = [
    "ReportGetBotsReportParams",
    "Filter",
    "FilterAppModelsAgentAnalyticsFiltersPathFilter",
    "FilterBotNameFilter",
    "FilterBotProviderFilter",
]


class ReportGetBotsReportParams(TypedDict, total=False):
    domain: Required[str]
    """Domain to query logs for."""

    metrics: Required[List[Literal["count", "citations", "indexing", "training", "last_visit"]]]

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date for logs.

    Accepts: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS, or full ISO
    timestamp.
    """

    date_interval: Literal["day", "week", "month", "year"]
    """Date interval for the report. (only used with date dimension)"""

    dimensions: List[Literal["date", "path", "bot_name", "bot_provider"]]
    """Dimensions to group the report by."""

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End date for logs.

    Accepts same formats as start_date. Defaults to now if omitted.
    """

    filters: Iterable[Filter]
    """Filters for bots report."""

    order_by: Dict[str, Literal["asc", "desc"]]
    """Custom ordering of the report results.

    The order is a record of key-value pairs where:

    - key is the field to order by, which can be a metric or dimension
    - value is the direction of the order, either 'asc' for ascending or 'desc' for
      descending.

    When not specified, the default order is the first metric in the query
    descending.
    """

    pagination: Pagination
    """Pagination settings for the report results."""


class FilterAppModelsAgentAnalyticsFiltersPathFilter(TypedDict, total=False):
    """Filter by request path"""

    field: Required[Literal["path"]]

    operator: Required[
        Literal[
            "is",
            "not_is",
            "in",
            "not_in",
            "contains",
            "not_contains",
            "matches",
            "contains_case_insensitive",
            "not_contains_case_insensitive",
        ]
    ]

    value: Required[Union[str, SequenceNotStr[str]]]


class FilterBotNameFilter(TypedDict, total=False):
    """Filter by bot name (user agent)"""

    field: Required[Literal["bot_name"]]

    operator: Required[
        Literal[
            "is",
            "not_is",
            "in",
            "not_in",
            "contains",
            "not_contains",
            "matches",
            "contains_case_insensitive",
            "not_contains_case_insensitive",
        ]
    ]

    value: Required[
        Union[
            Literal[
                "Amazonbot",
                "ClaudeBot",
                "Claude-User",
                "Claude-SearchBot",
                "Applebot",
                "Applebot-Extended",
                "Bytespider",
                "DeepSeek",
                "DuckAssistBot",
                "DuckDuckBot",
                "Googlebot",
                "Googlebot-News",
                "Googlebot-Video",
                "Googlebot-Image",
                "Google-Extended",
                "Storebot-Google",
                "Google-CloudVertexBot",
                "meta-externalfetcher",
                "meta-externalagent",
                "bingbot",
                "MicrosoftPreview",
                "ChatGPT-User",
                "GPTBot",
                "OAI-SearchBot",
                "OAI-Operator",
                "PerplexityBot",
                "Perplexity-User",
                "Grok-PageBrowser",
                "YouBot",
            ],
            List[
                Literal[
                    "Amazonbot",
                    "ClaudeBot",
                    "Claude-User",
                    "Claude-SearchBot",
                    "Applebot",
                    "Applebot-Extended",
                    "Bytespider",
                    "DeepSeek",
                    "DuckAssistBot",
                    "DuckDuckBot",
                    "Googlebot",
                    "Googlebot-News",
                    "Googlebot-Video",
                    "Googlebot-Image",
                    "Google-Extended",
                    "Storebot-Google",
                    "Google-CloudVertexBot",
                    "meta-externalfetcher",
                    "meta-externalagent",
                    "bingbot",
                    "MicrosoftPreview",
                    "ChatGPT-User",
                    "GPTBot",
                    "OAI-SearchBot",
                    "OAI-Operator",
                    "PerplexityBot",
                    "Perplexity-User",
                    "Grok-PageBrowser",
                    "YouBot",
                ]
            ],
        ]
    ]


class FilterBotProviderFilter(TypedDict, total=False):
    """Filter by bot provider"""

    field: Required[Literal["bot_provider"]]

    operator: Required[
        Literal[
            "is",
            "not_is",
            "in",
            "not_in",
            "contains",
            "not_contains",
            "matches",
            "contains_case_insensitive",
            "not_contains_case_insensitive",
        ]
    ]

    value: Required[
        Union[
            Literal[
                "openai",
                "anthropic",
                "chatgpt",
                "deepseek",
                "google",
                "microsoft",
                "perplexity",
                "apple",
                "bytedance",
                "amazon",
                "meta",
                "duckduckgo",
                "you",
                "xai",
                "grok",
                "gemini",
            ],
            List[
                Literal[
                    "openai",
                    "anthropic",
                    "chatgpt",
                    "deepseek",
                    "google",
                    "microsoft",
                    "perplexity",
                    "apple",
                    "bytedance",
                    "amazon",
                    "meta",
                    "duckduckgo",
                    "you",
                    "xai",
                    "grok",
                    "gemini",
                ]
            ],
        ]
    ]


Filter: TypeAlias = Union[FilterAppModelsAgentAnalyticsFiltersPathFilter, FilterBotNameFilter, FilterBotProviderFilter]
