# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel

from .persona_profile import PersonaProfile
from .category import Category
from .organization import Organization

__all__ = ["OrganizationGetPersonasResponse", "Data"]


class Data(BaseModel):
    id: str

    name: str

    persona: PersonaProfile

    category: Category

    organization: Organization


class OrganizationGetPersonasResponse(BaseModel):
    data: List[Data]
