# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BotProviderFilter"]


class BotProviderFilter(TypedDict, total=False):
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
