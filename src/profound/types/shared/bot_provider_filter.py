# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BotProviderFilter"]


class BotProviderFilter(BaseModel):
    """Filter by bot provider"""

    field: Literal["bot_provider"]

    operator: Literal[
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

    value: Union[
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
