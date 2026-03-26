# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BotNameFilter"]


class BotNameFilter(TypedDict, total=False):
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
