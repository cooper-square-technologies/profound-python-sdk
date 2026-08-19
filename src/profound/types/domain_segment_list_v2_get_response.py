# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["DomainSegmentListV2GetResponse", "DomainSegmentListV2GetResponseItem"]


class DomainSegmentListV2GetResponseItem(BaseModel):
    id: str

    name: str


DomainSegmentListV2GetResponse: TypeAlias = List[DomainSegmentListV2GetResponseItem]
