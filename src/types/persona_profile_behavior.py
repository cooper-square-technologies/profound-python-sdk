# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PersonaProfileBehavior"]


class PersonaProfileBehavior(BaseModel):

    pain_points: Optional[str] = FieldInfo(alias="painPoints", default=None)

    motivations: Optional[str] = None
