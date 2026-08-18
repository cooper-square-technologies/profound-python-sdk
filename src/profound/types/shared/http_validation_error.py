# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional, Union

from ..._models import BaseModel

__all__ = ["HTTPValidationError", "Detail"]


class Detail(BaseModel):
    loc: List[Union[str, int]]

    msg: str

    type: str

    input: Optional[object] = None

    ctx: Optional[object] = None


class HTTPValidationError(BaseModel):
    detail: Optional[List[Detail]] = None
