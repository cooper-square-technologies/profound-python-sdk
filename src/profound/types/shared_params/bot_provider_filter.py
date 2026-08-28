# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BotProviderFilter"]


class BotProviderFilter(TypedDict, total=False):
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
                "you.com",
                "xai",
                "grok",
                "gemini",
                "mistral",
                "huawei",
                "yandex",
                "baidu",
                "yahoo",
                "commoncrawl",
                "openclaw",
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
                    "you.com",
                    "xai",
                    "grok",
                    "gemini",
                    "mistral",
                    "huawei",
                    "yandex",
                    "baidu",
                    "yahoo",
                    "commoncrawl",
                    "openclaw",
                ]
            ],
        ]
    ]
