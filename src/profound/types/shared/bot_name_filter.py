# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BotNameFilter"]


class BotNameFilter(BaseModel):
    """Filter by bot name (user agent)"""

    field: Literal["bot_name"]

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
