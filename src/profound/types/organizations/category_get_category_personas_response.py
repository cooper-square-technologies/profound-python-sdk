# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..persona_profile import PersonaProfile

__all__ = ["CategoryGetCategoryPersonasResponse", "Data"]


class Data(BaseModel):
    id: str

    name: str

    persona: PersonaProfile


class CategoryGetCategoryPersonasResponse(BaseModel):
    data: List[Data]
