# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PersonaProfileBehavior"]


class PersonaProfileBehavior(BaseModel):
    motivations: Optional[str] = None

    pain_points: Optional[str] = FieldInfo(alias="painPoints", default=None)
