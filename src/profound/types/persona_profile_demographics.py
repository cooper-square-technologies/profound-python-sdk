# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PersonaProfileDemographics"]


class PersonaProfileDemographics(BaseModel):
    age_range: Optional[List[str]] = FieldInfo(alias="ageRange", default=None)
