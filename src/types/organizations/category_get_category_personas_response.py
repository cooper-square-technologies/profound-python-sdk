# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from ..._models import BaseModel
from ..persona_profile import PersonaProfile

__all__ = ["CategoryGetCategoryPersonasResponse", "CategoryPersona"]


class CategoryPersona(BaseModel):

    id: str

    name: str

    persona: PersonaProfile



class CategoryGetCategoryPersonasResponse(BaseModel):

    data: List[CategoryPersona]
