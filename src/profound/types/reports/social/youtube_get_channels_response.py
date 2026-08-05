# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ...._models import BaseModel

__all__ = ["YoutubeGetChannelsResponse"]


class YoutubeGetChannelsResponse(BaseModel):
    data: List[Dict[str, object]]

    info: Dict[str, object]
