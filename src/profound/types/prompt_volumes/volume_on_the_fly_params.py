# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from datetime import date
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

__all__ = ["VolumeOnTheFlyParams"]


class VolumeOnTheFlyParams(TypedDict, total=False):
    keyword: Required[str]

    matching_type: Required[Literal["exact_match", "phrase_match"]]

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    end_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    regions: SequenceNotStr[str]

    platforms: SequenceNotStr[str]

    organization_id: Optional[str]
    """Organization whose daily keyword allowance is used. Required in the JSON request body for API keys with multiple organizations that have API access. If omitted or null, defaults to the API key's sole organization with API access or the token's active organization. For OAuth/M2M tokens, any supplied organization_id must match the token's organization."""
